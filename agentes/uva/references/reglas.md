# Reglas de Uva (R1–R7) y trampas técnicas

Principios de dibujo y evaluación. Cada uno se formula como **regla → mecanismo → cómo comprobarlo**, con ejemplos genéricos. Los casos concretos de los que salieron están en `examples/casos.md` (no se cargan durante un encargo: describen soluciones de otros iconos y sesgarían el diseño).

## R1 · La proporción distingue antes que el detalle

- **Regla:** la silueta (relación ancho/alto, hacia dónde se estrecha o se abre, si está abierta o cerrada) es lo primero que se lee; el detalle interior apenas se percibe a 24px.
- **Mide la referencia, no el estereotipo:** toma la proporción y la dirección del contorno de la **referencia real** (foto o descripción), no de la forma típica del objeto. Si la proporción real coincide con la de otro icono, el desempate lo da R5, no deformar la silueta.
- **Comprobar:** tapa el detalle interior; ¿la silueta sola ya separa el objeto de su confusión principal?

## R2 · Probar contra las confusiones, no solo contra vecinos al azar

- **Regla:** un icono puede encajar con la familia y aun así significar otra cosa. Declara en E1 al menos 2 confusiones y pruébalas a 20–24px junto a tu icono; añade las que aparezcan al renderizar (el banco muestra hasta 4 a la vez).
- **Busca confusiones de dos tipos:**
  - **por silueta:** iconos con un contorno parecido (cilindros, botellas, cajas, cuencos…);
  - **por metáfora:** iconos que usan la misma idea visual (p. ej. "recipiente + algo que sale de él", "objeto + flecha"). Búscalos con `buscar-lucide.mjs` usando los términos de la metáfora, no solo los del objeto.
- **Comprobar:** en el banco, fila de familia y contexto oscuro: ¿alguna confusión se lee igual que tu icono?

## R3 · Líneas cruzadas forman trama

- **Regla:** verticales y horizontales que se cruzan se leen como tejido, rejilla, tabla o calendario; varias paralelas cercanas, como cesta o pila.
- **Comprobar:** si hay cruces o 3+ paralelas, ¿el resultado evoca canasta, rejilla o pila de discos?

## R4 · El movimiento necesita espacio reservado

- **Regla:** lo que se anima detrás o encima de un trazo queda tapado y no se percibe. Reserva la zona libre **antes** de dibujar el resto.
- **Comprobar:** en el fotograma intermedio (`banco.html#medio`), ¿la pieza móvil está sobre área libre?

## R5 · Una forma correcta puede coincidir con otro icono: el contexto desempata

- **Regla:** formas simples ya tienen significado en interfaces. Si la silueta fiel coincide con otro icono del dominio, no la deformes: añade un **modificador de contexto** (lo que sale del objeto, lo que lo acompaña, un rasgo de construcción propio) que la otra forma no tiene.
- **Comprobar:** con el modificador, ¿la confusión deja de leerse igual? ¿El modificador refuerza el significado (B2) en vez de añadir ruido?

## R6 · Igualar peso óptico, no tamaño de caja

- **Regla:** el ojo compara masa visual. Un objeto bajo o que deja aire para el movimiento se ve más pequeño que uno que llena la caja.
- **Comprobar:** junto a un icono que llene bien la cuadrícula (la mano del banco). Si se ve menor, escala el cuerpo usando la franja entre 1 y 2 unidades del borde: el mínimo de A2 (≥1) **nunca** se cruza; el margen recomendado de 2 sí puede ceder para igualar peso.

## R7 · Objetos compuestos: menos detalle a tamaño pequeño

- **Regla:** dos objetos lado a lado en 24 unidades tienen la mitad del espacio cada uno; el detalle repetido (vueltas, dientes, rayas) se vuelve mancha.
- **Comprobar:** a 20–24px, ¿cada parte se distingue? ¿Hay separación mínima (A6) entre partes?
- **Acción:** reduce las repeticiones o, si el icono también se usa grande, entrega `<id>.small.svg` para ≤24px. Solo cuando haga falta.

## Trampas técnicas

- **Selectores con descendencia:** reglas como `.contenedor .pieza{…}` no alcanzan el contenido clonado por `<use>` ni sobreviven a ciertos empaquetados. Cada pieza estilada lleva su propia clase con prefijo (`uva-<id>__pieza`) y cada regla usa **una sola clase**; los valores externos llegan por variables CSS (`--uva-accent`, `--uva-stroke`) y `currentColor`, que sí se heredan.
- **Especificidad en el bloque reducido:** si una pieza tiene reglas escalonadas con `:nth-of-type(…)`, el bloque `prefers-reduced-motion` debe igualar esa especificidad (`.uva-<id>__p,.uva-<id>__p:nth-of-type(n)`).
- **Rellenos y grosor:** al bajar el trazo, los puntos rellenos se vuelven pesados; escala su radio con el grosor.
- **Pares alineados se leen como ojos:** dos círculos a la misma altura dentro o sobre una forma redondeada forman una cara. Desalinéalos en diagonal o cambia sus tamaños.
- **Curvas repetidas apretadas:** espirales o vueltas curvas a 24px se enredan; un zigzag con uniones redondeadas suele leerse mejor.
