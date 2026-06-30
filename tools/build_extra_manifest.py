#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera manifests/extra.json a partir de la carpeta extra/.
=========================================================
Lo ejecuta AUTOMÁTICAMENTE el GitHub Action cada vez que alguien sube algo a
extra/ (mods, datapacks o resourcepacks propios del equipo). No hace falta
ejecutarlo a mano.

El launcher descarga estos archivos DIRECTAMENTE del repo (raw), así que tus
compañeros solo tienen que subir el archivo a extra/ — nada más.
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
IGNORE = {"readme.md", ".gitkeep"}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    files = []
    for cat in CATEGORIES:
        d = EXTRA / cat
        if not d.is_dir():
            continue
        for fp in sorted(d.rglob("*")):
            if not fp.is_file():
                continue
            if fp.name.lower() in IGNORE or fp.name.startswith("."):
                continue
            rel = fp.relative_to(EXTRA).as_posix()       # ej: mods/MiMod.jar
            files.append({
                "path": rel,                              # dónde va en el juego
                "url": f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/extra/{rel}",
                "sha256": sha256(fp),
                "size": fp.stat().st_size,
            })

    out = {
        "name": "CobbleverseMMO — contenido del equipo (extra)",
        "file_count": len(files),
        "files": files,
    }
    dest = ROOT / "manifests" / "extra.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"extra.json generado: {len(files)} archivo(s)")
    for f in files:
        print("  +", f["path"])


if __name__ == "__main__":
    main()
