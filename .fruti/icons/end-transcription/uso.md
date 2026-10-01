# end-transcription · uso (pareja con transcribing)

1. **Botón con texto** (recomendado): `<button>[icono] Finalizar dictado</button>`. El SVG ya trae `aria-hidden="true"`.
2. **Solo con icono:** botón de 44×44 con `aria-label="Finalizar dictado"` en el `<button>`.
3. **Aparece junto al indicador** `transcribing` mientras el dictado esté activo; al pulsarlo, se ocultan los dos y el foco pasa a «Iniciar dictado».
4. **Sin movimiento:** es una acción instantánea.
5. **No lo uses para pausar ni silenciar.** Si un día hay pausa, necesita su propio icono (dos barras), distinto de este cuadrado.
