#!/usr/bin/env python3
"""Build only the explicit public source directory; never copy workspace assets."""
from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
source = root / 'site'
target = root / 'dist'
# Only overwrite files from the public source; refuse unexpected output content.
expected = {p.relative_to(source) for p in source.rglob('*') if p.is_file()}
if target.exists():
    unexpected = {p.relative_to(target) for p in target.rglob('*') if p.is_file()} - expected
    if unexpected:
        raise SystemExit('Unexpected dist files; inspect before building: ' + str(unexpected))
for rel in expected:
    destination = target / rel
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source / rel, destination)
print(f'Built {len(expected)} public files in dist/')
