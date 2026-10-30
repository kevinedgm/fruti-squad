# Informe de resultados · rediseño r2 (membrete y paginación)

Prototipo: `informe.html` con tres ejemplos (bebidas: mezcal, 9 ensayos, 1 hoja; aguas: 30 ensayos, 2 hojas; alimentos: 4 ensayos, 1 hoja) y dos tipos (oficial / preliminar). Impresiones: `informe-corto.pdf`, `informe-largo.pdf` (oficiales), `informe-largo-preliminar.pdf`, `informe-alimentos-preliminar.pdf`. Regenerar: `python3 gen.py`. Datos, clientes, límites y responsables de ejemplo.

## Membrete
- Banda superior azul real con el logo de Nisa Nabani en blanco, «Informe de resultados» y el área; pestaña pera con folio y fecha de emisión; filete pera bajo la banda.
- Filo vertical pera → azul en el borde izquierdo de cada hoja.
- Marca de agua del logo al 3.5 %.
- Pie institucional (razón social, acreditación EMA, leyenda de reproducción, domicilio) y «Página X de N · RP-06-21 · folio».
- Sello «laboratorio acreditado» junto a las firmas.

## Tipo de informe: el color dice para qué sirve
- **Oficial** (para el organismo de certificación): banda azul real #052A76, logo blanco, pestaña pera, «Informe de resultados».
- **Preliminar**: banda del color del área, tomado de los secundarios del manual de marca (no de los colores de área de NisaLab):
  - Aguas: cian #00B4D8, texto azul real (5.3:1; blanco daría 2.5:1).
  - Bebidas alcohólicas: azul #3D67AE, texto blanco (5.6:1).
  - Alimentos: naranja #F48C06, texto azul real (5.4:1; blanco daría 2.4:1).
  - Logo en una tinta: blanco sobre bebidas, azul real sobre cian y naranja.
- El preliminar no depende solo del color: título «Informe preliminar», «no válido para certificación», chip PRELIMINAR en la pestaña, marca de agua diagonal y aviso al inicio de la descarga de responsabilidad. Así se distingue también impreso en blanco y negro.

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
- Qué tipo recibe un informe que mezcla un bloque para certificación y otro para control de calidad.
- Norma real de acidez y sus límites; ensayos acreditados (◊).
- Suplementos (S1, S2…): franja «Este informe reemplaza a…».
- Llevar las reglas de paginación al generador real (TCPDF).
