# Manik Impulsa · loader

Dos propuestas con el símbolo **exacto** del logotipo (las dos piezas originales, sin redibujar). El pulso es el hueco entre ellas.

| Variante | Qué hace | Ciclo | Técnica |
|---|---|---|---|
| **Latido** | El símbolo late dos veces (crece al 108 %, rebota, 104 %) y descansa | 1.2 s | `transform: scale` (funciona en todos los navegadores) |
| **Barrido** | El símbolo «se enciende» de izquierda a derecha como un monitor y se apaga por la derecha | 1.6 s | `clip-path: inset()`; si el navegador no lo soporta, se ve el logo quieto |

Vista previa: `manik-loader-latido.gif`, `manik-loader-barrido.gif`; en vivo: `prueba.html` (incluye simulación de «reducir movimiento»).

Verificado solo en Chromium. Safari y Firefox: sin probar.

## Uso

```html
<div role="status" class="loader" style="width:48px;height:48px">
  <img src="/manik-loader-latido.svg" alt="">
  <span class="sr-only">Cargando…</span>
</div>
```

- El SVG va oculto (`aria-hidden` / `alt=""`); el aviso «Cargando…» lo da el contenedor con `role="status"`.
- Color: `#6e6eb5` por defecto. En fondo oscuro, `--manik-color: #8f8fc6` (solo si el SVG va en línea; con `<img>` las variables CSS no entran).
- El lienzo tiene margen para que el latido no se recorte: el símbolo ocupa ~90 % del cuadro.

## Normas aplicadas

- **Bucle infinito:** permitido porque es progreso real (norma de Uva §29, `loop` solo para progreso) y porque WCAG 2.2.2 exime la animación de una fase de carga en la que no se puede interactuar. Si la carga deja la página usable, el loader debe desaparecer al terminar.
- **Reducir movimiento:** sin escala ni barrido; el símbolo solo cambia de opacidad (100 % ↔ 55 %, 1.6 s), que sigue indicando «trabajando» (norma §31).
- **Sin destellos:** ningún cambio supera 3 por segundo (WCAG 2.3.1).
- **Un solo movimiento a la vez** (norma §30).

## Pendiente (decisión tuya)

- Elegir Latido o Barrido.
