# 👋 CobbleverseMMO — Guía para el equipo

Bienvenido/a. Aquí subes **mods, datapacks, texturas y noticias** del modpack.
**No necesitas instalar nada** — todo se hace desde esta web (github.com). 🎉

---

## 1. Primer paso (una sola vez)

Te llega un email de GitHub: **"DropsIZI invited you to collaborate"** → pulsa
**Accept invitation**. (O entra a https://github.com/DropsIZI/cobbleversemmo-modpack/invitations)

Ya está. Con eso puedes editar todo.

---

## 2. Subir un mod / datapack / textura propio

1. Aquí en GitHub, entra a la carpeta **`extra`** y elige dónde va:
   - **`extra/ambos`** → se aplica a Normal **y** Lite (lo normal)
   - **`extra/normal`** → solo a la versión Normal
   - **`extra/lite`** → solo a la versión Lite
2. Dentro, entra a la subcarpeta según el tipo:
   - **`mods`** → mods `.jar`
   - **`datapacks`** → datapacks `.zip` (Pokémon nuevos, etc.)
   - **`resourcepacks`** → texturas `.zip`
3. Pulsa **`Add file ▾` → `Upload files`**
4. **Arrastra tu archivo** a la página
5. Abajo, botón verde **`Commit changes`**

✅ ¡Listo! En ~1 minuto se procesa solo y, al siguiente **JUGAR**, todos los
jugadores lo descargan automáticamente. Varios podéis subir a la vez sin pisaros.

> Ejemplo: un mod para las dos versiones → lo subes a `extra/ambos/mods/`

---

## 3. Quitar un mod que da fallo

¿Un mod rompe el juego? Bórralo:

1. Entra al archivo (ej. `extra/ambos/mods/elmod.jar`)
2. Pulsa el icono de **papelera 🗑️** (arriba a la derecha) → **Commit changes**

✅ El launcher lo **borra solo del PC de cada jugador** en su siguiente JUGAR.
(No toca los mods que el jugador haya puesto por su cuenta.)

---

## 4. Poner una noticia o evento (con imagen)

1. **Si tu noticia lleva imagen:** súbela primero a la carpeta **`news/images`**
   (igual que un mod: Add file → Upload files).
2. Abre el archivo **`news.json`** → icono **lápiz ✏️** (editar).
3. Copia este bloque **arriba del todo** (justo después de `"news": [`) y rellénalo:

   ```json
   {
     "tag": "EVENTO",
     "date": "1 jul 2026",
     "title": "Título de tu noticia",
     "text": "Resumen corto (1-2 frases, sale en la tarjeta).",
     "body": [
       "Primer párrafo del texto completo.",
       "Segundo párrafo."
     ],
     "image": "https://raw.githubusercontent.com/DropsIZI/cobbleversemmo-modpack/main/news/images/TU-IMAGEN.png"
   },
   ```
   - Cambia `TU-IMAGEN.png` por el nombre real de tu imagen. Si no lleva imagen, pon `"image": ""`.
   - Pon una coma `,` al final del bloque si hay más noticias debajo.
4. Abajo, **`Commit changes`**.

✅ Aparece en el launcher **al instante**.

---

## ⚠️ Importante

- Los **mods** deben ser para **Fabric 1.21.1** o no cargarán.
- Esta carpeta `extra` es para contenido **propio y ligero**. Los mods grandes de
  Modrinth/CurseForge (Cobblemon, Sodium…) los gestiona el encargado del modpack.
- Los **datapacks de Pokémon** también tienen que estar en el **servidor** para que
  funcionen del todo (eso lo hace el admin aparte).

---

## ¿Dudas?
Pregunta en el Discord del equipo. ¡A darle caña! 🐉
