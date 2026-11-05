# TablaResultados

Tabla de resultados de una muestra: nombres en Poppins, valores en Google Sans Code alineados a la derecha.

- Encabezado en `label` sobre «bg»; filas de 40 px (`row-h`) separadas por «border».
- Resultado y especificación en `valor` / `valor-sm` (Google Sans Code), a la derecha: con cifras de ancho fijo y los mismos decimales, el punto decimal queda en columna.
- Unidad en su propia columna, en «text-muted».
- Estado: pocillo de 10 px (`pozo`) del color del estado + texto. Fuera de especificación también pone el valor en «fuera» y en 600.
- La fila que se está capturando lleva fondo «primary-soft», filete y punto pera: es la muestra activa.
- El consumidor provee: filas con parámetro, método, valor, unidad, especificación y estado; los decimales que fija cada método.
