# Declaración de cumplimiento · FichaMedico · r04

| Campo | Valor |
|---|---|
| Ruta | R2 → dirección elegida (C + horarios de B) |
| Fidelidad | F2 |
| Pregunta de diseño | ¿La combinación conserva la claridad de C (cada consultorio con su precio y forma de agendar) y suma los horarios de B sin volver la ficha demasiado alta? |
| Artefactos | brief.md · propuestas/index.html (y publicar.html) · hallazgos.md · declaracion.md |
| Modifica producción | No |

## Estándares leídos
Los de r01–r03 (protocolo de Kiwi en el repo, contrato adaptativo, kit neutral), WCAG 2.2 AA.

## Desviaciones del protocolo
Las de r01 (referencias de la skill desde Kiwi en el repo; una principal por ficha).

## Comprobaciones ejecutadas
- check_artifact.py: ✔ (0 errores, 0 avisos).
- Navegador: 2 versiones (elegida, actual) × 3 marcos × 8 estados = 48 combinaciones · errores JS: 0 · desborde: 0 · controles < 24 px: 0 · fichas con más de una principal: 0.
- Alturas en compact 393 (elegida): 452 · 330 · 374 · 557 px (antes de compactar: 549 · 342 · 386 · 602).

## Matriz de adaptación
| Elemento | compact (< 600) | medium (600–1023) | expanded (≥ 1024) | Motivo | Técnica | Foco/estado |
|---|---|---|---|---|---|---|
| Lista | 1 columna | 2 columnas | 2 columnas + filtros laterales | Comparar | Grid por ancho | Conserva filtros y posición |
| Médico | Avatar 64 junto al nombre | Igual | Foto 132 a la izquierda | Espacio | Container query de ficha (520 px) | — |
| Consultorio abierto | Horarios (≤ 3) + «Agendar» a la derecha | Igual | Igual, en la columna derecha | Decidir sin salir de la lista | Bloque | Horario elegido se conserva |
| Otros consultorios | Fila compacta + contorno | Igual | Igual | Formas mixtas visibles | Grid de fila | Botón propio por fila |

## Comprobaciones NO ejecutadas
- Texto ampliado 200 %, teclado y lector de pantalla, prueba con pacientes, interacción de «Ver horarios» de otro consultorio, F3 con el sistema real.

## Traspaso
- **→ lima:** congelar la anatomía (D1–D5) en el contrato de FichaMedico; decidir D6 (regla de píldora).
- **→ coco:** F3 de la ficha en el sistema «Directorio Manik» (cian real, Onest, avatares).

## Siguiente paso del usuario
Aprobar la anatomía para pasarla al sistema (F3), o pedir ajustes.
