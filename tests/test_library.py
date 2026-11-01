from pathlib import Path
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'lib'))
from compass import library


def test_locked_corpus_and_rendered_payload_agree():
    manifest = library.verify_library()
    assert len(manifest['documents']) == 11
    raw = (Path(library.library_directory()) / 'library.js').read_text(encoding='utf-8')
    payload = json.loads(raw.removeprefix('window.PARAMETRICALLY_STANDARDS = ').rstrip(';\n'))
    for doc in payload['documents']:
        assert doc['markdown'] == library.read_document(doc['file'])
    assert all(d['id'] != 'ofis' for d in payload['documents'])


def test_paginated_read_reconstructs_large_annex_without_loss():
    chunks, line = [], 1
    while line is not None:
        result = library.read('ek-6', line, 200)
        chunks.append(result['markdown'])
        assert result['source_status']['whole_document_review_complete'] is False
        line = result['next_line']
    assert '\n'.join(chunks) == library.read_document('ek-6.md').rstrip('\r\n')


@pytest.mark.parametrize('value', ['../LICENSE', 'sources/20260805-2.htm.txt', 'C:/Users', 'ek-10'])
def test_read_rejects_unlisted_document_ids(value):
    with pytest.raises(ValueError):
        library.read(value)


@pytest.mark.parametrize('value', [0, -1, 201, True, '20'])
def test_pagination_rejects_invalid_limits(value):
    with pytest.raises(ValueError):
        library.read('yonetmelik', max_lines=value)


def test_turkish_search_has_source_context_and_bounds():
    result = library.search('İSİMLENDİRME', limit=3)
    assert result['total_matches'] > 3
    assert result['returned'] == 3
    assert all(hit['line'] > 0 and hit['file'].endswith('.md') for hit in result['hits'])
    assert result['source_status']['current_legal_status'] == 'UNVERIFIED'
    with pytest.raises(ValueError):
        library.search(' ')


def test_table_preserves_source_cell_coordinates_and_spans():
    result = library.read_table('p001-t01', limit=2)
    assert result['page'] == 1
    assert len(result['cells']) == 2
    assert all(set(('row', 'column', 'rowspan', 'colspan', 'bbox', 'text')).issubset(c) for c in result['cells'])
    assert result['next_offset'] == 2
    with pytest.raises(ValueError):
        library.read_table('p999-t99')


def test_file_path_escape_is_rejected(tmp_path):
    for path in ['../secret', 'a/../../secret', '/absolute', 'C:/secret', 'a\\secret']:
        with pytest.raises(ValueError):
            library._safe_file(str(tmp_path), path)


def test_changed_reading_document_is_rejected(tmp_path):
    manifest = {'documents': [{'id': 'test', 'file': 'test.md'}], 'files': {'test.md': '0' * 64}}
    (tmp_path / 'manifest.json').write_text(json.dumps(manifest))
    (tmp_path / 'test.md').write_text('Tampered')
    with pytest.raises(ValueError, match='differs'):
        library.read_document('test.md', str(tmp_path))
