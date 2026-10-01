# turtle · uso

1. **Inserta el SVG inline** (o vía `<use>`): así hereda `currentColor` y puede animarse. Como `<img src>` no hereda color ni se esconde.
2. **Dentro de un control:** botón de al menos 44×44. Si solo lleva el icono, el nombre va en el botón: `<button aria-label="Tortuga">`. El SVG ya trae `aria-hidden="true"`.
3. **Activa el movimiento al interactuar** (el icono no detecta solo el cursor):

```js
const svg = boton.querySelector('.uva-turtle');
const esconder = () => { svg.classList.remove('uva-turtle--esconder'); void svg.getBBox(); svg.classList.add('uva-turtle--esconder'); };
boton.addEventListener('pointerenter', esconder);
boton.addEventListener('focus', esconder);
boton.addEventListener('click', esconder);
svg.addEventListener('animationend', () => svg.classList.remove('uva-turtle--esconder'));
```

4. **No lo pongas en bucle:** se esconde una vez por interacción (WCAG 2.2.2). Con «reducir movimiento» del sistema no se mueve; el feedback lo da el estado del botón (fondo y anillo de foco).
5. **Grosor y color:** `--uva-stroke` cambia el grosor (un solo valor para toda la familia, también `rabbit`); el color sale de `color` del contenedor.
6. **Con el conejo:** son de la misma familia (silueta continua, miran a la derecha). Si un producto los usa como «lento / rápido», eso es una metáfora nueva: regístrala aparte, no cambies el significado de este icono.
