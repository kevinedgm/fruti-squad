# Informe de resultados · rediseño r1

Prototipo: `informe.html` (hoja carta; `informe.pdf` es su impresión). Regenerar: `python3 gen.py`. Datos de ejemplo: cliente, lote y responsable ficticios; métodos y estructura tomados de los informes NNMZ/NNBA actuales (no se versionan los PDF reales del cliente).

## Problema
El formato actual amarra «una norma = un informe»: la norma va en el título de los resultados y en la descarga de responsabilidad. Si piden un parámetro bajo otra norma (p. ej. acidez fuera de NOM-070), se emite un segundo informe.

## Solución
- **Bloques por norma de referencia.** Cada bloque lleva su norma, su título, su propósito («para fines de certificación» / «de control de calidad») y el conteo de declaraciones. Un informe puede tener 1, 2 o más bloques; con uno solo, se ve igual que hoy.
- **Descarga de responsabilidad armada con la lista de normas** («válido de acuerdo con NOM-070 para los ensayos del bloque 1; Norma B para los del bloque 2»).
- **Declaración por ensayo** (Cumple / No cumple / No aplica) con el intervalo de aceptación (límites ajustados por Uexp, PP-01 / ILAC-G8) bajo los límites. Sin límite: «No aplica».
- Numeración continua de ensayos (1…n) a través de los bloques; ◊ marca ensayo no acreditado.
- QR de verificación de autenticidad (propuesta; enlazaría a NisaResults).

## Hallazgo en los informes actuales
NNMZ-56151: «Alcoholes superiores» 542.63 con máximo 500 y el formato no lo señala; en el rediseño queda como «No cumple».

## Pendiente
- Norma real del bloque de acidez y sus límites.
- Qué ensayos son acreditados (marca ◊).
- Variantes por área (aguas, alimentos) con la misma estructura de bloques.
- Suplementos (S1, S2…): franja «Este informe reemplaza a…».
