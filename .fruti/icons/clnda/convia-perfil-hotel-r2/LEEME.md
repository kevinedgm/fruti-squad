# Convia · perfil de hotel r2

Comentarios del usuario sobre r1 (2026-10-31): no copiar la estructura de Facebook; diseño propio con el tema del giro (azul hoteles) y el logo «Convia | Hoteles»; portada en mosaico; habitaciones sin tarjetas gigantes (miniaturas); casi todos lo verán en el teléfono, todo al alcance del dedo.

## Decisiones r2
- **Tema del giro**: todo el acento usa `categorias.hoteles` de `tema.json` (texto #2260ab, fondo #dae4ec, punto #2a78d6). Logo `convia-final/sellos/hoteles-logotipo-giro.svg` (generado con `logos-giro.cjs`, existe para los 6 giros). El pie conserva el logo base de Convia.
- **Portada en mosaico**: celular 1 grande + 2 (la última con «+N fotos»); escritorio 1 grande + 4.
- **Ficha tipo llavero** encima del mosaico: muesca arriba, sello del giro, nombre, «desde», volverían, Favorito, rasgos «revisado por Convia», Quiero ir / ¿Ya fuiste?
- **Boleto** de horarios: llegada · salida · recepción.
- **Pestañas abajo en el celular** (Cuartos · Fotos · El hotel · ¿Volverían? · Llegar) + botón flotante «Reservar por WhatsApp». En escritorio las pestañas van arriba del contenido y el contacto en columna lateral fija.
- **Cuartos en lista compacta**: miniatura 64 px, nombre, capacidad, precio; se despliega con fotos en tira, detalles y «Preguntar por esta habitación».
- Fotos con filtros (Habitaciones, Áreas comunes, Desayuno y terraza); visor con deslizar y flechas.
- Mismos datos ficticios y reglas que r1 (fotos de relleno desenfocadas fuera del repo; contactos inertes).
- Publicado: https://claude.ai/artifact/Q39D6bxh733WB2cVWFPKWF. Uso: `python3 gen.py <carpeta con img/>`.
