# Evaluaciones de Fruti Squad

Propósito: medir si un cambio al squad (una regla nueva en un AGENT.md, un contrato de runtime, cambiar cómo se ejecuta una etapa) mejora o empeora el resultado, en lugar de juzgarlo a ojo con una sola corrida.

Idea tomada de "Building agents: when to fold subagents into your main agent loop" (Anthropic): un conjunto pequeño y fijo de tareas de punta a punta con rúbrica, cada tarea corrida más de una vez, y **un cambio a la vez**; se conserva solo lo que no rompe ningún caso.

## Relación con `fruti test`

`fruti test` ya es la prueba de aceptación de una petición: crea una ronda `.fruti/tests/rNN/` y exige un veredicto por dimensión. Lo que faltaba es **repetir las mismas peticiones** para comparar versiones. Por eso cada caso de `evals/casos/` se lanza con:

```bash
fruti test --case evals/casos/03-tabla-de-cuentas.md
```

La ronda queda marcada con `case: 03-tabla-de-cuentas` en su `request.md`, y así se comparan rondas del mismo caso.

## Cómo se corre

1. En un proyecto de prueba con Fruti Squad instalado, lanza el caso con `fruti test --case …` y pide al agente que ejecute la ronda completa (Kiwi → Lima → Coco → Bruno → Coco → Lima → Mora).
2. **Corre cada caso dos veces** (dos rondas). Solo cuenta como pasa lo que pasa en las dos.
3. Califica con una conversación nueva: "Califica `.fruti/tests/rNN/` con `evals/casos/NN-….md`; para cada casilla di cumple / no cumple con evidencia (archivo y regla)". Además de las casillas, vale el `result.md` de la ronda.
4. Anota en `evals/resultados.md`: fecha, versión, qué cambió, caso, ronda 1, ronda 2.

## Cómo se compara un cambio

- Corre todos los casos antes y después.
- Compara **caso por caso**: un total igual puede esconder un caso que se rompió y otro que se arregló.
- Si algún caso empeora, el cambio se ajusta o se deshace antes de probar otro.

## Partes de cada caso

| Parte | Qué comprueba |
|---|---|
| Ruta | Qué agentes deben actuar y cuáles no (por ejemplo, un cambio de token no pasa por Kiwi) |
| Debe | Las decisiones y evidencias que el caso exige |
| No debe | Invariantes de `AGENTS.md`: valores crudos fuera de tokens, F2 con color, PASS sin todas las dimensiones, Lima rediseñando F2, Preview que no es el componente verificado. Una sola marcada hace fallar el caso |
