# Declaración de cumplimiento · FichaMedico · r02

| Campo | Valor |
|---|---|
| Ruta | R2 (Actual + A/B/C) |
| Fidelidad | F2 |
| Pregunta de diseño | La de r01, más: ¿se entiende un consultorio que agenda en línea y por teléfono, y los botones tienen el peso, la densidad y la forma correctos? |
| Artefactos | brief.md (delta) · propuestas/index.html (y publicar.html) · hallazgos.md · declaracion.md |
| Modifica producción | No |

## Estándares leídos
Los mismos de r01 (`agentes/kiwi/references/…`, `.fruti/contracts/adaptativo.md`, kit neutral), WCAG 2.2 AA.

## Desviaciones del protocolo
- Las de r01 (referencias de la skill tomadas de Kiwi en el repo; una principal por ficha).
- «Actual» se deja como referencia sin la revisión de botones, para comparar.

## Comprobaciones ejecutadas
- check_artifact.py: ✔ (0 errores, 0 avisos).
- Navegador: 4 versiones × 3 marcos × 8 estados = 96 combinaciones · errores JS: 0 · desborde: 0 · controles < 24 px: 0 · fichas con más de una principal: 0.
- Medición de botones en compact 393 (área sólida / tipos): Actual 5–11 % · A 3–5 % · B 4–5 % · C 3–6 %.
- Estados: los de r01 + consultorio con ambas formas (con y sin conexión).

## Matriz de adaptación
Igual que r01, más:
| Elemento | compact | medium | expanded | Motivo | Técnica | Foco/estado |
|---|---|---|---|---|---|---|
| Acción principal | A su ancho, a la derecha | Igual | Igual | Peso y alcance del pulgar | flex con margen automático | — |
| «o llama al …» (ambas formas) | Línea propia sobre la acción | Igual | Igual | No cabe junto al botón a 390 | Bloque | Enlace `tel:` con número visible |
| Sin conexión, ambas formas | «Llamar» pasa a principal | Igual | Igual | Agendar requiere red | Estado | Aviso de por qué |

## Comprobaciones NO ejecutadas
- Texto ampliado al 200 %, teclado y lector de pantalla, prueba con pacientes, F3 con el cian real.

## Traspaso
- **→ lima:** decidir si los horarios dejan la píldora (regla del sistema) y el modelo de forma de agendar con «ambas».
- **→ coco:** F3 de la versión elegida.

## Siguiente paso del usuario
Elegir A, B o C.
