# Aprobación · Promociones de Impulsa · r02

- **Aprobado por el usuario:** 2026-11-04 («apruebo las promociones, pásalas al prototipo»).
- **Congelado:** tarjeta en la lista (banner 357:104 como en Impulsa, «Patrocinado» primero, título como texto, anunciante · vigencia; ancho completo, borde punteado, sin «Agendar»); posición después del 2.º resultado, máx. 1 cada 5, nunca 2 seguidas, solo de la especialidad o zona; sin imagen = solo texto; si falla, la lista sale sin ella. Página: banner 16:9 completo, título, descripción, precio con precio normal, vigencia, lugar, condiciones, anunciante con cédulas, «Agendar con esta promoción» (o «Llamar» si está fuera del directorio), aviso legal al pie.
- **Implementado en:** DS v11 (componente Anuncio → promoción patrocinada) y prototipo v13 (`#promo-<id>`; promociones de ejemplo en «Piel» y «Niñas y niños»).

## Decisiones de implementación
- «Agendar con esta promoción» abre el perfil del anunciante en «Agenda tu cita», con el aviso «Promoción … se aplica al agendar aquí»; el precio con promoción llega a «Confirma tu cita», «Cita confirmada» y «Detalle de su cita».
- Cada promoción tiene su propio precio normal (la de hepatitis incluye la vacuna: normal $1,500, no el precio de la consulta).
- La promoción deja de aplicarse al volver al inicio o a los resultados.

## Enmienda 2026-11-04 · mostrar Impulsa Manik (decisión del usuario)
- Objetivo: que los médicos se pregunten qué es Impulsa y sepan que es parte del ecosistema Manik (no que el paciente confíe en la promoción).
- Lista: la línea del anunciante termina en «con Impulsa Manik» (solo texto; el ecosistema fija 24 px mínimo para sellos). «Patrocinado» sigue primero.
- Página: al pie, sello oficial de Impulsa (`impulsa.svg` del DS Ecosistema Manik, copiado en `directorio-ds/ecosistema/sello-impulsa.svg`, 32 px) + «Promoción publicada con Impulsa Manik, la herramienta de campañas del ecosistema Manik» + «¿Eres médico? Conoce Impulsa».
- El violeta de Impulsa solo dentro de su sello. Implementado: DS v12, prototipo v14.
- Pendiente: el destino de «Conoce Impulsa» (página para médicos).

## Sin resolver
- Aviso o permiso de publicidad en salud (COFEPRIS): no verificado.
- Anunciantes fuera del directorio; estado «promoción vencida» solo en el wireframe.
