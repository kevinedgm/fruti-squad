# Caso 01: tarjeta de resumen (componente nuevo)

## Petición
`Diseña una tarjeta de resumen de cuenta: nombre del cliente, saldo pendiente, número de muestras sin pagar y una acción "Ver cuenta"`

## Ruta esperada
Kiwi F2 → Lima contrato → Coco F3 y auditoría → Lima gate → Mora.

## Debe
- [ ] F2 en gris neutro con `data-piece` en cada pieza y grupo.
- [ ] Matriz adaptativa compact / medium / expanded con qué se conserva, cambia y oculta.
- [ ] Una sola acción principal; el saldo con más peso que los datos secundarios.
- [ ] Lima clasifica reuso / extensión / nuevo con motivo.
- [ ] `fidelity.json` existe y es `pass`.
- [ ] Preview de Mora renderiza el componente verificado de esta ronda.

## No debe
- [ ] Color de marca, sombra o movimiento decorativo en F2.
- [ ] Valores crudos de color, espacio o tipografía en el componente.
- [ ] PASS general con alguna dimensión en PARTIAL o FAIL.
