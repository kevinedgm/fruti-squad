# Guía y estándar de iconografía accesible

> **Norma de Uva.** Este documento es la fuente normativa de Uva para iconografía; `../estandares.md` es la rúbrica operativa que lo aplica. Si discrepan, gana este documento, salvo las decisiones del usuario registradas en `.fruti/runtime/uva.yaml` (`decisions`).
>
> **Alcance en el squad:** solo Uva lo adopta. Las secciones de implementación (botones, teclado, foco, tooltips, toggles, disclosure) Uva las aplica a sus **recomendaciones de uso** en la propuesta y el handoff; no implementa componentes.
>
> **Texto incompleto:** se recibió hasta la sección 34, interrumpida. Las secciones posteriores, si existen, están pendientes.
>
> **Observación (sin modificar el texto):** el ejemplo de §2.1 usa `category: destructive-action`, que no aparece en la taxonomía de §3. Uva lo trata como `action`; pendiente de aclarar por el autor de la norma.

Estándar de diseño, semántica, interacción, movimiento, accesibilidad y gobierno de iconografía para Design Systems.

- Versión: 1.0
- Base visual: Lucide Icons
- Base normativa: WCAG 2.2 + WAI-ARIA Authoring Practices Guide
- Aplicación: Web, PWA, desktop, tablet y mobile

---

## Índice

| Archivo | Secciones | Contenido | Etapa |
|---|---|---|---|
| `01-seleccion.md` | §2–10 | principios, taxonomía, selección, registro semántico, lenguaje visual Lucide, balance, peso, complejidad, tamaños | E1, E2 |
| `02-uso-interfaz.md` | §11–26 | área interactiva, target size, botones, teclado, nombre accesible, decorativos, etiquetas, tooltips, color, contraste, estados, foco, toggle, disclosure | E5 (recomendaciones de uso; C1–C5 de la rúbrica) |
| `03-movimiento.md` | §27–34 | animación, categorías, tokens, principios, movimiento reducido, interacción, automáticas, destellos | E4 |

La numeración § original se conserva en los encabezados de cada archivo: las citas «§n» de la rúbrica, las reglas y el manual siguen siendo válidas.

## 1. Propósito

Los iconos no deben tratarse simplemente como recursos gráficos.

Dentro de un Design System, un icono es una unidad de comunicación capaz de representar: acciones; objetos; navegación; estados; relaciones; jerarquías; feedback; dirección; controles; información.

Un sistema de iconografía debe establecer reglas para:

1. seleccionar iconos;
2. diseñar iconos nuevos;
3. asignar significado;
4. utilizarlos consistentemente;
5. combinarlos con texto;
6. hacerlos interactivos;
7. animarlos;
8. hacerlos accesibles;
9. adaptarlos a diferentes dispositivos;
10. gobernar su evolución.

El objetivo no es construir una galería de SVG. El objetivo es construir un lenguaje visual consistente.
