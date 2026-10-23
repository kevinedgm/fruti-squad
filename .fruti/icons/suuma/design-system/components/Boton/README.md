# Boton

Botón de acción. La acción primaria va en tinta; el cadmio queda para una sola acción de marca por pantalla.

- `primary`: `primary` con `on-primary`. La acción principal de la pantalla: Contactar, Publicar perfil, Reservar.
- `secondary`: borde y texto en `text`. `ghost`: texto subrayado en `text`. `danger`: borde y texto `danger`, siempre con confirmación.
- `marca`: fondo `cadmio` con texto `on-cadmio` (13.1:1). Una por pantalla y solo para acciones de marca (destacar, compartir); nunca para confirmar ni pagar.
- 44 px de alto mínimo (`control-h`); 52 px en la cabecera de perfil. Radio `radius-sm`. Foco: anillo 2 px en `focus`.
- El consumidor provee: etiqueta (verbo concreto), estado de carga y `aria-disabled`.
