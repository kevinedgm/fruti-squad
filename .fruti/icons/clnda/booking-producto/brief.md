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
fechas + huéspedes → habitaciones disponibles con precio total → elegir habitación (y tarifa) → datos del huésped → **pago o garantía según la política del hotel** → confirmación con folio → correo.
Errores: sin disponibilidad (sugerir fechas cercanas), habitación tomada mientras pagaba, pago rechazado, sesión reanudada.

## Pagos (usuario, 2026-10-30)
El pago no es una decisión del producto sino una **configuración de cada hotel**, en una capa de pagos con varios proveedores (idea del usuario: «tipo Grana Payment», Stripe Connect, PayPal).
- Hotel elige **métodos**: Stripe (tarjeta), PayPal, y los que se agreguen (Mercado Pago, OXXO, transferencia SPEI: por verificar con cada proveedor).
- Hotel elige **política**: pago total, anticipo (% o primera noche) o solo solicitud.
- Modelo tipo Connect: cada hotel conecta su propia cuenta; el dinero llega al hotel y CLNDA puede cobrar comisión por reserva o suscripción (incógnita de negocio).
- El paso de pago del huésped se arma con lo que el hotel activó; si solo hay «solicitud», el paso desaparece y la confirmación dice «pendiente de confirmar».
- Incógnita: qué es «Grana Payment» (no está en este repositorio); si existe como módulo, su contrato manda.

## Hechos / supuestos / incógnitas
- Hecho: sitio completo con reservas; marca del hotel frente al huésped.
- Supuesto: hoteles pequeños o boutique en México, sin equipo técnico; idioma español e inglés.
- Incógnitas: qué edita el hotel solo y qué hace CLNDA; sincronización con OTAs (channel manager); si también se ofrece el motor suelto para hoteles que ya tienen sitio; varias monedas; dominio propio del hotel.
