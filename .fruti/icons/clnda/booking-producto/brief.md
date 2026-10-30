# CLNDA Booking · brief funcional (borrador 1, 2026-10-30)

## Modelo
CLNDA vende a cada hotel **su sitio web completo con reservas integradas**: dominio y marca del hotel, pie «hecho por CLNDA». No es marketplace: un sitio por hotel; el huésped reserva y paga directo con el hotel.

## Enunciado
El **huésped** necesita **reservar una habitación en fechas concretas** directamente con el hotel, porque hoy lo hace por teléfono, WhatsApp o una OTA con comisión.
El **hotel** necesita **publicar habitaciones, tarifas y disponibilidad y recibir reservas confirmadas** sin depender de intermediarios.

- Verbo principal (huésped): reservar habitación. Resultado verificable: folio de reserva + correo de confirmación.
- Verbo principal (hotel): recibir y gestionar reservas. Resultado verificable: la reserva aparece en el panel y bloquea la disponibilidad.

## Dos superficies
1. **Sitio del hotel** (marca del hotel): inicio, habitaciones, galería, servicios, ubicación/contacto, flujo de reserva.
2. **Panel CLNDA Booking** (marca CLNDA Booking): habitaciones, tarifas, calendario de disponibilidad, reservas, contenido del sitio, ajustes de marca.

## Flujo de reserva (huésped, propuesta)
fechas + huéspedes → habitaciones disponibles con precio total → elegir habitación (y tarifa) → datos del huésped → **pago o garantía (incógnita)** → confirmación con folio → correo.
Errores: sin disponibilidad (sugerir fechas cercanas), habitación tomada mientras pagaba, pago rechazado, sesión reanudada.

## Hechos / supuestos / incógnitas
- Hecho: sitio completo con reservas; marca del hotel frente al huésped.
- Supuesto: hoteles pequeños o boutique en México, sin equipo técnico; idioma español e inglés.
- Incógnitas: cobro en línea (total, anticipo o solo solicitud); qué edita el hotel solo y qué hace CLNDA; sincronización con OTAs (channel manager); si también se ofrece el motor suelto para hoteles que ya tienen sitio; varias monedas; dominio propio del hotel.
