# Convia · manual de identidad (v2, 2026-10-30)

Directorio web de planes, lugares y talleres de Oaxaca. Marca independiente.

## Decisiones
- **Nombre:** Convia (convite + vía), con v.
- **Símbolo:** E1b, estrella de un solo trazo a mano, inclinada; abstraída de las estrellas del convite (`../convia-r7/E1b.svg`).
- **Dirección:** elegante y pulcra (el usuario descartó lo festivo/infantil de las rondas de color y tipo).
- **Color:** paleta Cantera: papel #f7f5f0, tinta #1b1d1a, cantera #2f5a45 (único acento), texto secundario #5b605a, línea #e2ded4; oscuro: #141714 / #f2f0ea / cantera clara #8fc4a8. Contrastes en `tema.json`.
- **Tipografía (aprobada por el usuario):** Fraunces 500 con SOFT 100 (logotipo y títulos) + Figtree (texto). Sustituye a Gloock + Instrument Sans: el usuario notó que lo recto no hacía juego con la estrella suave.
- **Forma:** radio 16 px (tarjetas, fotos), 12 px (campos), botones en píldora.
- **Color por categoría:** cafés, restaurantes, hoteles boutique, talleres, museos y galerías, recorridos; tres tonos cada una (punto, fondo, texto AA). Validado con el validador de paletas: separación con daltonismo PASS (ΔE 8.9); entre ámbar y naranja ΔE 14.9 (casi 15); ámbar y verde agua bajo 3:1 sobre papel. Por eso la categoría siempre lleva su nombre.

## Submarcas por categoría
- `sellos/<categoria>-sello.svg` (claro), `-sello-solido.svg`, `-logotipo.svg` («Convia | Categoría»); PNG 512 en `png/`. Generar: `python3 sellos.py <carpeta con Fraunces-Suave-500.ttf y Figtree-650.ttf>` y `node sellos-png.cjs`.
- Sello mínimo 64 px; la estrella del logotipo de categoría siempre en cantera.

## Íconos de categoría
- `iconos/<categoria>.svg` (currentColor) y `<categoria>-color.svg` (sobre su fondo). Trazo de plumón con terminaciones redondas, familia de la estrella. Generar: `python3 iconos.py`. Siempre junto al nombre; mínimo 16 px.

## Archivos
- `svg/`: simbolo, simbolo-oscuro, simbolo-tinta (currentColor), logotipo, logotipo-oscuro, logotipo-tinta, palabra, app-icon, favicon (cambia con el tema), og (1200×630). Texto convertido a trazos.
- `png/`: app-icon 512/192/180, simbolo 512, og 1200×630.
- `tema.json`: tokens, contrastes, reglas.
- `guia.html`: manual de identidad (publicado como página), generado con `guia.py`.
- Regenerar: `python3 gen.py <carpeta con Fraunces-Suave-500.ttf>`, `node png.cjs`, `python3 guia.py`.

## Pendiente
- Marcanet (IMPI) clases 9, 35, 39, 42; dominios y redes.
- Guía de fotografía.
- Aplicar los colores de categoría a la portada web (`../convia-web-r1/`).
- Textos de marca en inglés.
