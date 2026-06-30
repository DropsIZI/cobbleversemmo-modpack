# Carpeta `extra/` — contenido propio del equipo

Aquí el equipo sube **sus propios** mods, datapacks y resource packs (los que NO
vienen de Modrinth/CurseForge). El launcher los descarga **automáticamente**.

## Elige la versión donde va tu archivo

| Carpeta | Va a... |
|---|---|
| **`extra/ambos/`** | Normal **y** Lite (lo más común) |
| **`extra/normal/`** | solo **Normal** |
| **`extra/lite/`** | solo **Lite** |

Dentro de cada una, mete el archivo en su subcarpeta:
- **`mods/`** → mods `.jar` (para **Fabric 1.21.1**)
- **`datapacks/`** → datapacks `.zip` (Pokémon nuevos, etc.)
- **`resourcepacks/`** → texturas `.zip`

Ejemplo: un mod para las dos versiones → `extra/ambos/mods/mimod.jar`

## Cómo subir (sin instalar nada)

1. Entra a https://github.com/DropsIZI/cobbleversemmo-modpack
2. Navega a la carpeta correcta (ej. `extra/ambos/mods`)
3. **Add file → Upload files** → arrastra tu archivo → **Commit changes**

Un robot (GitHub Action) regenera la lista solo, y al siguiente **JUGAR** los
jugadores lo descargan.

## Quitar algo (¡y que se borre del PC de los jugadores!)

Borra el archivo de su carpeta aquí en GitHub (botón 🗑️ → Commit). El launcher
detecta que ya no está y **lo elimina automáticamente del PC de cada jugador** en
su siguiente JUGAR. (No toca los mods que el jugador haya añadido por su cuenta.)

## Notas
- Es para contenido **propio y ligero**. Los mods grandes de terceros los gestiona
  el encargado con el perfil de Modrinth.
- El `.jar` debe ser para **Fabric 1.21.1** o no cargará.
