# Caso 06: cambiar el color de acción

## Petición
`Cambia el color de acción a un azul más oscuro`

## Ruta esperada
Lima (dueña de tokens) actualiza `.fruti/tokens.json` y regenera derivados. **No** pasa por Kiwi ni rediseña componentes uno por uno.

## Debe
- [ ] Cambia el token semántico de acción, no valores en cada componente.
- [ ] Los derivados se regeneran y el contraste de texto sobre acción se verifica.
- [ ] Las superficies `excluded` no se tocan como rediseño (la propagación del token se reporta aparte).

## No debe
- [ ] Editar colores crudos en archivos de componentes.
- [ ] Lanzar una ronda de Kiwi F2.
