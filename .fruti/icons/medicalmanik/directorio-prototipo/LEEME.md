# Directorio Manik · prototipo navegable (2026-11-04)

Pedido: «genera un artifact con un prototipo del directorio Manik». Regenerar: `python3 gen.py` → `prototipo.html`.

- Sistema: «Directorio Manik» (`../directorio-ds/`): tokens, Urbanist + Onest, avatares de silueta, iconos Lucide, logotipo.
- Flujo: inicio → búsqueda (pantalla completa en celular, píldora en escritorio) → resultados (FichaMedico aprobada r03 opción C, filtros en hoja inferior con conteo en vivo, orden, anuncio, vacíos) → perfil (consultorios con precio y forma de agendar propios, próximos horarios, barra de acción fija en celular) → elegir día y hora → confirmar (validación) → cita confirmada.
- **Propuesta sin aprobar:** las tres pantallas de agendar están marcadas «Pantalla propuesta · por aprobar».
- Datos de ejemplo: médicos, direcciones, precios y teléfonos ficticios (555). Solo «Piel/Dermatología» tiene médicos; otras categorías muestran el estado vacío.
- Verificación: Playwright a 390 y 1300 px por todo el flujo: 0 errores JS, 0 desborde, controles ≥ 24 px.

- 2026-11-04: inicio reemplazado por el aprobado (inicio/r03): con lugar hoy, resuelve tus dudas, cómo funciona, ¿eres médico?

- 2026-11-04: perfil del médico reemplazado por el aprobado (perfil-medico/r03): agenda con días y horas, secciones que solo aparecen con datos, formación desde cédulas, Dr. Mario Díaz Soto en «Niñas y niños». Confirmación con nombre + celular.
- 2026-11-04: «Agendar» de la ficha lleva al perfil (Agenda tu cita, consultorio elegido); se retira la pantalla «Elige día y hora».
