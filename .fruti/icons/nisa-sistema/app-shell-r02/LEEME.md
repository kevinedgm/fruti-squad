# App Shell NisaLab · r02 (pendiente de aprobación)

`python3 gen.py` → `shell.html`. Misma URL que r01: https://claude.ai/artifact/Xg6DANcBq6hsdsv9eNHKk5
Comentario de r01: «muy cuadrado, muy rígido; no me gusta el color de la superficie; casi blanco, más sombras, bordes más sutiles en los campos; más delicado, editorial tipo Medium o Apple».

Cambios (en `gen.py`, diccionario PROPUESTA; mismos nombres de token, valores nuevos; tokens.json NO cambia hasta aprobarse):
- bg #F2F4F8 → #F7F8FA (casi blanco; text-muted encima 6.4:1, text 16.0:1).
- border #DFE3EC → #E6E9EF.
- radius-sm 6 → 8 · radius-md 8 → 12 · radius-lg 12 → 16.
- shadow-1, shadow-2 e inset más amplias y suaves.
Estructura: sidebar sobre el lienzo sin borde; el contenido es una hoja blanca flotante (radio 16, sombra amplia); navbar translúcida; tabla sin fondo de encabezado, filetes finos, filas de 56 px; título de página 30/38.
Campos delicados: borde suave (border) en los cuatro lados + línea inferior en border-control (3.3:1 sobre blanco) para cumplir WCAG 1.4.11; foco con línea azul y halo primary-soft.
Comprobado: 4 vistas y 390 px sin desbordes; ningún control < 24 px; sin errores de JS.
