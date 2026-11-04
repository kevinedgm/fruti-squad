# Brief funcional · Hacer una pregunta · r01

**Ruta:** R1 · **Fidelidad:** F0 (flujo). Las pantallas (F2) vienen después de cerrar las incógnitas que cambian estados.

**Enunciado:** una persona sin cuenta necesita preguntar a un médico porque tiene una duda de salud y aún no sabe si necesita consulta.
**Pregunta de diseño:** ¿qué pasos y avisos necesita para saber siempre en qué va su pregunta, sin cuenta?
**Verbo principal:** enviar una pregunta. **Resultado verificable:** recibe el correo «Dra. X respondió a tu pregunta».

## Hechos (usuario)
1. Para preguntar se pide el correo.
2. Se envía un enlace de confirmación.
3. La pregunta no se publica sola: pasa por un filtro de calidad.
4. Si se aprueba, se publica y se avisa por correo.
5. Cuando un médico responde, llega un correo con quién respondió.

## Inferencias
- Sin cuenta, el correo es la única forma de seguir la pregunta: cada correo lleva enlace directo.
- El enlace de confirmación también prueba que el correo es real y frena el spam.
- La pantalla tras enviar debe decir el siguiente paso («revisa tu correo»), no «gracias».

## Riesgos que el diseño debe cubrir (recomendación)
- **Urgencias:** una pregunta puede describir una emergencia. El formulario debe decir antes de enviar: «Si es una urgencia, llama al 911 o acude a urgencias» (número por país). El filtro tarda; una urgencia no puede esperar.
- **Datos personales:** la pregunta es pública. El formulario pide no incluir nombre, teléfono ni datos que identifiquen; el correo nunca se publica.
- **No es consulta:** la respuesta orienta, no diagnostica; esto se dice junto a cada respuesta.

## Incógnitas
1. Si el filtro no aprueba: ¿se avisa por correo y se dice el motivo (para que la reescriba)?
2. ¿El filtro es una persona, automático o ambos? (cambia el tiempo de espera que prometemos).
3. ¿Cuánto dura el enlace de confirmación y qué pasa si nunca se confirma?
4. ¿Llega un correo por cada médico que responde, o solo el primero?
5. ¿Se puede preguntar desde Centroamérica igual (número de urgencias por país)?
