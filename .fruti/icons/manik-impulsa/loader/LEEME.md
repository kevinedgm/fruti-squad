# Manik Impulsa · loader

Ronda 2. La ronda 1 (Latido y Barrido, en `descartadas/`) se rechazó por poco original: solo animaba el logo desde fuera.

En esta ronda la animación sale de la estructura del logo. El pulso no es un dibujo encima de la burbuja: es el **hueco** que la parte en dos piezas.

| Concepto | Idea | Ciclo |
|---|---|---|
| **Monitor** ✅ elegido | La burbuja es una ventana a una señal continua. El pulso entra por la derecha, la cruza, sale por la izquierda y se detiene justo cuando la M coincide con el logo. Fuera de la burbuja la señal es una línea fina; al cruzarla se ensancha en el hueco exacto del logo. | 1.8 s (0.54 s quieto + 1.26 s de recorrido) |
| **Nace** | Primero se dibuja la línea del pulso sola; la burbuja nace desde la punta de su cola alrededor de ella; se sostiene como logo y se recoge en la cola. | 2.4 s |
| **Habla** | La burbuja se abre por el pulso como una boca: la pieza de arriba sube, la de abajo baja, y por dentro corre una señal. Luego se cierra. | 1.6 s |

Vista previa: `manik-loader-*.gif`. En vivo, en claro y oscuro y con «reducir movimiento» simulado: `prueba.html`.

## Cómo se construyó (para reproducirlo)

1. Las dos piezas del logo se renderizaron por separado a 4 px por unidad.
2. Se ajustó el círculo de la burbuja con mínimos cuadrados: centro (265.97, 226.1), radio 136.1, residuo máximo 0.5 unidades.
3. El hueco del pulso = dentro del círculo, fuera de las dos piezas y cerca de ambas. Se vectorizó con potrace.
   - Un trazo uniforme no sirve: en los picos el hueco tiene la parte de arriba plana y es más alto que un trazo. Con trazo, el fotograma de reposo difería un 7 % del logo.
4. Fidelidad del fotograma de reposo frente al logo original, en píxeles dentro de la burbuja:
   - Monitor: 0.08 % distinto.
   - Nace: 0.16 % distinto.
   - Habla: usa las piezas originales, sin cambios.

## Uso

Monitor y Nace recortan el hueco pintándolo del color del fondo, así que necesitan conocerlo:

```html
<div role="status" style="height:48px; --manik-color:#6e6eb5; --manik-bg:#ffffff">
  <!-- pegar aquí el SVG en línea -->
  <span class="sr-only">Cargando…</span>
</div>
```

- Con `<img src="…svg">` las variables CSS no entran: el fondo queda en blanco y el color en `#6e6eb5`. Sirve solo sobre fondo blanco.
- En fondo oscuro: `--manik-color:#8f8fc6; --manik-bg:<color del fondo>`.
- Los estilos están acotados a cada loader (`.manik-loader--monitor .b`…), así que pueden convivir en la misma página.
- Habla no necesita `--manik-bg`.

## Normas aplicadas

- **Bucle infinito:** permitido porque es progreso real (norma de Uva §29) y porque WCAG 2.2.2 exime la animación de una fase de carga. El loader debe desaparecer al terminar la carga.
- **Reducir movimiento:** sin desplazamiento ni escala; el logo queda quieto y solo cambia de opacidad (100 % ↔ 55 %, 1.6 s) (norma §31).
- **Sin destellos:** WCAG 2.3.1.
- **Movimientos encadenados**, nunca dos distintos a la vez (norma §30). En Nace, la línea y la burbuja se solapan unos 0.5 s.

Verificado solo en Chromium. Safari y Firefox: sin probar. Ninguno de los tres usa animaciones dentro de `<mask>` o `<clipPath>`, que es lo que más falla en Safari.

## Decisiones

- **Elegido (2026-10-06):** Monitor.
- **Pulido 1:** fuera de la burbuja se veía raro: allí la señal era el propio hueco del logo, una barra gruesa de 27.5 unidades a la izquierda y 15.75 a la derecha, con un quiebre donde cambiaba de alto. Ahora es una línea fina (9 unidades) por el centro del hueco, y el regreso entre pulsos es una curva suave. Ver `monitor-antes-despues.png`.

## Fuente

`fuente/`: `gap.py` vectoriza el hueco (`gap.d`) a partir de las dos piezas del logo (`paths.txt`); `gen.py` genera los tres SVG. Necesitan Python con numpy, scipy, scikit-image, pillow y potracer, y Chromium para renderizar las piezas.
