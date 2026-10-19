# Xila · paquete de marca

La **greca bordada**: la greca escalonada de Mitla hecha en punto de cruz. Cada puntada es una X (la inicial de Xila) y la última, en cobalto, es el último valor: la anatomía editorial de la librería (línea con su valor al final, sin leyenda) convertida en símbolo.

Decidido con el usuario el 2026-10-19 (`../LEEME.md`): J + paleta Cobalto + par tipográfico «Editorial».

## Archivos

| Archivo | Uso |
|---|---|
| `svg/simbolo.svg` / `-oscuro`, `png/simbolo-512.png` / `-oscuro-512.png` | Símbolo: 17 puntadas |
| `svg/simbolo-16.svg` | Para 16–24 px: 9 puntadas más gruesas |
| `svg/favicon.svg`, `png/favicon.ico` (16/32/48), `png/favicon-{16,32,48}.png` | Favicon; el SVG cambia solo al tema oscuro |
| `svg/app-icon.svg`, `png/icon-{192,512}.png` | Icono de app o docs (azulejo cobalto, puntadas en manta, la última en hilo) |
| `svg/app-icon-redondeado.svg`, `png/icon-redondeado-512.png` | Para tiendas y presentaciones |
| `svg/avatar.svg`, `png/avatar-512.png` | Avatar de GitHub y npm (circular) |
| `svg/wordmark.svg` / `-oscuro`, `png/wordmark*.png` | Símbolo + «xila» |
| `svg/banda.svg`, `png/banda.png` | La greca corriendo como en un huipil: textura de marca para cabeceras y fondos (baldosa de 64 que se repite) |
| `svg/tarjeta-redes.svg`, `png/tarjeta-redes.png` | Vista previa de enlaces, 1200×630 |
| `tema.json` | Tokens de la paleta Cobalto, tipografía y anatomía, listos para el tema de la librería |
| `lamina.png` | Vista general |
| `gen.py` | Genera los SVG: `python gen.py <carpeta con InstrumentSans[wdth,wght].ttf>` |

El nombre va en trazados (Instrument Sans 700, SIL OFL): no depende de la fuente instalada.

## Color: paleta Cobalto

| Token | Claro | Oscuro | Contraste | Uso |
|---|---|---|---|---|
| manta | `#f6f1e8` | `#15171f` | — | Fondo |
| tinta (`currentColor`) | `#15171f` | `#f6f1e8` | 15.9:1 | Texto y puntadas |
| cobalto (`--xila-color`) | `#1f4bd8` | `#7a9bff` | 6.1 · 6.8 | Línea principal, selección, el dato, la última puntada |
| hilo | `#d14e0a` | `#ff8a3d` | 3.9 · 7.6 | Acento de marca; como texto en claro `#ad3f09` (5.35:1) |

**Categórica de siete** (gráficos): cobalto, hilo, jacaranda, ciruela, índigo, jade, nopal. Validada con simulación de protanopia, deuteranopia y tritanopia (Machado 2009): la distancia mínima entre pares es ΔE 24.3 en claro y 21.2 en oscuro en las cuatro visiones; todas ≥3.3:1 sobre el fondo. Valores en `tema.json`.

**Heatmap:** manta → `#9fb3e8` → cobalto → marino `#0b1f5c`.

Con el SVG en línea, `--xila-color` cambia el color de la última puntada; como `<img>` se usan los valores por defecto o los archivos `-oscuro`.

## Tipografía

- **Hallazgo (títulos):** Fraunces 600, opsz 72.
- **Interfaz:** Instrument Sans 400.
- **Cifras:** JetBrains Mono 600.
- **Marca:** Instrument Sans 700 (solo el nombre).

## Uso

- Tamaño mínimo: símbolo 24 px; por debajo, `simbolo-16`; wordmark 96 px de ancho.
- Margen libre: una puntada (6 unidades de 64).
- La última puntada es siempre la de color: es el dato, no un adorno.
- No rellenar las puntadas ni cambiar su grosor; no girar la greca.

Verificado en Chromium. Firefox y WebKit, sin probar.
