# App de planes en Oaxaca · brief (borrador 1, 2026-10-30)

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
- Propuesta para curado vs abierto: **híbrido**. Registro abierto (cualquier negocio sube su ficha, talleres y eventos); los planes recomendados se curan.

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

## Incógnitas
- ¿Curado (solo lo recomendado) o abierto (cualquier negocio se registra)?
- ¿Quién paga y qué? (¿listado gratis, destacado de pago, solo como gancho?)
- Idioma (turista nacional / extranjero), nombre y marca, solo Oaxaca capital o el estado.
