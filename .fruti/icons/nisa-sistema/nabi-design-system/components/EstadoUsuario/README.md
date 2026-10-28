# EstadoUsuario

Estado de una cuenta de usuario: icono + texto sobre el fondo suave del estado, con los mismos colores semánticos que los estados de muestra.

| Estado | Color | Icono | Cuándo |
|---|---|---|---|
| Activo | `conforme-soft` / `on-conforme-soft` | círculo con palomita | Puede entrar |
| Invitación enviada | `pendiente-soft` / `on-pendiente-soft` | sobre | Aún no crea su contraseña |
| Suspendido | `alerta-soft` / `on-alerta-soft` | pausa | Acceso detenido por un administrador; reversible |
| Bloqueado | `fuera-soft` / `on-fuera-soft` | candado | Bloqueo por intentos fallidos; se desbloquea solo o por sistemas |
| Dado de baja | `surface-sunken` / `text-muted` | prohibido | Ya no trabaja en el laboratorio; se conserva por trazabilidad |

- El color sigue al significado, no al módulo: verde = está bien, azul = pendiente, naranja = requiere atención, rojo = impedido, gris = fuera de uso.
- Nunca solo color ni solo punto: icono y palabra siempre.
- El pera no es un estado: marca el registro en curso (ver TablaUsuarios).
- Los nombres de estado son una propuesta: confirmar con la política de cuentas del laboratorio.
