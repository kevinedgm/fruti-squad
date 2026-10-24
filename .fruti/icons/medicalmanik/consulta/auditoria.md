# Consulta · auditoría visual y estructural (vistas de gestión y formularios)

Fuente de criterios: la regla de auditoría que dio el usuario (estructura, jerarquía, contraste, espaciado, controles, formularios, estados, consistencia). El documento «Brief de Diseño UI: Vistas de Gestión y Formularios» con sus valores no está en el repositorio: se usaron los tokens del sistema Ecosistema Manik en su lugar.
Contexto: ~40 % de los médicos usuarios tiene más de 50 años y migra desde Word o libreta.

## Cumplimientos previos
- Estructura: barra del paciente (cabecera) → índice de secciones (herramientas) → nota (datos) → panel de entregables.
- Foco visible de 2 px en todos los controles; etiquetas arriba de cada campo; errores de signos con icono y texto.

## Correcciones
| Hallazgo | Antes | Después |
|---|---|---|
| Secciones sin delimitar del fondo | borde 1.17:1 sobre lienzo; superficie 1.07:1 | lienzo #E8ECF3, borde #B9C2D3 (1.51:1) y cabecera de sección con banda #F1F4F9 y divisor |
| Bordes de campo | 3.28:1 | 5.41:1 (#5F6A84) |
| Texto secundario | #4A5674 (7.3:1) | #3E4A66 (8.8:1) |
| Placeholder | gris del navegador | #5F6A84 (5.4:1) |
| Letra pequeña | 12–13 px en referencias, etiquetas y ayudas | mínimo 14 px; cuerpo y campos 17 px |
| Tamaño ajustable | no existía | «Tamaño de letra: Normal / Grande» (16→18 px base, todo en rem), se recuerda por usuario |
| Botones solo con icono | quitar (×), pausar | «× Quitar», «Pausar» con texto |
| Objetivos pequeños | dosis 38 px, selector de hoja 34 px | 44 px y 40 px |
| Estado sin resultados | buscadores sin mensaje | «Sin resultados para «…». Prueba con el nombre genérico» |
| Deshabilitado | «Terminar» siempre activo | deshabilitado con el motivo escrito («Para terminar: resuelve la contraindicación») |
| Miedo a equivocarse | quitar era definitivo | aviso «Se quitó Paracetamol · Deshacer» |
| Alineación de signos | un error de varias líneas estiraba los campos vecinos | campos alineados arriba |

## Verificado (Chromium, 1500 px)
- Sin errores de consola; sin desplazamiento horizontal de página.
- Estados: contraindicación (error), sin resultados (vacío), deshabilitado con motivo, deshacer, foco por teclado, letra grande.
- Medido en la página: lienzo rgb(232,236,243), borde de sección rgb(185,194,211), borde de campo rgb(95,106,132); en «Grande» el cuerpo mide 19.1 px y las referencias 15.75 px.

## Pendientes
- Estado de carga (esqueleto) y error de guardado: no dibujados.
- Prueba con médicos mayores de 50 años (5 segundos y una consulta completa): no realizada.
- Lectores de pantalla y zoom del navegador al 200 %: no verificados.
- Valores exactos del brief original: no disponible en el repositorio.
