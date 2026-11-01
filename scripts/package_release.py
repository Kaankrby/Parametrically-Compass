"""Create and verify a self-contained pyRevit extension ZIP."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'lib'))
from compass.library import verify_library


def package():
    verify_library()
    version = (ROOT / 'VERSION').read_text().strip()
    allowed = ['Compass.tab', 'lib', 'mcp_server', 'scripts', 'docs']
    files = [p for folder in allowed for p in (ROOT / folder).rglob('*')
             if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc']
    files.extend(ROOT / name for name in ['README.md', 'LICENSE', 'NOTICES.md', 'AGENTS.md',
                                         'CONTRIBUTING.md', 'VERSION', 'extension.json',
                                         'requirements-mcp.txt', 'corpus-lock.json'])
    manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    target = dist / ('ParametricallyCompass-%s.zip' % version)
    prefix = 'ParametricallyCompass.extension/'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in sorted(files):
            archive.write(p, prefix + p.relative_to(ROOT).as_posix())
        archive.writestr(prefix + 'release-manifest.json', json.dumps(manifest, indent=2) + '\n')
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == {prefix + name for name in manifest} | {prefix + 'release-manifest.json'}
        for name, digest in manifest.items():
            assert hashlib.sha256(archive.read(prefix + name)).hexdigest() == digest, name
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    target.with_suffix('.zip.sha256').write_text(digest + '  ' + target.name + '\n')
    print('PASS: ZIP CRC, file list and %s SHA-256 records: %s' % (len(manifest), target))
    return target


if __name__ == '__main__':
    package()
