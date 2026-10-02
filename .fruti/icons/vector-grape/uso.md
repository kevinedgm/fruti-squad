# vector-grape · uso

Icono de la skill Uva: un racimo cuyo tallo es un trazado vectorial con su anclaje seleccionado y su manejador. Monocromo (`currentColor`), trazo 1.5, 24×24. Sustituye a `icon-forge`.

1. **Estático por defecto.** Es el icono de la skill (Codex, GitHub, avatar): no se mueve solo.
2. **Anima solo al entrar en «Uva está dibujando»** (progress): el tallo se traza, aparece el anclaje, sale el manejador y su punta (0,86 s, una vez); luego queda quieto mientras dure el estado. No lo repitas en bucle ni al pasar el puntero: decorar con movimiento lo prohíbe la norma (§28).

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function empezarADibujar(svg) {                 // svg = el .uva-vector-grape del indicador
  if (reducir.matches) return;                  // sin movimiento: el icono completo ya dice el estado
  svg.classList.remove('uva-vector-grape--dibujar');
  void svg.getBBox();                            // reinicia la animación
  svg.classList.add('uva-vector-grape--dibujar');
}
svg.addEventListener('animationend', (e) => {
  // la punta es la última pieza: quitar la clase cuando termina
  if (e.target.classList.contains('uva-vector-grape__punta')) svg.classList.remove('uva-vector-grape--dibujar');
});
```

3. **Con texto** cuando indique el estado: `[icono] Dibujando…` dentro de un contenedor con `role="status"`; el SVG queda oculto (`aria-hidden="true"`).
4. **Botón solo con icono:** el nombre va en el botón, no en el SVG (área 44×44):
   ```html
   <button type="button" aria-label="Abrir Uva"><svg …vector-grape… aria-hidden="true" focusable="false"></svg></button>
   ```
5. **Fuera de una página** (`<img>`, favicon, avatar) `currentColor` no se hereda y se pinta negro: para fondo oscuro exporta una copia en claro. GitHub no acepta SVG como avatar: PNG cuadrado.
