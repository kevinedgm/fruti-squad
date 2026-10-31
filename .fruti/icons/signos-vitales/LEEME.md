# Uva · indicadores de signos vitales (captura de signos, Expediente Manik) · r1

Pedido del usuario (2026-10-31): icono para el sistema de medición de la captura de signos vitales que alerte cuando un signo está alto o muy bajo (temperatura, tensión arterial, frecuencia cardiaca, frecuencia respiratoria, SpO₂…; el mensaje se cortó tras «SpO2,»). El color del indicador se manipula con CSS: debe ser SVG.

Revisión: `revision.html` (publicada) · `python3 gen.py` → `variantes/<id>-<estilo>.svg`.

## Decisión de estructura [propuesta]
- **Un SVG por signo** (5, no 15): glifo + piezas `__alto`, `__bajo` (y `__normal`, `__riel` en el estilo C) ocultas por defecto.
- El contenedor elige el estado con variables (heredan por `<use>`, cumplen la regla de una clase por selector): `--uva-alto:1`, `--uva-bajo:1`, `--uva-normal:1`; color con `--uva-accent` (alto = error, bajo = info, normal = éxito del sistema).
- Trazo 2 (Lucide de las apps Manik). **Choque:** los iconos previos `../heart-rate-high`, `../blood-pressure-high`, `../glucose-high` usan trazo 1.5, solo «alto» y animación; dentro de Manik estos nuevos los sustituirían [por confirmar].

## Glifos
Temperatura: termómetro · Presión: manómetro (baumanómetro aneroide) · FC: corazón · FR: pulmones · SpO₂: oxímetro en el dedo (no gota: la gota ya es glucosa). Corregido en el banco: pulmones que se leían «db» y SpO₂ que parecía cactus. Riesgo vigente: el oxímetro a 16 px puede parecer llave o enchufe; el manómetro, reloj o velocímetro (mitiga el texto).

## Estilos de indicador (check-icon: 15/15 sin fallos bloqueantes)
- **A · Flecha** [recomendado]: la lectura más directa de alto/bajo.
- B · Triángulo relleno: más peso, pero se confunde con reproducir/desplegar.
- C · Nivel (riel + punto): muestra también «normal», pero el riel casi no se ve a 16 px.

## Reglas
SVG en línea o `<use>` (como `<img>` no recibe variables) · siempre con texto («38.9 °C · Alta») · quieto (estado de toda la consulta) · los umbrales los define el área médica.

## Pendiente
Elección del estilo · ¿faltan signos? (glucosa capilar, peso/IMC, dolor) · ¿sustituir los tres iconos anteriores? · registro semántico (Lima).
