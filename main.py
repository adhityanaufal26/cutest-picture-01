# Cutest-picture-01 entry: copy the cute picture entry.png beside this file to /output/entry.png.
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
shutil.copyfile(src, out)
assert os.path.getsize(src) == os.path.getsize(out)
