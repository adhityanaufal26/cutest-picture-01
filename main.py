# Cutest-picture-01 entry: copy the cute picture entry.png beside this file to /output/entry.png.
import os
import shutil

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
shutil.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"), os.path.join(out, "entry.png"))
