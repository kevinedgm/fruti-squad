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
- 2026-11-04: «Cita confirmada» aprobada (cita-confirmada/r01): resumen, calendario .ics, vista del mensaje; aviso de horario ocupado en «Confirma tu cita».
- 2026-11-04: «Detalle de su cita» aprobado (detalle-cita/r01): #cita y #cita-cambiar; cancelar con diálogo; regla de 24 h; la hora se reserva al confirmar y se libera al cambiar o cancelar.
- 2026-11-04: «Busca por lo que sientes» con sellos circulares en tres tamaños (categorias/r02).
- 2026-11-04: promociones de Impulsa (promocion/r02): tarjeta en resultados, página #promo-<id>, precio con promoción hasta la cita.
- 2026-11-04: «con Impulsa Manik» en la tarjeta y sello de Impulsa al pie de la página de la promoción.
- 2026-11-04: 9 médicos de ejemplo más (salud mental, alimentación, salud íntima, chequeo general, pediatría), completos y con poca información; todas las categorías tienen resultados; «Con lugar hoy» muestra 3; maestrías con su propia cédula; sin número de teléfono repetido en consultorios solo por teléfono.
- 2026-11-04: leyenda del inicio, opción B («Encuentra a tu médico cerca de ti.»).
- 2026-11-04: simulación de la foto de marca 4:5 en el inicio (ilustración + tarjetas flotantes; etiqueta «Simulación»).

Publicado: https://claude.ai/artifact/EfXbngHaw3pqZ8EbN8egFM

- 2026-11-10: paleta cambiada a la del design system «Mi Médico Manik» (https://claude.ai/artifact/GeGQEx9qFjmmKyDSemA34R) con `colores_2026-11-10.py` (solo color; tipografía, radios y sombras sin cambio). Respaldo previo: `../directorio-prototipo-copia-2026-11-10/`. Acción en `teal`, texto de acción en `teal-hover`; `luz-cian` → `menta-hielo`; sellos menta-hielo / luz-calida / turquesa-suave; Impulsa en lila; cédula verificada en teal-hover sobre menta-hielo; avatares con degradado avatar-inicio → luz-calida y silueta en tinta al 28 % (recoloreados en `gen.py`, los SVG del sistema no cambian). Pendientes: logo sigue en #009BB0; `confianza-texto` y `error-presionado` son locales; `pleca`, `turquesa` y `resaltador` definidos pero sin uso; el sistema `directorio-ds` aún tiene la paleta anterior. Verificación: Playwright a 390 y 1300 px en 7 pantallas, 0 errores JS, 0 desborde; todo texto ≥ 4.5:1 salvo la estrella (1.8:1, siempre junto al número, como indica la guía). Publicado v19.
