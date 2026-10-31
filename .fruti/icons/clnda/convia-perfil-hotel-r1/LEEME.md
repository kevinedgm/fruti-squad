# Convia · perfil de negocio: hotel (r1)

Pedido del usuario (2026-10-31): perfiles completos por giro, «tipo Instagram o Facebook», que al negocio le den gusto tener. Se empieza por hoteles.

## Estructura (orden = cómo decide quien busca hotel)
1. Portada + avatar + giro + nombre + zona y «desde $» + «X de cada 10 volverían» + Favorito Convia.
2. Acciones: **Reservar por WhatsApp** (única principal) · Llamar · Quiero ir · ¿Ya fuiste?
3. Subnavegación fija: Resumen · Habitaciones · Galería · Amenidades · ¿Volverían? · Cómo llegar · Novedades.
4. Resumen: descripción, datos rápidos, rasgos «Va bien para» (**revisados por Convia**).
5. Habitaciones: foto + nº de fotos (visor), capacidad, cama, m², extras, precio desde (de referencia; confirma el hotel).
6. Galería: 1 grande + 4 y «+N» → visor (teclado ← →, Esc).
7. Amenidades (**las declara el hotel**) y «No tiene» con alternativa.
8. ¿Volverían?: métrica grande y tu calificación si ya fuiste.
9. Cómo llegar: mapa, dirección, botón a Google Maps.
10. Novedades: cronología de publicaciones del hotel.
- Lateral (escritorio): «Para reservar» (Convia no reserva: contacto directo, sin comisión) + horarios. Celular: barra fija WhatsApp · Llamar · Llegar.

## Datos
- Hotel ficticio. Fotos de relleno desenfocadas (02, 03, 07, 11, 12, 13), fuera del repo. Contactos `951 000 000x` y `ejemplo.com`: los botones solo muestran un aviso.
- Íconos de amenidades: `../convia-final/amenidades.py`.
- Uso: `python3 gen.py <carpeta con img/>`. Publicado: https://claude.ai/artifact/Xk5jc437yEkzgu4vCgT7eW
