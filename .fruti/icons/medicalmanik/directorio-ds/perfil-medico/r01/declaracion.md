# Declaración de cumplimiento · Perfil del médico · r01

- **Ruta / fidelidad:** R1 · F2 (kit neutral). Contenido real del ejemplo del usuario (con teléfono y cédulas ficticios).
- **Estándares leídos:** brief, kit de wireframe, anatomía aprobada de FichaMedico r03 C (cabecera y consultorio), `.fruti/contracts/adaptativo.md`, WCAG 2.2 AA.
- **Artefactos:** `propuestas/index.html`, `propuestas/publicar.html`.

## Comprobaciones ejecutadas
- `check_artifact.py index.html --fidelidad F2`: 0 errores, 0 avisos.
- Playwright 393 / 834 / 1440 × 7 estados: 0 desbordes de página (la barra de secciones y la galería se desplazan en horizontal a propósito), 0 controles menores de 24 px, 1 acción primaria visible por vista, 0 errores JS.
- Revisión visual a 393 y 1440 px del estado principal.

## Comprobaciones NO ejecutadas
- Texto ampliado al 200 %, teclado completo, lector de pantalla.
- Que la barra de secciones marque la sección activa al desplazarse (en el wireframe es estática).
- Revisión visual a 834 px.

## Desviaciones
- Ninguna sobre la anatomía aprobada de FichaMedico.
