# Ecosistema Manik · IA · ronda 3 (movimiento con significado)

Pedido del usuario (2026-10-31): le gustan las animaciones 4 (órbita), 5 (respiración) y 6 (trazo) de la ronda 2; «trabajemos sobre» (mensaje cortado; interpretado: desarrollar esas tres).

Publicado: https://claude.ai/artifact/Hnb9NJKfCua7sBinsiKTEt

## Propuesta: cada movimiento dice algo distinto
| Movimiento | Significado | Cuándo | Veces | Duración | Texto del botón |
|---|---|---|---|---|---|
| 5 · Respiración | «Te invito» | cursor o foco sobre «IA» | 1 | 1.6 s | IA |
| 4 · Órbita | «Estoy analizando» | signos vitales, CIE-10, contraindicaciones, resumen | bucle | 1.8 s/vuelta | Analizando… |
| 6 · Trazo | «Estoy redactando» | padecimiento actual, sugerencias de cuidado | bucle | 2 s | Redactando… |
| 6 · Trazo (una vez) | «Llegó algo nuevo» | destello del sello «Sugerido por IA» al aparecer | 1 | 1.4 s | — |

Cada acción del menú declara su tipo (analiza o redacta). El borrador del padecimiento se escribe palabra por palabra y queda editable.

## Accesibilidad
Texto del botón cambia con el estado; `aria-busy` y región viva («Analizando…», «Listo: …»); el resultado recibe el foco; `prefers-reduced-motion` apaga todo y muestra el texto completo de inmediato. Ninguna animación en bucle en reposo.

## Datos de ejemplo
Paciente ficticia. Códigos CIE-10 reales usados como ejemplo (J02.9, J03.9, R50.9); cada uno muestra «Por:» con el dato que lo sustenta. [supuesto: CIE-10, pendiente confirmar]

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; flujo completo con teclado y ratón (respira, analiza, redacta, acepta, descarta); controles ≥ 20 px (casillas 20 px; botones 44 px).

**Aprobado por el usuario (2026-10-31): la regla «respira, orbita, traza».**

[pendiente: diálogo de revisión por función; tokens `ia`, `ia-hover`, `ia-destello` a materializar en `design-system/project/tokens.json`]
