# Prueba multi-herramienta (Claude Code, Codex, Kiro)

Comprueba que cada herramienta llega a la política (`.fruti/policy.md`) y sigue "rutea primero, lee después". Se hace una herramienta a la vez.

## 0. Preparación (una vez por herramienta)

1. Crea una carpeta vacía con un `form.html` pequeño (formulario de 3 campos).
2. Instala: `node bin/install.mjs install --target <claude|codex|kiro> --dest <carpeta>`.
3. Comprueba que existen:

| Herramienta | Debe existir |
|---|---|
| Claude | `CLAUDE.md` con `@.fruti/policy.md` |
| Codex | `AGENTS.md` con la línea "lee `.fruti/policy.md`" |
| Kiro | `.kiro/steering/fruti-squad.md` |
| Las tres | `.fruti/policy.md`, `.fruti/runtime/*.yaml` |

Si falta algo, la falla es del instalador, no de la herramienta.

## 1. Prueba de carga

Abre la herramienta en esa carpeta y pide: **"rediseña este formulario"**. No menciones la política ni los archivos. Observa sin intervenir:

| # | Qué mirar | Pasa si… |
|---|---|---|
| a | ¿Leyó `.fruti/policy.md`? | Lo abrió antes de su primera acción de diseño. En Claude basta con que cite sus reglas (se carga por `@`). |
| b | ¿Qué contrato runtime abrió? | Abrió `kiwi.yaml` y solo ese. |
| c | ¿Abrió `references/` de golpe? | No. Solo los que `kiwi.yaml` lista para la operación. |
| d | ¿Pidió decisiones que no eran de producto? | No. Debe marcar lo faltante como `unresolved`. |
| e | ¿Escribió `.fruti/handoffs/current.json`? | Sí, con campo `round`. |

## 2. Prueba de inferencia prohibida (opcional)

Añade un `old.css` con colores crudos (p. ej. `#ff6600`) y pide: **"haz un botón nuevo"**.

- **Pasa:** usa tokens o marca el valor como `unresolved`.
- **Falla:** copia `#ff6600`. Es la regla central de "Approved Sources Only".

## 3. Registro

| Herramienta | a | b | c | d | e | Notas |
|---|---|---|---|---|---|---|
| Claude | | | | | | |
| Codex | | | | | | |
| Kiro | | | | | | |

Tokens: en Claude, `/context` muestra cuánto ocupan las instrucciones al arrancar. En Codex y Kiro no hay equivalente verificado: cuenta los archivos que abrió.

## Criterio de salida

- **Cierras** si las tres pasan a y b, y ninguna falla c.
- **Falla a** en una herramienta → el problema es su puntero (redacción o ubicación); se arregla primero.
- **Falla c** → el problema es `kiwi.yaml`; decidir si hace falta una regla más.

El comportamiento de un agente varía entre ejecuciones: una prueba por herramienta es una pista, no una garantía. Si algo falla, repite una vez antes de cambiar código.
