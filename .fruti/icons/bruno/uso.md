# bruno · uso

Icono del agente Bruno: silueta de perro genérica de perfil (cuerpo compacto, patas cortas y anchas, cabeza redonda con oreja caída, cola corta), sin raza, de la familia de `rabbit` y `turtle`. Monocromo (`currentColor`), trazo 1.5, 24×24.

1. **Inline o vía `<use>`**: así hereda el color y se anima. Como `<img>` queda estático y negro.
2. **Dos movimientos, cada uno con su significado** (nunca en bucle ni decorativo):
   - `uva-bruno--contento` → **mueve la cola** (feedback, 640 ms): cuando Bruno responde o termina una tarea.
   - `uva-bruno--avisar` → **ladra dos veces** (attention, 600 ms): cuando Bruno tiene un aviso. Con moderación: no en cada mensaje.

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function animar(svg, modo) {               // modo: 'contento' | 'avisar'
  if (reducir.matches) return;             // sin movimiento: el texto o el control dicen el estado
  const c = `uva-bruno--${modo}`;
  svg.classList.remove(c); void svg.getBBox(); svg.classList.add(c);
}
svg.addEventListener('animationend', (e) => {
  // cola: termina la cola; ladrido: termina la segunda repetición del cuerpo (o el impulso de respaldo)
  svg.classList.remove('uva-bruno--contento', 'uva-bruno--avisar');
});
```

3. **Con texto** cuando informe: `[icono] Bruno tiene un aviso` dentro de `role="status"`; el SVG queda oculto (`aria-hidden="true"`).
4. **Botón solo con icono:** `<button type="button" aria-label="Abrir Bruno">` (área 44×44); el nombre va en el botón, no en el SVG.
5. **Safari y otros navegadores que no animan la forma** (`d`): el ladrido se convierte en un leve impulso del icono entero; la cola funciona igual (es un giro).

6. **PNG (512×512, icono a 360 px):** `bruno-claro.png` (fondo blanco), `bruno-oscuro.png` (fondo negro) — sirven como avatar con recorte circular — y `bruno-transparente.png` (trazo negro sin fondo, para fondos claros). Como imagen fija no se anima.
