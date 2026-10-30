# Mesanda · boceto en grises, ronda 1 (F2, clicable)

Ruta R1 · fidelidad F2: estructura, flujo y conteo de toques, sin marca. `index.html` (clicable), capturas `plano.png`, `orden.png`, `cuenta.png`. Kit de wireframe de la skill no disponible en este entorno: grises propios, una tipografía del sistema.

## Pantallas
1. **Plano** (modo servicio): mesas con estado (libre punteada, reservada con hora, ocupada con comensales y tiempo, cuenta pedida con «!»), zonas en pestañas, panel «Te necesitan».
2. **Orden**: comensales a la izquierda (+ «Mesa (compartido)» y «+ Comensal»), categorías, platillos en foto, ticket agrupado por comensal, notas rápidas en el último platillo agregado («+ Nota» en los demás), «Enviar a cocina (n)» y «Pedir cuenta».
3. **Cuenta**: una sola o por comensal, propina, forma de pago (efectivo, tarjeta, cargar a habitación), «Cobrar y liberar mesa».

## Evidencia
Prueba automática (1280 y 390 px, sin errores ni desbordes): mesa libre → 2 comensales → 3 platillos en dos comensales y dos categorías → 1 nota → enviar = **9 toques**.

## Hallazgos para la ronda 2
- Las notas deben depender del platillo (en el boceto «Sin cebolla» aparece en una limonada): modificadores configurados en el menú.
- «Por comensal»: decidir si cobra a cada persona o solo muestra la división.
- Pendientes del brief: cambiar y juntar mesas, cancelar platillo enviado, cocina en pantalla o impresora, «Cargar a habitación» solo con CLNDA Booking.
