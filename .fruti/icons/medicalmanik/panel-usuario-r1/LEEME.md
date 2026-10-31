# Ecosistema Manik · panel de usuario r1

Pedido del usuario (2026-10-31): en el portal donde se eligen las apps (el «panel de usuario», antes «inicio del ecosistema») el usuario actualiza su cuenta personal y su perfil público en el directorio Manik: insignia de Manik, ver cómo luce su perfil, configurar su información y ver si su perfil está visible o no.

Publicado: https://claude.ai/artifact/VNxkbvMrXLvDcR1uB8Yjdz · `python3 gen.py <dir>` (sellos e insignia como `<img>` data URI para evitar ids de máscara repetidos).

## Estructura
- Izquierda: **Tus apps** (la tarea principal del panel; apps sin acceso apagadas, como dicta el sistema).
- Derecha: **Tu perfil en Manik · directorio** (pin cian del directorio, ficha, estado, acciones) y **Tu cuenta** (datos personales, seguridad, avisos, cerrar sesión).
- Móvil: una columna; apps primero.

## Estados del perfil [propuesta]
| Estado | Señal | Acciones |
|---|---|---|
| Visible | verde, ojo, «Visible en Manik» + dirección | Ver mi perfil público · Editar perfil |
| Oculto | gris, ojo tachado, fecha | Mostrar en Manik · Editar perfil |
| Incompleto | aviso, «No publicado · faltan N datos», barra y lista | Completar perfil · Vista previa |
| En revisión | info, verificación de cédula | Ver · Editar |

- **Ver mi perfil público:** diálogo con la ficha tal como la ve el paciente, con el logotipo Manik y el cian de interfaz del directorio (#00788A); en estados no visibles dice «Vista previa · los pacientes aún no la ven».
- **Editar perfil:** hoja lateral con el interruptor «Visible en Manik» (bloqueado si está incompleto o en revisión) y las secciones del perfil. **Ocultar pide confirmación** (los pacientes dejan de encontrarte); mostrar no.
- Solo roles con perfil público (médicos) ven el bloque; una asistente solo ve «Tu cuenta».

## Supuestos e incógnitas
- [supuesto] Solo médicos tienen perfil público. ¿Clínicas también?
- [supuesto] Existe verificación de cédula antes de publicar («En revisión»).
- [supuesto] Secciones del perfil: datos públicos, foto, consultorios y horario, servicios y costos.
- Dirección `manik.mx/…` provisional (dominio sin confirmar). Persona y precio ficticios.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; controles ≥ 24 px; flujo ocultar con confirmación; vista pública; rol asistente sin bloque de perfil.
