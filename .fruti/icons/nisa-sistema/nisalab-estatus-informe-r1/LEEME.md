# NisaLab · iconos de estatus del informe · ronda 1 (2026-11-03)

Pedido: iconos para «En proceso», «Listo para generar informe» e «Informe generado» (recepción → emisión del informe de resultados).

Fuente aprobada: componente `EstadoMuestra` (`../nabi-design-system/components/EstadoMuestra/`). Los colores de pastilla son los tokens `muestra-en-proceso`, `muestra-generando-informe` y `muestra-terminada`; no cambian.

## Direcciones
- A · Actual: el círculo se llena (mitad, tres cuartos, lleno con palomita). La palomita calada usa máscara (blanco/negro de máscara; Uva COL2 la marca).
- B · El objeto de cada etapa: matraz, portapapeles con palomita, documento con sello. Choca con iconos del menú (`flask-conical` = Código de ensayo, `file-check` = Informes en `nabi-iconos-lab`).
- C · Insignia con la siguiente acción (recomendada): círculo + puntos / flecha / palomita. Se extiende a No ingresada (`circle-dashed`) y Cancelada (`ban`).
- D · Pasos del 1 al 3: tres puntos que se llenan.

## Pendiente (usuario / Lima)
- Elegir dirección.
- Renombre: «Generando informe» → «Listo para generar informe», «Terminada» → «Informe generado». Confirmar si «Informe generado» incluye «enviado» o si «Enviado» es otro estado. Si se aprueba, Lima renombra tokens y EstadoMuestra.

Archivos: `gen.py` (genera `variantes/`, `variantes.json`, `revision.html`), `plantilla.html`.
