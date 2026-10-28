# Fidelidad estructural F2 → F3 (FID-GEOMETRY-001)

## El problema que resuelve

Kiwi entrega un F2 correcto en compact, medium y expanded. Al construir F3, la geometría se pierde: el icono se aleja del texto, la acción cae entre el título y el subtítulo, el botón se vuelve un bloque de ancho completo. Antes de esta regla nadie lo detectaba, porque:

- la revisión visual era un *judgment* de Coco con severidad `warning`, así que nunca bloqueaba;
- Coco se auditaba a sí mismo y Lima aceptaba ese reporte sin volver a revisarlo;
- el F2 viajaba como texto interpretable y chocaba con defaults genéricos (acciones a ancho completo en móvil).

## Cómo funciona

1. Kiwi marca cada pieza y cada grupo del F2 con `data-piece="<id>"`, anidados como los grupos.
2. Coco conserva las mismas marcas en F3.
3. `fruti fidelity` abre ambos en cada viewport de verificación, mide las cajas y compara:

| Chequeo | Falla cuando |
|---|---|
| `presence` | una pieza del F2 no está marcada en F3 |
| `visibility` | una pieza visible en F2 se oculta en F3, o al revés |
| `grouping` | una pieza cambia de grupo, o el grupo se disuelve (`display: contents`) |
| `relation` | cambia el orden o la fila entre piezas hermanas (izquierda / derecha / encima / debajo) |
| `intrusion` | una pieza ajena queda metida entre los miembros de un grupo |
| `gap` | una separación fija cambia más de ×2 (con 16 px de holgura); una separación elástica se colapsa |
| `size` | el ancho o alto cambia más de ×2 (con 24 px de holgura) |

No compara colores, tipografía ni estilo: eso es la expresión visual de Coco. Compara las decisiones que Kiwi congeló.

**Separación fija vs. elástica.** Si en el F2 una separación es igual en todos los viewports (12 px entre icono y texto), es una decisión de espaciado y se compara estrictamente. Si crece con el espacio (el hueco entre la identidad y la acción por `space-between`), es elástica y solo falla si se colapsa.

**Libertades aprobadas.** En el F2, `data-piece-free="size"`, `"gap"` o `"all"` declaran que esa pieza puede cambiar de tamaño o separación. Registra el porqué en el decision record.

## Probarlo con este ejemplo

Necesita Playwright con Chromium en el proyecto (`npm i -D playwright && npx playwright install chromium`).

```bash
# Respeta el F2: otra fuente y otra paleta, misma geometría → PASS
fruti fidelity --f2 docs/fidelidad/kiwi-f2.html --f3 docs/fidelidad/f3-correcto.html

# Reproduce los tres errores reales → FAIL con 15 hallazgos
fruti fidelity --f2 docs/fidelidad/kiwi-f2.html --f3 docs/fidelidad/f3-roto.html
```

En un proyecto real, `--f3` puede ser la URL de la ruta en el servidor de desarrollo.

Códigos de salida: `0` pass · `1` fail · `2` uso incorrecto · `3` bloqueado (sin navegador, sin marcas o archivo inaccesible). Un bloqueo nunca cuenta como PASS.
