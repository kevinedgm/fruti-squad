# Valores y resultados

La segunda fuente existe para una sola cosa: que un resultado se lea, se compare y se copie sin error. Todo valor analítico va en **IBM Plex Mono** con cero con barra.

## Qué va en Plex Mono

- Resultados y lecturas: `7.42`, `0.012`, `1.2 × 10³`.
- Unidades junto al valor: `mg/L`, `UFC/100 mL`, `°Bx`, `% v/v`, `µS/cm`.
- Especificaciones y límites: `6.5 – 8.5`, `≤ 0.010`, `LD 0.002`, `LC 0.005`.
- Incertidumbre: `7.42 ± 0.05`.
- Identificadores: muestra `NN-26-00417`, lote `L-2026-10-147`, certificado `CER-26-0091`.
- Fechas y horas de análisis en tablas: `2026-10-24 09:42`.

Los nombres de parámetro (pH, Plomo, Coliformes totales), los métodos (NMX-AA-008-SCFI-2016) y el texto corrido van en Poppins.

## Cómo se escriben

- **Decimales:** los que reporta el método, nunca los que da el cálculo. El punto es el separador decimal.
- **Alineación:** en tablas, valores a la derecha; con cifras de ancho fijo los decimales quedan en columna.
- **Debajo del límite:** `< 0.002` (menor que el LD), no `0` ni «ND» a secas; si el informe usa ND, `ND (LD 0.002)`.
- **Unidad:** separada del valor por un espacio, en `text-muted` en tablas; en la ficha, el valor en `valor-xl` y la unidad en `valor`.
- **Notación científica:** `1.2 × 10³`, con signo de multiplicar real y superíndice; nunca `1.2E3` en la interfaz.
- **Rangos:** guion medio con espacios: `6.5 – 8.5`.
- **Estado:** el color nunca va solo. Fuera de especificación lleva icono, texto «Fuera» y el valor en `fuera`; conforme lleva icono y texto «Conforme».

## Estilos

| Estilo | Uso |
|---|---|
| `valor-xl` 32/36 | Resultado protagonista en la ficha de un parámetro |
| `valor` 14/20 | Resultados en tablas y tarjetas |
| `valor-sm` 12/16 | Especificación, LD/LC, incertidumbre |
| `folio` 13/18 | Muestra, lote, certificado |
