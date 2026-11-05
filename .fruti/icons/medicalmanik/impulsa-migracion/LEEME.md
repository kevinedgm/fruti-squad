# Impulsa Manik · guía de migración al sistema común

Aprobado (2026-11-05): «alinéalo en los tres puntos» (tipografía, color de acción, lienzo). Sin acceso al repositorio de Impulsa.
Publicado: https://claude.ai/artifact/AjTnxzTXKHqqHon5C3jsig · `python3 gen.py` → `guia.html` (valores leídos de `../design-system/project/tokens.json`).

Contenido: por qué · mapeo valor por valor (violeta solo en sello y tarjeta) · escala tipográfica · cambio de anchos medido · código CSS listo para copiar · orden (lienzo → acción → tipografía → shell AppPequena) con comprobación de cada paso · búsquedas en el código · qué no cambia.
Medido (Chromium, Google Fonts; supuesto Ubuntu 400 en texto, 500 en botones y títulos): texto 16 px −2 a −3 %; botones +12 a +18 %; títulos +5 a +16 %. Lienzo #F4F4F4 → #F5F7FB: ΔE 1.03. Blanco sobre azul Manik 8.54:1 (sobre violeta 7.27:1).
No verificado: el código real de Impulsa (dónde están los valores, si usa variables, pesos de Ubuntu reales).
Registrado en: README del sistema de diseño (vía build.py) y documento de arquitectura (v4).
