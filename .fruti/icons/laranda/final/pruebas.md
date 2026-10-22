# Pruebas de color · Laranda

## Validador de paleta (OKLab, CVD), modo claro sobre hueso #F6F4EF, todas las parejas

Palette (light, surface #F6F4EF, categorical): 5 slots
  [PASS] Lightness band         all 5 inside L 0.43–0.77
  [PASS] Chroma floor           all 5 >= 0.1
  [WARN] CVD separation         worst all-pairs #0E8F5E↔#E0611A ΔE 7.4 (protan) · tritan 14.8
  [PASS] Normal-vision floor    worst all-pairs #D9A400↔#E0611A ΔE 15.7 (normal)
  [WARN] Contrast vs surface    below 3:1 — relief required (visible labels or table view): [["#D9A400",2.06]]

  → ALL CHECKS PASS  (CVD in the 6–8 floor band is legal ONLY with secondary encoding: direct labels, gaps, or texture)
  scope: categorical palettes only. For a lone status/text color check WCAG text contrast; for a sequential ramp, lightness monotonicity.


## Modo oscuro

El brief no define modo oscuro. Este paquete deriva solo los dos colores de marca para fondos oscuros (lila #C4B5F0 y naranja oscuro #F2A074, contrastes abajo). Los colores de estado en oscuro quedan sin definir: deben validarse cuando exista el design system.

## Contraste WCAG
tinta/hueso                      16.83:1  AA texto
tinta suave/hueso                 7.71:1  AA texto
violeta/hueso                     6.98:1  AA texto
blanco/violeta                    7.67:1  AA texto
naranja/hueso                     3.24:1  AA grande / gráfico
tinta/naranja tinte              12.13:1  AA texto
tinta/oro                         8.16:1  AA texto
blanco/verde                      4.11:1  AA grande / gráfico
blanco/rojo                       7.21:1  AA texto
hueso/tinta                      16.83:1  AA texto
lila/tinta                        9.88:1  AA texto
naranja oscuro/tinta              8.86:1  AA texto
violeta/lila (icono app)          4.10:1  AA grande / gráfico
hueso/violeta (línea app icon)    6.98:1  AA texto

Lectura: todo texto de interfaz va en tinta o tinta suave sobre hueso (AA). El naranja y el verde sobre hueso o con texto blanco pasan solo como texto grande o como gráfico: botones y chips de esos colores llevan texto de 18 px o más, o texto en tinta. El oro siempre lleva texto en tinta.

Simulación de daltonismo (Machado 2009, protanopia, deuteranopia, tritanopia) sobre la lámina: `png/daltonismo.png`.
