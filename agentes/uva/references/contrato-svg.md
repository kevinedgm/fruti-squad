# Contrato técnico del SVG (E2, E6)

Reglas que cumple todo icono de Uva. La columna **Verifica** indica el código de `scripts/check-icon.mjs` que la comprueba; «manual» significa que el script no puede verificarla y hay que revisarla a mano (o en el banco/propuesta).

## Estructura y estilo

| Regla | Verifica |
|---|---|
| XML válido: ningún comentario `<!-- -->` contiene `--` (p. ej. el nombre de una clase `uva-<id>--<mod>` o una variable `--uva-…`). Inline en HTML pasa, pero como `<img>`, favicon o archivo no abre | X1 |
| `viewBox="0 0 24 24"` | A1 |
| Sin `width`/`height` fijos en el archivo final | A1b (recomendado) |
| En la raíz: `fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"` | COL1, A3, A4 |
| Un solo `stroke-width`, en la raíz | A3 |
| Raíz con clases `uva-icon uva-<id>`; `<id>` = `semanticName` (E1) | ID |
| Grosor por CSS: `.uva-<id>{stroke-width:var(--uva-stroke,1.5)}` | COL3 (recomendado) |
| Sin colores fijos (ni en atributos ni en CSS): solo `currentColor` y variables | COL2 |
| Acento: `.uva-<id>__acento{fill:var(--uva-accent,currentColor);stroke:none}` (o `stroke:` si el acento es un trazo) | manual (COL2 impide fijarlo) |
| **Una clase por regla, sin combinadores:** cada pieza estilada lleva su clase con prefijo `uva-<id>__<pieza>`; nunca `.uva-<id> .acento{…}`. Las reglas con descendencia no alcanzan el contenido clonado por `<use>`; las variables CSS y `currentColor` sí se heredan | SEL |
| `@keyframes uva-<id>-<nombre>` (prefijo para no colisionar si se inlinean varios iconos) | ID2 |
| Al reducir el grosor, reducir también los rellenos (puntos, gotas) para conservar el peso | manual (banco: fila de grosores) |

## Accesibilidad

| Regla | Verifica |
|---|---|
| Oculto por defecto con `aria-hidden="true"` (criterio de Lucide) | C2 |
| Solo si comunica algo esencial por sí solo: sin `aria-hidden`, con `role="img"` y `aria-label` (o `<title>`); nunca las dos cosas a la vez | C2, C2b (aviso para confirmar que de verdad informa solo) |
| En un botón con solo icono, `aria-label` va en el `<button>`, no en el SVG | manual (recomendación de uso, E5) |

## Movimiento

| Regla | Verifica |
|---|---|
| Termina en ≤5 s (repeticiones finitas, nada de `infinite`) y deja un fotograma estático con significado | D1 (duración); fotograma: manual (`banco.html#final`) |
| Bloque `@media (prefers-reduced-motion: reduce)` | D2 |
| Trazos animados con `stroke-dashoffset` llevan `pathLength` explícito | D5 |
| Para repetirlo, el componente vuelve a montar el icono o cambia de estado | manual (recomendación de uso) |

## Entrega y uso

| Regla | Verifica |
|---|---|
| El color solo se hereda si el SVG va **inline** o vía `<use>`; como `<img src>` no hereda `currentColor` (avisarlo al entregar) | manual |
| Una variante de referencia de una librería (Lucide) se verifica como referencia, sin las convenciones `uva-*` | REF |

## Nombres de clase por etapa

- **E2 (variantes):** raíz `uva-<id>-a`, piezas `uva-<id>-a__<pieza>`, keyframes `uva-<id>-a-<nombre>` (lo mismo con `-b`, `-c`…), para que sus `<style>` no se pisen.
- **E6 (entrega):** la elegida pasa a `uva-<id>`, `uva-<id>__<pieza>` y `uva-<id>-<nombre>`; archivo `<semanticName>.svg`.

## `registro.yaml` (E6)

Entrada propuesta del registro semántico (norma §5.1). Es una propuesta: el registro del proyecto, si existe, no lo edita Uva.

```yaml
semanticName: distilling
icon: { library: custom, name: uva-distilling }   # o { library: lucide, name: Barrel }
category: status
accessibility: { defaultLabel: Destilando }
direction: { rtl: fixed }
motion: { allowed: progress }
status: proposed
usage: { label: required, iconOnlyButton: "44x44, nombre en el botón" }
```
