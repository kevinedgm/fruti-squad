# SelloCategoria

Riel de sellos para filtrar por categoría de servicio: un disco esmaltado con el icono de la categoría y su nombre debajo; «Todos» al inicio y «Más» al final.

- El sello es un timbre: el disco lleva siempre el esmalte de su categoría (`cat-N-fondo`) y el icono en su tinta (`cat-N-tinta`), no solo al activarse. Activo: anillo de 3 px en la tinta de la categoría y etiqueta en negrita; hover: anillo de 1.5 px. Nada depende solo del color: icono + nombre siempre.
- Disco de 44 px (`md`, riel bajo resultados) o 56 px (`lg`, riel protagonista en Inicio). Etiqueta `caption` 12/16 a 500, máx. 64 px de ancho.
- «Todos»: disco en `surface-sunken` con la palabra en versalitas. «Más»: disco punteado en `border-control`; un punto en `accent` avisa cuando el filtro activo está entre las categorías ocultas. En contexto `nav`, «Más» es un enlace «Ver todo →» y no abre panel.
- Patrón APG: `radiogroup` en el riel (flechas, Inicio, Fin); panel «Más» como diálogo modal con `listbox` y búsqueda a partir de 12 categorías. Foco: anillo `focus` de 2 px con separación de 2 px en `bg`.
- Las ocho tintas de categoría están validadas como paleta categórica (pares adyacentes, visión normal y daltonismo) y se asignan en orden fijo a las categorías; nunca se reciclan. El oro de Reservar no es una tinta de categoría.
- Carga: cinco esqueletos del mismo alto; error: una línea con «Reintentar» de 44 px.
- El consumidor provee: `categorias` (valor, etiqueta, icono, clase `cN`), `modelValue`, `size`, `context`, conteos y estados de carga y error. Implementación de referencia en Vue: `CategorySelloFilter.vue` en el repositorio de Laranda.
