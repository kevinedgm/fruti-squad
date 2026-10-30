# NisaLab · áreas · paquete final

Cada división de Nisa Nabani tiene su identidad dentro de NisaLab: «Área NisaLab» (por ejemplo, «Aguas NisaLab»). La célula que creció de Colonia toma el color y el ícono del área; el resto del racimo sigue azul real.

## Áreas
| Área | Token | Color | Blanco encima |
|---|---|---|---|
| Aguas | `area-aguas` | #007CA3 | 4.8:1 |
| Agrícolas | `area-agricolas` | #946400 | 5.1:1 |
| Ambiental | `area-ambiental` | #2F8247 | 4.8:1 |
| Alimentos | `area-alimentos` | #A6552D | 5.3:1 |
| Bebidas | `area-bebidas` | #7A5DA9 | 5.3:1 |
| Bebidas de agave | `area-agave` | #008478 | 4.6:1 |
| Farmacia | `area-farmacia` | #A14E78 | 5.4:1 |
| Consultoría | `area-consultoria` | #4C6BB4 | 5.2:1 |

Paleta en OKLCH con la misma luminosidad (0.54) e intensidad (0.12); solo cambia el tono, fuera del rango del pera.

## Archivos por área (`svg/<área>/`)
- `marca.svg`, `marca-blanco.svg` (sobre azul), `marca-1tinta.svg` (`currentColor`, ícono calado).
- `icono.svg` y `icono-1tinta.svg`: el ícono solo, en círculo, para listas, filtros y etiquetas.
- `logotipo.svg`, `logotipo-blanco.svg`, `logotipo-1tinta.svg`: el área en Poppins 600 y «NisaLab» en Poppins 400, convertidos a trazos.
- `png/<área>/`: marca, marca-blanco e ícono a 16, 32, 64, 128 y 512 px; logotipos a 512 y 1024 px de ancho.
- `tema.json`: paleta, tokens y contrastes. Regenerar: `python3 gen.py <carpeta con poppins-latin-*-normal.woff> <carpeta temporal>` y `node png.cjs`.

## Reglas
1. El color del área solo identifica el área; nunca indica estado (los estados tienen sus propios colores).
2. El ícono siempre va en blanco sobre el color del área, o calado en la versión a una tinta.
3. El nombre del área siempre acompaña a la marca o al ícono: el color no es la única señal.
4. El racimo de Colonia no se rota ni se reacomoda; solo cambia la célula que creció.
5. Los colores de área nunca aparecen en tablas: ahí todo color es estatus. En tablas se usa `icono-1tinta.svg` en gris + nombre.
6. Mínimo 16 px en pantalla; a 24 px o menos, lo que se lee es el color, por eso el nombre es obligatorio.

## Pendiente
- Confirmar si «Bebidas alcohólicas» sustituye a «Bebidas de agave», es un área nueva o queda como en el manual.
