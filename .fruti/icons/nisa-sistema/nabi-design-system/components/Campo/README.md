# Campo

Campo de captura. El texto va en Poppins; el valor de un resultado se escribe en Plex Mono, alineado a la derecha, con la unidad fija al final.

- 40 px de alto, borde «border-control», radio `radius-md`. Etiqueta `label` arriba; ayuda `caption` abajo.
- Campo de resultado: `datos` a 15 px, `text-align: right`, unidad como sufijo en «text-muted». Acepta solo el número; la unidad la pone el método.
- Validación contra la especificación al salir del campo: borde y mensaje en «fuera» con el límite escrito en `datos`. No bloquea la captura: un resultado fuera se registra y se marca.
- El consumidor provee: etiqueta (parámetro y símbolo), unidad, especificación, decimales del método y el `id`.
