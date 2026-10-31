# Convia · perfil de museo r1

Primer perfil sobre el **modelo aprobado perfil + actividad + sede** (`../convia-final/modelo-datos.md`). Patrón del hotel r2 + hoja de actividad de recorridos/talleres, con el color de museos.

## Estructura
- El museo es un perfil `lugar`. Acción principal: **Cómo llegar** (no se reserva la entrada).
- Boleto: estado de hoy · entrada · exposiciones en sala.
- Pestañas: **Actividades** · Colección · Visita · ¿Volverían? · Llegar.
- **Actividades** = todas las que el museo organiza **o** donde es sede, en tres grupos: **Ahora · Próximas · Pasadas**. Cada tarjeta dice el tipo, la fecha o el rango, «Organiza el museo» u «Organiza X · aquí en el museo», y el precio, o en las pasadas «N marcaron que fueron · X de cada 10 volverían».
- **Hoja de actividad**:
  - siempre: **Organiza** (con «Ver perfil» si es otro) y **Dónde**;
  - exposición: rango desde → hasta, incluida con la entrada;
  - taller con precio: te llevas, fechas con cupo, lugares × precio, mensaje de WhatsApp a quien organiza;
  - evento gratis: «Guardar en Mis lugares», sin apartar;
  - pasada: «Así fue» y botón a próximas.
- Colección (salas y fotos), Visita (entrada, horario, guardarropa, visitas guiadas, amenidades).

## Datos
- Museo, actividades, organizadores (Colectivo Hilo Largo, Ana P., ilustradora), cifras y contactos ficticios; fotos de relleno, fuera del repo. «Pinta tu timbre postal» es el ejemplo que dio el usuario.
- «Marcaron que fueron» = personas que registraron «Ya fui» en Convia [propuesta: el organizador puede declarar además su asistencia].
- Publicado: https://claude.ai/artifact/VLXvEMM7XVw6T5MbYVhG5u. Uso: `python3 gen.py <carpeta con img/>`.
