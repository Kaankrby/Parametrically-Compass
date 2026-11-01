# -*- coding: utf-8 -*-
"""Shared read-only corpus API for IronPython, CPython and MCP."""
from __future__ import unicode_literals

import hashlib
import io
import json
import os
import re
import unicodedata

from compass import __version__

PDF_SHA = '7dc88971d3a7a8ae837ef148169fa5bf6c9ce7a01cc8fcd560ae3d342bb0ecb3'
HTML_SHA = 'ac662505610e9a8b34ecc9116a04d0843992d5b95820eaba1b4c12e9679c2703'
WARNING = 'TEYİT BEKLİYOR: OCR ve güncel konsolide mevzuat bütünüyle doğrulanmamıştır. Hukuki uygunluk onayı değildir.'
try:
    text_type = unicode
except NameError:
    text_type = str


def library_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def _safe_file(root, name):
    if not isinstance(name, text_type) or not name or '\\' in name or ':' in name:
        raise ValueError('Invalid corpus path')
    if any(part in ('', '.', '..') for part in name.split('/')):
        raise ValueError('Corpus path traversal rejected')
    root = os.path.normcase(os.path.realpath(root))
    target = os.path.realpath(os.path.join(root, *name.split('/')))
    if not os.path.normcase(target).startswith(root.rstrip(os.sep) + os.sep):
        raise ValueError('Corpus path outside library')
    return target


def _sha(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        while True:
            block = stream.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def _json(path):
    with io.open(path, encoding='utf-8') as stream:
        return json.load(stream)


def _manifest(directory=None):
    return _json(os.path.join(directory or library_directory(), 'manifest.json'))


def verify_library(directory=None):
    root = directory or library_directory()
    manifest = _manifest(root)
    expected_ids = set(['baslangic', 'yonetmelik'] + ['ek-' + str(i) for i in range(1, 10)])
    if manifest.get('schema_version') != 1 or manifest.get('source_pages') != 241:
        raise ValueError('Unsupported library manifest')
    docs = manifest.get('documents', [])
    if len(docs) != 11 or set(d['id'] for d in docs) != expected_ids:
        raise ValueError('Missing or unexpected corpus documents')
    files = manifest.get('files', {})
    required = set(['index.html', 'reader.js', 'reader.css', 'library.js',
                    'sources/20260805-2-1.pdf', 'sources/20260805-2.htm.txt'])
    required.update(d['file'] for d in docs)
    if not required.issubset(set(files)):
        raise ValueError('Required library assets missing from manifest')
    for name, digest in sorted(files.items()):
        path = _safe_file(root, name)
        if not os.path.isfile(path) or _sha(path) != digest:
            raise ValueError('Library asset missing or changed: ' + name)
    if files['sources/20260805-2-1.pdf'] != PDF_SHA or files['sources/20260805-2.htm.txt'] != HTML_SHA:
        raise ValueError('Original source archive changed')
    return manifest


def reader_documents(manifest, collection='compass'):
    if collection != 'compass':
        raise ValueError('Only the Compass regulation collection is available')
    return manifest['documents']


def read_document(filename, directory=None):
    root = directory or library_directory()
    manifest = _manifest(root)
    if filename not in [d['file'] for d in manifest['documents']]:
        raise ValueError('Unknown reading document')
    path = _safe_file(root, filename)
    if _sha(path) != manifest['files'][filename]:
        raise ValueError('Reading document differs from manifest')
    with io.open(path, encoding='utf-8') as stream:
        return stream.read()


def _unescape(value):
    for old, new in (('&lt;', '<'), ('&gt;', '>'), ('&quot;', '"'),
                     ('&#x27;', "'"), ('&#39;', "'"), ('&amp;', '&')):
        value = value.replace(old, new)
    return value


def read_document_text(filename, directory=None):
    value = read_document(filename, directory)
    value = re.sub(r'</t[dh]>\s*<t[dh]\b[^>]*>', ' | ', value, flags=re.I)
    value = re.sub(r'</tr>', '\n', value, flags=re.I)
    value = re.sub(r'<br\s*/?>', ' ', value, flags=re.I)
    value = re.sub(r'</?(?:table|tbody|thead|tfoot|caption|tr|td|th)\b[^>]*>', '', value, flags=re.I)
    return _unescape(value)


def _bounded(value, minimum, maximum, name):
    if isinstance(value, bool) or not isinstance(value, int) or not minimum <= value <= maximum:
        raise ValueError('%s must be between %s and %s' % (name, minimum, maximum))
    return value


def source_status(directory=None):
    manifest = _manifest(directory)
    return {'package_version': __version__, 'corpus_repository': manifest['corpus_repository'],
            'corpus_commit': manifest['corpus_commit'], 'source_pdf_sha256': PDF_SHA,
            'publication_snapshot': '2026-08-05 / 33331', 'current_legal_status': 'UNVERIFIED',
            'review_status': 'OCR_UNREVIEWED', 'whole_document_review_complete': False,
            'warning': WARNING, 'model_access': False}


def list_documents(directory=None):
    return {'source_status': source_status(directory), 'documents': _manifest(directory)['documents']}


def _document(document_id, directory=None):
    matches = [d for d in _manifest(directory)['documents'] if d['id'] == document_id]
    if len(matches) != 1:
        raise ValueError('Unknown document id; use list_documents')
    return matches[0]


def read(document_id, start_line=1, max_lines=100, directory=None):
    _bounded(start_line, 1, 100000, 'start_line')
    _bounded(max_lines, 1, 200, 'max_lines')
    doc = _document(document_id, directory)
    lines = read_document(doc['file'], directory).splitlines()
    if start_line > len(lines):
        raise ValueError('start_line exceeds document length')
    selected = []
    size = 0
    for line in lines[start_line - 1:start_line - 1 + max_lines]:
        if size + len(line) > 50000:
            if not selected:
                raise ValueError('Source line too long; use the original Markdown resource')
            break
        selected.append(line)
        size += len(line) + 1
    end_line = start_line + len(selected) - 1
    return {'source_status': source_status(directory), 'document': doc,
            'sha256': _manifest(directory)['files'][doc['file']],
            'start_line': start_line, 'end_line': end_line, 'total_lines': len(lines),
            'next_line': end_line + 1 if end_line < len(lines) else None,
            'markdown': '\n'.join(selected),
            'note': 'A slice may contain part of an HTML table; preserve rowspan/colspan and source context.'}


def _fold(value):
    value = value.replace('İ', 'i').replace('I', 'ı').lower().replace('ı', 'i')
    return ''.join(c for c in unicodedata.normalize('NFKD', value) if not unicodedata.combining(c))


def search(query, document_id='', limit=10, directory=None):
    if not isinstance(query, text_type) or not query.strip() or len(query) > 200:
        raise ValueError('query must contain 1 to 200 characters')
    _bounded(limit, 1, 50, 'limit')
    words = _fold(query).split()
    docs = [_document(document_id, directory)] if document_id else _manifest(directory)['documents']
    hits, total = [], 0
    for doc in docs:
        section = ''
        for number, line in enumerate(read_document(doc['file'], directory).splitlines(), 1):
            if line.startswith('## '):
                section = line[3:]
            plain = _unescape(re.sub(r'<[^>]*>', ' ', line))
            folded = _fold(plain)
            if all(word in folded for word in words):
                total += 1
                if len(hits) < limit:
                    at = max(0, folded.find(words[0]) - 80)
                    hits.append({'document_id': doc['id'], 'title': doc['title'],
                                 'file': doc['file'], 'line': number, 'section': section,
                                 'excerpt': plain[at:at + 500], 'source_url': doc.get('source_url'),
                                 'pdf_page_range': [doc.get('first_page'), doc.get('last_page')]})
    return {'source_status': source_status(directory), 'query': query,
            'total_matches': total, 'returned': len(hits), 'hits': hits}


def read_table(table_id, offset=0, limit=50, directory=None):
    if not isinstance(table_id, text_type) or not re.match(r'^p[0-9]{3}-t[0-9]{2}$', table_id):
        raise ValueError('Use a source table fragment id such as p035-t01')
    _bounded(offset, 0, 10000, 'offset')
    _bounded(limit, 1, 100, 'limit')
    root = directory or library_directory()
    relative = 'sources/structured-annexes.json'
    path = _safe_file(root, relative)
    if _sha(path) != _manifest(root)['files'][relative]:
        raise ValueError('Structured source differs from manifest')
    source = _json(path)
    for page in source['pages']:
        for table in page['tables']:
            if table['id'] != table_id:
                continue
            cells = table['cells']
            if offset >= len(cells):
                raise ValueError('offset exceeds table cell count')
            fields = ('row', 'column', 'rowspan', 'colspan', 'bbox', 'text',
                      'review', 'source_review', 'source_verifications')
            selected = [dict((k, c[k]) for k in fields if k in c) for c in cells[offset:offset + limit]]
            return {'source_status': source_status(root), 'page': page['page'],
                    'table_id': table_id, 'title': table.get('title'),
                    'source_table': table.get('source_table'), 'table_review': table.get('review'),
                    'total_cells': len(cells),
                    'offset': offset, 'cells': selected,
                    'next_offset': offset + len(selected) if offset + len(selected) < len(cells) else None,
                    'note': 'Fragment of a source table; other pages may continue the same numbered table.'}
    raise ValueError('Source table fragment not found')
