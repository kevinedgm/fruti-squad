# NisaLab · tipos de parámetro · paquete final

Cada tipo de parámetro tiene su **ficha de elemento**: dos letras blancas (Poppins 600, convertidas a trazos) sobre un cuadrado redondeado azul real `#052A76` (contraste 13.1:1). Sirve para marcar, agrupar y filtrar parámetros.

## Tipos
| Tipo | Letras | Token | Ejemplos |
|---|---|---|---|
| Microbiológicos | Mb | `parametro-microbiologicos` | Coliformes, E. coli, Salmonella, mohos y levaduras |
| Fisicoquímicos | Fq | `parametro-fisicoquimicos` | pH, conductividad, turbidez, dureza, sólidos |
| Metales | Me | `parametro-metales` | Plomo, arsénico, mercurio, cadmio, hierro |
| Orgánicos | Or | `parametro-organicos` | Plaguicidas, compuestos volátiles, hidrocarburos |
| Nutrimentales | Nu | `parametro-nutrimentales` | Proteína, grasa, humedad, cenizas, fibra |

## Por qué así
Tres señales conviven en una fila de resultados y cada una usa un canal distinto:
- **Área:** círculo de color (tono).
- **Tipo de parámetro:** cuadrado azul con letras (forma + texto). Nunca cambia de color.
- **Estado:** color semántico (verde, ámbar, rojo) con texto.

Prueba: en escala de grises la fila se sigue leyendo (ver `lamina.html`).

## Archivos (`svg/<tipo>/`)
- `ficha.svg`: sobre fondos claros.
- `ficha-blanco.svg`: ficha blanca con letras azules, sobre azul real o fotos oscuras.
- `ficha-1tinta.svg`: `currentColor`, letras caladas (máscara).
- `png/<tipo>/`: las tres versiones a 16, 24, 32, 64, 128 y 512 px.
- `tema.json`: tipos, letras, tokens y reglas.
- Regenerar: `python3 gen.py <carpeta con poppins-latin-600-normal.woff> <carpeta temporal> [carpeta de fuentes para la lámina]` y `node png.cjs`.

## Reglas
1. El tipo nunca usa tono.
2. La ficha va con el nombre del tipo al lado; en columnas angostas, el nombre va en tooltip y en el nombre accesible.
3. Dos letras, mayúscula + minúscula, sin punto.
4. Mínimo 16 px; 18–20 px en filas de tabla.
5. No rotar, no colorear por tipo, no usar solo el contorno.
6. Un tipo nuevo usa dos letras que no choquen con las existentes ni con símbolos químicos que se lean como resultado (Pb, Hg, As).
