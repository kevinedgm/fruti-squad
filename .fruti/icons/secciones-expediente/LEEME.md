# Uva · iconos de sección del expediente · r1

Pedido del usuario (2026-11-01): un icono para la sección donde se registran valores de laboratorio (colesterol, triglicéridos, HbA1c, glucosa) y otro para la sección de exploración física (habitus exterior, cabeza, cuello, tórax, abdomen, extremidades y más).

Revisión: `revision.html` (publicada) · `python3 gen.py`. Misma familia que `../antecedentes/` (retícula 24, trazo 2, formas simples).

## E1
- Lucide 1.66: test-tube, test-tubes (laboratorio de química), stethoscope («médico/consulta» en general), person-standing, scan; ninguno dice «exploración física».
- Confusiones a evitar: gota = glucosa (iconos previos); busto = antecedentes personales; estetoscopio = consulta.

## Variantes (check-icon 6/6 sin fallos bloqueantes)
| Sección (id) | A | B | C | Recomendada |
|---|---|---|---|---|
| Laboratorio (lab-results) | tubo de muestra con tapón y nivel | hoja de resultados con gota | dos tubos (Lucide) | **A** |
| Exploración física (physical-exam) | cuerpo en encuadre de revisión | cuerpo de frente | estetoscopio (Lucide) | **A** |

## Pendiente
Elección · registro semántico (Lima) · ¿iconos por región dentro de la exploración (cabeza, tórax, abdomen…)? No se pidieron.
