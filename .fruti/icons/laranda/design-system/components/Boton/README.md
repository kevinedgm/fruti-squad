# Boton

Botón de acción con cinco variantes; el oro es exclusivo de Reservar.

- `reserve`: solo «Reservar» y «Confirmar cita». Fondo `reserve`, texto `on-reserve`. Uno por pantalla.
- `primary`: la acción principal de la pantalla cuando no es reservar: `brand` con `on-brand`.
- `secondary`: borde `brand`, texto `brand`. `ghost`: solo texto. `danger`: borde y texto `danger`, para cancelar o eliminar, siempre con confirmación.
- 44 px de alto mínimo (`control-h`); 52 px (`control-h-lg`) para Reservar en la cabecera. Radio `radius-lg`. Foco: anillo 2 px en `focus`.
- El consumidor provee: etiqueta (verbo concreto), estado de carga y `aria-disabled`.
