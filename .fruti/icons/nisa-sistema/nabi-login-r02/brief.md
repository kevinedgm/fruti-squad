# Brief funcional · Nabi · inicio de sesión · r02

**Ruta:** R1 · **Fidelidad:** F3 (sistema real: Nabi DS `../nabi-design-system/tokens.json` + propuesta v2) · **Fecha:** 2026-10-28
**Fuentes leídas:** `../nabi-design-system/` (README, tokens.json, componentes Boton, Campo, Carga), `../nabi-final/` (símbolo, lockup, carga, tema), `../nabi-ui-ronda-1/` (logins A/B/C), `../LEEME.md`, `../../medicalmanik/referencias/WCAG-Design-Reference.md`, petición del usuario (28/10/2026).

## Enunciado
El personal del laboratorio (analistas, supervisores de calidad, recepción) necesita **entrar a Nabi** en segundos al empezar la jornada, porque es la puerta diaria al sistema; además es la primera impresión del sistema ante auditores y clientes, y hoy el sistema se ve plano (blanco sobre blanco).

## Pregunta de diseño
¿La identidad v2 (fondo «papel de laboratorio», sombras teñidas, voz editorial) da personalidad sin quitar claridad, y las microinteracciones informan el estado del acceso en lugar de decorar?

- **Verbo principal:** entrar (iniciar sesión).
- **Resultado verificable:** el botón pasa a «Verificando…» y luego a «Listo» y se muestra la transición al inicio; o aparece un error que dice qué pasó y cómo seguir.
- **Dato/acción dominante:** el formulario y su botón «Entrar».

## Usuarios y permisos
| Usuario | Necesita | Permiso |
|---|---|---|
| Analista, supervisor, recepción | Entrar con su cuenta | Cuenta activa del laboratorio |
| Persona con cuenta bloqueada | Saber cuánto esperar y a quién escribir | — |

## Estados
Inicial · escribiendo · correo con formato inválido (al salir del campo) · Bloq Mayús activo · verificando · credenciales incorrectas · últimos intentos · cuenta bloqueada · sin conexión · éxito.

## Flujo anterior / posterior
Abrir Nabi o cerrar sesión → inicio de sesión → inicio de Nabi. Rama: «¿Olvidaste tu contraseña?» → recuperación (fuera de esta ronda).

## Riesgo por acción
| Acción | Tipo | Confirmación |
|---|---|---|
| Entrar | Reversible | Ninguna; bloqueo de doble envío mientras verifica |
| Mostrar contraseña | Reversible | Ninguna; texto del botón cambia |
| Mantener la sesión | Reversible | Ninguna; ayuda sobre equipos compartidos |

## Continuidad
| Situación | Comportamiento |
|---|---|
| Conexión lenta | Botón en «Verificando…» con la carga de Nabi; lo escrito no se borra |
| Sin conexión | Aviso persistente arriba del formulario; «Entrar» deshabilitado con el motivo escrito |
| Error | Mensaje arriba del formulario con causa y salida; la contraseña se conserva para corregirla |
| Sesión reanudada | Fuera de alcance (incógnita) |
| Cambio de tamaño | Se conserva lo escrito y el foco; la columna editorial se reduce a encabezado |

## Alcance MoSCoW
- **Must:** correo, contraseña con Mostrar, Entrar con estados, errores, sin conexión, bloqueo, gestor de contraseñas y pegar permitidos (3.3.8).
- **Should:** aviso de Bloq Mayús, mantener la sesión, placa que responde a la escritura.
- **Could:** acceso con cuenta de Microsoft/Google, enlace al correo.
- **Won't:** recuperación de contraseña, segundo factor, registro (las cuentas las crea el laboratorio).

## Hechos · Supuestos · Incógnitas
**Hechos:** marca Nabi (placa 4×4, N de pocillos, muestra pera), azul #052A76 y pera #C2D225, Archivo + IBM Plex Mono, tema claro; logins A/B/C de la ronda 1 sin elección registrada.
**Supuestos (declarados):** 5 intentos y bloqueo de 15 minutos; correo `@nisanabani.mx` de ejemplo; contacto `sistemas@nisanabani.mx` de ejemplo.
**Incógnitas:** proveedor de identidad (¿Microsoft 365?), segundo factor, política de «mantener la sesión».
