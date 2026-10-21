# Plan A · Diagnóstico y tablero de producción para marcas de mezcal

Versión 0.1 · semana 1 · CLNDA Studio

## La oferta en una frase

En dos semanas convierto sus registros de producción (libretas, Excel, PULZ o lo que tengan) en un tablero que dice cuánto cuesta cada litro, dónde se pierde producto y qué tres cosas cambiar primero.

## Paquete cerrado

| | Diagnóstico | Diagnóstico + tablero |
|---|---|---|
| Precio | $15,000 MXN | $25,000 MXN |
| Plazo | 1 semana | 2 semanas |
| Entrega | Informe de 2 páginas con costo por litro, rendimiento y mermas por lote, y 3 recomendaciones | Lo anterior más el tablero interactivo con sus datos (como el demo) y una sesión de 1 hora para leerlo juntos |
| Qué necesito de ustedes | Registros de los últimos 12 lotes: kg de agave, litros, grado, costos, y mermas por etapa si las anotan | Lo mismo, más ventas por canal si quieren ver margen |
| Garantía | Si en el diagnóstico no encuentro al menos una pérdida mayor al precio del servicio, cobro la mitad | Igual |

Después (no se vende en la primera reunión): actualización mensual del tablero por $3,000 MXN/mes, o conexión directa a PULZ si lo usan.

## A quién

Marcas medianas que ya exportan o venden a nivel nacional, y asociaciones de productores. La persona: gerente de operaciones o administrador, no el maestro mezcalero.

## Qué se dice y qué no

- Se dice: mermas, costo por litro, rendimiento por kilo, margen por canal, qué lote salió mal y por qué.
- No se dice: Xila, Grana, Vue, dashboard, framework, ciencia de datos.

## El demo

Tablero con un palenque ficticio de 12 lotes: https://claude.ai/artifact/NxYQZreiTKxHwPYVriqtxS (privado; compartir con enlace antes de la reunión o mostrar en pantalla). Datos y página en `demo/`.

En 5 minutos se enseña en este orden: la frase de arriba (litros, costo, cuánto se perdió), la gráfica de mermas (señalar el lote rojo), las tres recomendaciones. Nada más.

## Prospección (semana 2)

Mensaje en frío, por WhatsApp o correo, a 20 nombres:

> Hola [nombre], soy Kevin, desarrollador y científico de datos en Oaxaca. Trabajo con palenques y marcas para sacar de sus registros cuánto cuesta cada litro y dónde se pierde producto. Tengo un tablero de ejemplo de 5 minutos; ¿te lo muestro esta semana?

Lista de 20 en `prospectos.csv` (vacía: se llena con nombre, marca, cargo, contacto, origen del contacto, estado).
