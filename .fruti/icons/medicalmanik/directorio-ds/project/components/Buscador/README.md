# Buscador

Buscador. **Celular primero:** un solo campo que abre la búsqueda a pantalla completa; en escritorio, la píldora doble.

- **Celular, cerrado:** un botón-campo blanco de 60 px bajo el titular: «¿Qué necesitas?» y, debajo, el lugar actual («Cerca de Angelópolis, Puebla»). Abre la búsqueda (`aria-haspopup="dialog"`).
- **Celular, abierto:** pantalla completa con «Volver», los dos campos con etiqueta visible, «Usar mi ubicación», sugerencias que marcan en negrita lo escrito (especialidad, síntoma o médico) y «Buscar» a todo el ancho abajo, al alcance del pulgar. El teclado no tapa el botón: la pantalla se ajusta a la altura visible.
- **Tableta:** igual que celular en vertical; en horizontal, la píldora doble.
- **Escritorio (≥ 1024 px):** píldora con «Qué necesitas» y «Dónde», iconos en `cian-ui`, botón «Buscar» en `tinta`, sombra `shadow-buscador`, foco en toda la píldora.
- El consumidor provee: valores, sugerencias, ubicación (con permiso) y la acción de búsqueda (`role="search"`).
