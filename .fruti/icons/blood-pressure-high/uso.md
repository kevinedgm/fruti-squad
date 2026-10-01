# blood-pressure-high · uso

1. **Siempre con texto.** El icono refuerza la alerta («152/98 mmHg · Presión alta»); no la sustituye. Junto al texto, el SVG ya trae `aria-hidden="true"`. Si alguna vez va solo, el nombre accesible es «Presión arterial alta».
2. **Inserta el SVG inline** (o vía `<use>`): así hereda el color de la alerta (`color` del contenedor) y puede animarse. Como `<img src>` queda estático y negro.
3. **Late solo cuando llega una lectura alta nueva**, no cada vez que se pinta la pantalla. Si una lista carga con diez pacientes en alta y los diez laten a la vez, deja de ser un aviso y se vuelve ruido.

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function alertaNueva(svg) {               // svg = el .uva-blood-pressure-high de esa lectura
  if (reducir.matches) return;            // sin movimiento: el icono quieto ya dice el estado
  svg.classList.remove('uva-blood-pressure-high--latir');
  void svg.getBBox();                     // reinicia la animación si ya estaba
  svg.classList.add('uva-blood-pressure-high--latir');
}
svg.addEventListener('animationend', (e) => {
  if (e.animationName === 'uva-blood-pressure-high-latir') svg.classList.remove('uva-blood-pressure-high--latir');
});
```

4. **Deja espacio a las ondas.** Salen 2–3 px fuera de la caja del icono. Un contenedor con `overflow: hidden` pegado al icono las corta en los bordes; dale relleno o `overflow: visible`.
5. **Mientras la presión siga alta, quieto.** Late 3 veces (2,4 s) y se detiene (WCAG 2.2.2). No lo pongas en bucle.
6. **Color y grosor:** el color sale de `color` del contenedor; `--uva-accent` cambia solo el color de las ondas; `--uva-stroke` cambia el grosor de toda la familia.
7. **Reservado para presión.** Para frecuencia cardíaca alta usa `heart-rate-high` (misma familia: líneas de velocidad y latido rápido).
