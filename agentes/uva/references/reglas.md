# Reglas de Uva (R1–R7) y trampas técnicas

Cada regla salió de un fallo real observado en el banco de prueba, no de una suposición. Formato: **regla → mecanismo → cómo comprobarlo → caso que la originó.**

## R1 · La proporción distingue antes que el detalle

- **Mecanismo:** a 24px el ojo lee primero la silueta (relación ancho/alto y hacia dónde se estrecha); el detalle interior apenas se percibe.
- **Comprobar:** tapa el detalle interior; ¿la silueta sola ya separa el objeto de su confusión principal?
- **Caso:** tina v1 (alta, abierta arriba, con aros) se leía como *bote de basura*. Agregar duelas no lo resolvió; hacerla **ancha y baja** sí. Con la foto real se corrigió otra vez: la tina **no se abre hacia arriba** (eso la hacía *cubeta*); sus paredes son casi rectas.

## R2 · Probar contra las confusiones, no solo contra vecinos al azar

- **Mecanismo:** un icono puede encajar con la familia y aun así significar otra cosa.
- **Comprobar:** en el banco, coloca 2–3 iconos con los que podría confundirse (declarados en E1) a 24px junto al tuyo.
- **Caso:** sin el bote de basura al lado, la tina v1 "parecía bien".

## R3 · Líneas cruzadas forman trama

- **Mecanismo:** verticales + horizontales que se cruzan se leen como tejido o rejilla.
- **Comprobar:** si hay cruces, ¿el resultado evoca canasta, rejilla, tabla o calendario?
- **Caso:** tina B2 (aro + duelas verticales) se leyó como *canasta*; alambique con duelas, como *tambor/maceta*.

## R4 · El movimiento necesita espacio reservado

- **Mecanismo:** lo que se anima detrás o encima de un trazo queda tapado y no se percibe.
- **Comprobar:** en el fotograma intermedio de la animación, ¿la pieza móvil está sobre área libre?
- **Caso:** las burbujas de la tina v1 nacían dentro de la boca y desaparecían bajo el borde. Se rediseñó dejando el tercio superior libre.

## R5 · Una forma correcta puede coincidir con otro icono: el contexto desempata

- **Mecanismo:** formas geométricas simples (cilindro, botella, caja) ya tienen significado en interfaces.
- **Comprobar:** busca en el **mismo dominio** del producto qué iconos comparten la silueta.
- **Casos:**
  - Tina A3 (cilindro con aro, idéntica a la foto) = icono de *base de datos*. Lo resolvieron las **burbujas** (contexto), no más detalle.
  - Alambique con olla+columna unidas en contorno suave = *botella* (riesgo alto en un producto de mezcal). Lo resolvió un **hombro en escalón**, fiel a la foto; la botella se estrecha suavemente.

## R6 · Igualar peso óptico, no tamaño de caja

- **Mecanismo:** el ojo compara masa visual. Un objeto bajo que deja aire arriba se ve más pequeño que uno que llena la caja.
- **Comprobar:** pon el icono junto a uno que llene bien la cuadrícula (p. ej. una mano). Si se ve menor, escala el cuerpo hasta igualar, aunque invada ligeramente el margen.
- **Caso:** la tina (baja, con zona libre para burbujas) se veía más pequeña que la mano en el contexto oscuro estilo Claude.

## R7 · Objetos compuestos: menos detalle a tamaño pequeño

- **Mecanismo:** dos objetos lado a lado en 24 unidades tienen la mitad del espacio cada uno; el detalle se vuelve mancha.
- **Comprobar:** a 22–24px, ¿cada parte se distingue? ¿Hay al menos 2 unidades de separación entre partes?
- **Acción:** reduce detalle (p. ej. 2 vueltas de serpentín en vez de 3) o, si el icono también se usa grande, entrega `<id>.small.svg` para ≤24px. Solo para iconos que lo necesiten; uno simple (la tina) no.
- **Caso:** alambique con serpentín de 3 vueltas, denso a 22px; 2 vueltas se leen limpias.

## Trampas técnicas

- **`<use>` y selectores con ancestro:** `.uva-icon .acento{…}` no alcanza el contenido clonado por `<use>`; los rellenos del acento desaparecieron. Usa selectores sin ancestro externo y transmite valores con variables CSS (`--uva-accent`, `--uva-stroke`), que sí se heredan.
- **Rellenos y grosor:** al bajar el trazo de 2 a 1.5/1, los puntos (burbujas, gotas) se vuelven pesados. Escala su radio con el grosor.
- **Serpentín curvo:** las vueltas curvas se enredaron y chocaron con la olla; el zigzag con uniones redondeadas se lee mejor a 24px.
