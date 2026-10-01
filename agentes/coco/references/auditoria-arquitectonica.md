# Auditoría arquitectónica de componentes (Paso 5.4)

Se carga cuando coco **crea, modifica, refactoriza, valida o audita un componente** (incluida R0 de arquitectura). Una ronda que solo prototipa en el Hub no la necesita.

## Cuándo corre

Siempre que analices, crees, modifiques, refactorices o valides un componente: no solo compruebes que «funciona», evalúa si es **sostenible**.

## Scripts, policy y censo

- Si el perfil declara `governance_scripts.audit_component` y una `governance_policy`, ejecútalos y aplica la policy.
- Si no, aplica los principios universales de abajo (clasificación, no sobrearquitectura, responsabilidades separadas) por revisión manual y decláralo como `manual`.
- Al crear o mover un componente, **cénsalo** en el manifiesto del registry si el perfil lo usa, y corre el `coverage` si está declarado.

## Reporte

- Findings con severidad (`CRITICAL/HIGH/MEDIUM/LOW/INFO`), acción (`AUTO_FIX/REFACTOR/RECOMMENDATION/REVIEW_REQUIRED/NO_ACTION`) y confianza (`high/medium/low`).
- Un **RECOMMENDED ACTION PLAN** ordenado por dependencia.
- Un **Component Health** descriptivo.

## Reglas de oro

- **No sobrearquitectar:** cada capa, ViewModel, composable o wrapper existe solo si reduce acoplamiento, duplicación o complejidad reales. La reutilización no borra el conocimiento del dominio; no conviertas todo en un genérico gigante.
- **No autofix con confianza baja.**
- Una refactorización arquitectónica **no** cambia en silencio comportamiento/contenido/negocio/jerarquía/flujos/permisos/navegación/responsive: si hay que tocarlos, es `REVIEW_REQUIRED`.

## Preguntas de responsabilidad

Antes de dar un componente por saludable, responde: ¿quién es responsable de los datos, quién los transforma, quién conoce el dominio, quién controla composición/estilo común/navegación/estado? ¿Podría cambiar el backend sin rehacer la UI, y el design system sin editar cada feature? Si las responsabilidades están separadas, la arquitectura es saludable.
