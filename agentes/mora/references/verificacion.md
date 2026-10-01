# Verificación (detalle de los checks del §7)

Ejecuta solo los checks pertinentes y declara los no disponibles.

1. **Servir el Hub.** Usa `mora.serve_command` cuando la aplicación lo requiera (vacío → `python3 -m http.server`). `file://` puede cargar recursos relativos simples, pero módulos, `fetch`, CORS y rutas absolutas pueden requerir HTTP; no atribuyas todo fallo de estilos al protocolo.
2. **Ruta y shell.** Confirma HTTP/route, carga del shell activo y ausencia de imports del shell deprecado.
3. **DOM y accesibilidad estructural.** Valida HTML/DOM, IDs únicos, anchors, enlaces internos, `aria-current`, `aria-expanded` y `aria-controls` cuando apliquen.
4. **Estándar.** Verifica que las secciones sigan el estándar y que el índice contextual derive de secciones reales.
5. **Cobertura y registry.** Ejecuta cobertura/censo si existe y valida el JSON si se editó el registry (solo los campos permitidos a mora: ver «Límites»).
6. **Fuentes propietarias.** Contrasta metadata y API con su fuente propietaria.
