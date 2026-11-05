# Dialogo

Ventana sobre la página para trabajar un registro o tomar una decisión. Dos tamaños, una sola estructura: encabezado, cuerpo y pie. La identidad está en el encabezado: avatar con el color del tono, contexto en azul, título y subtítulo.

## Anatomía del encabezado
1. **Avatar**: 48 × 48, radio `radius-lg`, fondo suave del tono e ícono de 24 en el color del tono.
2. **Contexto**: `overline` en `primary`, mayúsculas, +0.06 em. Tipo de diálogo y código (BITÁCORA · BIT-02-01).
3. **Título**: `title-1` en `text`. Lo que se hace o se decide.
4. **Subtítulo**: `body` en `text-muted`. Una frase: vigencia, norma, folio.
5. **Cerrar**: 40 × 40, sin fondo, `text-muted`. Esc también cierra.

Encabezado, cuerpo y pie sobre `surface`, con márgenes de 24 y filete `border` entre ellos. El borde izquierdo del contenido coincide con el del avatar. Los datos agrupados (promedio, resumen) van sobre `bg`, radio `radius-md`.

## Tonos
| Tono | Avatar | Botón principal | Cuándo |
|---|---|---|---|
| Neutro | `primary-soft` / `primary` | `primary` | Trabajar un registro, confirmar, enviar |
| Aviso | `alerta-soft` / `alerta` | `primary` | Fuera de plazo, cerca del límite, requiere justificación |
| Destructivo | `fuera-soft` / `fuera` | `fuera` | Rechazar, cancelar, eliminar: no se deshace |
| Éxito | `conforme-soft` / `conforme` | `primary` («Listo») | Confirmación después de registrar |

El tono solo cambia el avatar y, si es destructivo, el botón. La estructura no cambia.

## Tipografía
| Papel | Estilo | Color | Sobre blanco | Uso |
|---|---|---|---|---|
| Contexto | `overline` (11px/16px · 600) | `primary` | 13.1:1 | Tipo de diálogo y código. Mayúsculas, +0.06 em. Ata el texto al color del avatar. |
| Título | `title-1` (22px/30px · 600) | `text` | 17.0:1 | Lo que se hace o se decide. Una línea si cabe. |
| Subtítulo | `body` (14px/22px · 400) | `text-muted` | 6.8:1 | Una frase de contexto: vigencia, norma, folio. |
| Sección | `title-2` (16px/24px · 600) | `text` | 17.0:1 | Agrupa campos dentro del cuerpo. |
| Etiqueta | `label` (13px/18px · 500) | `text` | 17.0:1 | Nombre de cada campo. |
| Texto | `body` (14px/22px · 400) | `text` | 17.0:1 | Explicaciones y consecuencias. |
| Ayuda | `caption` (12px/18px · 400) | `text-muted` | 6.8:1 | Metadatos, límites, pistas. |
| Dato | `valor` (14px/20px · 500) | `text` | 17.0:1 | Valores medidos y códigos. Cifras de ancho fijo. |
| Resultado | `valor-xl` (32px/36px · 500) | `text` | 17.0:1 | El valor protagonista, uno por diálogo. |
| Botón | `button` (14px/20px · 600) | `primary` | 13.1:1 | Verbo + objeto. |

El peso separa niveles (600 títulos, 500 etiquetas y datos, 400 texto); el color separa importancia (tinta para leer, gris para acompañar, azul para contexto y acción).

## Medidas y capas
- Ancho: trabajo 720 px, decisión 440 px. En celular, hoja inferior a todo el ancho; avatar de 40.
- Separaciones: avatar ↔ texto 16 · secciones 24 · campos 16 · etiqueta ↔ campo 6.
- Sombras: `shadow-overlay` en el diálogo, `shadow-inset` en campos, `shadow-primary` en el botón principal.
- Velo detrás del diálogo: tinta al 55 %.

## Pie
Ayuda opcional a la izquierda (`caption`, `text-muted`); a la derecha la secundaria y una sola principal. Verbo + objeto: «Registrar lecturas», «Rechazar bitácora».

## Accesibilidad
- `role="dialog"` (trabajo) o `role="alertdialog"` (decisión) con `aria-modal="true"` y `aria-labelledby` al título.
- Al abrir, el foco va al primer campo o, si no hay, al título; el foco queda atrapado dentro y vuelve al botón que lo abrió al cerrar.
- Esc y «Cerrar»/«Cancelar» cierran sin cambios. En destructivos el botón principal nunca es el foco inicial.
- El tono nunca es la única señal: el título y el texto dicen la consecuencia.

Aprobado el 2026-11-05 (ronda `dialogos-r02`).
