# Ecosistema Manik · app shell · r02 (aprobada 2026-11-05)

Pedido (2026-11-05): «los appshells con navbar, sidebar, footer, los sidebars con módulos y submódulos y para aplicaciones pequeñas que solo tienen 2 secciones una alternativa distinta».
`python3 gen.py` → `shell.html`. Reemplaza la propuesta r01 (`../shell/`, 2026-10-24, nunca aprobada: anterior a la identidad actual, sin submódulos, y ponía la acción «Nueva campaña» como pestaña).
Reutiliza los controles aprobados (`../controles-r01/gen.py`, importado) y los iconos Lucide de la r01; valores de `../design-system/project/tokens.json`.

## Qué resuelve
- Demo interactiva: Expediente (módulos con submódulos), Agenda (menú plano), Impulsa (2 secciones), en escritorio, tableta y celular (container queries).
- Barra superior 64 px según EncabezadoApp (sello y nombre, búsqueda, avisos, ecosistema antes del avatar, cuenta).
- Barra lateral 264 px: módulos 44 px; submódulos desplegables (botón con aria-expanded) en filas de 40 px colgando de una línea guía; actual en manik-soft + aria-current; padre en negritas; suma de pendientes en grupos cerrados.
- Riel 72 px con etiqueta flotante y menú flotante para submódulos (Esc devuelve el foco).
- Tableta < 1024: cajón con velo `scrim`, X/Esc/tocar fuera, foco de regreso. Celular < 640: búsqueda como icono, sello sin nombre, tabla en filas.
- Pie 44 px dentro de la columna de contenido.
- App pequeña: sin barra lateral; pestañas (enlaces con aria-current) bajo la barra superior; contenido centrado a 1120 px; en celular las pestañas se reparten el ancho.
- Regla de patrón por número de destinos: 2–3 pestañas · 4–7 lateral plana · módulos con submódulos (dos niveles, nunca tres).

## Decisiones nuevas [propuesta]
Ancho 264 px (r01 decía 248) · riel 72 · submódulos sin icono en 40 px · solo se abre el grupo actual · pie dentro del contenido · contenido de app pequeña 1120 px · tableta como cajón · preferencia de riel recordada por persona.

## Verificación
Playwright, marco de 1320, 834 y 390 px y página a 390: sin desbordes ni errores; sin IDs duplicados; ningún control < 24 px; cajón y menú flotante con foco y Esc probados. No ejecutado: lector de pantalla real, zoom 200 %.

## Aprobación (2026-11-05)
Aprobada por el usuario. Integrada al sistema de diseño (versión 9) con `../design-system/shell_integracion.py` (AppShell, BarraLateral, AppPequena, EncabezadoApp por ancho; 6 tokens de layout) y resumida en el manual (subsección App shell).
