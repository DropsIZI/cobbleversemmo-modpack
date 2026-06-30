# Carpeta `extra/` — contenido propio del equipo

Aquí el equipo sube **sus propios** mods, datapacks y resource packs (los que NO
vienen de Modrinth/CurseForge). El launcher los descarga **automáticamente** junto
con el modpack base.

## Cómo subir algo (¡sin instalar nada!)

1. Entra a https://github.com/DropsIZI/cobbleversemmo-modpack
2. Abre la carpeta correcta:
   - **`extra/mods/`** → tus mods propios (`.jar`, para **Fabric 1.21.1**)
   - **`extra/datapacks/`** → datapacks (Pokémon nuevos, etc.) (`.zip`)
   - **`extra/resourcepacks/`** → texturas / resource packs (`.zip`)
3. Botón **Add file → Upload files** → arrastra tu archivo → **Commit changes**

¡Listo! Un robot (GitHub Action) regenera la lista automáticamente y, al siguiente
**JUGAR**, todos los jugadores lo descargan.

## Notas
- Esto es para contenido **propio y ligero**. Los mods grandes de Modrinth/CurseForge
  (Cobblemon, Sodium…) los gestiona el encargado del modpack con el perfil de Modrinth.
- El archivo se aplica a **ambas** versiones (Normal y LITE).
- Para **quitar** algo: bórralo de su carpeta aquí en GitHub (botón 🗑️) y commit.
  (Ojo: a los jugadores que ya lo descargaron no se les borra solo; solo deja de
  ser obligatorio.)
- Que el `.jar` sea para **Fabric 1.21.1** o no cargará.
