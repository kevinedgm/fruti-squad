# glucose-high · uso

1. **Siempre con texto.** El icono refuerza la alerta («245 mg/dL · Glucosa alta»); no la sustituye. Junto al texto, el SVG ya trae `aria-hidden="true"`. Si alguna vez va solo, el nombre accesible es «Glucosa alta».
2. **Inserta el SVG inline** (o vía `<use>`): así hereda el color de la alerta y puede animarse. Como `<img src>` queda estático y negro.
3. **Cae solo cuando llega una lectura alta nueva**, no cada vez que se pinta el panel (igual que el resto de la familia).

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function alertaNueva(svg) {               // svg = el .uva-glucose-high de esa lectura
  if (reducir.matches) return;            // sin movimiento: el icono quieto ya dice el estado
  svg.classList.remove('uva-glucose-high--caer');
  void svg.getBBox();
  svg.classList.add('uva-glucose-high--caer');
}
svg.addEventListener('animationend', (e) => {
  if (e.animationName === 'uva-glucose-high-caer') svg.classList.remove('uva-glucose-high--caer');
});
```

4. **Deja espacio:** al subir y con la onda sobresale ~1–2 px de la caja; sin `overflow: hidden` pegado al icono.
5. **Familia de alertas del panel:** objeto del dato + señal de «alto». Glucosa = gota + flecha; presión = corazón + flecha; pulso = corazón + líneas de velocidad. Si un día hay «glucosa baja», misma gota con la flecha hacia abajo (icono propio, no rotar este).
6. **Color y grosor:** `color` del contenedor; `--uva-accent` solo para la onda; `--uva-stroke` para el grosor de toda la familia.
