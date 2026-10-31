# Convia · perfil de taller r1

Patrón aprobado (hotel r2) + hoja de fechas y cupo de recorridos r1 (aprobado), con el color de talleres.

## Lo propio del taller
- El negocio es el **estudio**; pestañas: Talleres · **Piezas** (hechas por alumnos) · **Maestros** · ¿Volverían? · Contacto.
- Lista compacta de talleres (nivel, duración, edad mínima, próxima fecha, precio).
- Hoja por taller:
  1. maestro que lo da y «volverían» de ese taller (o «Taller nuevo · aún sin número» si tiene menos de 10 asistentes);
  2. **Te llevas** destacado (la pieza y cuándo se recoge);
  3. **Qué vas a hacer**: pasos numerados con miniatura;
  4. **¿Cuántos lugares?**: empieza en 1 (se aparta por persona), tope = lugares que quedan en esa fecha; precio fijo por persona, materiales incluidos; mínimo para confirmar y cupo;
  5. próximas fechas con «¡queda 1!» / «¡quedan 2!»;
  6. incluye / no incluye / **qué llevar**; dónde es;
  7. mensaje de WhatsApp prellenado con «Lo vi en Convia».
- Rasgo «Para ir solo» en la ficha (enlaza con la intención «Un taller para ir solo» del directorio).

## Datos
- Estudio ficticio (el «Taller Barro Vivo» del directorio): maestros, precios, fechas y contactos inventados; fotos de relleno desenfocadas, fuera del repo.
- Publicado: https://claude.ai/artifact/5WRkf4WB9J64pmTM1JWMRK. Uso: `python3 gen.py <carpeta con img/>`.
