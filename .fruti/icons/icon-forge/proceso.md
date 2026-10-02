# icon-forge · registro completo del proceso

Cómo se llegó al icono de la skill Uva: cada paso, lo que se midió, lo que falló y por qué se decidió lo que se decidió.
Convención: **[Hecho]** = medido o comprobado; **[Juicio]** = lectura visual o criterio de diseño; **[Desvío]** = algo que el contrato de Uva pide y no se hizo (o se hizo distinto).

---

## 0. El encargo

El usuario pidió usar Uva para el icono de la propia skill, con estas condiciones:

- **Significado:** «forja / construcción precisa de iconos», con una referencia sutil a Uva.
- **No debe parecer:** una fruta, una app de recetas, una herramienta de IA genérica ni un editor de imágenes.
- **Uso:** icono de skill en Codex y GitHub; reconocible a 24×24; también avatar y favicon. Sin texto ni letras. Monocromo con `currentColor`.
- **Proceso pedido:** (1) buscar antes en Lucide; (2) tres variantes que cambien solo la metáfora: uva abstracta de módulos o nodos · herramienta de forja sobre una forma de icono · retícula de icono con un rasgo sutil de racimo; (3) evaluar reconocimiento, diferenciación y riesgo de confusión; (4) recomendar una; (5) entregar el SVG.
- **Contrato técnico:** `viewBox="0 0 24 24"` · margen visual ≥2 px · trazo 1.5 con extremos y uniones redondeados · `stroke="currentColor"`, `fill="none"` · sin colores fijos, degradados, sombras, máscaras ni detalle que se pierda a 16 px · piezas con clases `uva-` · versión decorativa con `aria-hidden="true"` y explicación de uso en botón · validar con `check-icon.mjs` y corregir los errores bloqueantes.

---

## 1. Enrutamiento: qué se cargó y qué no

La política del repo (`AGENTS.md`) obliga a enrutar antes de leer: identificar al dueño, leer su contrato de runtime y cargar solo lo que ese contrato lista para la operación.

1. **[Hecho]** Rama activa: `claude/mango-2.0`, con el árbol de trabajo limpio.
2. **[Hecho]** Se leyó `.fruti/runtime/uva.yaml`. Operación `create_icon` = E1 Entender → E2 Prototipar → E3 Evaluar → E4 Animar (solo si es estado o proceso) → E5 Proponer → E6 Entregar. El mismo contrato fija las decisiones de familia que se aplicaron:
   - trazo 1.5, por decisión previa del usuario;
   - separación mínima entre elementos ≥ grosor del trazo, es decir ≥1.5;
   - id = `semanticName` (archivo `<id>.svg`, clase `uva-<id>`, piezas `uva-<id>__<pieza>`);
   - base: rejilla 24, padding 2, extremos y uniones redondeados, `currentColor`.
3. **[Hecho]** Para E1 se leyó `assets/brief-template.md`.
4. **[Hecho]** Para E2 se leyeron el índice de `references/reglas.md` (R1–R7 y las trampas técnicas) y `references/contrato-svg.md`, leído antes en la sesión.
5. **[Hecho]** Para E3 se leyeron las instrucciones de `assets/banco-prueba.html` (marcadores `UVA:ICONOS` y `UVA:CONFUSIONES`, modos `#final`, `#medio` y `#reducido`) y la cabecera de `scripts/render-banco.mjs`.
6. **[Desvío]** El contrato lista `references/norma/01-seleccion.md` (§2–10) para E1 y `references/estandares.md` (la rúbrica) para E3. **No se leyeron.** El brief siguió la plantilla, que resume el orden de decisión de la norma (§4). La evaluación usó las reglas R1–R7 y el banco renderizado, no la rúbrica completa.
7. **[Hecho]** No se cargaron los ejemplos de `examples/`: el contrato lo prohíbe durante un encargo porque sesgan el diseño.

---

## 2. E1 · Búsqueda en Lucide

Comando: `node agentes/uva/scripts/buscar-lucide.mjs anvil hammer grape forge grid pen-tool component shapes`
Resultado (lucide-static 1.49.0, 1857 iconos; el número es la puntuación de coincidencia):

| Puntos | Icono | Etiquetas relevantes | Lectura **[Juicio]** |
|---|---|---|---|
| 13 | `anvil` | forge, blacksmith, metal, heavy | Dice «herrería, peso», no «iconos». |
| 8 | `component` | design, module, symbol | Dice «componente de diseño». |
| 8 | `grape` | fruit, wine, food | Justo lo que el encargo prohíbe (fruta, recetas). |
| 8 | `hammer` | build, construction, diy | Dice «bricolaje o construcción» en general. |
| 8 | `pen-tool` | vector, drawing, path | Dice «editor vectorial»; el encargo excluye «editor de imágenes». |
| 8 | `shapes` | triangle, square, circle, toy | Dice «formas o juguete». |
| 6 | `grid-2x2`, `grid-3x3`, `layout-grid`… | table, rows, columns | Dicen «tabla o maquetación». |

**Conclusión [Juicio]:** ninguno comunica por sí solo «construir iconos», así que se dibuja un icono propio. Como el contrato pide (`include_partial_lucide_match_as_variant`), las coincidencias parciales entran en el banco como **confusiones de referencia**: `grape`, `anvil`, `boxes` y `pen-tool`.

---

## 3. E1 · Brief (una línea por campo)

- **Nombre semántico y categoría:** `icon-forge` · marca propia (la identidad de la skill). La norma dice que una marca no se dibuja y se usa el logotipo del tercero; aquí la marca es nuestra, así que sí se dibuja.
- **¿Ya existe?:** búsqueda de la sección 2; solo coincidencias parciales.
- **Concepto vs. significado:** objeto = retícula, racimo, yunque · significado = «Uva: forja precisa de iconos».
- **Uso:** 24 px como icono de skill; 16 px como favicon; avatar. Sin texto. Decorativo cuando lo acompaña el nombre de la skill.
- **Estilo:** base de Uva (no hay tokens de icono en el proyecto); trazo 1.5.
- **Confusiones iniciales:** `grape` (fruta), `anvil` (herrería), `boxes` (módulos o almacén), `pen-tool` (editor).
- **Criterio de éxito:** a 16–24 px no se confunde con ninguna de las confusiones y se lee como «construir iconos».

**[Desvío]** El brief no se guardó como `brief.md`; se presentó en el chat.

---

## 4. E2 · Tres variantes (una por metáfora pedida)

Todas comparten la raíz exigida: `viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"`, más un `<style>` con `stroke-width:var(--uva-stroke,1.5)` para ajustar el grosor. Los nombres de E2 llevan sufijo de variante (`uva-icon-forge-a`, `-b`, `-c`), como pide el contrato, para que sus estilos no se pisen.

### A · Racimo abstracto de módulos
- **Geometría:** 6 cuadrados redondeados de 4×4 (`rx 1`) en filas de 3-2-1: fila 1 en y=5 (x=4.5, 10, 15.5), fila 2 en y=10.5 (x=7.25, 12.75), fila 3 en y=16 (x=10). Separación entre módulos 1.5. Tallo curvo `M12 5V3.5c1 0 2-.5 2.5-1.25`.
- **Hipótesis:** módulos (construcción) en forma de racimo (Uva) sin ser fruta, porque son cuadrados y no esferas.

### B · Forja: yunque con un icono encima
- **Geometría:** «icono» recién forjado = cuadrado redondeado de 6.5×6.5 (`rx 1.75`) en (7, 4). Yunque = `M4 12h16v1.5a2 2 0 0 1-2 2h-3l1.5 4.5h-9L9 15.5h-.5C6 15.5 4 14 4 12z`. Chispas = 3 puntos rellenos (r 0.9) en triángulo (16.5, 4.25 · 19.5, 4.25 · 18, 6.85).
- **Hipótesis:** el yunque dice «forja», el cuadrado dice «icono» y las chispas en racimo son el guiño a Uva.

### C · Retícula de icono con rasgo de racimo
- **Geometría:** marco de 18×18 en (3, 3) con `rx 4` (la forma de un icono de app); 3 nodos (círculos r 2) en (9.25, 11), (14.75, 11) y (12, 15.75); tallo `M12 9V6.5`.
- **Hipótesis:** el marco dice «icono», los nodos alineados dicen «construcción geométrica» y la disposición 2+1 con tallo es el racimo.

---

## 5. Primera validación y un fallo del verificador

1. **[Hecho]** `check-icon.mjs` sobre las tres variantes: todo correcto (X1, A1, A1b, A3, A4, COL1, COL2, COL3, C2, SEL, D0) salvo **ID ❌ «clases "uva-icon uva-<id>"»** en las tres.
2. **[Hecho] Diagnóstico.** El verificador extrae el id con `/\buva-(?!icon\b)([\w-]+)/`, para saltarse la clase base `uva-icon`. Pero `\b` (límite de palabra) también se cumple ante un guion. En `uva-icon-forge-a`, «icon» va seguido de «-», así que la búsqueda negativa lo descarta como si fuera la clase base. Resultado: **cualquier id que empiece por `icon-` era imposible de validar.** El fallo estaba en la herramienta, no en el icono.
3. **[Hecho] Corrección** en `agentes/uva/scripts/check-icon.mjs`: `/\buva-(?!icon(?![\w-]))([\w-]+)/`. Ahora solo se excluye `uva-icon` cuando es la palabra completa (no la siguen ni letras ni un guion).
4. **[Hecho] Comprobación de regresión.** Se pasó el verificador por todos los iconos existentes (`agentes/uva/examples/*.svg`, `.fruti/icons/*/*.svg`). Solo fallan `grana.svg` y `grana-favicon.svg`. Con `git stash` (verificador sin el cambio) `grana.svg` da las mismas líneas de fallo (A3, A4, COL1, COL2, ID): son anteriores al cambio y esperables, porque Grana es un logotipo de marca relleno y con color, no un icono de línea de la familia.

---

## 6. E3 · Banco 1: tres variantes contra cuatro confusiones

- **Montaje [Hecho]:** se copió `banco-prueba.html`. En `UVA:ICONOS` van las 3 variantes, sin comentarios y con `data-nombre`. En `UVA:CONFUSIONES` van los SVG reales de Lucide (`buscar-lucide.mjs --svg <nombre> --stroke 1.5`) de `grape`, `anvil`, `boxes` y `pen-tool`. Captura: `render-banco.mjs banco.html --modo final`.
- **Qué muestra el banco:** comparación directa a 24 y 20 px con las confusiones; tamaños de la norma (14, 16, 20, 24, 32, 48 y 96 de inspección); familia a 24 px (casa, mano, variante, reloj) para el peso óptico (R6); contexto oscuro con color por estado a 22 y 44 px.
- **[Hecho]** El icono es estático, así que los modos `#medio` y `#reducido` (que prueban animaciones) no aportan nada y no se renderizaron. E4 no aplica.

**Lectura [Juicio]:**
- **A:** a 16 px los 6 módulos se funden en una mancha (R7: demasiadas piezas para 24 unidades). Con el tallo, la silueta global es la de `grape`. Riesgo alto de leer «fruta» o «bloques».
- **B:** «forja» se entiende a 32 px o más y las chispas en racimo funcionan como guiño. Pero a 16–20 px aparece una confusión no prevista: **parece un inodoro o un lavabo**. Causa: una caja centrada encima de una forma con cintura. Se añade `toilet` a las confusiones (R2: se suman las que aparecen al renderizar).
- **C:** la silueta más simple: nítida incluso a 14 px y claramente distinta de las cuatro confusiones. Débil en «forja».

---

## 7. Iteración con causa: B2

- **Causa a corregir:** el parecido con un inodoro viene de la caja centrada sobre un pie con cintura.
- **Cambio:** yunque de arquetipo con el cuerno en punta a la izquierda (`M3 11.5h18v2a2 2 0 0 1-2 2h-2.5l1.5 4.5h-8l1.5-4.5H10c-3.5 0-6-1.5-7-4z`), el icono forjado descentrado a la derecha (6×6 en 12.5, 4) a 1.5 de la superficie, y las chispas movidas a la izquierda (5.25, 5 · 8.25, 5 · 6.75, 7.6).
- **Banco 2 [Hecho]:** B, B2 y C contra `grape`, `anvil`, `toilet` (Lucide) y `pen-tool`.
- **Resultado [Juicio]:** B2 mejora el arquetipo, pero a 16–20 px **sigue leyéndose como inodoro o lavabo**. Mientras haya una caja sobre un pie con cintura, la silueta coincide.
- **Decisión:** dejar de iterar la vía del yunque. Dos rondas con la causa identificada y sin convergencia indican que el problema es la metáfora, no el ajuste.

---

## 8. Evaluación y recomendación (pasos 3 y 4 del encargo)

| Variante | Reconocimiento a tamaño real | Diferenciación | Riesgo de confusión |
|---|---|---|---|
| A · módulos | bajo: mancha a 16 px | baja | alto: `grape`, bloques |
| B / B2 · yunque | medio: la forja solo a ≥32 px | media | alto: `toilet` a 16–20 px |
| C · retícula + racimo | alto: nítida a 14 px | alta | bajo-medio: «app de frutas», trébol |

**Recomendación: C.** El marco redondeado se lee como «icono» a primera vista y los nodos alineados como construcción; el racimo queda como guiño sin llegar a fruta. Límite reconocido: **«forja» no se dibuja literalmente**; hacerla explícita (el yunque) costaba legibilidad.

---

## 9. E6 · Primera entrega y auditoría geométrica posterior

1. **[Hecho]** C se renombró a los nombres definitivos (`uva-icon-forge`, piezas `__reticula`, `__tallo`, `__nodo`) en `.fruti/icons/icon-forge/icon-forge.svg`, con `registro.yaml` (entrada propuesta de §5.1: categoría brand, `motion: none`, etiqueta por defecto «Uva», confusiones probadas) y `uso.md` (uso decorativo, botón con nombre accesible, color y exportación). El verificador pasa sin errores.
2. **[Hecho] Fallo que el verificador no detecta: los nodos se tocaban.** El borde exterior de un círculo es radio + medio trazo = 2 + 0.75 = 2.75. Los dos nodos superiores tenían los centros a 5.5 = 2 × 2.75, así que **separación 0**, por debajo del mínimo de familia (≥1.5). En el banco a 96 px se veían pegados.
3. **[Hecho] Recalculo:** r = 1.75 (borde exterior 2.5), centros a 6.5 entre sí (1.5 de separación). Medido: nodo-nodo 1.5/1.5/1.5; nodo-marco 2.5 y 2.12. Pero el tallo quedó a **1.25 del marco** (<1.5) y a 0.44 de un nodo. Ese segundo punto se resolvió en la variante siguiente.
4. **Banco 3 [Hecho]:** el icono final contra `grape`, `anvil`, `toilet` y `pen-tool`. **[Juicio] Confusión nueva:** con los nodos sueltos, tres círculos dentro de un cuadrado redondeado se leen como **cara 3 de un dado**, como **enchufe** y como **cara** (dos «ojos», tallo-nariz, nodo-boca). Mientras se tocaban se leían como racimo. Al cumplir la regla de separación se perdió la lectura de racimo.

---

## 10. Iteración final: C2 (nodos unidos por el tallo)

- **Causa:** sin conexión visible entre los nodos, el ojo los lee como agujeros (enchufe) o puntos (dado, cara).
- **Cambio:** el tallo se convierte en una Y que **une** los dos nodos superiores: `M12 6v2.25` + ramas `M12 8.25l-1.9 1.44` y `M12 8.25l1.9 1.44`, que terminan exactamente en el contorno de cada nodo (a 1.6 de su centro). Nodos de r = 1.6 en (8.9, 10.75), (15.1, 10.75) y (12, 16.12).
- **Medidas [Hecho]:**
  - nodo-nodo 1.5 / 1.5 / 1.5;
  - nodo-marco: izquierda 2.8, abajo 1.78, arriba 4.65;
  - tallo-marco 1.5;
  - margen exterior del marco 2.25 (≥2).
  - Las uniones rama-nodo son deliberadas: es la conexión que da la lectura de racimo, no elementos que deban separarse.
- **Banco 4 [Hecho]:** C (nodos sueltos) y C2 (nodos unidos) contra `dice-3` (Lucide), `grape`, `anvil` y un **enchufe redibujado** (marco + dos agujeros + ranura), porque Lucide no tiene un enchufe visto de frente: su `plug` es la clavija.
- **Lectura [Juicio]:**
  - C se parece al enchufe redibujado y a una cara.
  - C2 se lee como racimo o grafo de nodos y queda lejos del dado, cuyos puntos van en diagonal y sin unión.
  - A 16 px C2 está algo más cargado, pero sigue siendo legible.
  - Con los grosores 2 / 1.5 / 1.25 / 1 mantiene la forma.
- **Decisión:** C2 sustituye a C como `icon-forge`. `check-icon.mjs` pasa sin errores. Las confusiones probadas se actualizaron en `registro.yaml`.

---

## 11. Lo que quedó entregado

| Archivo | Qué es |
|---|---|
| `icon-forge.svg` | El icono final (C2), decorativo. |
| `registro.yaml` | Entrada propuesta de registro: categoría, etiqueta por defecto «Uva», sin movimiento, confusiones probadas (`grape`, `anvil`, `boxes`, `pen-tool`, `toilet`, `dice-3`, enchufe). |
| `uso.md` | Uso decorativo; botón solo con icono con el nombre en el `<button>` (`aria-label="Abrir Uva"`, área 44×44); `currentColor` no se hereda como `<img>`, favicon o avatar; GitHub no acepta SVG como avatar. |
| `banco.html`, `banco.png` | Banco 4: la comparación que decidió entre C y C2. |
| `agentes/uva/scripts/check-icon.mjs` | Corrección de la expresión del id. |

Commit `73974f1` en `claude/mango-2.0`, subido al remoto.

---

## 12. Desvíos y pendientes, dichos claro

- **[Desvío]** No se leyeron `norma/01-seleccion.md` ni `estandares.md`, aunque el contrato los lista para E1 y E3. La evaluación se apoyó en R1–R7 y en los bancos renderizados.
- **[Desvío]** E5 no generó `propuesta.html` ni pidió elegir antes de entregar: el encargo pedía recomendar una y entregar su SVG. Las variantes descartadas están en el banco y en este registro.
- **[Desvío]** No se guardaron `brief.md` ni `handoff.json`; otros iconos del repo, como `rabbit`, sí tienen `handoff.json`.
- **[Pendiente]** «Forja» no está dibujada de forma literal: es la concesión que se hizo a favor de la legibilidad.
- **[Pendiente]** Exportaciones para avatar y favicon: PNG 512×512 en versión clara y oscura, porque fuera de una página `currentColor` se pinta negro.
- **[Hecho, fuera del icono]** La corrección del verificador beneficia a cualquier icono futuro con id `icon-…`.
