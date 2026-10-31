# Uva · iconos de antecedentes clínicos (Expediente Manik) · ronda 1

Pedido del usuario (2026-10-31): iconos para alergias, personales no patológicos, personales patológicos, cirugías, vacunas, heredofamiliares, ginecoobstétricos y perinatales.

Revisión publicada: https://claude.ai/artifact/HFGvp1mpi99dKmJkwrKeP1 · `python3 gen.py` → `variantes/<id>-<v>.svg`, `variantes.json`; `revision.html` = `plantilla.html` + datos.

## E1 · Entender
- Contexto: pestañas/secciones de antecedentes del expediente; siempre con texto al lado (el icono ayuda a encontrar, no sustituye el nombre).
- Estilo: retícula 24, padding 2, **trazo 2** (el proyecto usa Lucide a 2; norma: un solo grosor por familia), puntas y uniones redondas, `currentColor`.
- Búsqueda en Lucide 1.66: coincidencias parciales syringe, baby, dna, scissors, hand, house-heart, thermometer; sin coincidencia para embarazo/útero ni alergia (solo «*-off» de alimentos). Se usan como variantes de referencia.

## E2/E3 · Variantes y evaluación (24; `check-icon.mjs`: 24/24 sin fallos bloqueantes)
| Concepto (id) | A | B | C | Recomendada |
|---|---|---|---|---|
| Alergias (allergies) | flor con polen | pastilla con admiración | mano con ronchas | **B**: la alergia crítica es a medicamentos |
| No patológicos (non-pathological-history) | persona con hoja | casa con corazón | manzana | **A**: pareja con patológicos |
| Patológicos (pathological-history) | persona con cruz | carpeta con cruz | termómetro | **A**: misma persona, cruz en vez de hoja |
| Cirugías (surgeries) | bisturí | tijeras (Lucide) | cicatriz con puntadas | **C**: propio de la consulta; tijeras = «cortar» |
| Vacunas (vaccines) | jeringa (Lucide) | frasco ámpula | jeringa vertical con gota | **B**: la jeringa diagonal = «medicamento» |
| Heredofamiliares (family-history) | genograma | ADN (Lucide) | adulto y niño | **A**: convención médica |
| Ginecoobstétricos (gyneco-obstetric-history) | útero | embarazo de perfil | símbolo femenino | **A**: reúne gineco y obstetricia; ♀ = «sexo» |
| Perinatales (perinatal-history) | bebé (Lucide) | recién nacido envuelto | huella de pie | **B**: bebé de Lucide = «pediatría» |

Corregido en el banco: pastilla con triángulo ilegible → admiración; bisturí que parecía espátula; frasco que parecía batería; escudo con jeringa recargado → jeringa vertical con gota.

## Pendiente
- Elección del usuario por concepto. Luego: SVG finales, registro semántico por icono (lo gobierna Lima) y prueba con médicos (¿se reconocen con su nombre?).
- Banco completo de Uva (`render-banco.mjs`) con confusiones a 16 px: no ejecutado en esta ronda; se usó un banco propio a 64/24/16 px.
