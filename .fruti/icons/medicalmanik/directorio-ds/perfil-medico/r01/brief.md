# Brief funcional · Perfil del médico · r01

**Ruta:** R1 (una dirección) · **Fidelidad:** F2 (kit neutral) · **Fecha:** 2026-11-04
**Contenido de ejemplo:** perfil del Dr. Mario Díaz Soto dado por el usuario (bio, consultorio, formación, padecimientos, dudas frecuentes, opiniones, galería). Teléfono y cédulas sustituidos por ficticios.

**Enunciado:** una mamá o papá necesita decidir si este médico es el indicado para su hijo y contactarlo, porque llegó desde resultados, un enlace compartido o una pregunta/artículo y aún no lo conoce.
**Pregunta de diseño:** ¿en qué orden debe ver la información para decidir rápido en celular, sin perder la acción de contacto?
**Verbo principal:** contactar (llamar o agendar) a este médico. **Resultado verificable:** la llamada sale o se abre «Agendar» con el consultorio correcto.

## Preguntas del paciente, en orden (jerarquía)
1. ¿Atiende lo que tiene mi hijo? → especialidad + **padecimientos**.
2. ¿Es confiable? → cédulas con número, calificación y opiniones verificadas, formación.
3. ¿Dónde, cuánto y cómo lo contacto? → consultorio con precio y forma de agendar (anatomía de FichaMedico r03 C).
4. ¿Cómo es él? → sobre mí, galería, dudas frecuentes.

| Nivel | Contenido |
|---|---|
| N1 | Foto, nombre, especialidad, cédulas, calificación · consultorio (lugar, precio, forma de agendar) · acción Llamar/Agendar |
| N2 | Padecimientos · resumen de opiniones + 2 recientes · sobre mí |
| N3 | Formación académica (con la cédula de cada título) · dudas frecuentes · galería · su actividad en Manik |

## Hechos
- 1 consultorio (Hospital NeoDemo Xalapa), contacto por teléfono.
- Dos especialidades (Pediatría y Gastroenterología y Nutrición Pediátrica) → puede tener dos cédulas de especialidad.
- «Dudas frecuentes» las escribe el médico (pregunta y respuesta); son distintas de las preguntas de pacientes de «Resuelve tus dudas».
- 1,037 opiniones, calificación 5.

## Supuestos
- Consultorio solo por teléfono → la acción principal es **Llamar**.
- Las opiniones muestran nombre de pila del paciente (como en el ejemplo).

## Incógnitas
1. Precio de la consulta: no viene en el ejemplo y es obligatorio para publicar.
2. ¿Se muestran todas las cédulas de especialidad o solo la principal en la cabecera? (Propuesta: cabecera = profesional + especialidad principal; todas en Formación.)
3. Formación: Pediatría y Gastroenterología, ambas en 2010; verificar el año con el médico (es un dato, no un problema de diseño).
4. ¿El paciente puede tocar un padecimiento? (Propuesta r01: solo informativo, para no sacarlo del perfil.)
5. Galería: ¿qué fotos se permiten (consultorio, equipo, el médico)? ¿Se moderan?

## Riesgo por acción
- Llamar / Copiar número / Cómo llegar / Compartir: reversibles, sin confirmación.

## Continuidad
- Sin conexión: el perfil ya cargado sigue legible; «Llamar» funciona (es del teléfono); «Agendar» no.
- Error al cargar opiniones: solo esa sección avisa y ofrece reintentar.
