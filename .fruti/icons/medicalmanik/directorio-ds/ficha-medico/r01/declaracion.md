# Declaración de cumplimiento · FichaMedico · r01

| Campo | Valor |
|---|---|
| Ruta | R2 (Actual + A/B/C) |
| Fidelidad | F2 |
| Pregunta de diseño | ¿Puede el paciente saber en cada ficha, en un celular, dónde atiende, cuánto cuesta ahí, cuándo hay lugar y cómo agendar, sin confundir consultorios? |
| Artefactos | brief.md · propuestas/index.html (y publicar.html) · hallazgos.md · declaracion.md |
| Modifica producción | No (tampoco el sistema de diseño publicado) |

## Estándares leídos
- Protocolo de gobernanza de interfaz (skill). Sus `references/` y `assets/` no estaban en la instalación; se usaron las copias del agente Kiwi del repo: `agentes/kiwi/references/brief-funcional.md`, `fidelidad.md`, `wireframing.md`, `geometry-contract.md`, `validacion.md`, `.fruti/contracts/adaptativo.md`, plantillas de `agentes/kiwi/assets/plantillas/` y `wireframe-kit.css`.
- Sistema «Directorio Manik» v5 (solo para contenido, cortes y reglas de negocio; no para lo visual: F2 es neutro).
- WCAG 2.2 AA (objetivos ≥ 24 px, foco visible del kit, estados con forma + texto).

## Desviaciones del protocolo
- Referencias de la skill ausentes en la instalación: sustituidas por las de Kiwi en el repo (mismo contenido de protocolo). `references/hig-web-pwa.md` no se leyó para esta ronda (F2 de un componente; no hay navegación nueva).
- Una acción principal por ficha (no por vista): cada ficha es un bloque de decisión propio. Declarado en hallazgos.

## Comprobaciones ejecutadas
- check_artifact.py: ✔ (0 errores, 0 avisos).
- Navegador (Playwright/Chromium): 4 versiones × 3 marcos (393 / 834 / 1440) × 8 estados = 96 combinaciones · errores JS: 0 · desborde en fichas o en la lista: 0 · controles < 24 px: 0 · fichas con más de una principal: 0.
- Alturas de ficha en compact 393: Actual 366–427 · A 339–460 · B 310–354 · C 232–339 px.
- Estados representados: default, carga, vacío por filtros, error de horarios, sin conexión, horario ocupado, sin lugar en 2 semanas, contenido largo; más sin foto (3 siluetas), sin opiniones, formas mixtas.

## Matriz de adaptación
| Elemento | compact (< 600) | medium (600–1023) | expanded (≥ 1024) | Motivo | Técnica | Foco/estado |
|---|---|---|---|---|---|---|
| Lista | 1 columna | 2 columnas | 2 columnas + filtros persistentes | Comparar sin perder contexto | Grid por ancho del marco | Conserva posición y filtros |
| Ficha | Avatar 64 junto a la identidad; bloque/filas a todo el ancho; acción a todo el ancho | Igual que compact (cada columna < 520) | Foto 132 a la izquierda; contenido en columna derecha | La ficha decide por SU ancho, no por el dispositivo | Container query de ficha a 520 px | Horario elegido y foco se conservan al cambiar |
| Filtros | Botón «Filtros (n)» → hoja | Botón → hoja | Panel lateral fijo | Espacio | Mismo estado de filtros | Esc cierra la hoja; foco vuelve al botón |
| Horarios (A, B, Actual) | Máx. 3 + «Más horarios» | Igual | Igual | No saturar | — | aria-pressed |
| Consultorios (C) | Máx. 2 filas + «Ver n más» | Igual | Igual | Formas mixtas visibles | — | Cada fila con su acción |

## Comprobaciones NO ejecutadas
- Texto ampliado al 200 % y zoom del navegador.
- Recorrido con teclado (Tab/Esc) y lector de pantalla; solo se usan botones y enlaces nativos con foco visible del kit.
- Prueba con pacientes (la diferencia entre A y C depende de ella).
- Localización y formatos de moneda fuera de MXN.
- Hoja de filtros abierta (se representa como botón; el componente ya existe en el sistema).

## Hallazgos
Ver `hallazgos.md`.

## Traspaso
- **→ coco:** tras la elección, F3 de la ficha con el sistema Directorio Manik (tokens existentes; sin colores nuevos).
- **→ lima:** actualizar el contrato de FichaMedico (anatomía y estados) y decidir la regla «una principal por ficha».
- **→ mora:** nada aún.

## Siguiente paso del usuario
Elegir A, B o C (o una mezcla explícita) y responder las incógnitas 1 y 2 del brief.
