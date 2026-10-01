# transcribing · uso (pareja con end-transcription)

1. **Siempre con texto** en la barra de pestañas: `[icono] Transcribiendo`. El SVG va oculto (`aria-hidden`); el contenedor con `role="status"` anuncia el cambio a los lectores de pantalla.
2. **Visible en todas las pestañas** mientras el dictado esté activo (vive en la barra, no dentro de una pestaña).
3. **Anima solo al empezar** el dictado (1,8 s) y queda quieto con el punto. No lo vuelvas a animar al cambiar de pestaña.

```js
const reducir = matchMedia('(prefers-reduced-motion: reduce)');
function iniciarDictado(svg) {           // svg = el .uva-transcribing de la barra
  if (reducir.matches) return;           // sin movimiento: el punto ya se ve
  svg.classList.remove('uva-transcribing--iniciar');
  void svg.getBBox();
  svg.classList.add('uva-transcribing--iniciar');
}
svg.addEventListener('animationend', (e) => {
  // la onda termina antes: quitar la clase solo cuando termina el punto
  if (e.animationName === 'uva-transcribing-punto') svg.classList.remove('uva-transcribing--iniciar');
});
```

4. **El punto es el acento:** `--uva-accent` en el contenedor (p. ej. el rojo de «grabando» del sistema). Sin acento, el punto sale del color del texto y sigue leyéndose por la forma.
5. **Al finalizar,** oculta el indicador y mueve el foco a «Iniciar dictado» (quien usa teclado no se pierde).
