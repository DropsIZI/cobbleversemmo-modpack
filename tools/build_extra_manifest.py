#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera manifests/extra-normal.json y manifests/extra-lite.json a partir de extra/.
=================================================================================
Lo ejecuta AUTOMÁTICAMENTE el GitHub Action cada vez que alguien sube/quita algo
en extra/. No hace falta ejecutarlo a mano.

Estructura de carpetas:
  extra/ambos/   → va a Normal Y Lite
  extra/normal/  → va SOLO a Normal
  extra/lite/    → va SOLO a Lite
cada una con subcarpetas mods/ , datapacks/ , resourcepacks/

El launcher descarga estos archivos directamente del repo (raw).
"""

import hashlib
import json
from pathlib import Path

OWNER = "DropsIZI"
REPO = "cobbleversemmo-modpack"
BRANCH = "main"

ROOT = Path(__file__).resolve().parent.parent          # raíz del repo
EXTRA = ROOT / "extra"
CATEGORIES = ("mods", "datapacks", "resourcepacks")     # → carpetas del juego
# carpeta de scope -> versiones a las que aplica
SCOPES = {"ambos": ("normal", "lite"), "normal": ("normal",), "lite": ("lite",)}
IGNORE = {"readme.md", ".gitkeep"}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    per_version = {"normal": [], "lite": []}

    for scope, versions in SCOPES.items():
        for cat in CATEGORIES:
            d = EXTRA / scope / cat
            if not d.is_dir():
                continue
            for fp in sorted(d.rglob("*")):
                if not fp.is_file():
                    continue
                if fp.name.lower() in IGNORE or fp.name.startswith("."):
                    continue
                rel = fp.relative_to(EXTRA / scope).as_posix()   # ej: mods/MiMod.jar
                entry = {
                    "path": rel,                                  # dónde va en el juego
                    "url": f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/extra/{scope}/{rel}",
                    "sha256": sha256(fp),
                    "size": fp.stat().st_size,
                }
                for v in versions:
                    per_version[v].append(entry)

    out_dir = ROOT / "manifests"
    out_dir.mkdir(parents=True, exist_ok=True)
    for v in ("normal", "lite"):
        files = per_version[v]
        dest = out_dir / f"extra-{v}.json"
        dest.write_text(json.dumps(
            {"name": f"CobbleverseMMO — extra del equipo ({v})",
             "file_count": len(files), "files": files},
            indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"extra-{v}.json: {len(files)} archivo(s)")
        for f in files:
            print("   +", f["path"])


if __name__ == "__main__":
    main()
