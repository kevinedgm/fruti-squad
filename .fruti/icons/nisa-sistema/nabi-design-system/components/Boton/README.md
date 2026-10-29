# Boton

Botón de acción: el primario va en azul real; los destructivos en borde «fuera».

- `primary`: «primary» con «on-primary». Una acción principal por vista: Liberar resultados, Registrar muestra, Emitir certificado.
- `secondary`: fondo «surface», borde «border-control», texto «primary». `ghost`: solo texto en «primary». `danger`: borde y texto «fuera», siempre con confirmación y motivo.
- 40 px de alto (`control-h`), 44 px en táctil. Radio `radius-sm`. Texto `button` en Poppins. Foco: anillo de 2 px en «focus».
- El pera no es color de botón.
- El consumidor provee: verbo + objeto, estado de carga (con la animación de carga a 16 px) y `aria-disabled`.
