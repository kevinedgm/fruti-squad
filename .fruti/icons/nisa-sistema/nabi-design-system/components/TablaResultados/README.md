# TablaResultados

Tabla de resultados de una muestra: nombres en Archivo, valores en Plex Mono alineados a la derecha.

- Encabezado en `label` sobre «surface-sunken»; filas de 40 px (`row-h`) separadas por «border».
- Resultado y especificación en `valor` / `valor-sm` (Plex Mono), a la derecha: con cifras de ancho fijo y los mismos decimales, el punto decimal queda en columna.
- Unidad en su propia columna, en «text-muted».
- Estado: pocillo de 10 px (`pozo`) del color del estado + texto. Fuera de especificación también pone el valor en «fuera» y en 600.
- La fila que se está capturando lleva fondo «pera-soft» y pocillo pera: es la muestra activa.
- El consumidor provee: filas con parámetro, método, valor, unidad, especificación y estado; los decimales que fija cada método.
