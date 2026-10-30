# Convia · paquete final de identidad (v1, 2026-10-30)

Directorio web de planes, lugares y talleres de Oaxaca. Marca independiente.

## Decisiones
- **Nombre:** Convia (convite + vía), con v.
- **Símbolo:** E1b, estrella de un solo trazo a mano, inclinada; abstraída de las estrellas del convite (`../convia-r7/E1b.svg`).
- **Dirección:** elegante y pulcra (el usuario descartó lo festivo/infantil de las rondas de color y tipo).
- **Color:** paleta Cantera: papel #f7f5f0, tinta #1b1d1a, cantera #2f5a45 (único acento), texto secundario #5b605a, línea #e2ded4; oscuro: #141714 / #f2f0ea / cantera clara #8fc4a8. Contrastes en `tema.json`.
- **Tipografía:** Gloock (logotipo y títulos) + Instrument Sans (todo lo demás). OFL.
- Color y tipografía los elegí yo con la dirección del usuario («elegancia, pulcritud»), pendientes de su confirmación.

## Archivos
- `svg/`: simbolo, simbolo-oscuro, simbolo-tinta (currentColor), logotipo, logotipo-oscuro, logotipo-tinta, palabra, app-icon, favicon (cambia con el tema), og (1200×630). Texto convertido a trazos.
- `png/`: app-icon 512/192/180, simbolo 512, og 1200×630.
- `tema.json`: tokens, contrastes, reglas.
- `guia.html`: guía de marca (publicada como página).
- Regenerar: `python3 gen.py <carpeta con Gloock.ttf>` y `node png.cjs`.

## Pendiente
- Marcanet (IMPI) clases 9, 35, 39, 42; dominios y redes.
- Guía de fotografía.
- Textos de marca en inglés.
