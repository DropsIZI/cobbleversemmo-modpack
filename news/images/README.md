# Imágenes de noticias

Pon aquí las imágenes que quieras mostrar en las noticias del launcher.

## Cómo usarlas

1. Copia tu imagen en esta carpeta (`news/images/`). Recomendado: `.png` o `.jpg`, formato **horizontal** (ej. 1280×548 / proporción 21:9 se ve mejor en el lector de noticias).
2. En `news.json`, pon en el campo `"image"` la URL **raw** de tu imagen:

   ```
   https://raw.githubusercontent.com/DropsIZI/cobbleversemmo-modpack/main/news/images/TU-IMAGEN.png
   ```

   (cambia `TU-IMAGEN.png` por el nombre real de tu archivo)

3. Haz commit y push. El launcher la mostrará al instante (lee `news.json` en vivo).

## Consejos
- Usa nombres sin espacios ni acentos: `evento-verano.png`, no `Evento Verano.png`.
- Si dejas `"image": ""` la noticia sale sin imagen (con un marcador). Es válido.
- Pesa las imágenes (idealmente < 500 KB) para que carguen rápido.
