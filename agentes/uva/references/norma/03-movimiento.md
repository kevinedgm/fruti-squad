# Norma de Uva · movimiento

> Parte de la *Guía y estándar de iconografía accesible* v1.0 (secciones §27–34). Índice y notas: `README.md` de esta carpeta. Se carga en E4 (y `references/movimiento.md` da los patrones CSS).

## 27. Animación de iconos

La animación debe utilizarse con intención. Un icono puede animarse para comunicar: cambio de estado; feedback; progreso; causalidad; transición; atención temporal. No debe animarse simplemente para hacer la interfaz más llamativa.

---

## 28. Categorías de motion

- **State transition.** Ejemplo: `ChevronDown → ChevronUp`. Puede utilizar rotación.
- **Feedback.** Ejemplo: `Save → Check`. Comunica que una acción terminó.
- **Progress.** Ejemplo: `LoaderCircle`. Indica procesamiento real.
- **Attention.** Ejemplo: `Bell`. Debe utilizarse con extrema moderación.
- **Decorative motion.** Ejemplo: `Sparkles`, bounce, floating. Debe evitarse por defecto.

---

## 29. Motion tokens

| Token | Duración | Uso |
|---|---|---|
| motion.instant | 0–80 ms | cambio inmediato |
| motion.fast | 100–160 ms | feedback |
| motion.base | 160–240 ms | transición |
| motion.slow | 240–400 ms | cambio espacial |
| motion.loop | variable | progreso real |

Estos rangos son una decisión del Design System, no requisitos WCAG.

---

## 30. Principios de movimiento

Una animación debería ser: purposeful; brief; predictable; reversible; interruptible; non-blocking.

Evitar: excessive bounce; large zoom; continuous shake; parallax innecesario; oscillation; multiple simultaneous motions.

---

## 31. Reduced Motion

Debe respetarse:

```css
@media (prefers-reduced-motion: reduce) {
    .icon-motion {
        animation: none;
        transition: none;
    }
}
```

Importante: reduced motion no significa reproducir exactamente la misma animación más lentamente. En algunos casos eso puede incluso prolongar la exposición al movimiento.

Preferir `movement ↓ instant state change` o `movement ↓ subtle opacity change`, siempre conservando la información.

---

## 32. Animación iniciada por interacción

WCAG 2.3.3 aborda animaciones disparadas por interacción. Cuando el movimiento no sea esencial debe existir una forma de evitarlo o respetarse la preferencia correspondiente.

Ejemplos: expand, collapse, open, close, switch, navigation transition — deben disponer de una variante reducida cuando utilicen movimiento significativo.

---

## 33. Animaciones automáticas

WCAG 2.2.2 aborda contenido que: comienza automáticamente; contiene movimiento; dura más de cinco segundos; aparece junto a otro contenido. Cuando aplica, debe poder: pause, stop, hide — salvo que sea esencial.

Política recomendada: no utilizar loops decorativos automáticos persistentes.

---

## 34. Flashing

No utilizar flashing para llamar la atención. Especialmente evitar: rapid brightness changes; alternating high contrast; strobe effects; rapid blinking.

WCAG contiene criterios específicos destinados a reducir el riesgo de conv… *(texto recibido incompleto a partir de aquí)*
