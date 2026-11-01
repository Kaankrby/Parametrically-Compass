"""Build the offline UI and verify the locked upstream corpus without network access."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'lib/compass/data'
ANNEXES = [
    (1, 1, 'Proje kodu belirleme esasları'), (2, 2, 'Dosya isimlendirme esasları'),
    (3, 14, 'Mahal isimlendirme esasları'), (4, 20, 'CAD ortamında çizim hazırlama esasları'),
    (5, 29, 'BIM modelindeki IFC sınıfları ve varlık isimlendirme esasları'),
    (6, 35, 'IFC sınıflarının öznitelik ile özellik tanımları'),
    (7, 221, 'Proje ile ilgili IFC sınıflarının öznitelik tanımları'),
    (8, 237, 'BIM modeli gelişim seviyesi'), (9, 238, 'Model kalite kontrol formu'),
]
OFFICIAL = 'https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2.htm'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def section_id(title):
    value = unicodedata.normalize('NFKD', title.lower().replace('ı', 'i'))
    value = ''.join(c for c in value if not unicodedata.combining(c))
    return re.sub('[^a-z0-9]+', '-', value).strip('-')


def build(check=False):
    lock = json.loads((ROOT / 'corpus-lock.json').read_text(encoding='utf-8'))
    for name, expected in lock['files'].items():
        raw = (DATA / name).read_bytes()
        if len(raw) != expected['bytes'] or sha(raw) != expected['sha256']:
            raise ValueError('Locked upstream source differs: ' + name)
    source = json.loads((DATA / 'sources/structured-annexes.json').read_text(encoding='utf-8'))
    docs = [dict(id='baslangic', title='Compass kullanım rehberi', group='Başlangıç',
                 file='README.md', status='Kullanım ve kaynak sınırları'),
            dict(id='yonetmelik', title='Yönetmelik ana metni', group='Parametrically Compass',
                 file='yonetmelik.md', status='Resmî HTML aktarımı · yayımlanma nüshası', source_url=OFFICIAL)]
    for index, (number, first, title) in enumerate(ANNEXES):
        last = ANNEXES[index + 1][1] - 1 if index < 8 else 241
        titles, section_pages, legacy_sections = {}, {}, {}
        for page in source['pages'][first - 1:last]:
            for table in page['tables']:
                key = table.get('source_table') or table['id']
                titles.setdefault(key, table['title'])
                section_pages.setdefault(section_id(titles[key]), page['page'])
            if page['tables']:
                table = page['tables'][0]
                legacy_sections['pdf-sayfa-' + str(page['page'])] = section_id(titles[table.get('source_table') or table['id']])
        docs.append(dict(id='ek-' + str(number), title='EK-%s · %s' % (number, title),
                         group='Parametrically Compass', file='ek-%s.md' % number,
                         status='Metin ve tablolar · OCR teyidi gerekli',
                         first_page=first, last_page=last, source_url=OFFICIAL.replace('.htm', '-1.pdf'),
                         section_pages=section_pages, legacy_sections=legacy_sections))
    payload_docs = [dict(doc, markdown=(DATA / doc['file']).read_text(encoding='utf-8')) for doc in docs]
    payload = 'window.PARAMETRICALLY_STANDARDS = ' + json.dumps(
        {'documents': payload_docs}, ensure_ascii=False, separators=(',', ':')
    ).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029') + ';\n'
    target = DATA / 'library.js'
    if check:
        if target.read_text(encoding='utf-8') != payload:
            raise ValueError('library.js is stale; run build_reader.py')
    else:
        target.write_text(payload, encoding='utf-8', newline='\n')
    files = {p.relative_to(DATA).as_posix(): sha(p.read_bytes()) for p in sorted(DATA.rglob('*'))
             if p.is_file() and p.name != 'manifest.json'}
    manifest = dict(schema_version=1, title='Parametrically Compass', source_pages=241,
                    source_pdf_sha256=source['source_sha256'], corpus_repository=lock['repository'],
                    corpus_commit=lock['commit'], review_status='OCR_UNREVIEWED',
                    current_legal_status='UNVERIFIED', files=files, documents=docs)
    target = DATA / 'manifest.json'
    if check:
        if json.loads(target.read_text(encoding='utf-8')) != manifest:
            raise ValueError('Reader manifest is stale')
    else:
        target.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(('PASS' if check else 'BUILT') + ': 11 documents, %s files, locked corpus %s' % (len(files), lock['commit']))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    build(parser.parse_args().check)
