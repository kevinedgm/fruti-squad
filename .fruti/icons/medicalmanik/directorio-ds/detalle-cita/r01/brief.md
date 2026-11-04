# Brief funcional · Detalle de su cita · r01

**Ruta:** R1 · **Fidelidad:** F2 (kit neutral) · **Fecha:** 2026-11-04
**Entrada:** el enlace del mensaje de confirmación o del recordatorio (sin cuenta, sin iniciar sesión).
**Enunciado:** quien agendó necesita revisar, cambiar o cancelar su cita sin cuenta, porque sus planes cambiaron o quiere saber cómo llegar.
**Pregunta de diseño:** ¿cómo dejar cambiar o cancelar fácil sin que se cancele por error, y qué pasa cuando ya no se puede?
**Verbos:** revisar · cambiar · cancelar. **Resultado verificable:** el nuevo mensaje confirma el cambio o la cancelación.

## Hechos
- Cambiar o cancelar: hasta 24 h antes de la cita (usuario, 2026-11-04).
- Confirmación inmediata, sin aceptación del médico; no hay cuenta de paciente.

- El enlace vence al terminar el día siguiente a la cita (usuario, 2026-11-04).

## Inferencias / reglas propuestas
- A menos de 24 h: «Cambiar» y «Cancelar» no se ofrecen; se explica por qué y se ofrece llamar al consultorio.
- Las 24 h se cuentan en la zona horaria del consultorio.
- Cambiar = elegir otro horario del mismo consultorio; la hora anterior se libera al confirmar el cambio (no antes).
- Cancelar es destructivo: pide confirmación con la fecha y la hora escritas; «No, conservarla» es la opción segura.
- Cita pasada: se ofrece «Opinar» (solo quien tuvo cita puede opinar: aquí nacen las opiniones verificadas).

## Riesgo por acción
| Acción | Tipo | Confirmación |
|---|---|---|
| Cómo llegar · Agregar al calendario | Reversible | No |
| Cambiar fecha u hora | Reversible (se puede volver a cambiar si faltan más de 24 h) | Resumen «de → a» antes de confirmar |
| Cancelar | Destructiva (libera el horario) | Diálogo con fecha y hora |

## Seguridad (recomendación)
- El enlace no pide sesión: quien lo tenga puede cancelar. El código del enlace debe ser largo e imposible de adivinar; cada cambio o cancelación avisa por mensaje al celular de la cita.

## Estados
Más de 24 h · Elegir nueva hora · Confirmar cancelación · Cancelada · Menos de 24 h · Cita pasada · Enlace vencido o inválido · El consultorio canceló.
