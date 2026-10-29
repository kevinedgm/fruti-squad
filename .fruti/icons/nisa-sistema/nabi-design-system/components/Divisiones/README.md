# Divisiones

Las ocho divisiones de Nisa Nabani con el icono y el color de su manual (2026), y cómo aparecen dentro de Nabi.

- **Azulejo:** el icono del manual tal cual, en vector. 36 px en listas y encabezados de división; 16 px junto al nombre en tablas y filtros.
- **Nombre:** siempre en «text», nunca en el color de la división (Aguas, Ambiental, Alimentos y Bebidas de agave no llegan a 4.5:1 como texto sobre blanco).
- **Color:** tokens `div-*`. Identifica la división; nunca indica estado. Los estados usan `conforme`, `alerta`, `pendiente` y `fuera`.
- **Accesibilidad:** el azulejo es decorativo (`aria-hidden`) porque el nombre siempre lo acompaña. Por eso el glifo blanco sobre cian o naranja del manual se conserva aunque baje de 3:1.
- **Marca:** el logo de Nisa Nabani y el lema van en documentos para clientes, membretes y certificados, no dentro de las pantallas de trabajo.
