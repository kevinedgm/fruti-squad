# Brief · <semanticName>

<!-- Plantilla de E1. Una línea por campo, sin párrafos. Orden de decisión de la norma §4 (norma/01-seleccion.md):
     significado → categoría → símbolo reconocido → Lucide → conflictos → texto → accesibilidad → registro.
     Lo que Uva decide sin confirmación del usuario se marca «(supuesto)» en la línea del campo al que afecta y se copia
     al campo `supuestos` de la propuesta; si es de categoría (objeto frente a estado o proceso), indica qué movimiento
     tendría la otra lectura. Borra estos comentarios al rellenar. -->

- **Nombre semántico y categoría (§2.1, §3):** `semanticName` en inglés y kebab-case (`delete`, `syncing`) · categoría de la taxonomía: decorative, action, navigation, informative, status, toggle, disclosure, directional, object o brand. <!-- Brand: no se dibuja, se usa el logotipo del tercero. El semanticName es también el id (archivo <semanticName>.svg, clase uva-<semanticName>): se nombra por lo que significa, no por el objeto que dibuja (§2.4). Si la categoría es object, el semanticName es el nombre genérico del objeto en su función (bulk-container, no la marca ni el modelo). -->
- **¿Ya existe? (§2.2, §4.3–4.4):** términos buscados con `buscar-lucide.mjs` (concepto, sinónimos, significado) → resultado. <!-- Si un icono de Lucide representa bien el significado, ese es el resultado: la propuesta lo recomienda y Uva solo dibuja si el usuario lo pide o si ninguno sirve. Los parciales entran en E2 como variante de referencia (el más cercano; uno descartado en una ronda anterior se cita, no se repite). -->
- **Consistencia (§2.4–2.5):** ¿el significado ya tiene otro icono en el producto? ¿este símbolo ya significa otra cosa?
- **Vocabulario del dominio:** qué significa ya cada objeto candidato en este oficio o producto. <!-- buscar-lucide no lo sabe: sale del perfil, del registro, de lo que dijo el usuario o del conocimiento del oficio. Si no está verificado, es un supuesto. -->
- **Concepto y significado:** objeto («reloj de arena») ≠ significado en la interfaz («pendiente: en espera»). <!-- NN/g: reconocer la forma ≠ interpretar el significado. Para un concepto abstracto, lista 2–3 metáforas (1–2 objetos reconocibles + un modificador): serán variantes en E2. -->
- **Uso:** tamaño real (16/20/24px) · dónde aparece · iconos vecinos · ¿lleva etiqueta de texto? · nombre accesible. <!-- Salvo casa, imprimir y lupa, ningún icono es universal. Con etiqueta o dentro de un botón → icono oculto (nombre en el botón); solo y con significado esencial → nombre accesible. El nombre describe el propósito, no el dibujo («Buscar», no «icono de lupa»; §15) y contiene el texto visible si lo hay (§18). Si va en botón solo con icono: área 44×44 (§11–12). -->
- **Estilo:** fuente del ADN (tokens → librería del perfil → base de Uva) y grosor de la familia.
- **Rasgos distintivos:** silueta y proporción medidas en la referencia (R1) · 2–3 rasgos que lo hacen este objeto · qué se descarta · vista más legible.
- **Confusiones del dominio:** al menos 2, por silueta y por metáfora (R2, R5) <!-- busca también con los términos de la metáfora; el banco muestra hasta 4 a la vez; las que aparezcan al renderizar se añaden aquí. -->
- **Criterio de éxito:** qué debe pasar en el banco para darlo por bueno.
