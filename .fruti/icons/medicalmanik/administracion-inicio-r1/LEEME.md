# Administración Manik · pantalla principal r1

Pedido del usuario (2026-10-31): «sigue con la pantalla principal de administración». Antes: app interna del equipo MedicalManik donde se configura todo (usuarios activos, configuración del sistema…).

Publicado: https://claude.ai/artifact/JazqqbkMCU1SzAY1DMmqHv · `python3 gen.py <dir>`.

## Brief
- Usuario: equipo MedicalManik (soporte, operación, dirección). Tarea al entrar: saber si el ecosistema está bien y qué requiere atención; entrar a configurar.
- Dato protagonista: **usuarios activos** (pedido explícito) y **pendientes**.

## Estructura
- Barra lateral con el sello de Administración: Resumen · Personas (Usuarios, Clínicas y grupos, Directorio manik con contador) · Producto (Apps y planes, Pagos con contador, Configuración, Actividad). En móvil, menú lateral que se cierra con Esc o tocando fuera.
- Búsqueda global (usuario, clínica, correo o cédula; atajo «/»).
- 4 cifras: usuarios activos (según periodo), clínicas activas, perfiles visibles en manik, pendientes.
- **Requiere atención:** cédulas por verificar (vienen del estado «En revisión» del panel de usuario), pagos no procesados (correo «Pago no procesado»), cuentas bloqueadas, app lenta; cada fila con su acción.
- **Usuarios activos por app** con periodo Ahora / Hoy / 7 días.
- **Actividad reciente** (quién cambió qué y cuándo; lo automático marcado).
- **Estado de las apps** (incluye manik y Administración).
- **Configuración:** roles y permisos, seguridad, apps y planes, correos, avisos del sistema, integraciones.

## Supuestos [por confirmar]
- Una persona que usa varias apps cuenta una vez, en la app donde pasó más tiempo (así las barras suman el total).
- La verificación de cédulas la hace el equipo desde Administración.
- Secciones de configuración propuestas; el mensaje original se cortó en «a nivel…».
- Cifras, personas y correos de ejemplo.

## Verificación
Playwright 1440, 820 y 390 px: sin desbordes ni errores JS; controles ≥ 24 px; cambio de periodo actualiza barras y cifra. Corregido en prueba: botón de menú visible en escritorio, estado «Administración» desbordado, barra superior 5 px más ancha que el teléfono.
