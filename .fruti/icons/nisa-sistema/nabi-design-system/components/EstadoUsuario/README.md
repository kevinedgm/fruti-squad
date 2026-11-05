# EstadoUsuario

Estado de una cuenta de usuario: icono + texto sobre el fondo suave del estado, con los mismos colores semánticos que los estados de muestra.

| Estado | Color | Icono | Cuándo |
|---|---|---|---|
| Activo | `conforme-soft` / `on-conforme-soft` | círculo con palomita | Puede entrar |
| Invitación enviada | `bg` / `text-muted` | sobre | Aún no crea su contraseña |
| Suspendido | `alerta-soft` / `alerta` | pausa | Acceso detenido por un administrador; reversible |
| Bloqueado | `fuera-soft` / `fuera` | candado | Bloqueo por intentos fallidos; se desbloquea solo o por sistemas |
| Dado de baja | `bg` / `text-muted` | prohibido | Ya no trabaja en el laboratorio; se conserva por trazabilidad |

- El color sigue al significado, no al módulo: verde = está bien, gris = pendiente, ámbar = requiere atención, rojo = impedido, contorno sin relleno = fuera de uso. Ninguno es color de división.
- Nunca solo color ni solo punto: icono y palabra siempre.
- El pera no es un estado: marca el registro en curso (ver TablaUsuarios).
- Los nombres de estado son una propuesta: confirmar con la política de cuentas del laboratorio.
