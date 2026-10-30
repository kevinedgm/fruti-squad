# NisaStudio · paquete final

App interna de Nisa Nabani para crear piezas de redes y avisos con plantillas de la marca: efemérides, avisos («mañana no laboramos»), promoción de servicios y carruseles «¿Sabías que…?». Entra por hub.nisanabani.com.

## Símbolo · Encuadre
Dos esquinas de recorte (trazo 8, puntas redondas, radio 6) y tres células dentro (radios 15, 11 y 6); la mediana, arriba a la derecha, en acento. Componer una pieza.

## Color
| Color | Hex | Uso | Contraste |
|---|---|---|---|
| Degradado | 135°, #4F46E5 → #14B8A6 | Ícono de app, superficies de marca | — |
| Índigo | #4F46E5 | Inicio del degradado | Blanco 6.3:1 |
| Turquesa | #14B8A6 | Fin del degradado; acento sobre blanco | Blanco 2.5:1 (solo títulos grandes) |
| Índigo profundo | #3730A3 | Logotipo y símbolo sobre claro | Sobre blanco 9.9:1 |
| Amarillo claro | #FDE68A | Acento del símbolo sobre el degradado | Sobre índigo 5.0:1 |

## Archivos (`svg/`, `png/`)
- `simbolo`, `simbolo-blanco`, `simbolo-1tinta`; `logotipo`, `logotipo-blanco`, `logotipo-1tinta`, `logotipo-respaldo`, `logotipo-respaldo-blanco`, `logotipo-vertical` («Nisa» Poppins 700 + «Studio» Poppins 400, a trazos).
- `app-icon`, `app-icon-maskable`, `favicon`: PNG de 16 a 512 px. `tema.json`.
- Regenerar: `python3 gen.py <woff de Poppins> <carpeta temporal> <fuentes para la lámina>` y `node png.cjs`.

## Reglas
1. Texto blanco pequeño sobre el lado índigo; sobre el turquesa solo títulos grandes.
2. Una sola célula de acento por símbolo.
3. Índigo y turquesa son de la app; las piezas que genera usan la identidad de Nisa Nabani.
4. No rotar el encuadre ni sacar las células de las esquinas.

## Pendiente
- Búsqueda de anterioridades de «NisaStudio» ante el IMPI.
- Definir las plantillas (efeméride, aviso, promoción, carrusel) y sus formatos (1080 × 1350, 1080 × 1920).
