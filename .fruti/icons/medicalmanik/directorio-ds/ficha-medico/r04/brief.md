# Brief funcional · FichaMedico · r04 (dirección elegida)

**Ruta:** R2 → dirección elegida · **Fidelidad:** F2 · **Fecha:** 2026-11-04 · Brief base: `../r01/brief.md`; deltas en `../r02/brief.md` y `../r03/LEEME.md`.

## Decisión del usuario
«Me gusta la opción C, pero de la B me gusta que muestra algunos horarios disponibles.» → C + horarios.

## Anatomía (propuesta para congelar)
1. **Médico:** avatar o foto, nombre, especialidad, cédula verificada, calificación (o «Nuevo en Manik»).
2. **Consultorio abierto** (el más cercano que cumple los filtros): lugar · distancia | «Consulta» + precio; forma de agendar («Agenda en Manik», «Por teléfono» o «Agenda en Manik o por teléfono»); día + «Más horarios»; hasta 3 horarios; «o llama al …» (si también recibe llamadas) + **Agendar** (único sólido). Solo teléfono: número, «Copiar número» + **Llamar** (sólido).
3. **Otros consultorios** (máx. 1 más visible): fila compacta con lugar · distancia · precio, forma de agendar con su próximo lugar o su teléfono, y un botón de contorno: «Ver horarios» (abre los horarios de ese consultorio) o «Llamar». Con 3+: «Ver n consultorios más».

## Registro de decisiones
| id | decisión | fuente | porque | afecta | estado |
|---|---|---|---|---|---|
| D1 | C + horarios de B | usuario | elección explícita | todos | frozen |
| D2 | Solo el primer consultorio va abierto | inferencia | los horarios de todos duplicarían la altura (≥ 600 px en compact) | compact, medium | proposed |
| D3 | Botón de otros consultorios: «Ver horarios» (no «Agendar») | inferencia | no se agenda sin elegir hora; el botón dice lo que pasa | todos | proposed |
| D4 | «Más horarios» en la línea del día; «o llama» junto a «Agendar» | inferencia (densidad) | −97 px en la ficha más común | compact | proposed |
| D5 | «Agenda en Manik» | usuario | «En línea» se leía como video | todos | frozen |
| D6 | Horarios con esquinas de 10 px; acciones en píldora | inferencia (r02) | elegir ≠ hacer | todos | proposed (pide cambio de regla del sistema) |
