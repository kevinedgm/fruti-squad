# Boton

Botón de acción con cinco variantes; el oro es exclusivo de Reservar y el primario va en tinta.

- `reserve`: solo «Reservar» y «Confirmar cita». Fondo `reserve`, texto `on-reserve`. Uno por pantalla.
- `primary`: la acción principal cuando no es reservar: `primary` (tinta) con `on-primary`. Así el oro es el único color fuerte de la pantalla.
- `secondary`: borde y texto en `text`. `ghost`: solo texto, en `brand`. `danger`: borde y texto `danger`, siempre con confirmación.
- 44 px de alto mínimo (`control-h`); 52 px (`control-h-lg`) para Reservar en la cabecera. Radio `radius-sm`. Foco: anillo 2 px en `focus`.
- El consumidor provee: etiqueta (verbo concreto), estado de carga y `aria-disabled`.
