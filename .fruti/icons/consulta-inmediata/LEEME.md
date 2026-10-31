# Uva · consulta inmediata (Expediente Manik) · r1

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

## Decisión del usuario (2026-10-31)
**Variante A, calendario con rayo.** La usa **el médico desde Expediente Manik** (no Agenda). Archivo final `immediate-consult.svg`; entrada propuesta en `registro.yaml`.

## Consecuencia propuesta (rechazada por el usuario, 2026-10-31)
Se propuso que el botón «+ Nueva consulta» de la barra lateral de Expediente (prototipo `../medicalmanik/calendario/`) pasa a «Agendar cita» con calendar-plus, para no tener dos formas de «crear consulta»: agendar (después) y consulta inmediata (ahora). **El usuario dijo que no: la barra lateral se queda como está.**

## Pendiente
Registro semántico en el proyecto (Lima).
