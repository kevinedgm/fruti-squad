# PULZ · paquete de marca

La **Z del trasiego**:
- dos barras son dos tanques (recursos);
- la diagonal es el movimiento;
- el lote pasa del tanque de arriba al de abajo.

El nombre es «PUL» en Unbounded 800 y la Z es el símbolo. Decidido con el usuario en cuatro rondas (`../LEEME.md`): **Añil + Unbounded**.

## Archivos

| Archivo | Uso |
|---|---|
| `svg/simbolo.svg` / `-oscuro`, `png/simbolo-512.png` / `simbolo-oscuro-512.png` | Símbolo solo |
| `svg/simbolo-animado.svg`, `png/simbolo-animado.gif` | El lote se vacía arriba, corre por la diagonal y llena la barra de abajo. 2.2 s, una vez. Con «reducir movimiento», reposo directo |
| `svg/simbolo-16.svg` | Versión para 16–24 px, sin lote |
| `svg/wordmark.svg` / `-oscuro`, `-animado` / `-animado-oscuro`, `png/wordmark*.png`, `png/wordmark-animado.gif` | Nombre completo |
| `svg/favicon.svg`, `png/favicon.ico` (16/32/48), `png/favicon-{16,32,48}.png` | Favicon; el SVG cambia solo a modo oscuro (`prefers-color-scheme`) |
| `svg/app-icon.svg`, `png/apple-touch-icon.png` (180), `png/icon-192.png`, `png/icon-512.png` | Icono de la PWA y de iOS |
| `svg/app-icon-maskable.svg`, `png/icon-maskable-512.png` | `purpose: "maskable"` en el manifest (margen seguro del 26 %) |
| `svg/app-icon-redondeado.svg`, `png/icon-redondeado-512.png` | Para tiendas y presentaciones que no recortan |
| `svg/firma.svg` / `-oscuro`, `png/firma*.png` | «hecho con PULZ» para los portales de cada palenque |
| `svg/tarjeta-redes.svg`, `png/tarjeta-redes.png` | Vista previa de enlaces (WhatsApp, redes), 1200×630 |
| `lamina.png` | Vista general |
| `gen.py` | Genera todos los SVG: `python gen.py <carpeta de fuentes>` |

El texto está en trazados (Unbounded, SIL OFL): no depende de la fuente instalada.

## Color

| Token | Claro | Oscuro | Qué colorea |
|---|---|---|---|
| Tinta (`currentColor`) | `#121217` | `#f2f2f6` | Barras y «PUL» |
| Añil (`--pulz-color`) | `#3346e0` | `#7d8bff` | Diagonal y lote |
| Fondo | `#f2f2f6` | `#121217` | Fondo de marca |

El añil viene del tinte de añil oaxaqueño.

### Contraste medido

| Par | Ratio | Uso permitido |
|---|---|---|
| Tinta / fondo | 16.72:1 | Texto |
| Añil `#3346e0` / fondo claro | 6.08:1 (6.79:1 sobre blanco) | Texto y gráfico |
| Añil `#7d8bff` / fondo oscuro | 6.23:1 | Texto y gráfico |
| Cal / añil (icono de app) | 6.08:1 | Gráfico |
| Tinta / añil | ❌ 2.75:1 | Ninguno. Por eso, en el icono de app, la Z va en cal y solo el lote va en tinta |
| «hecho con» (tinta al 72 %) | 7.54:1 claro · 8.94:1 oscuro | Texto |

## Marca blanca (portales de cada palenque)

- **Variable de color:** en el portal `pulz.mx/e/<slug>`, la firma toma el color de la empresa con `--pulz-color: <color de la empresa>`. Hay que usar el SVG en línea, porque con `<img>` las variables no entran.
- **Contraste:** el color de la empresa debe dar al menos 3:1 sobre el fondo del portal. Si no llega, la firma se queda en tinta (`--pulz-color: currentColor`).
- **Escala:** dentro de un portal, PULZ es discreto: solo la firma, nunca el wordmark grande.

## Uso

- **Tamaño mínimo:**
  - símbolo completo: 24 px;
  - por debajo de 24 px, `simbolo-16`;
  - wordmark: 72 px de ancho.
- **Margen libre:** el alto de una barra.
- **Animación:**
  - solo en momentos de espera o al abrir la app;
  - una vez, sin bucle (≤ 5 s, WCAG 2.2.2).
- **No hacer:**
  - poner la diagonal en tinta sobre añil (2.75:1);
  - separar la Z del «PUL»: va al espacio de una letra.
- **Tipografía de la interfaz:** Unbounded es solo para la marca. El cuerpo de la PWA necesita una letra legible al sol, y esa decisión es aparte.

Verificado en Chromium. Firefox y WebKit, sin probar.
