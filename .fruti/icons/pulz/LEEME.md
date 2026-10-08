# PULZ · identidad

Encargo del usuario (2026-10-08): nueva identidad para la PWA PULZ (registro y trazabilidad de producción de mezcal; repo `kevinedgm/pulz`, `docs/PULZ_MAESTRO.md`).

## Decisiones del usuario

- **Se descarta la marca actual** (`pulz-mark`: círculo con línea de pulso y brote, sobre violeta). Se leía como «salud» o «monitor cardiaco».
- **Paleta nueva desde la identidad.** Contexto: el documento maestro pedía tinta azul `#173F87` + barro y Atkinson Hyperlegible; el código actual usa violeta `#6D4AFF` + coral y Manrope/Instrument Serif. Ninguna de las dos se toma como base.
- **El nombre no tiene significado.** El símbolo cuenta el trabajo (lote, recurso, movimiento, trazabilidad), no la palabra.

## Condiciones del producto que pesan en la marca

- PULZ vive detrás de la marca de cada palenque (portal `pulz.mx/e/<slug>` con logo y color de la empresa; la PWA instalada lleva el nombre de la empresa). Dentro de los portales, PULZ es una presencia discreta («hecho con PULZ»).
- Uso de campo: una mano, bajo el sol, objetivos de 44 px y contraste alto.

## Paleta propuesta (por medir)

| Nombre | Hex | Origen |
|---|---|---|
| Maguey | `#2f5d58` | el verde azulado del agave |
| Cobre | `#b4582f` | el alambique |
| Cal | `#f4efe6` | la pared encalada del palenque; fondo |
| Tierra | `#2a211c` | el humo del horno; tinta |

## Ronda 1 · símbolo (`ronda-1/banco.png`)

| Concepto | Idea | Lectura |
|---|---|---|
| A · pencas-datos | Roseta de maguey con pencas de alturas distintas, como barras | Se lee como planta en maceta; la lectura de «datos» casi no aparece |
| **B · traza** | Una «P» dibujada como la ruta de un lote, con paradas; la última, en cobre, es el lote | La más propia y la única que cuenta la trazabilidad. Moderna. A 16 px las paradas se vuelven ruido: necesitará una versión simplificada. Riesgo: plano de metro o circuito |
| C · piña | Piña jimada con rombos y muñones | Granada o piña tropical |

## Ronda 2 · abstractos (la ronda 1 se rechazó por literal: «algo disruptivo, moderno»)

Ideas del producto, no objetos (`ronda-2/banco.png`):

| Concepto | Idea | Lectura |
|---|---|---|
| **Z · movimiento** | «Todo es lote, recurso y movimiento»: dos barras (recursos) unidas por una diagonal en cobre (movimiento). Es la Z del nombre | La más fuerte: clara a 16 px, geométrica, propia. Sobre tierra, las barras desaparecen: necesita una versión oscura con barras en cal |
| Cortes | Puntas, corazón y colas de la destilación: la banda gruesa de cobre es el corazón | ❌ Se lee como hamburguesa o como icono de menú |
| Primitivas | Recurso (cuadrado), lote (círculo) y movimiento (flecha) | Se lee como el icono de «abrir enlace externo»; sobre oscuro se pierde la flecha |

## Ronda 3 · la Z del trasiego (usuario: «más complejo, dinámico, como Grana y Hecho en Oaxaca»)

- **Historia:** *trasiego* es pasar líquido de un tanque a otro: lote, recurso y movimiento en un solo gesto.
  - La barra de arriba es un tanque con el lote en cobre.
  - Se vacía, el líquido corre por la diagonal y llena la barra de abajo.
- **Reposo:** tanque de arriba vacío, trasiego en cobre y lote ya en el tanque de abajo. El logo quieto conserva la historia.
- **Animación:** `trasiego-simbolo.gif`, `trasiego-wordmark.gif`; ~2.2 s, una vez. Con «reducir movimiento», reposo directo.
  - 0.5–1.2 s: se vacía el tanque de arriba.
  - 0.9–1.6 s: corre el trasiego.
  - 1.4–2.2 s: se llena el de abajo.
- **Color de cada palenque:** el cobre es la variable `--pulz-color`. En el portal de una empresa, la firma «hecho con PULZ» toma su color (probado con azul, verde y vino). Las barras toman `currentColor`.
- **Nombre:** «PUL» en Archivo (peso 820, ancho 112) y la Z es el símbolo, como la O de Oaxaca.
- **Versión oscura:** barras en cal.
