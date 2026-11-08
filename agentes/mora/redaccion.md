# Redacción de las páginas del Design Hub

Cuándo se usa: al escribir o revisar el texto de una página (modos M2 y M3). La **estructura** de la página la fija `.fruti/contracts/documentation.yaml`; este archivo solo dice **cómo se escribe** lo que va dentro. Si chocan, gana el contrato.

Adaptado de la *Google Developer Documentation Style Guide* vía wondelai/skills (`technical-documentation`, MIT, © 2025 Wondel.ai). Las reglas propias del inglés (contracciones, abreviaturas latinas, lista de palabras) no aplican en español.

## Voz

| Regla | Evita | Usa |
|---|---|---|
| Segunda persona o imperativo, nunca "el usuario" ni "nosotros" para instruir | "El desarrollador debe pasar `intent`." | "Pasa `intent` para indicar la acción." |
| Voz activa | "El foco es devuelto al botón por el diálogo." | "El diálogo devuelve el foco al botón." |
| Presente | "El campo mostrará un error." | "El campo muestra un error." |
| Sin "simplemente", "fácil", "solo tienes que", "por favor" | "Simplemente agrega el componente." | "Agrega el componente." |
| Sin fechas ni "nuevo" que caducan | "La nueva variante compacta…" | "La variante compacta…" |
| La condición antes de la instrucción | "Usa `loading` si la acción tarda." | "Si la acción tarda más de un segundo, usa `loading`." |
| Una idea por oración | Oraciones con tres "y" | Dos oraciones |

## API (sección `api` del contrato de documentación)

La API la dicta el código (`code_owns_api`); estas reglas solo dicen cómo describirla.

- **Props.** Una frase nominal que describe el valor y empieza con "El" o "La": "La acción que representa el botón."
- **Booleanos.** Si la prop activa una acción: "Si es `true`, … Si es `false`, …". Si describe un estado: "`true` si …; `false` en otro caso."
- **Opcionales.** Dilo y cierra con el valor por omisión: "Opcional. El tamaño del control. Por omisión, `md`."
- **Unidades y rangos.** Siempre en la descripción: "El tiempo de espera, en milisegundos. Entero de 0 a 2000."
- **Eventos.** Verbo en presente y qué datos lleva: "Se emite cuando cambia la selección; lleva el valor nuevo."
- **Deprecación.** La primera oración nombra el reemplazo, luego la versión en que se elimina y una línea de migración: "Obsoleto: usa `intent="danger"`. Se elimina en 3.0. Cambia `variant="red"` por `intent="danger"`."

## Procedimientos y ejemplos

- Pasos numerados, uno por acción, en imperativo.
- El resultado esperado va después del paso que lo produce, no antes.
- Cada ejemplo de código compila tal cual o marca sus marcadores de posición: `<NOMBRE_DEL_PROYECTO>`.
- Nada de "haz clic aquí": el texto del enlace dice a dónde lleva.

## Revisión rápida antes de publicar

1. ¿Alguna oración instruye sin decir a quién? Pásala a imperativo.
2. ¿Hay "será", "fue hecho", "simplemente", "nuevo"? Reescríbelas.
3. ¿Cada prop tiene tipo, valor por omisión y unidad cuando aplica?
4. ¿Cada deprecación nombra su reemplazo en la primera oración?
