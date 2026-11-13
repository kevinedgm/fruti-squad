SAM es la herramienta con la que el equipo de desarrollo y soporte registra, mueve y cierra su trabajo. Su marca se resume en tres decisiones: el símbolo Tarjetas dice «actividad» sin letra, Voltaje es un relleno que marca lo activo, y Onest se usa igual en la marca y en la interfaz. La interfaz se construye con Grana; este sistema es la capa de marca y de dominio encima de Grana.

## Voz y contenido

- Escribe en español, en segunda persona («Te toca revisar la evidencia»), con frases cortas y verbos concretos: «Avanzar etapa», «Adjuntar evidencia», «Nueva actividad». Nunca «Gestionar».
- Usa mayúscula solo al inicio y en nombres propios: «Mis actividades», no «Mis Actividades».
- Nombra los estados por lo que significan para quien trabaja: «En curso», «Revisión», «Nuevo», «Vencida».
- Los folios van tal cual en `folio`: `INC-2041`, `TAR-0187`. Las fechas, cortas: «Vence hoy, 18:00», «15 nov».
- Los errores dicen qué pasó y cómo seguir, sin disculpas: «No se pudo adjuntar el archivo: pesa más de 20 MB. Comprímelo y vuelve a intentar.»
- Sin emojis.

## Color

- Pinta la página con `surface`, las tarjetas con `surface-raised` y los hovers con `surface-sunken`. Texto en `ink`; metadatos en `ink-muted`.
- `brand` (Voltaje) es solo relleno: botón principal, estado activo y la tarjeta del símbolo. Pon encima `on-brand`. Nunca escribas texto en `brand`.
- Todo relleno `brand` lleva contorno `brand-edge`. En oscuro no se nota; en claro es lo que lo separa del fondo (Voltaje sobre Papel mide 1.1:1).
- El foco es `focus`, 3 px sólidos con 3 px de separación, en todos los controles. Nunca Voltaje.
- Una sola acción principal en Voltaje por vista. Las demás, secundarias (borde `line-control`) o de texto.
- `danger` (vencida, errores), `warning` (por vencer) e `info` (avisos) llevan siempre su palabra: el color no basta.
- En la app, Voltaje entra en `--g-color-brand` de Grana y `on-brand` en `--g-color-on-brand`. El resto de la equivalencia con los tokens de Grana está pendiente: no conocemos su lista completa.

## Tipografía

- Todo en Onest (`sans`). Títulos de pantalla en `title` (celular) o `display` (escritorio), uno por vista; secciones en `subtitle`; texto en `body`.
- Títulos de actividad en `item-title`; metadatos en `body-sm` y `ink-muted`; botones en `label`; estados en `caption`.
- Folios, horas y datos en columna, en `folio` (JetBrains Mono) con números tabulares.
- Ambas fuentes vienen de Google Fonts (licencia OFL); no hay archivos de fuente en el sistema.

## Espacio, forma y profundidad

- Espaciado en pasos de 4 px (`space-1` a `space-8`). Margen lateral mínimo `space-4` en celular.
- Radios: `radius-sm` en botones, campos y tarjetas; `radius-md` en paneles y diálogos; `radius-pill` en estados.
- Sin sombras: la profundidad la dan las superficies (`surface` → `surface-raised`) y los bordes `line`.
- Altura mínima de controles: `control-height` (44 px).

## Movimiento

- Solo para explicar un cambio de estado: la tarjeta que avanza de etapa se desliza hacia delante 8 px y se asienta (200 ms, curva de salida `cubic-bezier(0.16, 1, 0.3, 1)`).
- Con `prefers-reduced-motion`, el cambio es inmediato, sin desplazamiento.

## Símbolo y logotipo

- Símbolo Tarjetas: la tarjeta anterior en contorno de tinta (ya pasó), la actual en Voltaje con contorno de tinta y la palomita en `on-brand`.
- Desde `symbol-min` (32 px) usa el símbolo grande; por debajo, el chico (tarjetas más separadas, trazo más grueso).
- Logotipo horizontal en la barra de la app y documentos; vertical en portadas e inicio; compacto (sin «Simple Activity Manager») donde no cabe el descriptor.
- No lo deformes, no cambies Voltaje por otro color, no quites el contorno sobre fondo claro, no separes la palomita.
- Como `<img>` usa las versiones «sobre-oscuro» o «sobre-claro» (colores fijos). En línea, el símbolo hereda la tinta con `currentColor`.

## Iconografía

- Los iconos de interfaz los pone Grana. Pendiente de definir: qué familia usa Grana y si la marca necesita alguno propio.
- El icono pequeño de las notificaciones push es una silueta blanca de una tinta (`notificacion-96.png`).

## Componentes

Botón, Estado, Tarjeta de actividad y Barra de la app son componentes de dominio de SAM sobre Grana. Cada uno tiene su guía y su vista previa en ambos temas.
