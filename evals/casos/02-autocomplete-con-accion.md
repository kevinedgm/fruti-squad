# Caso 02: autocomplete de cliente con acción "Nuevo"

## Petición
`Diseña un campo para elegir cliente con búsqueda mientras escribe y un botón "Nuevo cliente" al lado`

## Ruta esperada
Kiwi → Lima → Coco → Lima gate → Mora.

## Debe
- [ ] Patrón combobox: teclado (flechas, Enter, Escape) y anuncio de resultados.
- [ ] Geometría decide qué crece y qué conserva su ancho; el botón no se parte en dos líneas en compact.
- [ ] Estados: cargando, sin resultados, error, deshabilitado, foco.
- [ ] Área táctil del botón ≥ 44 CSS px.

## No debe
- [ ] Opciones solo accesibles con ratón.
- [ ] El campo y el botón con la misma jerarquía visual sin motivo.
