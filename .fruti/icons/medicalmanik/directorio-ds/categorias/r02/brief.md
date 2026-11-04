# Brief · Sellos de categorías · r02 (delta sobre r01)

- **Decisión del usuario (2026-11-04):** dirección A (sello circular), con diferentes tamaños para que en celular no sean tan grandes.
- **Mecanismo:** la leyenda del arco escala con el sello; por debajo de ~104 px quedaría en menos de 8 px (ilegible). Por eso los tamaños cambian de contenido.
- **Escala propuesta (variantes del componente):**
  | Tamaño | Sello | Dónde | Contenido |
  |---|---|---|---|
  | Compacto | 88 px | Celular, 3 por fila | Doble anillo + círculo interior grande + pictograma grande; sin leyenda |
  | Mediano | 112 px | Tableta, 3 por fila | Con leyenda en arco |
  | Grande | 132 px | Escritorio, 6 en fila | Con leyenda en arco |
  Regla de respaldo: si un sello queda por debajo de 104 px por el espacio disponible, toma la forma compacta (container query).
- **Efecto medido:** alto de las 6 categorías en celular 623 px (r01) → 344 px (r02).
- **Comprobado:** sin desbordes ni controles menores de 24 px (390 y 1300 px); la leyenda no aparece en compacto y sí en mediano y grande; sin errores JS. Contraste igual que r01.
- **No ejecutado:** lector de pantalla, texto ampliado.
- **Pendiente tras aprobar:** Lima registra los tamaños como variantes de TarjetaCategoria en el DS; luego Coco lo lleva al prototipo.
