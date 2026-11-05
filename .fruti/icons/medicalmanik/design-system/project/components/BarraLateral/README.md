# BarraLateral

Barra lateral de módulos y submódulos. Aprobada 2026-11-05.

- **Medidas:** `sidebar-width` 264 px, fondo «surface», borde derecho «line», relleno 12 px. Módulo: fila de 44 px, icono Lucide de 20 px en «muted», texto 15 px.
- **Submódulos:** el módulo que los tiene es un `<button aria-expanded aria-controls>` con flecha (no un enlace); sus submódulos cuelgan de una línea guía de 1.5 px «line», sin icono, en filas de 40 px y texto «muted». Solo se abre el grupo de la página actual; los demás, cuando la persona los abre. Dos niveles como máximo.
- **Dónde estoy:** la página actual en «manik-soft», texto «manik» 600 y `aria-current="page"`; su módulo padre en 600 con el icono en «manik».
- **Pendientes:** contador en píldora «manik-soft» con texto «manik» y `aria-label` («3 pendientes»). Un grupo cerrado muestra la suma de sus submódulos.
- **Pie de la barra:** Ayuda y «Plegar menú».
- **Riel** (`rail-width`, 72 px): solo iconos; el nombre aparece en una etiqueta flotante al pasar o enfocar; los pendientes, como punto. Un módulo con submódulos abre un menú flotante (`shadow-pop`) con su título y sus submódulos; Esc lo cierra y devuelve el foco. La preferencia de riel se recuerda por persona.
- **Tableta y celular:** la misma barra, como cajón de 300 px (ver AppShell).
