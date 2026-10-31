# Uva · consulta inmediata (Agenda Manik) · r1

Pedido del usuario (2026-10-31): icono para «consulta inmediata» (alguien quiere consulta médica ya), en un botón flotante en una esquina de la agenda.

Revisión: https://claude.ai/artifact/X94LrvANnnwxHX4u1WexqH · `python3 gen.py` → `variantes/immediate-consult-<v>.svg`, `revision.html`.

## E1
- semanticName: `immediate-consult` · concepto: **ahora, sin cita** (no urgencia). Se descartan sirena y ambulancia (dicen «emergencia»).
- Lucide 1.66: sin coincidencia; partes: calendar-clock, calendar-plus, timer, zap («quick» entre sus etiquetas).
- Estilo: retícula 24, trazo 2 (Lucide de las apps Manik), `currentColor`; en el botón, blanco sobre azul Manik.
- Confusiones probadas dentro del botón: plus, calendar-plus, zap, timer, cross, siren.

## E2/E3 (check-icon: 3/3 sin fallos bloqueantes)
- **A · Calendario con rayo** [recomendada]: hermano de «Nueva cita» (calendar-plus): cita normal vs. cita ya. Riesgo: rayo = energía/flash, mitigado por el calendario y el texto.
- B · Cronómetro con cruz: riesgo «tiempo de espera».
- C · Cruz con estela: riesgo, dentro de un botón flotante la cruz se lee «+ agregar».

## Reglas del botón [propuesta]
Con texto en pantallas anchas («Consulta inmediata»); solo icono en el teléfono con `aria-label` y etiqueta al tocar/pasar el cursor · azul Manik, un solo botón flotante por pantalla · quieto en reposo; pacientes en espera como insignia numérica · abajo a la derecha a 16 px, por encima de la barra inferior.

## Pendiente
Elección del usuario · ¿quién lo usa? (supuesto: la asistente registra a un paciente que llega sin cita; si es el paciente desde manik, cambia el texto, no el icono) · registro semántico (Lima).
