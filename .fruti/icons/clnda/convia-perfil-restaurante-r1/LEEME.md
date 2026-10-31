# Convia · perfil de restaurante r1

Aplica el patrón aprobado del hotel r2 (tema del giro, mosaico, ficha llavero, boleto, pestañas abajo en celular) con el color de restaurantes.

## Decisión del usuario (2026-10-31): el menú vive en Convia
- El restaurante **captura su menú en Convia** y pone un **QR en sus mesas** que abre ese menú. Es el gancho: el comensal ya sentado conoce Convia sin buscarla.
- Vista QR (`index.html#qr`): sin portada; ficha compacta y **el menú primero**. Al final, «Guardar» y «Ver el lugar»; sin anuncios ni pasos que estorben al pedir.

## Pestaña Menú
- Secciones con accesos rápidos fijos (Para empezar · Platos fuertes · Postres · Bebidas).
- Cada platillo: nombre, descripción corta, precio; marcas «De la casa», «Vegano», «Picante».
- **Español / English** (traducción capturada por el restaurante o revisada por Convia [pendiente]).
- **Solo veganas**: filtra; respalda el rasgo «Opciones veganas» (regla: al menos 2 platillos completos marcados).
- Fecha de última actualización de precios, visible.

## Otros
- Boleto: estado de hoy calculado con el horario (abierto / hoy abre / mañana abre), precio, cuándo conviene reservar.
- El lugar: horario semanal con el día de hoy marcado, amenidades (las declara el negocio), «No tiene», novedades.
- Restaurante, menú, precios, contactos y dirección **ficticios**; fotos de relleno desenfocadas, fuera del repo.
- Pendiente: tarjeta de mesa con QR (la librería `qrcode` no está en esta sesión; `convia-final/distintivo.py` ya sabe dibujar QR).
- Uso: `python3 gen.py <carpeta con img/>`.
