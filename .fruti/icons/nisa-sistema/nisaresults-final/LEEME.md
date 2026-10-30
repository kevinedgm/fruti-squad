# NisaResults · paquete final

Portal de clientes de Nisa Nabani: cada cliente consulta sus resultados e informes y decide si publica la página de calidad de su agua con un código QR para sus huéspedes. Producto hermano de NisaLab y NisaData; es el que ve el cliente, por eso usa colores del manual de Nisa Nabani.

## Símbolo · Banda de control
Dos límites (barras de 88 × 7, radio 3.5) y tres células dentro (radios 9, 11 y 9); la del centro, más grande y en cian. Es la gráfica de monitoreo con su zona aceptable convertida en símbolo.

## Color
| Color | Hex | Uso | Contraste |
|---|---|---|---|
| Azul real | #052A76 | Símbolo, logotipo, encabezado del portal, acción principal | Blanco encima 13.1:1 |
| Cian | #00B4D8 | Una célula del símbolo, sección activa, punto del último análisis | Sobre azul 5.3:1 · sobre blanco 2.5:1 (nunca texto) |

Óptimo (verde) y No óptimo (rojo) son estados de resultado: la marca nunca usa verde ni rojo.

## Archivos (`svg/`, `png/`)
- `simbolo`, `simbolo-blanco`, `simbolo-1tinta`; `sello` (símbolo en círculo para la página pública).
- `logotipo`, `logotipo-blanco`, `logotipo-1tinta`, `logotipo-respaldo`, `logotipo-respaldo-blanco`, `logotipo-vertical`: «Nisa» Poppins 700 + «Results» Poppins 400, a trazos.
- `app-icon`, `app-icon-maskable`, `favicon`: PNG de 16 a 512 px.
- `tema.json`. Regenerar: `python3 gen.py <woff de Poppins> <carpeta temporal> <fuentes para la lámina>` y `node png.cjs`.

## Reglas
1. Una sola célula cian por símbolo.
2. La marca nunca usa verde ni rojo.
3. En la página pública manda la marca del cliente; el sello dice «Analizada por Nisa Nabani · laboratorio».
4. Cada resultado público cita contra qué norma o criterio se compara y la fecha de la última muestra.
5. Barras siempre horizontales; el símbolo no se rota.

## Pendiente
- Búsqueda de anterioridades de «NisaResults» ante el IMPI; subdominio.
- Confirmar la norma de referencia de cada tipo de agua (para uso y consumo humano: probablemente NOM-127-SSA1-2021; albercas: norma propia). No verificado.
- Quién decide qué parámetros y puntos se publican, y qué pasa con un resultado «No óptimo» en la página pública.
