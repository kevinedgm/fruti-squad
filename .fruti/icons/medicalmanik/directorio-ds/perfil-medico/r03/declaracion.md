# Declaración de cumplimiento · Perfil del médico · r03

- **Ruta / fidelidad:** R1 · F2 (kit neutral).
- **Estándares leídos:** brief r01 + delta r03, kit, FichaMedico r03 C, componente Horarios del DS (píldora), `.fruti/contracts/adaptativo.md`, WCAG 2.2 AA.

## Comprobaciones ejecutadas
- `check_artifact.py --fidelidad F2`: 0 errores, 1 aviso («2 primarias en marcado estático»); verificado en navegador que nunca coinciden visibles.
- Playwright 393 / 834 / 1440 × 12 estados: 0 desbordes de página (días, secciones y galería se desplazan en horizontal a propósito), 0 controles menores de 24 px, 1 primaria visible por vista (0 en «Carga» de escritorio, a propósito), 0 errores JS.
- Revisión visual: perfil mínimo a 393 px y perfil a medias a 1440 px.

## Comprobaciones NO ejecutadas
- Texto ampliado al 200 %, teclado completo, lector de pantalla.
- Interacción real (tocar día/hora no cambia el wireframe; los estados se eligen en el panel).

## Desviaciones
- Ninguna sobre la anatomía aprobada de FichaMedico.
