# Uva · indicador único «fuera de rango» · r2 (más simple)

Pedido del usuario (2026-10-31): no le gustó ninguna de r1 (`../fuera-de-rango/`: banda con flecha, medidor, escala con punto); «algo menos complejo, algo más simple».

Revisión: `revision.html` (publicada) · `python3 gen.py`. Mismo contrato que r1: un SVG `out-of-range`, estado con `--uva-alto/--uva-bajo/--uva-normal:1`, color con `--uva-accent`, trazo 2.

## Variantes (check-icon 4/4 sin fallos bloqueantes)
- A · Flecha (↑ / ↓; guion en rango): la convención de reportes de laboratorio. Riesgo: flecha = «subir/bajar» o «ordenar».
- **B · Triángulo relleno** (▲ / ▼; punto en rango) [recomendada]: convención de monitores; es la forma con más peso a 12–16 px y el color se ve completo.
- C · Chevrón (^ / v; guion): el más discreto; se confunde con «desplegar».
- D · Flecha en círculo (con fondo suave del color): se lee como señal; el círculo queda visible sin estado.

Sin estado, A, B y C no muestran nada (sin lectura = sin indicador).

## Pendiente
Elección · ¿retirar `heart-rate-high`, `blood-pressure-high`, `glucose-high` dentro de Manik? · registro semántico (Lima).
