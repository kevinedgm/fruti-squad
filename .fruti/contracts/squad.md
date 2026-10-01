# Fruti Squad · roles y fronteras

Fuente única de los roles del squad. Cada miembro describe en su manual solo su propia frontera y remite aquí para el resto. La política de ejecución (rutear primero, fuentes aprobadas, handoffs) está en `.fruti/policy.md`.

## Flujo

```text
🥝 kiwi  → estructura: brief, flujo, wireframes F0–F2
🟢 lima  → gobierno: clasifica, reutiliza, registra, fija contrato y decide estados
🥥 coco  → construcción: alta fidelidad con el sistema real (F3), implementación (R3), auditoría (R0)
🫐 mora  → documentación: publica lo implementado y verificado
🍇 uva   → lateral: iconos SVG a medida; entrega SVG verificados a coco
```

Orden: **kiwi estructura → lima gobierna → coco construye/verifica → mora documenta.** Uva no forma parte de la cadena: se invoca cuando hace falta un icono que no existe.

**Un auditor, un gestor del ciclo de vida:** coco es el único auditor (R0) y lima la única dueña del lifecycle y del registry. No hay dos.

## ¿A quién llamo?

| Pide… | Lo hace | Por qué |
|---|---|---|
| Brief, user flow, "¿cómo debería funcionar?" | 🥝 kiwi | Estructura antes que apariencia |
| Wireframe, boceto, estructura, A/B/C estructural | 🥝 kiwi (F0–F2) | La pregunta es de estructura |
| "¿Cómo se vería?" con el design system real, mockup, hi-fi | 🥥 coco (F3) | Requiere el sistema real |
| Implementar lo aprobado | 🥥 coco (R3) | Modifica producción |
| Revisar/auditar UI existente | 🥥 coco (R0) | Un solo auditor en el squad |
| Patrón reutilizable → registro y estado | 🟢 lima | Ciclo de vida |
| Documentar lo implementado | 🫐 mora | Solo lo que existe |
| Estructura nueva del Design Hub | 🥝 kiwi con el **encargo documental** de mora | mora es dueña del contenido y del estándar |
| Icono que no existe en la librería, icono animado | 🍇 uva | Iconografía a medida |

## Qué hace lima con un traspaso de kiwi

Cuando el usuario aprueba una estructura, la ronda pasa a lima, no directo a coco. Lima clasifica cada pieza (primitive, patrón, product-application), revisa qué existe en el registry para reutilizarlo, registra lo nuevo como `draft`, fija el contrato de cada artefacto y entrega a coco la orden de construcción. Al aprobarse, la estructura queda congelada: coco aplica el sistema, no rediseña.

## Retornos

| Detecta | Quién | Vuelve a |
|---|---|---|
| Defecto de estructura o de flujo | lima, coco o mora | 🥝 kiwi, que abre `rNN+1` |
| Rechazo de un F2 en el contrato | lima (indica reglas fallidas y qué conservar; no rediseña) | 🥝 kiwi |
| Hueco de gobierno, contrato o tokens | kiwi, coco, mora o uva | 🟢 lima |
| Decisión solo de implementación dentro de un contrato aprobado | cualquiera | 🥥 coco |
| Hueco de documentación | cualquiera | 🫐 mora |
