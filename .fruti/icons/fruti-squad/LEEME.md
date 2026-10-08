# Fruti Squad · icono (Espiral)

Ruta elegida el 2026-10-08, después de tres rondas (`ronda-1/`, `ronda-2/` y `ronda-3/`, que incluye el generador `final.py`).

Idea: un núcleo lima (el orquestador) y cinco módulos (los agentes) que se abren en espiral. Son piezas distintas que forman un solo flujo. No hay fruta literal.

## Afinado (ronda 3 → final)

A 16 px, la Espiral de la ronda 3 tenía huecos de 0.6 px entre brazos, así que se empastaba.

- **Primer intento (descartado):** agrandar los huecos achicando la figura. Quedaba pequeña y perdía la espiral.
- **Solución:** aumentar la **inclinación** de los brazos (salen más rápido hacia fuera: radio de 116 a 212 en 46°), con trazo 64, núcleo 44 y la figura al 86 % del cuadro.

| | Hueco entre brazos a 16 px | Hueco brazo–núcleo a 16 px |
|---|---|---|
| Ronda 3 | 0.62 px | 1.03 px |
| **Final** | **1.46 px** | **1.07 px** |

Evidencia: `evidencia-tamanos.png` (16–192 px) y `evidencia-maskable.png` (recortes de Android).

## Archivos

| Archivo | Uso |
|---|---|
| `fruti-squad.svg` | Icono principal (cuadro oscuro), estático |
| `fruti-squad-animado.svg` | Igual, con la entrada animada |
| `fruti-squad-tinta.svg`, `fruti-squad-tinta-animado.svg` | Una tinta (`currentColor`), sin fondo: toma el color del texto |
| `fruti-squad-entrada.gif` | Entrada animada para README o redes |
| `png/fruti-squad-{1024,512,460,256}.png` | Avatar de GitHub/npm (GitHub recomienda 460 px o más), presentaciones |
| `png/apple-touch-icon.png` | iOS (cuadrado lleno; iOS lo redondea) |
| `png/icon-{192,512}.png`, `png/icon-maskable-{192,512}.png` | PWA o docs instalables |
| `favicon/favicon.svg`, `favicon/favicon.ico`, `favicon/favicon-{16,32,48}.png` | Pestaña del navegador y Kiro |

Colores, modificables con variables CSS si el SVG va en línea: `--fs-fondo:#161616`, `--fs-claro:#F8F8F5`, `--fs-acento:#B7F34D`.

## Movimiento

- **Entrada:** los cinco módulos se despliegan girando, uno tras otro (cada 70 ms), y el núcleo se enciende al final. Dura 1.2 s y no se repite.
- Se aplica con la clase `fs-esp--entrada`, que va en los archivos `-animado`.
- Con «reducir movimiento», el icono aparece directamente completo.

## Contraste (WCAG)

| Par | Contraste |
|---|---|
| Claro `#F8F8F5` sobre fondo `#161616` | 17.0:1 |
| Lima `#B7F34D` sobre fondo `#161616` | 13.7:1 |
| Lima sobre claro | 1.24:1 — nunca poner el núcleo lima sobre fondo claro; ahí se usa la versión de una tinta |
| Tinta `#161616` sobre blanco | 18.1:1 |

## Uso

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

## Pendiente

- La identidad de Kiro (fantasma, morado) queda fuera a propósito: «for Kiro» va en texto.
- ~~Tarjeta para redes~~ hecha: tipografía Sora, logotipo y tarjetas en `logotipo/`.
