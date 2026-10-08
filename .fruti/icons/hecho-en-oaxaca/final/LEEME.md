# Sello «Hecho en Oaxaca / Made in Oaxaca»

Sello para los productos de Kevin. Viene de la **marmota** de las calendas, sin dibujarla literal:
- la esfera de manta con 12 costillas;
- la banda, donde en la calenda va el nombre del pueblo;
- la espiga con sus dos discos, visible solo arriba y abajo.

Decidido con el usuario en cuatro rondas (`../LEEME.md`):
- K2;
- un solo color de tema;
- un solo OAXACA para los dos idiomas;
- giro que se asienta en el sello apilado.

## Archivos

| Archivo | Uso |
|---|---|
| `svg/sello-horizontal.svg` / `-oscuro` | Sello principal bilingüe: «HECHO EN» y «MADE IN» comparten un solo OAXACA |
| `svg/sello-horizontal-animado.svg` / `-oscuro`, `png/sello-horizontal-animado.gif` | Versión web: «HECHO EN» y «MADE IN» se turnan girando dos veces, como las caras de la marmota, y se asientan apilados. Su reposo es el sello estático (diferencia medida: 1.7 % de píxeles, solo bordes suavizados). 4.8 s, una vez. Con «reducir movimiento», el sello aparece directamente en reposo |
| `svg/sello-vertical.svg` / `-oscuro` | Versión vertical: icono arriba, texto centrado |
| `svg/sello-es.svg`, `svg/sello-en.svg` / `-oscuro` | Un solo idioma |
| `svg/icono.svg` / `-oscuro`, `png/icono-{256,512}.png` | El icono solo: debe entenderse sin texto |
| `png/*.png` | PNG de todo lo anterior, con margen |
| `lamina.png` | Vista general |

El texto está en trazados (Bricolage Grotesque, SIL OFL): no depende de la fuente instalada.

## Color (como Grana)

| Variable | Por defecto | Qué colorea |
|---|---|---|
| `--oaxaca-color` | `#e4007c` rosa mexicano | Costillas (55 % de opacidad) y banda |
| `--oaxaca-texto` | `#db0077` en claro · `#f30084` en oscuro | Texto en color («MADE IN», «HECHO EN» de un solo idioma) |
| `--oaxaca-manta` | `#fff8ee` | La esfera |
| `currentColor` | tinta `#1a1210` · manta en oscuro | Contorno, espiga, OAXACA |

Con el SVG en línea se cambia el color así: `.sello { --oaxaca-color: #00838a; --oaxaca-texto: #00727a; }`. Con `<img>` las variables no entran: se usan los valores por defecto o los archivos `-oscuro`.

### Contraste

| Par | Claro (`#fbf5ea`) | Oscuro (`#1a1210`) |
|---|---|---|
| Tinta / manta (OAXACA) | 17.0:1 | 17.0:1 |
| Texto rosa (`--oaxaca-texto`) | 4.52:1 | 4.52:1 |
| Banda rosa mexicano (gráfico) | 4.22:1 | 4.03:1 |

- Texto a 4.5:1 y gráficos a 3:1.
- Si cambias `--oaxaca-color`, comprueba el texto: cempasúchil `#d97a00` da 2.87:1 sobre claro y no sirve para texto en fondo claro.

## Uso

- Tamaño mínimo:
  - sello con texto: 96 px de ancho (horizontal) o 64 px (vertical);
  - icono solo: 24 px.
- Margen libre alrededor: el alto de la banda.
- No volver a poner los colores del arcoíris ni dibujar la espiga atravesando la esfera: dentro de ella forma una cruz y se lee como punto de mira.
- Comprobación pendiente: enseñar el icono solo, sin texto, a 2 o 3 personas de Oaxaca y preguntar «¿qué es?».

Verificado en Chromium. Firefox y WebKit, sin probar.
