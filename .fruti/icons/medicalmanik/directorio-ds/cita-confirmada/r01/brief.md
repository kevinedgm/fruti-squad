# Brief funcional · Cita confirmada · r01

**Ruta:** R1 · **Fidelidad:** F2 (kit neutral) · **Fecha:** 2026-11-04
**Enunciado:** quien acaba de agendar (sin cuenta) necesita saber que su cita existe y tener lo necesario para llegar, porque no podrá volver a una cuenta a consultarla.
**Pregunta de diseño:** ¿qué debe ver y llevarse en este momento para no perder la cita?
**Verbo principal:** guardar la cita (en su calendario). **Resultado verificable:** la cita queda en su calendario y el mensaje llegó a su celular.

## Hechos
- Sin cuenta de paciente; confirmación y recordatorio por mensaje con enlace a «Detalle de su cita» (cambiar o cancelar).
- La consulta es presencial y se paga en el consultorio.
- Viene de «Confirma tu cita» (nombre + celular).

## Supuestos
- La cita queda confirmada al instante (el horario sale de la agenda del médico).
- El mensaje sale en segundos.

## Jerarquía
| Nivel | Contenido |
|---|---|
| N1 | «Tu cita está confirmada» · cuándo (día y hora completos) · con quién · dónde |
| N2 | Acción: Agregar a mi calendario · Cómo llegar · aviso del mensaje enviado (a qué número) |
| N3 | Precio y forma de pago · cambiar o cancelar · teléfono del consultorio · volver al inicio |

## Mecanismo del mensaje
- SMS con acentos o «ñ» se cobra en tramos de 70 caracteres (no de 160): el texto debe ser corto o se parte en varios mensajes. WhatsApp no tiene ese límite.
- El enlace del mensaje es la única puerta a la cita: debe funcionar sin iniciar sesión.

## Estados
- Confirmada (mensaje enviado) · No pudimos enviar el mensaje · Pendiente de que el médico acepte [incógnita] · Recordatorio del día anterior (mensaje).

## Incógnitas
1. ¿Canal: SMS, WhatsApp o ambos?
2. ¿Confirmación inmediata o el médico debe aceptar?
3. ¿Hasta cuándo se puede cancelar o cambiar (por ejemplo, 24 h antes)?
4. ¿El médico tiene indicaciones previas (llegar 10 min antes, estudios, ayuno)?
