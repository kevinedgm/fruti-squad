# Hallazgos · Nabi · inicio de sesión · r02

| Sev. | Hallazgo | Decisión | Responsable | Siguiente acción |
|---|---|---|---|---|
| Alta | La identidad v2 cambia tokens del sistema (fondo, sombras, voz editorial). | Se entrega como capa de propuesta (`nabi-identidad-v2.css`, `identidad-v2.md`); no toca `tokens.json`. | usuario → lima | Aprobar o ajustar; al aprobar, pasarla a `tokens.json` y borrar la capa. |
| Alta | La UI actual del producto usa Verdant (esmeralda) y Nabi usa azul y pera. | Este login sigue a Nabi porque el usuario pidió el sistema de Nabi. | producto | Decidir si Nabi sustituye a Verdant en toda la app. |
| Media | Política de intentos y bloqueo desconocida. | Supuesto: 5 intentos, 15 minutos. | producto / sistemas | Confirmar. |
| Media | Proveedor de identidad y segundo factor desconocidos. | No se dibujan. | sistemas | Confirmar si hay Microsoft/Google o 2FA. |
| Media | «Mantener la sesión» puede no estar permitido en equipos compartidos. | Se ofrece desmarcado. | producto | Confirmar política. |
| Baja | La placa reacciona a la longitud de lo escrito (no revela la contraseña, pero sí su longitud aproximada a quien mire la pantalla). | Aceptable en un login de escritorio; se puede desactivar en el campo de contraseña. | producto | Decidir si solo cuenta el correo. |
| Baja | Newsreader es una tercera familia tipográfica. | Limitada a voz editorial (lema, entradillas, estados de éxito). | lima | Registrar su uso en el sistema si se aprueba. |
