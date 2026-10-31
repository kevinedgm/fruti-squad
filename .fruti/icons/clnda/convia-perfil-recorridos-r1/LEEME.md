# Convia · perfil de recorridos r1

Patrón aprobado del hotel r2 con el color de recorridos. Pedido del usuario (2026-10-31): fotos de los lugares del tour, desde cuántas personas, precio, los lugares.

## Idea central
- El negocio es el **operador**; ofrece varios recorridos. Pestañas: Recorridos · Fotos · Nosotros · ¿Volverían? · Contacto.
- Lista compacta de recorridos (miniatura, tipo, duración, dificultad, próxima salida, «desde»). Al tocar uno se abre una **hoja** (de abajo en celular; panel lateral en escritorio):
  1. fotos en tira y «X de cada 10 volverían» de ese recorrido;
  2. **la ruta**: paradas numeradas con miniatura;
  3. **¿Cuántos van?**: contador − / + que calcula precio por persona y total con la tabla de precios por tamaño de grupo; mínimo para que salga y máximo;
  4. **próximas salidas** con lugares que quedan (el contador no deja pasar del cupo);
  5. incluye / no incluye; punto de encuentro;
  6. botón fijo «Apartar N · $total» y vista previa del mensaje de WhatsApp que se enviará (con «Lo vi en Convia», que mide de dónde llegan).
- Boleto: próxima salida · desde · tamaño de grupo.

## Datos
- Operador, guías, precios, fechas y contactos ficticios; paradas = lugares públicos de Oaxaca; fotos de relleno desenfocadas, fuera del repo.
- Accesibilidad: el «punto» de recorridos (#1baf7a) da 2.58:1 sobre papel, así que la métrica usa el color de texto del giro (#11704e). «¡quedan N!» en #7f3313 (7.07:1 sobre el verde claro).
- Publicado: https://claude.ai/artifact/5SJK5By7AyzoAjE7g6zJuf. Uso: `python3 gen.py <carpeta con img/>`.
