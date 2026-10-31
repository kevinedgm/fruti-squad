# Convia · demo interna r12 (portada con el logo doodle)

El usuario aprobó el hero r3 («se ve espectacular») y pidió integrarlo con el directorio. r12 = r11 + esa portada.

- **Portada**: logo de Convia al centro como doodle de temporada → frase de temporada (+ «Edición … · Agenda de … ›», abre la Agenda) → buscador grande → **sellos** (A dónde ir esta semana · Un café nuevo · Dónde comer hoy · Un taller para ir solo · Dónde dormir), con la misma lógica que las intenciones de antes → «Esta semana: N actividades · N exposiciones en curso · Ver agenda» (calculado de la agenda) → crédito del doodle.
- **Encabezado**: con el hero a la vista solo muestra Avisos y Mis lugares; al bajar (o en un perfil) aparecen el logo chico y el buscador. Los dos buscadores comparten lo escrito. Las pestañas se pegan justo debajo del encabezado aunque cambie de alto (se mide con ResizeObserver).
- **Va bien para** baja a una franja bajo el hero.
- **Búsqueda sin acentos ni mayúsculas** («cafe» = «Café»; antes no encontraba nada sin acento).
- Temporadas por fecha (Muertos, Guelaguetza, Noche de Rábanos); selector «temporada» en la barra de la demo.
- **Prototipo navegable** (pedido del usuario): cualquier tarjeta abre la página completa de su giro (café, restaurante, hotel, museo), aunque se repita para todos los del giro; cada actividad de la agenda y cada organizador abre la de su tipo (taller, recorrido, organizador o el lugar que organiza). Abren en pestaña nueva. En los 7 perfiles, «‹ Directorio» y el logo regresan a esta página.
- Lo demás igual que r11 (agenda, seguir, avisos, perfiles enlazados).
- Verificado en 1440, 820 y 390 px: sin desborde ni errores; encabezado y pestañas sin hueco; sellos llevan a su giro o a la Agenda.
- Publicada: https://claude.ai/artifact/HwDGhej6gr118my78mG6iT. Uso: `python3 gen.py <carpeta con img/>`.
