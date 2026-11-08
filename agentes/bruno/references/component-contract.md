# Contrato de implementación de una pieza

## API

- Las props expresan intención, no estilo.
- Los conjuntos cerrados se validan.
- La navegación usa enlaces o el enlace del router; las acciones usan `<button>`.
- Estado controlado: el componente no decide por su cuenta cuándo empieza o termina una operación.
- La adaptación responsive pertenece al contrato y al CSS, no a props por breakpoint.

## Terminado significa

- Las entregas de kiwi, lima y coco están presentes, o hay deuda autorizada de forma explícita.
- El build está en verde.
- El comportamiento y la accesibilidad funcional están verificados.
- No hay ninguna decisión visual inventada.
- El handoff y el estado apuntan a coco para la auditoría R0.
