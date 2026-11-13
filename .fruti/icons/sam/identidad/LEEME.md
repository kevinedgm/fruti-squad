# SAM · identidad

Encargo del usuario (2026-11-13): nueva identidad de marca para SAM rediseñado (sistema interno de tareas e incidencias, PWA, interfaz con Grana). Fuente: «00 · Resumen de producto: SAM rediseñado» (aprobado 2026-11-13).

## Decisiones del usuario (2026-11-13)
- Arquitectura: **independiente** de MedicalManik (no usa su teal ni su logo).
- Nombre: **se queda «SAM»**.
- Carácter: **ágil**.

## Hechos que condicionan
- Grana es «estructura fija, color tuyo»: el color de marca de SAM entra en `--g-color-brand` y tiñe la interfaz. Debe pasar 4.5:1 en claro y en oscuro.
- Fuera: carmín (de Grana) y teal (de MedicalManik).

## Ronda 1 (`ronda-1/banco.html`, `banco.png`) · símbolo en tinta + acento provisional
| Concepto | Idea | Lectura (Claude) |
|---|---|---|
| A · Relevo | S partida en dos mitades desplazadas; el tramo central en color es el testigo que pasa | Nace de la función central (mover trabajo entre personas o fases). A 16 px se lee como S con un punto de color; el pase solo se entiende desde 32 px |
| B · Recorrido | S de tramos rectos como camino entre etapas; un punto en color es la tarea | Muy legible a 16 px. Riesgo: se lee como S de display digital; el punto casi desaparece a 16 px |
| C · Pulso | S continua inclinada; el remate superior se suelta como aviso en color | La más «ágil» a primera vista. Riesgo: el punto en la esquina se confunde con el globo de notificación de cualquier app |

Pendiente de la ronda: el lockup «S + SAM» repite la S; se resuelve en la ronda del logotipo. Color y tipografía son provisionales.

**Ronda 1 rechazada (usuario, 2026-11-13):** «no me gusta, quiero una propuesta más moderna, tecnológica, disruptiva».

## Ronda 2 (`ronda-2/banco.html`, `banco.png`) · conceptos nuevos, presentación en oscuro
Acento provisional: lima `#c6f432` en oscuro, oliva `#4d7c0f` en claro. Nombre provisional en Geist 700 (A, B) y JetBrains Mono 700 (C).

| Concepto | Idea | Lectura (Claude) |
|---|---|---|
| A · Corte | S sólida rebanada en diagonal; la parte de arriba se adelanta sobre el corte | La más fuerte a 16 px y la más «disruptiva». Riesgo: las S cortadas en dos colores existen en marcas deportivas y de energía |
| B · Matriz | S de módulos en retícula 4 × 5; la fila central se desplaza y un módulo en color es la tarea | Muy tecnológica y animable. A 16 px los módulos se empastan: necesita versión chica con menos módulos |
| C · Terminal | «s» monoespaciada + cursor de subrayado («s_»); wordmark «sam_» | Habla el idioma de desarrollo y soporte. Primera versión con cursor de bloque se leía «SI»: se cambió a subrayado. Riesgo: la estética de terminal es común en herramientas para desarrolladores |

**Elegida (usuario, 2026-11-13): A · Corte.** «me gusta la A, desarróllala».

## Ronda 3 (`ronda-3/banco.html`, `banco.png`) · desarrollo de Corte
Símbolo:
- A1 · Depurada: r2 con desplazamiento 3.2 (antes 2.6); corte de 14°. El corte se lee desde 24 px.
- A2 · Corte profundo: 25° y más desplazamiento; más rota; la parte de arriba casi sale del cuadro a 128 px.
- A3 · En marcha: A1 inclinada 9°; más velocidad, más cercana a marcas deportivas.
- A4 · Para 16–24 px: trazo 10 y curvas abiertas; versión de favicon, complementa a la grande.

Logotipo (con A1): L1 símbolo + nombre (la S se repite) · L2 el símbolo es la S («SAM» con el símbolo como primera letra; falta ajuste óptico de altura y peso frente a «AM») · L3 nombre cortado (el corte de 14° atraviesa «SAM»; el símbolo queda para el icono).

**Elegidos (usuario, 2026-11-13): símbolo A1 + logotipo L3 (nombre cortado).** Por defecto de la ronda 3 (recomendación de Claude, sin objeción): A4 como versión de 16–24 px; pendiente de confirmar.

## Ronda 4 (`ronda-4/banco.html`, `banco.png`) · color
Corrección: el oliva provisional de las rondas 2 y 3 (`#4d7c0f`) da 4.45:1 sobre el claro `#f2f2ee`: no pasa texto AA. Aquí se usa `#3f6b0a`.

| Color | Oscuro | Claro | Contraste (acento/oscuro · texto en botón · acento/claro · blanco en botón) | Lectura |
|---|---|---|---|---|
| Voltaje (lima) | `#c6f432` | `#3f6b0a` | 15.4 · 15.4 · 5.6 · 6.3 | La más disruptiva; en claro se vuelve oliva, casi otro color |
| Señal (naranja) | `#ff8a3d` | `#b93a06` | 8.4 · 8.4 · 5.1 · 5.7 | Energía; se confunde con «advertencia» en una herramienta de incidencias |
| Cobalto (azul) | `#7d93ff` | `#3348d1` | 7.1 · 7.1 · 6.3 · 7.0 | El más estable en ambos temas; el azul es el color más común en software |

**Color elegido (usuario, 2026-11-13): Voltaje** (oscuro `#c6f432`, claro `#3f6b0a`).

## Ronda 5 (`ronda-5/banco.html`, `banco.png`) · tipografía
L3 en Voltaje con tres familias de Google Fonts (OFL), más título, texto y datos de la app:
- A · Geist 800 (texto Geist, datos Geist Mono): neutra y afilada; lo distintivo lo pone el corte.
- B · Unbounded 800 (texto Geist): ancha y redondeada, futurista; solo para nombre y títulos grandes.
- C · Archivo Expanded 800 (texto Archivo, datos JetBrains Mono): expandida, de cartel, industrial.
Pendiente: con la familia elegida, redibujar la S del símbolo A1 a partir de la S de esa letra para que símbolo y logotipo compartan forma.
