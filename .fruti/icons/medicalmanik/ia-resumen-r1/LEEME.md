# Ecosistema Manik · IA · antecedentes al abrir la consulta (r1)

Pedido del usuario (2026-10-31): al entrar a la consulta de un paciente, la IA ya analizó sus consultas previas y muestra un diálogo con un resumen rápido de su condición: qué se le detectó y qué se le recetó, para que el médico no tenga que leer todo el expediente.

Publicado: https://claude.ai/artifact/YYhgxYB5ZWmwHBZ5zaEE1W

## Flujo
Se agenda o se abre la consulta → la IA prepara el resumen antes (fuera de la vista) → el médico entra → el diálogo aparece con el resumen listo → «Empezar consulta» (o Esc, X, clic fuera) → el foco vuelve al botón «Antecedentes» de la cabecera, que lo reabre cuando quiera.

## Anatomía (de lo más rápido a lo más detallado)
1. **En pocas palabras:** 1 o 2 frases con la condición y su dirección (mejora / sigue alta).
2. **Para revisar hoy:** pendientes y cambios recientes (estudio sin resultado, dosis ajustada).
3. **Cómo ha cambiado:** series de los signos clave en las consultas resumidas.
4. **Últimas 3 consultas:** fecha, motivo, diagnóstico CIE-10, receta (cambios marcados) y signos; enlace a la consulta original.
5. Nota: hecho por IA, solo lectura, no se guarda en el expediente.

## Decisiones [propuesta]
- **Solo lectura, sin «aceptar»:** el resumen no escribe en el expediente, así que no necesita confirmación; la regla de borrador aplica cuando la IA escribe.
- **La alergia no es de la IA:** viene del expediente y vive en la cabecera, siempre visible.
- **Una sola acción primaria** en el diálogo: «Empezar consulta». La consulta de fondo no compite porque el diálogo es modal.
- **Movimiento:** al abrir con el resumen listo, el destello se traza una vez («llegó algo nuevo»); si aún analiza, el destello orbita en el diálogo y en el botón «Antecedentes».
- **Móvil:** hoja inferior a casi toda la altura, botones a lo ancho.

## Estados
Resumen listo · Aún analizando (se puede empezar igual) · Primera consulta (sin antecedentes) · No se pudo (remite al expediente completo).

## Supuestos e incógnitas
- [supuesto] Ventana del resumen: últimas 3 consultas. ¿O un periodo (6 meses)?
- [supuesto] Aparece siempre al entrar. ¿Solo si hay consultas previas? ¿Se puede desactivar por médico?
- [supuesto] CIE-10.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; `<dialog>` modal con foco inicial en «Empezar consulta», Esc cierra y devuelve el foco; región viva anuncia cada estado; controles ≥ 24 px.
