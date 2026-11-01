# Accesos rápidos de medicamentos · ronda 1 (2026-11-01)

Pedido: un icono para reutilizar los medicamentos de la última consulta y otro (o el mismo) para los medicamentos recomendados asociados a un diagnóstico. Contexto: receta del Expediente Manik, junto a «Agregar medicamento».

- Contrato Uva: viewBox 24, trazo 2 (`--uva-stroke`), puntas redondas, `currentColor`, `aria-hidden`; siempre acompañados de texto.
- Base común: la misma pastilla (`PASTILLA` en `gen.py`); el modificador de la esquina inferior derecha cambia el significado.
- `repeat-last-medications`: a historial (recomendada), b flecha de regreso, c reloj (riesgo: «horario de dosis»).
- `diagnosis-medications`: a etiqueta (recomendada, misma metáfora que «Sugerir códigos CIE-10»), b estrella, c lista.
- Si las recomendaciones vienen de la IA, no se usa este icono: va el destello y «Sugerido por IA» de Manik IA.
- Pendiente (usuario): elegir variantes; confirmar si los recomendados salen de un protocolo fijo o de la IA.

Archivos: `gen.py` (genera `variantes/`, `variantes.json`, `revision.html`), `plantilla.html`.
Revisión: https://claude.ai/artifact/RdJsJJVbS5rEk8vj8RbCdo
