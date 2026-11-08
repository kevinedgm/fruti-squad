# Caracterizar antes de cambiar un componente existente

Cuándo se usa: en modo rediseño, o cuando Bruno va a modificar un componente que ya está en producción. Se hace **antes** de tocar el código.

Adaptado de *Working Effectively with Legacy Code* (Michael Feathers) vía wondelai/skills (`working-with-legacy-code`, MIT, © 2025 Wondel.ai).

## Para qué

Una prueba de caracterización registra lo que el componente **hace hoy**, no lo que debería hacer. No falla cuando el código está mal: falla cuando el comportamiento **cambia**. Sirve para dos cosas:

- comprobar que lo marcado `preserve` en `.fruti/redesign/scope.yaml` sigue igual después del cambio, en lugar de suponerlo;
- separar lo que cambiaste a propósito de lo que rompiste sin querer.

Ejemplo: el selector de cuentas actual borra el texto cuando la búsqueda falla. Nadie lo pidió, pero un formulario aguas abajo puede depender de eso. Si lo fijas con una prueba, el rediseño decide si se conserva o se corrige; si no, cambia sin que nadie lo vea.

## Receta

1. Ubica la región que vas a tocar: las ramas de comportamiento del componente que el contrato nuevo modifica.
2. Escribe una aserción que sabes que es falsa (por ejemplo, que tras un error el texto vale `"???"`).
3. Córrela. El mensaje de fallo te dice lo que el componente hace de verdad.
4. Cambia la aserción para esperar el valor observado y nombra la prueba con lo que aprendiste.
5. Repite hasta que cada comportamiento que vas a alterar tenga su prueba. Ahí te detienes.

## Qué fijar en un componente de interfaz

- Eventos que emite y con qué datos.
- Valor del `v-model` o del estado controlado tras cada acción.
- Qué pasa con el foco y el teclado (Tab, Enter, Escape, flechas).
- Lo que se anuncia con ARIA (roles, `aria-expanded`, regiones vivas).
- Bordes: vacío, texto muy largo, error, respuesta lenta, valor nulo.

No fijes clases CSS ni estilos: la apariencia es de Coco y va a cambiar.

## Cuando el comportamiento actual es un bug

No lo corrijas mientras caracterizas. Fíjalo tal cual, márcalo en la prueba como comportamiento observado y anótalo en el handoff como decisión devuelta:

- si el `scope.yaml` dice `preserve`, se conserva;
- si no, el bug va a **lima** (contrato) o a **kiwi** (estructura), que deciden si el rediseño lo corrige.

## Salida

En el handoff, `verified` lista las pruebas de caracterización que siguen en verde después del cambio, y `returned_decisions` los bugs encontrados. Si el proyecto no tiene cómo correr pruebas de componentes, se reporta **no verificado** y se anota en `pending`.
