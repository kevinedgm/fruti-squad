# SAM · acceso y correos (artifact)

`acceso.html` (generado con `gen.py`): pantalla de login interactiva con sus estados y galería de las plantillas de `../correos/`.
Login con correo y contraseña (decisión del usuario, 2026-11-13). Estados: normal, campos vacíos, datos incorrectos, entrando, cuenta bloqueada, sin conexión, recuperar, enlace enviado, contraseña nueva, enlace vencido y contraseña cambiada.
Supuestos por confirmar (también en la página): bloqueo 15 min tras 5 intentos; contraseña de 12 caracteres o más; enlace de recuperación 1 h y de invitación 72 h; sin casilla «Mantener sesión»; los mensajes no revelan si un correo existe.
En la demo, «Entrar» siempre termina en «datos incorrectos» (no hay servidor).
