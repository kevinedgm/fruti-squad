# Aprobación · FichaMedico · r03 · opción C (2026-11-04)

Decisión del usuario: «apruebo FichaMedico · r03 · F2 opción C». La r04 (C + horarios) queda descartada.

## Anatomía congelada (R3: no se rediseña al implementar)
1. **Médico:** foto o avatar de silueta · nombre · especialidad · cédula verificada · calificación con número de opiniones; sin opiniones, solo la cédula.
   - Cambio 2026-11-04 (usuario): se retira «Nuevo en Manik».
2. **Consultorios en filas** (máx. 2 visibles; con 3+: «Ver n consultorios más»). Orden: el más cercano que cumple los filtros primero.
   - Línea 1: lugar · distancia · precio de consulta.
   - Línea 2: forma de agendar + próximo lugar («Agenda en Manik · Hoy, 16:30») o «Por teléfono · número». Fecha y hora nunca se separan.
   - Acción a la derecha: «Agendar» (abre la elección de horario de ese consultorio) o «Llamar» (`tel:`).
   - Con ambas formas: «Agendar» y debajo el enlace «o llama al …».
3. **Peso:** un solo botón sólido por ficha (la primera fila); las demás filas, contorno. Acciones en píldora; enlaces de texto con área táctil ≥ 36 px.
4. **Lenguaje:** «Agenda en Manik» (la cita es presencial), nunca «En línea».
5. **Estados:** sin conexión (Agendar no disponible; «Llamar» pasa a principal en la fila con teléfono), error de horarios, horario ocupado, sin lugar en 2 semanas, contenido largo, sin foto, sin opiniones.
6. **Adaptación:** compacta < 520–560 px de contenedor (avatar junto al nombre); amplia ≥ 560 px (foto 132 a la izquierda, filas a la derecha).

## Enmienda 2026-11-04 · cédulas con número (pedida por el usuario)
- La etiqueta «Cédula verificada» se sustituye por las cédulas con número, debajo de la especialidad: «Céd. Prof. 10234567 · Céd. Esp. 11876543».
- «Céd. Esp.» solo si el médico es especialista. Icono badge-check en `on-exito-suave` = verificadas por Manik (texto oculto para lector de pantalla: «Cédulas verificadas por Manik»).
- Cada cédula no se corta por dentro; en 390 px ocupan 2 líneas.
- Aplicado en: design system (FichaMedico, Insignias), prototipo (resultados y perfil), wireframe de inicio r02/r03.
- Números del prototipo y del DS: de ejemplo (el de la Dra. Soto es el que dio el usuario como ejemplo).
