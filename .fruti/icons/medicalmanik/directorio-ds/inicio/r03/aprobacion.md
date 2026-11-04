# Aprobación · Inicio Manik · r03 · F2

- **Aprobado por el usuario:** 2026-11-04 («apruebo el inicio r03, pásalo al prototipo»).
- **Congelado:** navegación (Especialidades · Preguntas · Artículos · Soy médico, sin «Entrar»), hero (registro verificado, titular, buscador, «Dónde» aproximado + «Usar mi ubicación», foto 4:5 desde tableta), «Busca por lo que sientes», «Con lugar hoy» (tarjeta con cédulas y «Ver» de contorno), «Resuelve tus dudas» (preguntas con quien responde + «Haz tu pregunta»; artículos con autor), «Cómo funciona», franja de confianza, «¿Eres médico?», pie. Una sola primaria: Buscar.
- **Implementado en:** `directorio-prototipo/` (prototipo v4).

## Enmienda 2026-11-04 · leyenda del inicio (opción B · Cercanía, elegida por el usuario)
- Título: «Encuentra a tu médico **cerca de ti**.» (antes: «Encuentra a tu médico, ve cuánto cuesta y agenda.»).
- Subtítulo: «Mira cuánto cuesta antes de ir y agenda sin pagar nada.» (antes: «La consulta es en su consultorio. Buscar y agendar es gratis.», ambiguo en «su consultorio»).
- Efecto medido: el título ocupa 2 líneas en celular (390 px) y el buscador queda visible sin desplazarse. Prototipo v16.

## Simulación de foto de marca (2026-11-04, pedido del usuario)
- El panel 4:5 lleva una ilustración de reemplazo (mamá con su hija, colores del DS) con la etiqueta «Simulación · foto de marca pendiente», y dos tarjetas flotantes de la interfaz: «Dra. Mariana Soto · Hoy, 16:30 · Agenda en Manik» (desde tableta) y «$900 · Consulta · precio a la vista» (solo escritorio, para no tapar caras en tableta).
- Decorativa (`aria-hidden`); no aparece en celular, como en el diseño aprobado.
- No es la foto final: la foto de marca sigue pendiente (dueño: marca). Al reemplazarla, conservar las tarjetas flotantes y no tapar las caras.

## Sin resolver (no se infirió)
- Foto de marca: no hay foto aprobada; panel de reemplazo «pendiente». Dueño: marca/Lima.
- Formato de precio: el wireframe usaba «MXN 900»; el prototipo sigue el DS («$900»). Dueño: Lima.
- Destinos aún no diseñados (pregunta, artículo, listados, página para médicos): avisan con un mensaje en el prototipo.

## Enmienda 2026-11-04 · portada en artículos (dato del usuario)
- Los artículos de médicos suelen tener imagen de portada: la tarjeta la muestra en lugar del icono.
- Celular y tableta: miniatura lateral cuadrada de 88 px (recorte centrado). Escritorio: miniatura de 160 px en 4:3. No se usa portada completa 16:9 en el inicio: a media columna medía unos 340 px de alto y desplazaba el resto.
- Sin portada: cuadro de color con el icono de la especialidad (respaldo).
- Imagen decorativa (`alt=""`): el título ya dice de qué trata.
- Sin resolver: proporción y tamaño mínimo que se pide al médico al subir la portada (dueño: Lima, junto con la página del artículo). La tarjeta de artículo es candidata a componente del DS.
- Portadas del prototipo: abstractas, de ejemplo.
