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

## Distintivo (usuario, 2026-10-30)
- Negocios aprobados reciben calca de ventana (10 cm) y tarjeta de mostrador con QR.
- **Vigencia anual por año calendario**: vence el 31 de diciembre; renovación en enero con revisión ligera (sigue abierto, fotos y horarios al día, sin reportes). Quien entra después del 1 de octubre recibe la del año siguiente. La visita de renovación es el momento de ofrecer la fase 2.

## Página principal r4 (usuario, 2026-10-31)
- Fondo **perla** (#f9f9f7), sin beige; superficies blancas.
- Estructura de **directorio por giro** (pestañas) con estantes: este fin de semana, nuevos, más buscados; entrada por intención («¿qué hago este fin?», «un café nuevo»).
- **Mis lugares (usuario, 2026-10-31)**: registro **personal** (para uno o con amigos), no verificación: lista «Quiero ir» → al ir se marca «Ya fui» y se califica con **escala propia, sin estrellas**: No era para mí · Estuvo bien · Me gustó · Volvería · De mis favoritos. La visita es autodeclarada.
- **Métrica pública (usuario, 2026-10-31): «X de cada 10 volverían»** = (Volvería + De mis favoritos) / visitas registradas. Sin estrellas ni likes; «No era para mí» y «Estuvo bien» cuentan en el total pero nunca se muestran aparte.
  - Menos de 10 visitas: «Recién llegado · sé de los primeros en ir» (sin número). [propuesta: umbral 10]
  - Distintivo **«Favorito Convia»**: ≥10 visitas y ≥40 % «De mis favoritos». [propuesta: umbrales] No es ranking.
- Sello del giro en el **encabezado de sección**; en la tarjeta solo el sello personal de «ya fui».
- Talleres y eventos muestran **«Organiza: …»**.
- Sellos personales: 5 de un giro = insignia [propuesta: número]. Prototipo r5 en `../convia-web-r5/`.
- Fotos reales libres para la simulación: bloqueadas por la red de la sesión (Unsplash, Openverse, Wikimedia); pendiente habilitar un dominio.
- Implica cuentas de usuario (fase 1 era solo información): [pendiente de decisión].

## Rasgos «Va bien para…» (usuario, 2026-10-31: intercambio de idiomas, cowork, networking; r8 en `../convia-web-r8/`)
- Familia nueva, distinta de: sello de giro (qué es), Favorito Convia (lo gana con visitas) e insignias del pasaporte (son tuyas). Por eso no se llaman «insignias».
- Un rasgo es un **hecho comprobable**, no una opinión: cada uno tiene regla escrita, se revisa en la visita anual y cualquiera puede avisar si ya no se cumple. [propuesta: quién verifica]
- Lista propuesta (8): Para trabajar, Intercambio de idiomas, Networking, Te atienden en inglés, Para ir solo, Con mascota, Opciones veganas, Silla de ruedas. Reglas en `../convia-final/rasgos.py`. [propuesta: lista y nombres]
- Intercambio de idiomas y Networking son **encuentros con día y hora**: la etiqueta siempre muestra cuándo.
- Tarjeta: máximo 2 rasgos visibles (+N más), etiqueta neutra punteada para no competir con el color del giro. Filtros combinables (todos a la vez).
- Negocios reales: sin rasgos hasta que el negocio los declare y se revisen.
- r9 (usuario): en la tarjeta los rasgos van solo como **sellitos de ícono** (nombre en texto oculto y al pasar el cursor); el nombre y la regla se leen en el **perfil del lugar**. Tarjetas de tamaño único, solo datos básicos.

## Perfiles de negocio por giro (usuario, 2026-10-31)
- **Modelo aprobado (2026-10-31): perfil + actividad + sede** → `../convia-final/modelo-datos.md`. Eventos, talleres, recorridos y exposiciones son actividades con organizador y sede; los independientes son perfiles `organizador`.
- Perfil completo «tipo Instagram/Facebook» que al negocio le dé gusto tener; **cada giro con su propia configuración**. Orden pedido: hoteles primero; luego restaurantes y cafés (menú con precios), recorridos (lugares, desde cuántas personas, precio), talleres, museos (exposiciones, eventos y talleres pasados y próximos, cuántos asistieron).
- Convia **no hace reservaciones**: el perfil da contacto directo (WhatsApp, teléfono, correo, web), horarios y enlace a Google Maps.
- Distinción en el perfil: **rasgos** «Va bien para» = revisados por Convia; **amenidades** = las declara el negocio. [propuesta]
- Hotel r1: `../convia-perfil-hotel-r1/` (estructura en su LEEME).
- r1 rechazado por el usuario: «no copiar Facebook». Pide **diseño propio con el tema de color del giro**, logo «Convia | <Giro>», portada en mosaico, cuartos en miniatura y todo **al alcance del pulgar** (uso mayoritario en teléfono). Hotel r2: `../convia-perfil-hotel-r2/`.
- **Aprobado por el usuario (2026-10-31): perfil de hotel r2.** Queda como patrón base de los perfiles por giro: tema de color del giro, logo «Convia | <Giro>», portada en mosaico, ficha llavero con sello, boleto de datos clave, pestañas abajo en celular + botón flotante de contacto, listas compactas con miniatura que se despliegan. Cada giro cambia sus pestañas y su contenido, no esta base.
- Logotipos de giro de un color: `../convia-final/sellos/<giro>-logotipo-giro.svg` (Cafés, Restaurantes, Hoteles, Talleres, Museos, Recorridos). [propuesta: «Hoteles» vs. «Alojamiento»]
- **Menú (usuario, 2026-10-31): se captura en línea en Convia** y el restaurante pone un **QR en la mesa** que abre ese menú en Convia: es el gancho de adquisición. Perfil de restaurante r1: `../convia-perfil-restaurante-r1/`.
  - Riesgo: capturar cuesta; [propuesta] Convia hace la primera captura desde la foto del menú como parte de la admisión, y el negocio solo actualiza precios.
  - [propuesta] La vista QR prioriza el menú; nada de anuncios ni registro para verlo.
  - **Identidad del QR de mesa r1** `../convia-qr-r1/` (usuario 2026-10-31): el establecimiento protagonista (su nombre/logo y su color), acción bilingüe (escanear / NFC), QR limpio, Convia discreto al pie («Menú en Convia»). Piezas: tarjeta de mesa 10×14, calca redonda 8 cm, tarjeta de barra 5.5×8.5. [pendiente: dominio de la dirección corta; verificar escaneo con teléfono]
    - r1.1 (usuario: se perdía el sello de Convia): **el QR vive dentro de la estrella de Convia, pintada con el color del lugar** («la estrella pone la forma; el lugar pone el color»); la calca es un sticker con forma de estrella.
    - r1.2 (usuario): estrella sólida más grande con el QR encajado al centro y **difuminado del color del lugar a blanco**, sin recuadro visible.
- **Cocinas de restaurantes (usuario, 2026-10-31):** buscar por tipo de comida, incluidas las **8 regiones de Oaxaca**. Catálogo cerrado `../convia-final/cocinas.py`. Directorio r10 `../convia-web-r10/` (filtro «¿Qué se te antoja?»).
  - [propuesta] 1 cocina principal + hasta 2 más; la regional se respalda con ≥2 platillos de esa región en el menú de Convia; «vegana» no es cocina (ya es rasgo); «variada» no se usa.
  - **Aprobado por el usuario (2026-10-31): la lista de cocinas (8 regiones + Otras) y cómo se muestra** (filtro «¿Qué se te antoja?», cocina en tarjeta, ficha y platillos). Las reglas de límite y respaldo siguen como propuesta.
  - Pendiente: si conviene un mapa de las 8 regiones (requiere datos geográficos reales, no dibujarlo de memoria).
- **Recorridos r1** `../convia-perfil-recorridos-r1/`: el perfil es del **operador**; cada recorrido abre una hoja con ruta por paradas, calculadora de precio según cuántos van (tabla por tamaño de grupo, mínimo y máximo), salidas con cupo, incluye/no incluye, punto de encuentro y mensaje de WhatsApp prellenado con «Lo vi en Convia». [propuesta: ese texto sirve para medir cuántos contactos llegan por Convia]
  - **Aprobado por el usuario (2026-10-31).**
- **Café r1** `../convia-perfil-cafe-r1/`: acción principal «Cómo llegar» (no se reserva); bloque «¿Sirve para trabajar?»; pestaña Encuentros; carta con origen del café y modo QR; muestra el estado «Recién llegado» (van 6 de 10 visitas).
  - **Aprobado por el usuario (2026-10-31).**
- **Taller r1** `../convia-perfil-taller-r1/`: el perfil es del **estudio**; hoja por taller con «Te llevas», «Qué vas a hacer», lugares × precio (empieza en 1, tope = cupo de la fecha), mínimo para confirmar, qué llevar; pestañas Piezas (de alumnos) y Maestros.
- **Museo r1** `../convia-perfil-museo-r1/`: primer perfil sobre el modelo perfil + actividad + sede; pestaña Actividades (Ahora · Próximas · Pasadas) con «Organiza» y «Dónde» en cada una; pasadas con «N marcaron que fueron».
- **Organizador independiente r1** `../convia-perfil-organizador-r1/`: verde base de Convia (no tiene giro), avatar, revisión visible, «Seguir», pestaña Dónde con sus sedes; cada actividad dice «En» con el color del giro de la sede. [propuesta: color, «Seguir» implica avisos]
- **«Seguir» con avisos de nuevas actividades: aprobado por el usuario (2026-10-31).** [pendiente: canal del aviso (correo, notificación web o WhatsApp)]
- Corrección 2026-10-31: las fechas de los perfiles tenían el día de la semana corrido; se ajustó el número del día y se verificó contra el calendario 2026.
- **Directorio r11** `../convia-web-r11/`: el modelo llega al directorio: pestaña **Agenda** (actividades por día, «Organiza · En», filtros y «Solo lo que sigo»), **Quiénes organizan** con «Seguir», **campana de avisos**, «Actividades aquí» en cada lugar y enlaces a los perfiles completos.
- **Hero del directorio** (usuario 2026-10-31: hero art moderno, único, que enmarque): ronda 1 con tres direcciones en `../convia-hero-r1/` (A convite de estrellas · B portal de arcos · C ventana del día). → el usuario eligió **B + C** y pidió **temporadas tipo doodle**. Hero r2 `../convia-hero-r2/`: arcos fijos + cielo vivo; por temporada cambian cielo, adornos, estrella del logo y texto; cada temporada es un dato y se elige por fecha. [propuesta: encargar cada edición a artistas de Oaxaca; pendiente: verificar uso del nombre «Guelaguetza»]
  - r3 (usuario): **el logo de Convia al centro es el protagonista y el doodle**; debajo frase de temporada, buscador e intenciones como **sellos**. Fondo discreto; los arcos salen del hero. `../convia-hero-r3/`
  - **Aprobado por el usuario (2026-10-31)** e integrado en el **directorio r12** `../convia-web-r12/` (portada doodle, encabezado que aparece al bajar, sellos, búsqueda sin acentos).

## Pendiente de operación (usuario, 2026-10-30: «tema de operación de negocio», se decide después)
- Quién carga los primeros lugares al lanzar (curaduría e invitación vs. solicitudes espontáneas) y cuántos necesita la fase 1.

## Identidad (usuario, 2026-10-30)
- Marca independiente de CLNDA. Evoca Oaxaca sin nombrarla. Español fácil en inglés. Personalidad: amigo que sabe.
- **Nombre: Convia** (convite + vía; con v). Rondas en `nombres-r1.md` a `nombres-r6.md`.
- Búsqueda web preliminar (no es búsqueda de marca): existe Convia Inc. (EE. UU., tecnología para edificios; otra clase y mercado) y una app sueca «Convie» de gastronomía y hotelería (nombre parecido, mismo rubro).
- **Símbolo: E1b** (estrella de un trazo a mano, inclinada; inspirada en las estrellas del convite). `../convia-r7/E1b.svg`.
- ~~Color: paleta B «Convite + cantera»~~ (2026-10-30: el usuario ya no está convencido; busca **elegancia y pulcritud**, no infantil). Antes:: fondo verde cantera #1f4d3a, principal magenta #d42a66, acento amarillo #ffc53d, apoyo verde #3f8f6b, papel #f6f3ea, tinta #15241d. Contraste WCAG 2.2 AA verificado en `../convia-color-r1/`.
- **Plataforma (usuario): directorio web** (responsive), no app móvil primero.
- Dirección visual: elegante, pulcra y suave. Portada de prueba en `../convia-web-r1/` (Fraunces suave + Figtree, paleta Cantera).
- **Identidad v2** en `../convia-final/`: paleta Cantera (primario #2f5a45; apoyo tinta, papel, arena, cantera suave), un color por categoría, Fraunces suave + Figtree (aprobadas por el usuario), formas suaves. Manual: https://claude.ai/artifact/6pcxK7T2c3mKpeSfYgGL51
- Pendiente: Marcanet (clases 9, 35, 39, 42), dominios y redes; prueba de recuerdo con 5 personas.

## Incógnitas
- ¿Curado (solo lo recomendado) o abierto (cualquier negocio se registra)?
- ¿Quién paga y qué? (¿listado gratis, destacado de pago, solo como gancho?)
- Idioma (turista nacional / extranjero), solo Oaxaca capital o el estado.
