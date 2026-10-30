# Informe de resultados · rediseño r2 (membrete y paginación)

Prototipo: `informe.html` con dos ejemplos (corto: mezcal, 9 ensayos, 1 hoja; largo: agua, 30 ensayos, 2 hojas). Impresiones: `informe-corto.pdf`, `informe-largo.pdf`. Regenerar: `python3 gen.py`. Datos, clientes, límites y responsables de ejemplo.

## Membrete
- Banda superior azul real con el logo de Nisa Nabani en blanco, «Informe de resultados» y el área; pestaña pera con folio y fecha de emisión; filete pera bajo la banda.
- Filo vertical pera → azul en el borde izquierdo de cada hoja.
- Marca de agua del logo al 3.5 %.
- Pie institucional (razón social, acreditación EMA, leyenda de reproducción, domicilio) y «Página X de N · RP-06-21 · folio».
- Sello «laboratorio acreditado» junto a las firmas.

## Paginación (reglas)
1. Hoja 1: banda completa, cliente, datos de muestra y recepción. Hojas siguientes: banda compacta y «Continuación del informe {folio}».
2. Las filas se reparten midiendo el contenido real; ninguna fila se corta.
3. Un bloque que sigue en otra hoja repite su encabezado con «(continuación)» y los títulos de columna; al pie de la hoja anterior, «Continúa en la página siguiente →».
4. Ningún título de bloque queda solo al final de una hoja (se mueve con su primera fila).
5. Observaciones, descarga de responsabilidad y firmas solo en la última hoja; si no caben, pasan completas a una hoja nueva.
6. Numeración de ensayos continua entre bloques y hojas.

## Formato de valores
Los valores se muestran tal como los entrega el laboratorio (sin redondeo); límites «a – b», «≤ b» o «≥ a»; intervalo de aceptación con los decimales del límite o de Uexp.

## Pendiente
- Norma real de acidez y sus límites; ensayos acreditados (◊).
- Suplementos (S1, S2…): franja «Este informe reemplaza a…».
- Llevar las reglas de paginación al generador real (TCPDF).
