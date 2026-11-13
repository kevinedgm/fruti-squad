# SAM · pantalla de gráficas (prototipo)

`graficas.html`, publicado como artifact. Datos ficticios. Decisiones del usuario (2026-11-13): dos pestañas, «Salud del trabajo» y «Mi rendimiento»; la usa todo el equipo.

- **Salud del trabajo** (equipo): abiertas, atrasadas, vencen esta semana y cerradas en el periodo; entradas y cierres por semana (líneas); abiertas por etapa hoy (barras); las más atrasadas.
- **Mi rendimiento** (personal): cerré, % a tiempo y mediana de días para resolver, frente al promedio del equipo; mis cierres por semana contra el promedio por persona; a tiempo y tarde (barra segmentada). Nadie ve a otra persona con nombre.
- Filtro de periodo (4, 8, 12 semanas) arriba, para toda la pantalla. Las cifras «hoy» y las etapas son del momento y no dependen del periodo.
- Series en la paleta categórica validada (azul, naranja; `validate_palette.js` pasa en claro sobre #ffffff y en oscuro sobre #16161a). Voltaje no se usa como color de datos. Tooltip con cruz, recorrido con flechas y tabla en cada gráfica.

**unresolved (PEND-003):** cómo se evalúa el rendimiento; si SA/IA necesitan una vista por persona con nombre; la definición de «a tiempo» y de «tiempo para resolver».
