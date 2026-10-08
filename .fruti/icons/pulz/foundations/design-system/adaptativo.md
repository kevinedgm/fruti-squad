# Adaptativo

El **ancho decide el layout**; la **entrada decide el tamaño de los controles** (ver Geometría). Son dos ejes independientes: una tablet tiene layout medio con controles de dedo.

| Modo | Ancho | Uso | Navegación | Columnas | Regla |
|---|---|---|---|---|---|
| Compacto | hasta 599 px | teléfono, 60 % | barra inferior: 4 destinos + «Más» | 1 | Una tarea por pantalla. La acción principal abajo, al alcance del pulgar. Lo secundario, plegado. |
| Medio | 600 a 1023 px | tablet, 10 % | riel lateral compacto con etiquetas | 8 | Lista y detalle pueden convivir. |
| Expandido | desde 1024 px | escritorio, 30 % | barra lateral completa | 12 | Maestro y detalle lado a lado; tablas completas. Contenido con ancho máximo de 1200 px. |

## Reglas

1. Compacto nunca es una tabla aplastada: una tabla en el teléfono se convierte en lista de tarjetas con las dos cifras que importan (°Brix, °C); el resto se abre al tocar.
2. Expandido nunca es el teléfono estirado: con 30 % del uso, el escritorio merece comparar tinas y ver el lote con su historial a la vez.
3. Los puntos de corte son de layout, no de verificación: se verifica en 360, 768, 1024 y 1440 px.
4. Zoom de texto al 200 % en cualquier modo sin romper la composición: anchos en unidades relativas.
