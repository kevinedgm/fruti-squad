# NisaLab · paquete final de marca

NisaLab es el sistema de laboratorio de Nisa Nabani. Se escribe «NisaLab», junto y con dos mayúsculas. Respaldo: «de Nisa Nabani».

Arquitectura: **Nisa Nabani** (empresa) → **NisaLab** (sistema) → **«Producto NisaLab»** (productos, por definir).

## Símbolo: Colonia
Cuatro células tangentes con la misma separación entre ellas; una sola en pera, arriba a la derecha: la que creció. Lo vivo que el laboratorio detecta, cuenta y certifica.

## Archivos
- `svg/simbolo.svg` (azul real y pera), `simbolo-1tinta.svg` (`currentColor`), `simbolo-blanco.svg` (blanco y pera, sobre azul).
- `svg/logotipo.svg`, `logotipo-blanco.svg`, `logotipo-1tinta.svg`, `logotipo-respaldo.svg` («de Nisa Nabani»), `logotipo-vertical.svg`. «Nisa» en Poppins 700 y «Lab» en Poppins 400, convertidos a trazos.
- `svg/app-icon.svg` (1024, símbolo blanco y pera sobre azul), `app-icon-maskable.svg` (zona segura de PWA) y `favicon.svg`.
- `png/<archivo>-{16,32,64,128,512}.png` para símbolo, íconos y favicon; `png/<logotipo>-{512,1024}.png` para logotipos. Con transparencia, salvo los íconos de app.
- `tema.json`: colores, contrastes, tipografía y tamaño mínimo.
- Regenerar: `python3 gen.py <carpeta con poppins-latin-*-normal.woff> <carpeta temporal>` y después `node png.cjs`.

## Reglas
1. El racimo es fijo: no se rota, no se reacomoda ni se le quitan o agregan células.
2. Una sola célula pera. El pera nunca es texto (1.7:1 sobre blanco).
3. Sobre azul se usa `simbolo-blanco`; en documentos a una tinta, `simbolo-1tinta`.
4. Área de respeto: el ancho de la célula grande alrededor de toda la pieza. Mínimo 16 px en pantalla y 6 mm impreso.
5. El logo de Nisa Nabani y el de NisaLab no se mezclan en una sola pieza: NisaLab lleva «de Nisa Nabani» como respaldo.

## Pendiente
- Revisar registro de marca de «NisaLab» en el IMPI y disponibilidad del dominio.
- Definir los productos («Recepción NisaLab», etc.) y su sello.
- Actualizar el design system de Nabi a NisaLab (nombre, símbolo y portada).
