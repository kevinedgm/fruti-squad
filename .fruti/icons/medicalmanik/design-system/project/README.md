# Ecosistema Manik

El sistema compartido de las apps clínicas de MedicalManik: un sello, seis productos «Producto + Manik», un inicio común y un selector para pasar de una app a otra. Una clínica u hospital entra una sola vez y elige a dónde ir.

## Arquitectura

- **MedicalManik** es la empresa y el sello madre: la M de pulso en el cuadro limpio.
- **Productos**, siempre «<Producto> Manik»: Expediente (médicos), Agenda (asistentes), Compras (compras y facturación), Farmacia, Impulsa (campañas de prevención y marketing) y Grupos (administradores de clínicas y hospitales).
- **Ecosistema Manik** es el conjunto. Su identificador es el mosaico de seis cuadros: el botón que abre el selector desde cualquier app.
- **Flujo:** inicio de sesión único → **Inicio del ecosistema** (todas las apps; la persona elige) → la app. Desde cualquier app, el botón del ecosistema abre el selector y lleva de vuelta al inicio.

## Los sellos

La línea de pulso es idéntica en los siete. Cada producto cambia solo el borde del contenedor, nunca la línea:

| Producto | Rasgo | Tipo |
| --- | --- | --- |
| Expediente | pestaña de carpeta | silueta |
| Agenda | argollas de calendario | pieza separada |
| Compras | borde dentado de ticket | silueta |
| Farmacia | cruz | pieza separada |
| Impulsa | flecha que sale de la esquina | pieza separada |
| Grupos | segunda tarjeta detrás | silueta |

- Las piezas separadas llevan un corte transparente: el sello funciona sobre cualquier fondo.
- La cruz de Farmacia va siempre en el color del producto, nunca en rojo (la cruz roja es un emblema protegido).
- Mínimo 24 px en interfaz. El mosaico del ecosistema es un emblema fijo: seis cuadros aunque se sumen productos.
- Archivos: grupo de assets «Sellos» (color, fondo transparente) y «Ecosistema» (mosaico en color y a una tinta).

## Color

**Dos papeles que no se mezclan.**

1. **Identidad (`app-<producto>`)**: dice en qué app estás. Va en el sello, en la tarjeta del inicio y del selector, y en el fondo suave de la tarjeta al pasar el cursor (`app-<producto>-soft`).
2. **Interfaz (`manik` y estados)**: la acción principal es azul Manik en todas las apps; los estados (`exito`, `aviso`, `error`, `info`) son los mismos en todas.

Por qué: tres colores de producto coinciden con estados (Farmacia ≈ éxito, Compras ≈ aviso, Grupos ≈ error). Si fueran color de botón, un «Guardar» rojo en Grupos se leería como peligro. Y el mismo botón en todas las apps evita reaprender al cambiar de app. Los estados llevan siempre icono y texto.

| Producto | `app-*` | Blanco encima |
| --- | --- | --- |
| Expediente | #234899 | 8.54:1 |
| Agenda | #007C8C | 4.93:1 |
| Compras | #A15C07 | 5.19:1 |
| Farmacia | #1B7F52 | 5.0:1 |
| Impulsa | #504CA1 | 7.27:1 |
| Grupos | #C73A55 | 5.04:1 |

- Neutros con un sesgo al azul: `canvas` #F5F7FB, `surface` blanco, `ink` #14213D (15.97:1), `muted` #4A5674 (7.31:1). `subtle` es solo gráfico.
- **Navegación clara.** El azul Manik y el violeta de Impulsa no alcanzan 3:1 sobre azul noche; por eso barras y menús van en `surface` y `noche` se reserva a portada e inicio de sesión.
- `cian` #00BDD0 es acento de la marca original: solo gráfico (2.29:1 con blanco).
- Tema claro únicamente, como Manik Impulsa en producción.

## Tipografía

- **Primaria · Sora** (Google Fonts): marca, saludos y títulos. Geométrica, coincide con la palabra MedicalManik. 600 en títulos; nunca en párrafos, tablas ni datos clínicos.
- **Secundaria · Atkinson Hyperlegible Next** (Google Fonts): toda la interfaz y todo dato. La diseñó el Braille Institute para que cada letra se distinga: 1, l e I; 0 y O; rn y m. En un expediente eso evita leer mal una dosis o una clave.
- Cifras tabulares (`font-variant-numeric: tabular-nums`) en tablas, dosis y signos.
- Piso de 13 px: nada clínico por debajo.
- Carga: `family=Sora:wght@400;600;700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700`.

## Espacio, forma y profundidad

- Espaciado 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64. Radios 10 · 14 · 18 · 24 · píldora: la misma escala que Manik Impulsa en producción.
- Profundidad por borde y espacio; sombra solo para tarjetas al pasar el cursor (`shadow-hover`) y planos flotantes (`shadow-pop`).
- Controles de 44 px; barra superior de 64 px.

## Iconografía

Lucide, trazo 2, retícula 24 (el mismo set de Impulsa). Un concepto, un icono; con texto al lado llevan `aria-hidden`. Estados: circle-check, triangle-alert, circle-x, info.

## Voz

Directa y clínica: el verbo dice lo que pasa («Guardar receta», «Surtir»). Los errores dicen el límite («Fuera de rango: máximo 100 mg al día»). Trato de usted o por título profesional en saludos («Buenos días, Dra. Ramírez»).

## Relación con Manik Impulsa (decisiones abiertas)

Manik Impulsa ya tiene su propio sistema en producción. Este sistema lo respeta en espacio, radios, sombras, estados e iconos, y difiere en tres puntos que hay que decidir:

1. **Tipografía:** Impulsa usa solo Ubuntu; aquí, Sora + Atkinson.
2. **Acción:** Impulsa usa su violeta (#504CA1) para botones; aquí la acción es azul Manik en todas las apps.
3. **Lienzo:** Impulsa usa grises neutros (#F4F4F4); aquí los neutros tienen un sesgo al azul.

## Pendientes

- Confirmar la regla de una sola app (¿se salta el inicio?) y los textos de «sin acceso».
- Decidir los tres puntos de Impulsa.
- Componentes por app (tablas, formularios largos, agenda) cuando se diseñe cada producto.
