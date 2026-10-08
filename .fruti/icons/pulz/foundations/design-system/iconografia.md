# Iconografía

- Familia: **Lucide** para lo genérico (casa, campana, reloj, ajustes) y los cinco iconos propios de etapa (assets/Iconos), todos a **trazo 2** para que no se note cuáles son de cada origen.
- Tamaño por entrada: `size-icon` 24 px con el dedo, 20 px con ratón. El trazo no se engrosa al reducir el icono.
- Color: `currentColor`. El icono toma el color del texto que acompaña. `anil` solo en el destino activo de la navegación. `pericon` nunca en iconos (1.6:1 sobre `canvas`).

## Los iconos de etapa

| Icono | Etapa | Sustituye a |
|---|---|---|
| `agave` | Maguey | Sprout |
| `earth-oven` | Horno cónico de tierra | Flame |
| `masonry-oven` | Horno de mampostería | Flame |
| `stone-mill` | Molienda (tahona) | Cog |
| `fermenting` | Fermentación (anima sus burbujas una vez, 4.8 s) | Barrel |

Los cinco se probaron a 24 y 20 px junto a los iconos con los que se confunden (brote, cono de helado, casa, engrane, base de datos). Las proporciones vienen del oficio, no de fotos del palenque: si hay fotos, se ajustan.

## Reglas

1. En la navegación y en las acciones importantes el icono va **siempre con etiqueta**; el icono queda `aria-hidden` y el nombre lo da la etiqueta.
2. Un icono sin texto solo en acciones universales (cerrar, menú, buscar), con el nombre accesible en el botón y un área de 44 × 44.
3. Ningún estado se comunica solo con el icono o el color: «Fermentando» siempre lleva su palabra.
4. La Z de PULZ es marca, no icono de interfaz: no se usa como botón.
