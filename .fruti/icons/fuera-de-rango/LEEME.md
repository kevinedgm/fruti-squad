# Uva · indicador único «fuera de rango» (captura de signos vitales, Expediente Manik) · r1

Pedido del usuario (2026-10-31): **un solo icono indicador** que diga «fuera de rango» (alto o bajo) y se adapte a todos los signos (temperatura, tensión arterial, FC, FR, SpO₂…), con el color controlado por CSS; no un icono por signo. Reemplaza el enfoque de `../signos-vitales/` (un glifo por signo), que queda como antecedente.

Revisión: `revision.html` (publicada) · `python3 gen.py` → `variantes/out-of-range-<v>.svg`.

## Contrato
- semanticName `out-of-range`. Un archivo; piezas por estado ocultas; el contenedor pone `--uva-alto:1`, `--uva-bajo:1` o `--uva-normal:1` y el color con `--uva-accent` (alto = error, bajo = info, normal = éxito). Sin clase: icono neutro (sin lectura).
- Las variables heredan por `<use>`; como `<img>` no funciona. Opacidades con `var()` y `calc(1 - var())` para abrir la línea que cruza la flecha (variante A).
- Trazo 2 (Lucide de las apps Manik). Qué signo es lo dice la etiqueta del campo.

## Variantes (check-icon 3/3 sin fallos bloqueantes)
- **A · Banda con flecha que sale** [recomendada]: dos líneas = rango; la flecha la atraviesa hacia arriba o abajo y la línea cruzada se abre. Riesgo: sin estado y a 16 px parece «=».
- B · Medidor de aguja: izquierda/derecha se lee más lento que arriba/abajo; parece velocímetro.
- C · Escala con punto fuera: claro de cerca; a 16 px parece reloj o anillo.

## Pendiente
Elección · ¿se retiran `heart-rate-high`, `blood-pressure-high`, `glucose-high` (trazo 1.5, por signo, animados) dentro de Manik? · umbrales por signo (área médica) · registro semántico (Lima).
