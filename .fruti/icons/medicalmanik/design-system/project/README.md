# Ecosistema Manik

El sistema compartido de las apps clínicas de MedicalManik: un sello, seis productos «Producto + Manik», un inicio común y un selector para pasar de una app a otra. Una clínica u hospital entra una sola vez y elige a dónde ir.

Comparte la identidad del directorio Manik (Urbanist, cian del pin y fondos de luz) en la marca, la portada, el inicio de sesión, el inicio del ecosistema y los títulos. Dentro de cada app manda la legibilidad clínica: Atkinson en interfaz y datos, y el botón en azul Manik.

## Arquitectura

- **MedicalManik** es la empresa y el sello madre: la M de pulso en el cuadro limpio.
- **Productos**, siempre «<Producto> Manik»: Expediente (médicos), Agenda (asistentes), Compras (compras y facturación), Farmacia, Impulsa (campañas de prevención y marketing) y Grupos (administradores de clínicas y hospitales).
- **Ecosistema Manik** es el conjunto. Su identificador es el mosaico de seis cuadros: el botón que abre el selector desde cualquier app.
- **Flujo:** inicio de sesión único → **Inicio del ecosistema** (todas las apps; la persona elige) → la app. Desde cualquier app, el botón del ecosistema abre el selector y lleva de vuelta al inicio.

## Administración Manik (interna, aprobada 2026-10-31)

- App del equipo MedicalManik: usuarios activos y configuración del sistema y de cada app. Sello: engrane separado en la esquina superior derecha; color grafito `app-administracion` #3A4558.
- **Solo la ven las cuentas de la empresa.** A diferencia de las apps sin acceso (apagadas con candado), para una clínica Administración no existe: no se muestra.
- En el inicio va en su propia fila, «Herramientas internas», con el chip «Solo equipo MedicalManik». El mosaico del ecosistema sigue de seis cuadros.
- El sello nunca sustituye al ícono de ajustes dentro de las apps (engrane de Lucide sin cuadro): el sello siempre lleva el cuadro con la línea de pulso.
- Prototipo: `../../administracion-r1/`.

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
| Administración (interna) | engrane en la esquina superior derecha | pieza separada |

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
| Administración (interna) | #3A4558 | 9.67:1 |

- Neutros con un sesgo al azul: `canvas` #F5F7FB, `surface` blanco, `ink` #14213D (15.97:1), `muted` #4A5674 (7.31:1). `subtle` es solo gráfico.
- **Navegación clara.** El azul Manik y el violeta de Impulsa no alcanzan 3:1 sobre azul noche; por eso barras y menús van en `surface`. `noche` queda para planos oscuros puntuales.
- **Luz de marca, como el directorio Manik:** portada, inicio de sesión e inicio del ecosistema van sobre `bruma` (#F5FAFB) con dos halos, `luz-cian` (#D3F0F4) y `luz-calida` (#FFEFD2). Dentro de las apps, `canvas`.
- `cian` #009BB0 es el cian del pin de Manik: acento gráfico (3.33:1 con blanco), nunca texto pequeño, fondo de texto ni color de producto.
- Tema claro únicamente, como Manik Impulsa en producción.

## Tipografía

- **Primaria · Urbanist** (Google Fonts): la letra del directorio Manik, así pacientes y clínicas ven la misma familia. Marca, saludos y títulos: 300 grande en portada e inicio; 600 en títulos y nombres de app. Nunca en párrafos, tablas ni datos clínicos.
- **Secundaria · Atkinson Hyperlegible Next** (Google Fonts): toda la interfaz y todo dato. La diseñó el Braille Institute para que cada letra se distinga: 1, l e I; 0 y O; rn y m. En un expediente eso evita leer mal una dosis o una clave.
- Cifras tabulares (`font-variant-numeric: tabular-nums`) en tablas, dosis y signos.
- Piso de 13 px: nada clínico por debajo.
- Carga: `family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700`.

## Espacio, forma y profundidad

- Espaciado 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64. Radios 10 · 14 · 18 · 24 · píldora: la misma escala que Manik Impulsa en producción.
- Profundidad por borde y espacio; sombra solo para tarjetas al pasar el cursor (`shadow-hover`) y planos flotantes (`shadow-pop`).
- Controles de 44 px (36 px compactos solo en tablas y filtros); barra superior de 64 px.

## Controles, formularios y diálogos (aprobado 2026-11-05)

Una sola familia para las siete apps: lo que cambia por app es el sello y el nombre; todo lo que se toca usa el azul Manik, 44 px, `radius-md` y el mismo foco. Rondas: `../../controles-r01/` y `../../formularios-r01/`.

- **Componentes:** Boton, Campo, Casilla, OpcionUnica, Interruptor, ControlSegmentado, ChipFiltro, Dialogo y el patrón Formulario.
- **Deshabilitado** (todas las piezas): «surface-soft», borde «line», texto «muted»; sin color de acción. Se dice por qué cerca del control.
- **Compacto** (`control-height-compact`, 36 px) solo en filas de tabla y barras de filtros.
- **Formularios:** una columna, orden de la tarea, grupos con título, ancho por dato, `form-max` 640 px, «(opcional)» en lo opcional, el botón principal nunca se deshabilita.
- **Contenedor por tamaño:** confirmación · diálogo hasta 6 campos · panel lateral 7 a 12 (pendiente) · página.
- **Diálogos:** `dialog-sm/md/lg` 400/560/720, `scrim` detrás, hoja inferior en celular, foco atrapado y de regreso, Esc con cambios pide descartar, clic fuera no cierra formularios.

## Iconografía

Lucide, trazo 2, retícula 24 (el mismo set de Impulsa). Un concepto, un icono; con texto al lado llevan `aria-hidden`. Estados: circle-check, triangle-alert, circle-x, info.

## IA (aprobado 2026-10-31)

Manual propio: **Manik IA** (`../../manik-ia/`), aislado de este manual; aquí solo el resumen.

La IA es una **función «IA»**, no un personaje ni un producto: los botones dicen verbo + «con IA». Prototipos: `../../ia-ronda-1/` a `../../ia-ronda-3/`.

- **Forma:** píldora azul noche (`ia` #0F1C3F, `ia-hover` #1B2B57) con el destello doble en cian claro (`ia-destello` #5FD3E2). La píldora la separa del botón primario (azul Manik, radio 14): la IA nunca es la acción principal de la vista. [tokens propuestos, aún no en `tokens.json`]
- **Todo lo que produce es borrador:** marca «Sugerido por IA», borde punteado; no entra al expediente sin confirmación del médico, completa o dato por dato; al aceptarse pierde la marca.
- **Cada dato muestra su origen** (frase del dictado o registro).
- **Movimiento con significado:** respira (halo, 1 vez) = invitación al pasar el cursor o con foco; orbita (bucle) = analizando datos («Analizando…»); traza (bucle) = redactando («Redactando…»); el destello del sello se traza una vez al llegar un resultado. Quieta en reposo; `prefers-reduced-motion` la apaga.

## Voz

Directa y clínica: el verbo dice lo que pasa («Guardar receta», «Surtir»). Los errores dicen el límite («Fuera de rango: máximo 100 mg al día»). Trato de usted o por título profesional en saludos («Buenos días, Dra. Ramírez»).

## Relación con Manik Impulsa (decisiones abiertas)

Manik Impulsa ya tiene su propio sistema en producción. Este sistema lo respeta en espacio, radios, sombras, estados e iconos, y difiere en tres puntos que hay que decidir:

1. **Tipografía:** Impulsa usa solo Ubuntu; aquí, Urbanist + Atkinson.
2. **Acción:** Impulsa usa su violeta (#504CA1) para botones; aquí la acción es azul Manik en todas las apps.
3. **Lienzo:** Impulsa usa grises neutros (#F4F4F4); aquí los neutros tienen un sesgo al azul.

## Pendientes

- Confirmar la regla de una sola app (¿se salta el inicio?) y los textos de «sin acceso».
- Decidir los tres puntos de Impulsa.
- Componentes por app (tablas, agenda) cuando se diseñe cada producto.
- Panel lateral (formularios de 7 a 12 campos con contexto visible).
