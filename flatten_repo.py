import os, shutil
from pathlib import Path
root=Path('.')
pkg=root/'Certification_Evidence'/'FINAL_SUBMISSION_PACKAGE'
for p in list(root.iterdir()):
    if p.name not in {'.git','flatten_repo.py'}:
        shutil.rmtree(p) if p.is_dir() else p.unlink()
for p in pkg.iterdir():
    dest=root/p.name
    shutil.copytree(p,dest) if p.is_dir() else shutil.copy2(p,dest)
(root/'flatten_repo.py').unlink(missing_ok=True)
