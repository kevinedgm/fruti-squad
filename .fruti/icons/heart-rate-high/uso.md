# heart-rate-high · uso

1. **Siempre con texto.** El icono refuerza la alerta («118 lpm · Pulso alto»); no la sustituye. Junto al texto, el SVG ya trae `aria-hidden="true"`. Si alguna vez va solo, el nombre accesible es «Frecuencia cardíaca alta».
2. **Inserta el SVG inline** (o vía `<use>`): así hereda el color de la alerta y puede animarse. Como `<img src>` queda estático y negro.
3. **Late solo cuando llega una lectura alta nueva**, no cada vez que se pinta la pantalla (igual que `blood-pressure-high`).

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function alertaNueva(svg) {               // svg = el .uva-heart-rate-high de esa lectura
  if (reducir.matches) return;            // sin movimiento: las líneas ya dicen «rápido»
  svg.classList.remove('uva-heart-rate-high--latir');
  void svg.getBBox();
  svg.classList.add('uva-heart-rate-high--latir');
}
svg.addEventListener('animationend', (e) => {
  if (e.animationName === 'uva-heart-rate-high-latir') svg.classList.remove('uva-heart-rate-high--latir');
});
```

4. **Deja espacio a las ondas:** salen ~2 px por la derecha de la caja del icono; sin `overflow: hidden` pegado al icono.
5. **Mientras la frecuencia siga alta, quieto.** Late 4 veces (1,9 s) y se detiene (WCAG 2.2.2).
6. **Con el de presión:** son una familia. Presión = flecha y latido normal; pulso = líneas de velocidad y latido rápido. No intercambies los símbolos (no pongas flecha aquí ni líneas en el de presión).
7. **Color y grosor:** `color` del contenedor; `--uva-accent` solo para las ondas; `--uva-stroke` para el grosor de toda la familia.
