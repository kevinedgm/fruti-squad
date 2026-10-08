# Movimiento

La firma es el **trasiego** del logo: lo que cambia de estado se vacía de un lado y se llena del otro, con las mismas curvas que el logo animado.

| Token | Valor | Para qué |
|---|---|---|
| rápido | 120 ms | Respuesta al tocar o pasar el ratón |
| base | 200 ms | Aparecer, desaparecer, vaciar |
| lento | 320 ms | Llenar, cambiar de pantalla |
| firma | 2.2 s | Solo el logo al abrir la app, una vez |
| vaciar | `cubic-bezier(.5, 0, .75, 0)` | Arranca lento y sale rápido |
| llenar | `cubic-bezier(.2, .8, .3, 1)` | Entra rápido y se asienta |
| estándar | `cubic-bezier(.2, .8, .2, 1)` | Todo lo demás |

## Patrones

- **El tanque sube o baja:** el nivel se llena desde la izquierda con «llenar» (320 ms). Nunca rebota.
- **Un lote cambia de etapa:** el chip anterior se vacía hacia la derecha («vaciar», 200 ms) y el nuevo se llena desde la izquierda («llenar», 320 ms).
- **Registrar una medición:** el botón se llena de `verde` y su texto pasa a «Guardado». La confirmación ocurre donde se tocó, sin ventana encima.

## Reglas

- Nada en bucle. Toda animación termina en un estado quieto con significado (WCAG 2.2.2).
- Con `prefers-reduced-motion`, el cambio es instantáneo, nunca la misma animación más lenta.
- Dos movimientos distintos a la vez no se combinan; vaciar y llenar encadenados cuentan como uno.
