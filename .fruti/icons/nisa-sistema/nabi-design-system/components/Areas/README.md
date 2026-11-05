# Areas

Las ocho áreas (divisiones) de Nisa Nabani dentro de NisaLab: «Área NisaLab». La célula que creció de Colonia toma el color y el ícono del área; el resto del racimo sigue azul real.

- **Color:** tokens `area-*`. Paleta OKLCH con la misma luminosidad (0.60) y la intensidad máxima que admite cada tono (tope 0.17); solo cambia el tono, fuera del rango del pera. Blanco del ícono encima de 3.7 a 4.3:1: cumple para gráficos (3:1) porque el color de área nunca lleva texto. Distancia a los colores de estado mayor que 8.
- **Ícono:** dibujado en retícula de 40, formas redondas y blancas. 16 px junto al nombre en filtros; en tablas, la versión a una tinta; 40 px en listas y encabezados de área.
- **Nombre:** siempre acompaña a la marca o al ícono; a 24 px lo que se lee es el color.
- **Nunca en tablas: en una tabla todo color es estatus; ahí el área va con su ícono a una tinta en «text-muted» y su nombre.**
- **Nunca estado:** los estados usan `conforme`, `alerta` y `fuera`; «Pendiente» va en gris (`text-muted` sobre `bg`).
- **Archivos:** grupo de assets «Áreas» (marca e ícono por área). El paquete completo vive en `nisalab-areas-final/`.
