# NisaLab · revisión de color del DS · r01 (propuesta, sin aprobar)

`python3 gen.py` → `revision.html`. Artefacto: https://claude.ai/artifact/AoN3oLa9MedKnmENXQ6Xhe
Fuente: `../nabi-design-system/tokens.json` (53 colores) y `components/*/preview.html` (usos con var()).
Criterio: queda si nombra algo que ningún otro nombra o si sin él algo no cumple contraste.
Resultado: 25 quedan (17 sin áreas), 27 se unen a un color existente, 1 se quita (alerta-fill). Cero nuevos.
Hechos: 4 valores repetidos (#052A76 ×3, #FFFFFF, #B42318, #166534); 27 de 53 se usan con var() en componentes.
Decisiones abiertas: (1) proceso y pago se unen a los estados (solo cambia el violeta); (2) conservar las 8 áreas; (3) pendiente pasa a gris de texto.
No aplica nada a tokens.json hasta aprobarse.
