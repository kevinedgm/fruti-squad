# Ecosistema Manik · paquete final

MedicalManik es la empresa y el sello madre. Cada producto se nombra «<Producto> Manik».

## Archivos
- `svg/<producto>.svg`: color, fondo transparente (los cortes son máscaras). Productos: medicalmanik (sello madre), expediente, agenda, compras, farmacia, impulsa, grupos.
- `svg/<producto>-1tinta.svg`: una tinta en `currentColor`; la línea queda calada.
- `svg/ecosistema.svg` / `ecosistema-1tinta.svg`: identificador del selector de apps (retícula 24, botón de interfaz).
- `png/<archivo>-{16,32,64,128,512}.png`: exportaciones en color con transparencia.
- `tema.json`: colores, para quién es cada producto y contrastes medidos.
- `gen.py <scratchpad>` regenera todo; `lamina.png` es la vista general.

## Reglas
1. La línea de pulso es idéntica en todos; nunca se redibuja por producto.
2. El rasgo de cada producto vive en el borde del cuadro y nunca corta la línea: silueta (carpeta, ticket, tarjeta detrás) o pieza separada por un corte (argollas, cruz, flecha).
3. El color de producto acompaña al nombre; nunca es la única señal.
4. La cruz de Farmacia va siempre en el verde del producto, nunca en rojo (emblema protegido).
5. El cian #00BDD0 es acento de marca: no se usa como fondo de texto ni como color de producto (2.29:1 con blanco).
6. El identificador del ecosistema es un emblema fijo de seis cuadros: no cambia si se suman productos; el selector sí muestra todas las apps.
8. Impulsa usa #504CA1, el violeta `accent-deep` que ya tiene su sistema en producción.
7. Nombre en interfaz: el producto en peso 600 y «Manik» en peso regular.

## Pendiente
- Confirmar si existe un inicio de sesión único entre apps (la maqueta del selector lo menciona como supuesto).
- La tipografía de la palabra MedicalManik original no está identificada; las láminas usan Sora como aproximación.
