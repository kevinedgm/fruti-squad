# CLNDA Studio · paquete final

Decisión (2026-10-21): símbolo C1 de la ronda 4 (la llave `{` en color de marca y el dato en tinta), paleta índigo + lima de la ronda 7, reparto C de la ronda 8 como regla y reparto B como variante permitida en oscuro. Logotipo: CLNDA en Space Grotesk 700 (trazados) con cursor de bloque.

## Color

| Token | Valor | Uso |
|---|---|---|
| tinta | `#0e0f1c` | texto en claro, fondo en oscuro, el dato en claro |
| fondo | `#f5f6fb` | fondo en claro, texto y dato en oscuro |
| índigo | `#4338ca` | llave en claro, acción primaria en claro |
| índigo-oscuro | `#8b8cf8` | llave sobre tinta (regla) |
| lima | `#c6f23d` | llave sobre tinta (variante de pantalla), cursor y acción primaria en oscuro |
| lima-claro | `#4d7c0f` | cursor y acentos lima sobre fondo claro |

Regla: el símbolo es índigo en los dos modos. La lima en la llave se permite solo sobre tinta y solo en superficies de pantalla donde la marca debe brillar: avatar de GitHub, app icon, portada de redes. Nunca lima sobre fondo claro (1.4:1).

## Archivos

| Archivo | Uso |
|---|---|
| `svg/simbolo.svg`, `simbolo-oscuro.svg`, `simbolo-lima.svg`, `simbolo-tinta.svg` | Símbolo claro, sobre tinta (índigo), sobre tinta (lima), una tinta. 32 px o más. |
| `svg/simbolo-16*.svg` | Versión 16–24 px: trazo más grueso y punto mayor. |
| `svg/favicon.svg` | Índigo en claro, lima en oscuro (`prefers-color-scheme`). `png/favicon.ico` 16·32·48. |
| `svg/app-icon.svg`, `app-icon-redondeado.svg`, `avatar.svg` | Tinta con llave lima. `app-icon-claro.svg` para fondos claros. PNG 512/192. |
| `svg/wordmark*.svg`, `lockup*.svg` | Logotipo y lockup en claro, oscuro (índigo) y oscuro (lima). |
| `svg/firma.svg`, `firma-oscuro.svg` | «hecho por CLNDA Studio» para pies de producto. |
| `svg/tarjeta-redes.svg` · `png/tarjeta-redes.png` | 1200×630 para redes. |
| `tema.json` | Tokens y reglas. |
| `gen.py` | `python gen.py <carpeta con SpaceGrotesk[wght].ttf>` |
| `lamina.html` / `lamina.png` | Todo en una hoja. |

Tipografía: Space Grotesk 700 marca, 400/500 interfaz; JetBrains Mono 500 código.
