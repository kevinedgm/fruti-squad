# Declaración de cumplimiento · Bitácora % Alcohol por volumen · r01

Ruta R1 · F3 con el sistema real (design system NisaLab v3: tokens.json, 25 colores, Poppins + Google Sans Code). Estándares leídos: tokens.json, README del DS, reglas de color 2026-11-05.

Se conserva: orden de secciones, campos, textos normativos, referencia de evaluación, acciones Cerrar y Registrar.

Cambios declarados (desviaciones del modal actual)
1. La norma pasa al encabezado (antes en el panel de lecturas): es dato del método, no de la corrida.
2. El criterio de aceptación va junto a la repetibilidad que juzga (antes en un recuadro al final).
3. El error de fecha aparece al salir del campo o al registrar, no al abrir (antes rojo sin haber tocado nada).
4. Firma pendiente en gris con reloj (antes ámbar): regla del sistema, pendiente no es urgente.
5. Registrar pasa a azul primario (antes verde de «éxito»): una sola primaria; el verde es estado.
6. Equipo como dato (nombre + código) en lugar de tabla de una fila.
7. Repetibilidad muestra su estado (Conforme / Fuera de criterio) con ícono y texto; el promedio avisa si sale del rango de referencia.
8. La fila de lectura enfocada lleva el filete pera (lo que está en curso).
9. Firmada: todo en solo lectura (lienzo gris + candado) y sin botón Registrar.

Comprobado: sin desbordes a 1200 y 390 px; ningún control menor de 24 px; sin errores de JS; Registrar vacío marca los 7 campos faltantes y lleva el foco al primero; cálculo 40.12/40.10/40.15 → promedio 40.12, repetibilidad 0.05 conforme; avisos visibles solo en su estado.
No comprobado: lector de pantalla real; navegación con teclado completa dentro del modal (trampa de foco); textos largos de equipo; texto ampliado al 200 %.
Incógnitas abiertas: si repetibilidad fuera de criterio bloquea Registrar; dónde se evalúa la reproducibilidad.
