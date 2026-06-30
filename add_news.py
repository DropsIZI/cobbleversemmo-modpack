#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agregar noticia al launcher — asistente sencillo.
==================================================
Ejecuta:  python add_news.py

Te hace unas preguntas y añade la noticia ARRIBA del todo en news.json
(las más nuevas se muestran primero en el launcher).

Después solo tienes que hacer commit y push:
    git add news.json news/images
    git commit -m "Nueva noticia: <titulo>"
    git push
"""

import json
import sys
from datetime import date
from pathlib import Path

NEWS_FILE = Path(__file__).parent / "news.json"
RAW_BASE = "https://raw.githubusercontent.com/DropsIZI/cobbleversemmo-modpack/main/news/images/"

MESES = ["ene", "feb", "mar", "abr", "may", "jun",
         "jul", "ago", "sep", "oct", "nov", "dic"]

TAGS_SUGERIDOS = ["EVENTO", "POKÉMON", "PARCHE", "REGIÓN", "TORNEO", "AVISO"]


def hoy():
    d = date.today()
    return f"{d.day:02d} {MESES[d.month - 1]} {d.year}"


def preguntar(texto, obligatorio=True, default=""):
    while True:
        v = input(texto).strip()
        if v:
            return v
        if not obligatorio:
            return default
        print("  (este campo es obligatorio)")


def main():
    print("=" * 58)
    print("  Agregar noticia al launcher CobbleverseMMO")
    print("=" * 58)
    print()

    if NEWS_FILE.exists():
        try:
            data = json.loads(NEWS_FILE.read_text(encoding="utf-8"))
        except Exception:
            print("  ⚠ news.json está dañado. Revísalo antes de continuar.")
            sys.exit(1)
    else:
        data = {"news": []}
    if isinstance(data, list):
        data = {"news": data}
    news = data.setdefault("news", [])

    print("  Etiquetas sugeridas:", ", ".join(TAGS_SUGERIDOS))
    tag = preguntar("  Etiqueta (ej. EVENTO): ").upper()

    title = preguntar("  Título: ")
    text = preguntar("  Resumen corto (1-2 frases, sale en la tarjeta): ")

    print("\n  Cuerpo de la noticia (texto completo del lector).")
    print("  Escribe un párrafo por línea. Línea vacía para terminar:")
    body = []
    while True:
        linea = input("   > ").strip()
        if not linea:
            break
        body.append(linea)
    if not body:
        body = [text]

    print("\n  Imagen (opcional).")
    print("  1) Pon tu imagen en la carpeta news/images/")
    print("  2) Escribe SOLO el nombre del archivo (ej. evento-verano.png)")
    print("  3) Déjalo vacío para una noticia sin imagen.")
    img_name = preguntar("  Nombre de la imagen: ", obligatorio=False)
    if img_name:
        img_path = NEWS_FILE.parent / "news" / "images" / img_name
        if not img_path.exists():
            print(f"  ⚠ Aviso: no encuentro news/images/{img_name}.")
            print("    Recuerda copiar la imagen ahí antes de hacer push.")
        image = RAW_BASE + img_name
    else:
        image = ""

    entry = {
        "tag": tag,
        "date": hoy(),
        "title": title,
        "text": text,
        "body": body,
        "image": image,
    }

    news.insert(0, entry)  # la más nueva primero

    NEWS_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("\n" + "=" * 58)
    print("  ✓ Noticia añadida a news.json")
    print("=" * 58)

    print("\n  ¿Subir a GitHub ahora? (s = sí / n = lo subo yo luego)")
    if preguntar("  > ", obligatorio=False).strip().lower() in ("s", "si", "sí", "y", "yes"):
        import subprocess
        here = NEWS_FILE.parent
        try:
            subprocess.run(["git", "add", "news.json", "news/images"], cwd=here, check=True)
            subprocess.run(["git", "commit", "-m", f"Noticia: {title}"], cwd=here, check=True)
            subprocess.run(["git", "push"], cwd=here, check=True)
            print("\n  ✓ ¡Subido! La noticia aparecerá en el launcher al instante.\n")
        except Exception:
            print("\n  ⚠ No se pudo subir automáticamente (¿git instalado / con acceso?).")
            print("    Súbela a mano:")
            print("      git add news.json news/images")
            print(f'      git commit -m "Noticia: {title}"')
            print("      git push\n")
    else:
        print("\n  Cuando quieras subirla:")
        print("    git add news.json news/images")
        print(f'    git commit -m "Noticia: {title}"')
        print("    git push\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n  Cancelado.")
