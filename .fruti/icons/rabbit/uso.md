# rabbit · uso

1. **Inserta el SVG inline** (o vía `<use>`): así hereda `currentColor` y puede animarse. Como `<img src>` no hereda color ni salta.
2. **Dentro de un control:** botón de al menos 44×44. Si solo lleva el icono, el nombre va en el botón: `<button aria-label="Conejo">`. El SVG ya trae `aria-hidden="true"`.
3. **Activa el salto al interactuar** (el icono no detecta solo el cursor):

```js
const svg = boton.querySelector('.uva-rabbit');
const saltar = () => { svg.classList.remove('uva-rabbit--saltar'); void svg.getBBox(); svg.classList.add('uva-rabbit--saltar'); };
boton.addEventListener('pointerenter', saltar);
boton.addEventListener('focus', saltar);
boton.addEventListener('click', saltar);
svg.addEventListener('animationend', () => svg.classList.remove('uva-rabbit--saltar'));
```

4. **No lo pongas en bucle:** salta una vez por interacción (WCAG 2.2.2). Con «reducir movimiento» del sistema no se mueve; el feedback lo da el estado del botón (fondo y anillo de foco).
5. **Grosor y color:** `--uva-stroke` cambia el grosor (un solo valor para toda la familia); el color sale de `color` del contenedor.
