# App Shell NisaLab · r01 (pendiente de aprobación)

`python3 gen.py` → `shell.html` (F3; color, tipografía, radios y sombras de `../nabi-design-system/tokens.json`). Ver `brief.md`.
Sidebar blanco 264 px (72 plegado; cajón de 300 con velo en celular): logotipo, accesos frecuentes, módulos con submódulos desplegables (aria-expanded), pendientes por submódulo, Ayuda y Plegar. Activo: fondo primary-soft, texto azul y filete pera (lo que está en curso).
Navbar blanca 64 px: menú, ruta, búsqueda (Ctrl K), avisos con conteo, aplicaciones Nisa, usuario (nombre, rol y área).
Footer: logotipo con respaldo, versión, estado del sistema, hora del servidor, soporte.
Comprobado: 4 vistas sin desbordes; 390 px sin desbordes; ningún control < 24 px; sin errores de JS; los submódulos abren y cierran.
Corregido antes de publicar: contenido del sidebar más ancho que su columna; texto de búsqueda en dos líneas; enlaces de ruta y soporte < 24 px; símbolo plegado diminuto por choque de la clase `s` con los enlaces de submódulo.
No comprobado: teclado completo en el cajón (trampa de foco), lector de pantalla.
