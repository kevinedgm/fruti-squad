# Convia · app de planes en Oaxaca · brief (borrador 1, 2026-10-30)

## Idea (usuario)
App/sitio tipo directorio de Oaxaca: cafeterías, hoteles boutique, museos, restaurantes, experiencias y tours. Se ofrece a esos negocios y funciona como **puerta de entrada** para venderles CLNDA Booking o Mesanda.

## Intención (usuario, 2026-10-30)
«No sabe uno qué plan hacer; siempre visitamos los mismos lugares». Descubrir cafés, restaurantes, tours, talleres y cosas para hacer solo. Orientada a Oaxaca.

Consecuencias (inferencia):
- No es un directorio (responde «¿dónde está X?», cuando ya sabes qué quieres) sino una app de **planes** (responde «¿qué hago?», cuando no lo sabes). La entrada es por intención, momento y compañía (hoy, este fin, solo, en pareja, con niños), no por categoría.
- Públicos (usuario, 2026-10-30): **gente de Oaxaca y turistas**. Buscar un hotel boutique en una app hecha para Oaxaca no es lo mismo que en Google o Booking.
  - Local: «¿qué hago hoy?», uso semanal, lo nuevo y los eventos, español.
  - Turista: «¿dónde me quedo y qué no me pierdo?», uso por viaje (antes y durante), español e inglés, fechas de viaje.
  - Quien sale solo (usuario, 2026-10-30): busca algo que hacer el fin de semana y **se inscribe**: talleres, clases, tours grupales. Filtro «para ir solo» (actividades donde llegas sin compañía y conoces gente).
    Datos que exige una actividad con inscripción: fecha y hora, cupo disponible, precio, idioma, nivel, punto de encuentro, política de cancelación. Flujo: ver → inscribirse (con pago o apartado) → confirmación → recordatorio.
    Inferencia: talleres y operadores de tours necesitan cobrar e inscribir; es otro producto que se les puede vender (inscripciones con cupo, como Booking pero para actividades con fecha).
  - Propuesta: un mismo contenido curado y dos entradas («Vivo aquí» / «Estoy de visita»), no dos apps.
  - Diferencia frente a Google y OTAs (inferencia): selección local de lugares pequeños y reserva directa con el hotel vía CLNDA Booking, sin comisión de intermediario (las OTAs cobran comisión al hotel; verificar rangos actuales antes de usar cifras).
- Lo nuevo importa: marcar «ya fui», guardar, y destacar lo que no has visitado.
- Talleres y eventos tienen fecha: el contenido caduca cada semana. Quien lo carga son los negocios (incentivo: exposición gratis), y esa carga es la relación que abre la venta de Booking y Mesanda.
- ~~Híbrido con registro abierto~~ → **Decisión del usuario (2026-10-30): entrada con aprobación.** Evitar negocios no establecidos o informales y cuidar la estética (imágenes, textos, identidad de marca).
  - Entrada: el negocio solicita (o se le invita) → el equipo revisa con criterios objetivos → aprobado o no.
  - Criterios propuestos (por validar): establecimiento físico o operador con registro verificable (RFC; para turismo, Registro Nacional de Turismo — verificar requisito vigente), domicilio y horario fijos, identidad de marca propia (logo), fotos que cumplan la guía.
  - Guía de contenido propuesta: fotos horizontales, luz natural, sin texto encimado, sin marcas de agua ni collages, resolución mínima; textos descriptivos, sin mayúsculas sostenidas ni emojis, extensión acotada.
  - Coherencia visual: la app envuelve todo con su propio diseño; la identidad del negocio aparece en lugares controlados (logo, foto de portada), no en sus colores por toda la ficha.
  - Cambios posteriores (eventos, fotos nuevas) también pasan por revisión.
- **Modelo de operación (usuario, 2026-10-30):** manual de estándares público → el negocio solicita acceso → el equipo revisa el establecimiento → se le genera acceso a un **panel de configuración** → el negocio carga y modifica su información → cada cambio queda en revisión y se publica tras aprobación (12 a 24 h).
  Dos compuertas: **admisión** (una vez, el establecimiento) y **moderación** (cada cambio, el contenido).
  Piezas que faltan (propuesta):
  1. Mientras un cambio está en revisión, sigue publicada la última versión aprobada (publicado vs borrador en revisión); la ficha nunca desaparece.
  2. Cambio rechazado: motivo que cita la regla del manual + corregir y reenviar.
  3. Cambios urgentes (cerrado hoy, evento cancelado, cambio de horario del día): quitan información y su riesgo estético es nulo → publicación inmediata o revisión en 1–2 h (por decidir).
  4. Eventos con fecha: enviarlos con al menos 48 h de anticipación para que la revisión no los deje fuera.
  5. El panel valida antes de enviar (orientación y resolución de fotos, extensión de textos, mayúsculas sostenidas): menos rechazos, menos carga del equipo.
  6. Capacidad del equipo: ¿12–24 h también en fin de semana?
  **Decisiones del usuario (2026-10-30):**
  - En revisión, el público sigue viendo la versión publicada.
  - Rechazo: el negocio hace los cambios y reenvía.
  - **Inmediato** (sin moderación): modificaciones a talleres, eventos u horarios ya publicados.
  - **Moderado** (12–24 h): evento nuevo, fotos nuevas, cambio de descripción del establecimiento y similares.
  - **Decisión del usuario (2026-10-30): la regla es por campo, no por objeto.** Inmediatos: fecha, hora, cupo, precio, cancelación, horario, «cerrado hoy». Moderados aunque sean de un evento existente: título, texto y fotos. Si no, cambiar la foto o el texto de un evento ya aprobado se saltaría la moderación.

## Fases (usuario, 2026-10-30)
- **Fase 1 · solo información.** Ficha de cada negocio: descripción, galería, ubicación, horario, contacto y redes sociales. Descubrir (portada curada, filtros) y guardar se mantienen. Sin reservas ni inscripciones: la acción de la ficha es **contactar** (WhatsApp, llamar, redes, cómo llegar).
- **Fase 2 · integraciones, poco a poco.** Hoteles → CLNDA Booking; restaurantes → Mesanda Reservas; después talleres y tours (inscripciones). No todo de golpe.
- Mecanismo (inferencia): en fase 1 se miden los contactos que la app genera por negocio (toques a WhatsApp, llamar, cómo llegar). Ese número es la evidencia para vender la fase 2: «este mes 40 personas te escribieron desde la app; con Booking reservarían directo».
- Criterio para pasar a fase 2 (propuesta, por definir): suficientes contactos mensuales por negocio para que la integración valga la pena.

## Mecanismo (inferencia)
Dos lados: **visitantes** que buscan qué hacer y **negocios** que quieren aparecer.
- Para el negocio: aparecer (gratis o barato) → relación con CLNDA → venta de Booking (sitio + reservas) o Mesanda (comandero).
- Para el visitante: descubrir y **reservar directo con el negocio** (sin comisión), coherente con CLNDA Booking (no es marketplace: el directorio manda al sitio propio del negocio).

## Riesgos
- Huevo y gallina: sin visitantes, aparecer no le vale nada al negocio; sin buenos negocios, no hay visitantes. Hay que decidir qué lado se arranca primero.
- Competencia directa: Google Maps y TripAdvisor ya listan todo; un directorio genérico pierde. La diferencia posible: curaduría local y reserva directa.
- Conexión desigual, resuelta en parte: Booking encaja (botón «Reservar» → sitio del hotel); con el complemento **Mesanda Reservas** (usuario) los restaurantes también tienen botón «Reservar mesa» que llega a su plano.

## Tabla de publicación por campo (decidida)
| Campo | Publicación |
|---|---|
| Fecha, hora, cupo, precio, política de cancelación | Inmediata |
| Horario del establecimiento, «cerrado hoy», evento cancelado | Inmediata |
| Título, descripción, fotos (de un evento existente o del establecimiento) | Moderada 12–24 h |
| Evento o taller nuevo | Moderado 12–24 h |
| Logo, nombre, categoría del establecimiento | Moderado 12–24 h (propuesta, por confirmar) |
Propuesta (por confirmar): «inmediato» = pasa la validación automática del panel y se publica; queda registrado para revisión posterior.

## Pendiente de operación (usuario, 2026-10-30: «tema de operación de negocio», se decide después)
- Quién carga los primeros lugares al lanzar (curaduría e invitación vs. solicitudes espontáneas) y cuántos necesita la fase 1.

## Identidad (usuario, 2026-10-30)
- Marca independiente de CLNDA. Evoca Oaxaca sin nombrarla. Español fácil en inglés. Personalidad: amigo que sabe.
- **Nombre: Convia** (convite + vía; con v). Rondas en `nombres-r1.md` a `nombres-r6.md`.
- Búsqueda web preliminar (no es búsqueda de marca): existe Convia Inc. (EE. UU., tecnología para edificios; otra clase y mercado) y una app sueca «Convie» de gastronomía y hotelería (nombre parecido, mismo rubro).
- **Símbolo: E1b** (estrella de un trazo a mano, inclinada; inspirada en las estrellas del convite). `../convia-r7/E1b.svg`.
- ~~Color: paleta B «Convite + cantera»~~ (2026-10-30: el usuario ya no está convencido; busca **elegancia y pulcritud**, no infantil). Antes:: fondo verde cantera #1f4d3a, principal magenta #d42a66, acento amarillo #ffc53d, apoyo verde #3f8f6b, papel #f6f3ea, tinta #15241d. Contraste WCAG 2.2 AA verificado en `../convia-color-r1/`.
- **Plataforma (usuario): directorio web** (responsive), no app móvil primero.
- Dirección visual nueva: elegante y pulcra. Prototipo de portada con tres paletas sobrias en `../convia-web-r1/` (Gloock + Instrument Sans).
- **Identidad v1** en `../convia-final/` (guía, SVG, PNG, tema.json): paleta Cantera (#2f5a45 sobre papel #f7f5f0) y Gloock + Instrument Sans, elegidas con la dirección del usuario; pendientes de su confirmación.
- Pendiente: Marcanet (clases 9, 35, 39, 42), dominios y redes; prueba de recuerdo con 5 personas.

## Incógnitas
- ¿Curado (solo lo recomendado) o abierto (cualquier negocio se registra)?
- ¿Quién paga y qué? (¿listado gratis, destacado de pago, solo como gancho?)
- Idioma (turista nacional / extranjero), solo Oaxaca capital o el estado.
