# Nabi · identidad de interfaz v2 (propuesta)

**Estado:** propuesta, no materializada en `../nabi-design-system/tokens.json` hasta que el usuario la apruebe.
**Petición:** conservar la pulcritud blanca de laboratorio, pero sin «blanco sobre blanco»: sombras pequeñas, contrastes suaves, pulcro como Notion y editorial como Medium; nada plano ni insípido.

## Qué cambia y por qué

| Token | v1 | v2 propuesta | Motivo |
|---|---|---|---|
| `bg` | #FFFFFF | **#F2F4F8** «papel de laboratorio» | Las superficies blancas se separan del fondo; se acaba el blanco sobre blanco. |
| `surface` | #FFFFFF | #FFFFFF | Igual: el blanco queda para lo que se trabaja. |
| `surface-raised` | — | **#FFFFFF + `shadow-1`** | Tarjeta en reposo: borde fino + sombra de 1–2 px teñida de tinta. |
| `surface-sunken` | #F4F6FA | **#EEF1F6** | Un paso más hundido que el fondo, para campos de solo lectura y encabezados de tabla. |
| `border` | #E2E5EC | **#DFE3EC** | Filete apenas más presente. |
| `shadow-1` | — | **0 1px 0 rgba(20,27,51,.03), 0 1px 2px rgba(20,27,51,.06)** | Tarjetas y tablas en reposo. Sombra teñida de tinta azul, no negra. |
| `shadow-2` | — | **0 1px 2px rgba(20,27,51,.05), 0 10px 28px -14px rgba(5,42,118,.22)** | Tarjeta que se presenta sola (login, diálogo pequeño). |
| `shadow-overlay` | 0 12px 32px rgba(5,42,118,.16) | igual | Menús y diálogos. |
| `shadow-inset` | — | **inset 0 1px 1px rgba(20,27,51,.05)** | Campos: se sienten hundidos, no dibujados. |
| `shadow-primary` | — | **inset 0 1px 0 rgba(255,255,255,.16), 0 1px 2px rgba(5,42,118,.30), 0 6px 14px -6px rgba(5,42,118,.45)** | El botón primario tiene cuerpo: brillo arriba, sombra abajo. Sin degradado. |
| `font-editorial` | — | **Newsreader** (itálica 400) | Tercera voz, solo editorial: lemas, entradillas, estados vacíos y portadas de documento. Nunca en tablas ni controles. |
| `textura-placa` | — | puntos de 1 px cada 24 px al 5 % | Rejilla de pocillos en fondos amplios (login, portadas). Nunca detrás de datos. |

## Lo que no cambia
- Azul real #052A76 (acción, foco, encabezado) y pera #C2D225 (la muestra; nunca texto, una sola visible).
- Archivo (habla) e IBM Plex Mono con cero con barra (mide).
- Estados con icono y texto; contraste de texto ≥ 4.5:1.

## Regla de uso de la profundidad
Sombra por rol, no por adorno: fondo `bg` → tarjeta `shadow-1` → tarjeta protagonista `shadow-2` → lo que flota `shadow-overlay`. Una pantalla densa usa casi solo `shadow-1`; el login y las portadas usan `shadow-2`.
