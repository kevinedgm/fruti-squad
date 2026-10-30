# Brief estratégico (usuario, 2026-10-30) · conflictos con la identidad nueva

El usuario entregó el «Brief estratégico para el manual de identidad de marca y posicionamiento comercial» (producto Fruti Squad Complete; inglés principal; referencia kevinedgm/fruti-squad-kiro). Choca con lo aprobado en las rondas 1–20 de esta carpeta:

| Tema | Brief | Identidad nueva aprobada hoy |
|---|---|---|
| Isotipo | Conservar el original: cinco módulos alrededor de un núcleo (Espiral de `../fruti-squad/`) | Sistema «Átomos»; orquestador «Espiral» de marcos girando (otro dibujo) |
| Paleta base | #161616 · #F8F8F5 · acento #B7F34D | Tinta #18181b · oscuro #0f0f12 · sin acento de marca único |
| Colores de agentes | Kiwi #7FCF5B, Lima #C9F36B, Coco #C89A68, Bruno #E5A447, Mora #8468E8 | Kiwi #34e0a1, Lima #d4ff3a, Coco #ff9f1c, Bruno #4361ee, Mora #f72585 (duotono, solo en el punto) |
| Tipografía | Sora | Bricolage Grotesque |
| Nombres | Kiwi UX Architecture, Lima Design System Governance, Coco Visual Engineering & Audit, Bruno Frontend Implementation, Mora Verified Documentation; paquete «Fruti Squad Complete» | Kiwi UX Architect, …, Coco UI Audit, Bruno Frontend Implementation Engineer, Mora Documentation & Knowledge Engineer; «Workflow Pack» |
| Agentes | Personajes cercanos y expresivos, no infantiles | Símbolos abstractos |

## Verificación de los colores del brief (validador de dataviz, sobre #161616)
- Contraste con el fondo oscuro: todos ≥ 4.4:1 (pasa).
- Sobre la superficie clara #F8F8F5 fallan para elementos gráficos (< 3:1): Kiwi 1.8, Lima 1.2, Coco 2.4, Bruno 2.0, acento #B7F34D 1.2. Solo Mora pasa (3.8).
- Daltonismo: Bruno #E5A447 ↔ Kiwi #7FCF5B ΔE 2.3 (deutan): indistinguibles. Bruno ↔ Coco ΔE 6.6 incluso con visión normal.
- Conclusión: el manual debe fijar variantes oscurecidas para fondo claro y apoyarse en la silueta, como exige el brief (WCAG 2.2 AA).

## Decisión (usuario, 2026-10-30): «b la nueva»
Manda la identidad nueva (símbolos Átomos, duotono, Bricolage Grotesque). Del brief se conservan estrategia, posicionamiento, público, personalidad, mensajes, arquitectura de marca, límites de afirmaciones y lista de aplicaciones. Los cambios quedan documentados en `manual/` (sección 2).
Pendiente: nombres de producto (brief: «Fruti Squad Complete», UX Architecture, Visual Engineering & Audit, Frontend Implementation, Verified Documentation; rondas: Workflow Pack, UX Architect, UI Audit, Frontend Implementation Engineer, Documentation & Knowledge Engineer). El manual v0.1 usa los de las rondas.
