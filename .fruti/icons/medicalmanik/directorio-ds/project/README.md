# Directorio Manik

Manik es lo que conoce el paciente: un directorio para encontrar médico, leer opiniones y agendar. Lema: «Tu médico, a la mano». En textos se escribe «Manik» (con mayúscula, sin «Mi» ni «Directorio» delante); en el logotipo, «manik». Se respalda con «de MedicalManik».

Este sistema sigue el manual de marca del directorio (dirección «bienestar», versión 2) y el prototipo de búsqueda y resultados. Tema claro único y deliberado.

## Fundamentos

- **El paciente decide rápido.** Cada pantalla responde primero quién, dónde, cuándo y cuánto cuesta; lo demás después.
- **Luz, no color.** Bruma y blanco dominan; la luz cian y la cálida dan ambiente; tinta para leer; cian de interfaz para lo que se toca; las estrellas son un detalle.
- **Confianza demostrable.** Cédula verificada, opiniones solo de citas agendadas y precios a la vista.
- **Personas reales.** Fotos de médicos reales en 3:4 y fotos de marca de México real; sin bancos de imágenes.

## Celular primero

El 70 % del uso será en celular y tableta, el 30 % en escritorio. Se diseña primero a 390 px; tableta y escritorio son ampliaciones.

- **Cortes:** celular < 640 px · tableta 640–1023 px · escritorio ≥ 1024 px (`bp-tableta`, `bp-escritorio`). Los componentes se adaptan al ancho de su contenedor (container queries) cuando pueden; la ficha cambia a 560 px (`ficha-amplia`).
- **Prioridad en la ficha:** médico (nombre, especialidad, cédula, calificación) → por consultorio: lugar, distancia y precio → forma de agendar y próximo lugar → acción. Unas dos fichas por pantalla de 390 × 844.
- **Pulgar:** la acción principal va abajo o a todo el ancho: «Buscar» al pie de la búsqueda, «Ver N especialistas» al pie de los filtros, barra de acción fija en el perfil (BarraAccion).
- **Llamar:** en un consultorio que agenda por teléfono, «Llamar» (`tel:`) es la acción principal y «Copiar número» la secundaria. El número siempre va escrito.
- **Nada se sale de la pantalla:** filtros en hoja inferior (BarraFiltros), chips que pasan de línea, máximo 2 consultorios visibles en la ficha.
- **Tableta:** dos columnas de fichas; búsqueda y filtros como en celular en vertical. **Escritorio:** buscador en píldora doble, filtros en fila; lista con mapa [propuesta].
- **Datos móviles:** fotos en WebP de 176 × 234 en la ficha de celular (≤ 20 KB); 480 × 640 solo en perfil y ficha amplia. Fuentes con `display=swap`.
- **Insets del dispositivo:** barras y hojas fijas al pie suman `env(safe-area-inset-bottom)`.

## Lugar en la familia MedicalManik

- **MedicalManik**: la empresa, sello madre.
- **Herramientas de la clínica** («Producto Manik»: Expediente, Agenda…): su propio sistema, Ecosistema Manik. Comparten con el directorio Urbanist, el cian del pin y los fondos de luz en marca y portada; dentro de las apps usan Atkinson y el botón azul Manik.
- **Manik**: el directorio para pacientes. Aquí el texto es **Onest**, porque el paciente escanea y decide; en las herramientas es Atkinson, porque el médico lee dosis y claves.

## Marca

- **Símbolo:** la línea de pulso de la familia (una M que es un latido) en un cuadro con punta de pin: «aquí, cerca de ti». Nunca se redibuja.
- **Logotipo:** «manik» en Sora 600 con espaciado −0.04 em, convertido a trazos; siempre los archivos, nunca reescrito con fuente.
- Versiones: color, una tinta, blanco; logotipo horizontal, vertical, con respaldo «de MedicalManik» y en blanco. Ícono de app y favicon.
- Área de respeto: un cuarto del ancho del símbolo por lado. Mínimo 24 px en pantalla y 8 mm impreso.
- Sin degradados en el sello: un solo color para imprimir, bordar y sellar.
- Archivos: grupos de assets «Marca» y «Logotipos».

## Color

| Token | Valor | Para |
| --- | --- | --- |
| `cian` | #009BB0 | Sello y áreas grandes de marca. Blanco encima 3.3:1: solo 24 px o más; nunca botones. |
| `cian-ui` | #00788A | Agendar, horarios, enlaces e iconos de acción. Blanco encima 5.2:1. |
| `tinta` | #14213D | Texto y logotipo (16.0:1 sobre blanco). |
| `muted` | #4A5674 | Texto secundario (7.3:1). |
| `bruma` | #F5FAFB | Fondo de página. |
| `luz-cian` / `luz-calida` | #D3F0F4 / #FFEFD2 | Halos de fondo; anuncios en la cálida. |
| `estrella` | #E3A21C | Solo la estrella (2.2:1): siempre con el número en tinta. |
| `exito` / `on-exito-suave` | #15814B / #157B4A | Confirmaciones; «Cédula verificada» usa el segundo sobre `exito-suave` (4.7:1). |
| `azul-medicalmanik` | #234899 | Solo en «de MedicalManik». |

- Halos: `radial-gradient` de `luz-cian` arriba a la izquierda y `luz-calida` a la derecha sobre `bruma`. La luz vive en fondos y fotografía, nunca en el sello.
- `cian-ui` sobre `luz-cian` da 4.3:1: válido para iconos, no para texto pequeño.

## Tipografía

- **Primaria · Urbanist**: titulares en 300, grandes y con el espaciado cerrado (−0.035 em); la palabra clave en 600 («Cuidarte ya no tiene que ser **difícil**»). Nombres de médicos, precios y categorías en 600.
- **Secundaria · Onest**: todo lo demás. Base 17 px. Horarios, precios y teléfonos con cifras tabulares.
- Carga: `family=Urbanist:wght@300..700&family=Onest:wght@400..700`.

## Forma, espacio y profundidad

- **Píldora para todo lo que se toca:** buscador, botones, horarios, chips y atajos.
- Radios: icono 14, icono de categoría 16, foto 20, categoría 24, ficha 28 (24 en celular).
- Espacio: 4 · 8 · 12 · 16 · 24 · 36 · 44 · 56, tomado del prototipo (por confirmar con desarrollo).
- Sombras suaves teñidas de tinta: buscador, ficha al pasar el cursor y tarjetitas flotantes. El resto se separa con borde `linea` y aire.
- Controles de 42 a 60 px; botones de cierre e iconos de 44 px; ancho máximo 1280 px.

## Iconografía

Lucide, trazo 2, en `cian-ui` (o `confianza-icono` sobre tinta). Dentro de un cuadro blanco (categorías) o un círculo `luz-cian` (portada). Con texto al lado, `aria-hidden`. Grupo de assets «Iconos».

## Voz

De tú, claro y sin tecnicismos, como una persona que conoce buenos médicos y te ayuda a llegar con uno.

| Así sí | Así no |
| --- | --- |
| «Dermatólogos cerca de ti» | «Directorio de profesionales de la salud» |
| «Hoy tiene espacio a las 11:30» | «Disponibilidad en el slot 11:30» |
| «Te mandamos un recordatorio un día antes» | «Su cita ha sido registrada exitosamente en el sistema» |
| «124 pacientes opinaron sobre la Dra. Herrera» | «¡Los mejores doctores!» |
| «Agenda en Manik» (la cita es presencial) | «En línea» o «Cita en línea»: se confunde con consulta por video |

## Consultorios

Un médico puede atender en varios consultorios. **Precio, horarios y forma de agendar son de cada consultorio**, no del médico (decisión 2026-11-04).

- **Para publicar**, cada consultorio necesita dirección, precio de consulta y al menos una forma de agendar: **agenda en Manik** (horarios; la cita es presencial), **por teléfono**, o **ambas**. Sin precio o sin forma de agendar, el consultorio no se publica y el perfil queda «Incompleto» [propuesta].
- **En resultados**, la ficha muestra los consultorios en filas (máx. 2; con más, «Ver n consultorios más»), el más cercano que cumpla los filtros primero. Cada fila lleva su precio, su forma de agendar y su acción (anatomía aprobada de FichaMedico).
- **Filtros por consultorio:** «Agenda en Manik», «Hasta $800» y «Con lugar hoy» se evalúan en cada consultorio.
- **Formas mixtas:** un consultorio puede agendar en Manik y otro solo por teléfono, o uno ofrecer las dos; cada uno muestra la suya. Con ambas, «Agendar» es la principal y «o llama al …» el enlace alternativo.
- En el perfil público, la lista de consultorios con su dirección, precio y forma de agendar [pendiente de diseñar].

## Fotografía

- **Retratos de médicos:** los sube cada médico. 3:4 vertical, mínimo 900 × 1200 px; servidos en WebP a 176 × 234 en la ficha de celular (≤ 20 KB) y a 480 × 640 en perfil y ficha amplia (≤ 120 KB). Luz natural, fondo liso y claro, sin filtros. Revisión antes de publicar: solo bloquea lo que confunde al paciente (que no sea la persona o no se vea su cara); la calidad se sugiere.
- **Sin foto:** avatar de silueta de médica o médico (o neutro si el perfil no lo indica) sobre el degradado `foto-inicio` → `foto-fin`. Decisión 2026-11-04; reemplaza la regla anterior de iniciales. La foto se sigue pidiendo en el panel.
- **Fotos de marca:** personas cuidándose en su vida diaria, México real; portada 4:5 en escritorio y 1:1 en celular.

## Accesibilidad

WCAG 2.2 AA: texto 4.5:1 en su fondo, controles de 42 px o más (objetivo mínimo 24 px), foco visible de 3 px (`focus`), estados con icono y texto, `prefers-reduced-motion` respetado. La estrella nunca va sola: el número va escrito.

## Pendientes

- Verde de «Cédula verificada»: el prototipo usaba #15814B sobre #E7F5EE (4.4:1, no cumple AA); aquí se oscurece a `on-exito-suave`.
- Estrella: el manual v2 usa #E3A21C; el paquete de marca anterior decía #F2B33D. Aquí manda el manual v2 (más reciente).
- Aviso e información (estado del perfil) usan los colores del ecosistema; decidir si pasan a tokens del directorio.
- Estado del perfil público: propuesta del panel de usuario, por confirmar (¿clínicas con perfil?, ¿verificación de cédula?).
- Perfil público con la lista de consultorios: por diseñar.
- Varios precios en un mismo consultorio (primera vez / subsecuente): sin decidir.
- Dominio `manik.mx` sin confirmar; datos de médicos, precios y teléfonos son de ejemplo.
- Escala de espacio tomada del prototipo; confirmar con desarrollo.
