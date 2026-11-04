# Brief funcional · Promociones de Impulsa en el directorio · r01

**Ruta:** R1 · **Fidelidad:** F2 (kit neutral) · **Fecha:** 2026-11-04
**Fuentes:** pedido del usuario; artifact «Ecosistema Manik» (README: Impulsa = campañas de prevención y marketing; color `app-impulsa` #504CA1 solo identidad de app); DS directorio · componente Anuncio.

**Enunciado:** quien busca médico necesita ver promociones relevantes sin confundirlas con resultados, porque una promoción puede ahorrarle dinero o recordarle prevenir, pero no es una recomendación de Manik.
**Pregunta de diseño:** ¿cómo intercalar una promoción con imagen en los resultados sin que se lea como un médico recomendado, y qué necesita su página para decidir?
**Verbo principal (paciente):** ver la promoción y aprovecharla (agendar o llamar). **Resultado verificable:** llega a la página de la promoción y de ahí a agendar con quien la ofrece.

## Hechos
- Las promociones vienen de Impulsa Manik: imagen de banner + título; al tocar, página con más detalle (usuario).
- El componente Anuncio del DS ya fija: «Patrocinado» primero y siempre visible; ancho completo de la lista; nunca imita una ficha.

## Inferencias / reglas propuestas
- Al paciente no se le nombra «Impulsa» (herramienta interna para clínicas): se dice «Patrocinado» + nombre del anunciante.
- No se usa el violeta de Impulsa en el directorio: en el ecosistema el color de producto identifica la app, no el contenido.
- Intercalado: nunca en la 1.ª posición; después del 2.º resultado; máximo 1 cada 5 resultados; nunca 2 seguidas; solo promociones de la especialidad o zona buscada.
- La imagen se recorta a una proporción fija (para que la lista no salte); el título va como texto real, no dentro de la imagen.
- Si el anunciante está en el directorio, la página lleva a su perfil y a agendar con él; si no, a llamar.

## Incógnitas
1. **Formato del banner que genera Impulsa** (proporción y tamaño; ¿trae texto dentro de la imagen?). Decide el recorte.
2. ¿Qué datos trae la promoción además de imagen y título? (precio, vigencia, condiciones, anunciante, destino).
3. Publicidad de servicios de salud en México: verificar con el área legal si debe mostrarse un número de aviso o permiso de publicidad (COFEPRIS) en la tarjeta o en la página. [No verificado.]
4. ¿Una promoción puede venir de alguien fuera del directorio (laboratorio, farmacia)?

## Estados
Resultados con promoción · Página de la promoción (anunciante en el directorio) · Anunciante fuera del directorio · Sin imagen · Promoción vencida · Carga.
