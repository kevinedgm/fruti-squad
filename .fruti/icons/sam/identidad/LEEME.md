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

**Ronda 5 rechazada (usuario, 2026-11-13):** «no me gusta ninguna, debe estar pensada en el contexto de la aplicación; SAM es Simple Activity Manager».

## Ronda 6 (`ronda-6/banco.html`, `banco.png`) · tipografía desde la app
Hecho nuevo: SAM = **Simple Activity Manager** (se usa como descriptor bajo el logotipo).
Criterio: la marca usa la misma letra que la interfaz; legible a 13–15 px en celular; números claros para folios, horas y fechas. Cada opción se muestra en una pantalla «Mis actividades» (oscuro y claro) con datos ficticios.
- A · Instrument Sans (datos JetBrains Mono): la letra de Grana; misma voz que la librería; compacta.
- B · Figtree (datos JetBrains Mono): geométrica y abierta; la más «simple»; algo menos densa.
- C · IBM Plex Sans (datos IBM Plex Mono): técnica; distingue I, l y 1; más seria.

**Replanteo (usuario, 2026-11-13): «creo que hay que replantear el logo y colores».** Motivos elegidos: el logo cortado es «demasiado agresivo» y «no dice actividad»; del color, falla «el oliva del modo claro». Quedan sin efecto A1 + L3 y el valor claro `#3f6b0a`.

## Ronda 7 (`ronda-7/banco.html`, `banco.png`) · replanteo
Regla de color nueva: el lima `#c6f432` no se oscurece. Solo es relleno (botón principal, estado activo, acento del símbolo) y siempre toca tinta (texto oscuro encima; contorno de tinta en claro). En claro, texto, enlaces y foco van en tinta. Lima sobre claro mide 1.1:1, por eso nunca va solo ni como texto.

| Símbolo | Idea | Riesgo |
|---|---|---|
| A · Etapas | dos etapas cumplidas (tinta) + la actividad en curso (píldora lima) | puede leerse como «escribiendo…» o carga |
| B · Ruta | la S es el camino, trazo redondo; la parada en lima es la actividad | a 16 px la parada intermedia se pierde |
| C · Tarjetas | la tarjeta de actividad pasa adelante y queda completada (palomita en tinta fija) | tarjetas y palomita son comunes en apps de tareas |

Nombre en Instrument Sans 700 (provisional) con el descriptor «Simple Activity Manager».

**Elegido (usuario, 2026-11-13): C · Tarjetas.** «me gusta la C, desarróllala».

## Ronda 8 (`ronda-8/banco.html`, `banco.png`) · desarrollo de Tarjetas
- C1 · Depurada: tarjetas 9:7, palomita más firme, la de atrás sólida.
- C2 · Atrás en contorno: la anterior solo como contorno («ya pasó»); más ligera; en claro pesa menos.
- C3 · Pila de etapas: tres tarjetas; más flujo, más cargada; se empasta a 16 px.
- C4 · Para 16–24 px: más desplazamiento y trazos más gruesos; complementa a la grande.
Logotipo con C1 y C2 en tres arreglos: horizontal (barra de la app, documentos), vertical (portada, pantalla de inicio) y compacto sin descriptor.

**Elegido (usuario, 2026-11-13): C2 (tamaños grandes) + C4 (16–24 px).**

## Ronda 9 (`ronda-9/banco.html`, `banco.png`) · prueba en contexto
Criterio acordado: si se lee bien en pestaña, icono de PWA y barra superior, se congela.
| Contexto | Resultado (observación de Claude en el render, a 1x y ampliado a 3x) |
|---|---|
| Pestaña, C4 a 16 px, claro y oscuro | Se distinguen dos tarjetas y la palomita; el lima identifica la pestaña entre las otras |
| Icono PWA, C2 a 40 px en icono de 56, Android (círculo) e iOS | El símbolo queda dentro de la zona segura; la máscara circular no lo recorta |
| Barra superior, C2 a 28 px + «SAM» | Se lee en claro y oscuro; el contorno de la tarjeta de atrás aguanta a 28 px |
| Notificación push, silueta de una tinta a 16 px (`notificacion.svg`) | Pasa: tarjeta delantera rellena con palomita calada |
No verificado: dispositivos reales (la prueba es una simulación en navegador) ni el ajuste del renderizado de favicon en cada navegador.

**CONGELADO (usuario, 2026-11-13): símbolo Tarjetas C2 (grande) + C4 (16–24 px) + silueta de notificación; color Voltaje `#c6f432` con la regla de relleno (ronda 7).** Desde aquí solo se pule; no se rediseña.

## Ronda 10 (`ronda-10/banco.html`, `banco.png`) · tipografía con el símbolo congelado
Criterio: la misma letra en marca e interfaz; legible a 13–15 px en celular; números claros; que acompañe las esquinas redondas. Folios en JetBrains Mono.
- A · Instrument Sans: la letra de Grana; compacta; terminales rectos frente a esquinas redondas.
- B · Figtree: geométrica y abierta; repite las curvas del símbolo; la más amable; más ancha.
- C · Onest: hecha para interfaces; punto medio entre A y B.
Sale IBM Plex Sans (ronda 6): angulosa frente al símbolo redondo.
