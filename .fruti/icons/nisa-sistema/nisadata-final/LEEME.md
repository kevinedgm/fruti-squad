# NisaData · paquete final

Panel de analítica de Nisa Nabani: tendencias, comportamiento y salud del laboratorio. Lee los datos de NisaLab. Es producto hermano de NisaLab: nombre y símbolo propios, mismo patrón «Nisa» + palabra y mismo respaldo «de Nisa Nabani».

## Símbolo · Columnas de células
Tres columnas de 1, 2 y 3 células: datos que crecen. Radios 10, 12 y 14; separación constante de 4 (como Colonia); base común. La célula de arriba de la columna alta es la única mandarina.

## Color
| Color | Hex | Uso | Contraste |
|---|---|---|---|
| Grafito | #1F2532 | Símbolo, logotipo, fondo del ícono de app | Blanco encima 15.3:1 |
| Mandarina | #FF8A1F | Una célula del símbolo y acentos de marca | Grafito encima 6.5:1 · sobre blanco 2.4:1 (nunca texto) |

## Archivos (`svg/`, `png/`)
- `simbolo`, `simbolo-blanco` (sobre grafito), `simbolo-1tinta` (`currentColor`).
- `logotipo`, `logotipo-blanco`, `logotipo-1tinta`, `logotipo-respaldo`, `logotipo-respaldo-blanco`, `logotipo-vertical`: «Nisa» Poppins 700 + «Data» Poppins 400, a trazos.
- `app-icon`, `app-icon-maskable` (zona segura 80 %), `favicon`: PNG de 16 a 512 px (incluye 180 y 192).
- `tema.json`: colores, contrastes y reglas. Regenerar: `python3 gen.py <woff de Poppins> <carpeta temporal> <fuentes para la lámina>` y `node png.cjs`.

## Reglas
1. Una sola célula mandarina por símbolo.
2. El color de producto vive en marca, ícono de app, acceso y navegación; nunca en tablas ni en estatus.
3. La mandarina no es alerta ni estado (no «pago parcial», avisos ni errores).
4. Las gráficas del panel usan su propia paleta de datos, no grafito y mandarina.
5. No rotar ni reacomodar las columnas; la base siempre abajo.
6. Mínimo 16 px en pantalla y 6 mm impreso.

## Pendiente
- Búsqueda de anterioridades de «NisaData» ante el IMPI.
- Paleta de datos para las gráficas del panel.
