# Declaración de cumplimiento · Inicio Manik · r01

| Campo | Valor |
|---|---|
| Ruta | R1 (una dirección) |
| Fidelidad | F0 (flujo) + F2 (estructura) |
| Pregunta de diseño | ¿El prospecto entiende en un vistazo qué es Manik y llega a resultados útiles en uno o dos toques, aunque no sepa qué especialista necesita? |
| Artefactos | brief.md · flujo.md · propuestas/index.html (y publicar.html con el flujo) · hallazgos.md · declaracion.md |
| Modifica producción | No |

## Estándares leídos
Protocolo de Kiwi en el repo (`brief-funcional.md`, `user-flow.md`, `fidelidad.md`, `wireframing.md`, `geometry-contract.md`, `validacion.md`), `.fruti/contracts/adaptativo.md`, kit neutral; sistema «Directorio Manik» (voz, celular primero); WCAG 2.2 AA.

## Desviaciones del protocolo
- Referencias de la skill tomadas de las copias de Kiwi en el repo (la skill instalada no trae sus archivos).
- No se hicieron preguntas antes de construir: las 3 incógnitas se representan como estados y quedan abiertas.

## Comprobaciones ejecutadas
- check_artifact.py: ✔ (0 errores, 0 avisos).
- Navegador: 3 marcos × 9 estados = 27 combinaciones · errores JS: 0 · desborde: 0 · controles < 24 px: 0 · acción principal visible: 0 o 1 por vista (el buscador es la acción dominante; en compact es un campo con contorno que abre la búsqueda).

## Matriz de adaptación
| Elemento | compact (< 600) | medium (600–1023) | expanded (≥ 1024) | Motivo | Técnica | Foco/estado |
|---|---|---|---|---|---|---|
| Navegación | Logo · Entrar · Menú | Igual | Especialidades · Soy médico · Entrar | Espacio | Container query | — |
| Próxima cita | Arriba, tarjeta a todo el ancho | Igual | Igual | Quien regresa viene por su cita | Condicional (cuenta) | — |
| Buscador | Campo único → pantalla completa | Igual | Píldora qué + dónde con sugerencias abajo | Teclado y pulgar | Dos piezas, un estado | Foco al campo «Qué»; Volver regresa al disparador |
| Foto de marca | Oculta | A la derecha del texto | A la derecha, 4:5 | En celular el buscador gana el primer vistazo | Grid | — |
| Lo que sientes | 2 columnas | 3 | 6 | Escaneo | Grid | — |
| Con lugar hoy | 1 columna | 2 | 3 | Muestra de valor | Grid | Se oculta si falla |
| Cómo funciona | Pasos en lista | 3 columnas | 3 columnas | Secuencia real | Grid | — |

## Comprobaciones NO ejecutadas
- Texto ampliado 200 %, teclado y lector de pantalla, prueba con prospectos, contenido real de «Con lugar hoy», F3 con el sistema.

## Traspaso
- **→ coco:** F3 del inicio con el sistema Directorio Manik tras aprobar.
- **→ lima:** regla de ubicación (permiso solo bajo petición) como norma del sistema.

## Siguiente paso del usuario
Aprobar la estructura y el titular, y responder las incógnitas 1–3.
