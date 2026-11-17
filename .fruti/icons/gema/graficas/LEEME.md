# GEMA · pantalla de gráficas (prototipo)

`graficas.html`, publicado como artifact, adaptado del de SAM. Datos ficticios. Decisión del usuario (2026-11-17): operación del laboratorio; la usan dirección y calidad.

- Filtros arriba: periodo (4, 8, 12 semanas) y sucursal (ambas, Oaxaca, CDMX).
- Cifras: muestras recibidas (frente al periodo anterior), abiertas hoy, informes a tiempo, tiempo de entrega.
- Muestras recibidas por semana y tipo (columnas apiladas, 4 tipos), abiertas por etapa hoy (barras), informes a tiempo por semana (línea, escala 0–100), tabla por sucursal, lista de informes que vencen hoy.
- Paleta categórica de 4 colores validada con `validate_palette.js` (claro sobre #ffffff: contraste < 3:1 en verde y amarillo, por eso leyenda + tabla; oscuro sobre #16161a: pasa). El navy de marca no se usa como color de datos.

**unresolved:** SUP-005 (la v1 no añade funciones nuevas): confirmar qué tablero tiene hoy el sistema; definición de «a tiempo» y de «tiempo de entrega»; si existe una meta de entrega.
