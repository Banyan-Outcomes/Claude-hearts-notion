#!/usr/bin/env python3
"""Build dist/cos-install.zip, the installer skill, for uploading in the Claude app.

Usage: python3 scripts/package_installer.py
The zip holds one folder, cos-install/, with SKILL.md inside, which is the format
Settings > Capabilities > Skills > Upload skill expects. No config is needed.
"""
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / ".claude" / "skills" / "cos-install" / "SKILL.md"
out = root / "dist" / "cos-install.zip"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(src, "cos-install/SKILL.md")
print(f"Wrote {out.relative_to(root)}. Upload it under Settings > Capabilities > Skills.")
