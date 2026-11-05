# App Shell NisaLab · r03 (pendiente de aprobación)

`python3 gen.py` → `shell.html`. Misma URL que r01/r02: https://claude.ai/artifact/Xg6DANcBq6hsdsv9eNHKk5

Comentario de r02: inputs con demasiada sombra; solo borde neutro muy suave, igual que la tabla; duda con la fuente; encabezado de sección (título, subtítulo, quizá icono) y área de trabajo enmarcada.

## Cambios
- Sin hoja flotante: la página está sobre `bg` #F7F8FA; navbar con borde inferior.
- Encabezado de sección: avatar con icono (52 px, blanco, aro de borde), contexto «Bitácoras · BIT-02-01 · NOM-070-SCFI-2016», título 28/36, subtítulo y acciones (Exportar, Nueva bitácora).
- Área de trabajo enmarcada: blanco, borde 1 px, radio 16, sin sombra. Contiene cabecera «Registros», filtros, tabla y paginación.
- Campos y botones: solo borde, sin sombra. Foco = borde primary + anillo primary-soft de 3 px.
- Pesos más ligeros: navegación 400, activo 500.
- Globo de avisos reducido (18 px) para no tapar la campana.

## Decisiones abiertas (conmutadores en la barra superior)
- **Borde de campos.** WCAG 2.2 AA 1.4.11 exige 3:1 para el borde que identifica un control.
  - Cumple: #8E95A6 → 3.0:1 sobre blanco (2.82:1 sobre #F7F8FA; los campos viven sobre blanco). Predeterminado.
  - Sutil: #D9DDE5 → 1.36:1. **No cumple AA**; solo para comparar.
- **Fuente.** Poppins (marca, manual Nisa Nabani) vs Geist. Cambiarla es decisión de marca.

## Conflicto con reglas vigentes
- El icono en el encabezado de sección contradice «Título sin icono» de `nabi-design-system/modulos.md`. Si se aprueba, se actualiza esa regla.
- Los valores de `PROPUESTA` (bg, border, border-control, radios, sombras) no están en `tokens.json`; se llevan al DS solo tras aprobación.

## Comprobaciones ejecutadas
- 4 vistas (escritorio, menú plegado, celular, celular con menú): desbordamiento 0, sin controles < 24 px, sin errores JS.
- 390 px: desbordamiento 0. Submódulo desplegable abre (aria-expanded).
- No ejecutadas: lector de pantalla real, texto ampliado al 200 %.
