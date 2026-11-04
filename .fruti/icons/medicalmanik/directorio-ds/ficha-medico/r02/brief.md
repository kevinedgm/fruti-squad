# Brief funcional · FichaMedico · r02 (delta sobre r01)

**Ruta:** R2 · **Fidelidad:** F2 · **Fecha:** 2026-11-04 · Brief base: `../r01/brief.md` (sin cambios salvo lo siguiente).

## Pedido del usuario
1. Un médico con más de un consultorio donde un consultorio acepta citas por el directorio **y además** por teléfono: ¿cómo se ve?
2. Revisar densidad, peso y radio de los botones.

## Cambios al modelo
- **Hecho nuevo:** la forma de agendar de un consultorio puede ser *en línea*, *por teléfono* o **ambas**.
- **Decisión (inferencia):** con ambas, «Agendar» es la acción principal (se completa dentro de Manik y confirma horario); llamar es la alternativa, como enlace con el número escrito («o llama al 222 555 0140»). Sin conexión, la principal pasa a «Llamar».

## Revisión de botones (medida en r01, compact 393)
| Aspecto | r01 | r02 (A/B/C) | Por qué |
|---|---|---|---|
| Radio | Todo en píldora (999): horarios y acciones iguales | Acciones en píldora; horarios con esquinas de 10 px | Elegir un horario no es una acción; la forma los separa sin color |
| Peso | Sólido a todo el ancho: 8–11 % del área de la ficha; «Copiar número» con el mismo peso que «Llamar» | Sólido a su ancho (mín. 132 px, derecha): 3–5 %; alternativas como enlace de texto | Una sola cosa pesa por ficha; en la lista no se forman franjas negras |
| Densidad | Horarios 40 px con 6 px entre ellos; enlaces de 32 px | Horarios 40 px con 8 px; enlaces con área táctil de 36–44 px | Menos toques errados con el pulgar |
| Ubicación | Principal a todo el ancho | Principal a la derecha | Al alcance del pulgar derecho; el texto de la izquierda queda libre |
