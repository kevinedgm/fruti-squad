# apollo · uso

Icono de Apollo (dev-launcher): un prompt `>_` dentro de una órbita; el satélite es el único neón. Trazo 1.5 en `currentColor`, 24×24.

1. **Color con tus tokens:** el trazo hereda `color` (usa `ink`); el satélite usa `--uva-accent`. Conéctalo a tu neón:
   ```css
   .uva-apollo{ --uva-accent: var(--signal); color: var(--ink); }
   ```
   En el tema Día usa el `signal` del tema claro: un cian claro sobre blanco no llega a 3:1.
2. **En reposo, plano:** sin halo ni movimiento (el brillo es estado, no decoración).
3. **Ignición → En órbita:** al arrancar un entorno (o la app), el satélite da una vuelta a la órbita (900 ms, una vez) y queda en su sitio. No lo repitas en bucle mientras el entorno corre: el estado «En órbita» lo dicen el badge (palabra + glifo ●) y, si aplica, `glow-go` en el componente, no el icono.

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function ignicion(svg) {                       // svg = el .uva-apollo
  if (reducir.matches) return;
  svg.classList.remove('uva-apollo--ignicion'); void svg.getBBox();
  svg.classList.add('uva-apollo--ignicion');
}
svg.addEventListener('animationend', () => svg.classList.remove('uva-apollo--ignicion'));
```

4. **Accesibilidad:** el SVG va oculto (`aria-hidden="true"`). Junto al nombre «Apollo», decorativo; en un botón solo con icono, el nombre va en el botón: `<button type="button" aria-label="Abrir Apollo">` (área 44×44).
5. **Tamaños:** 20–48 px recomendado; a 16 px (favicon) se reconoce la órbita con el satélite y el `>_` queda como marca.
