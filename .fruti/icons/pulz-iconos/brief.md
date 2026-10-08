# Briefs · iconos de dominio de PULZ (Uva E1)

Proyecto: PULZ (`kevinedgm/pulz`). Familia: Lucide a trazo 2 (`Icono.vue`: «un solo set canónico: Lucide»), así que Uva dibuja a 2.
Uso común: navegación por etapas (`app/destinos.ts`), 20–24 px, **siempre con etiqueta visible** → icono oculto (`aria-hidden`); el nombre lo da la etiqueta. Contraste: `currentColor` sobre los fondos de Foundations 1.0.0.
Referencias: sin fotos del usuario. Proporciones tomadas del conocimiento del oficio **(supuesto)**; R1 pide medir una foto real cuando la haya.
Hornos (respuesta del usuario 2026-10-08): horno cónico = hoyo en la tierra; horno = de mampostería, sobre el suelo.

## agave
- **Nombre y categoría:** `agave` · navigation (etapa Maguey; también objeto).
- **¿Ya existe?** buscado «agave plant succulent leaf» → `sprout` (lo usa hoy la app), `plant-pot`, `leaf`, `tree-palm`: brote blando, no maguey.
- **Consistencia:** sustituye a `sprout` en la etapa Maguey; `sprout` queda libre.
- **Rasgos:** roseta ancha y baja; pencas rectas, rígidas y de punta dura (no pétalos curvos).
- **Confusiones:** sprout, tree-palm, flame, crown (y loto, vista al renderizar).
- **Éxito:** a 24 px se lee planta de pencas rígidas, no flor, corona ni fuego; peso parecido a casa y mano.

## earth-oven
- **Nombre y categoría:** `earth-oven` · navigation (etapa Horno, horno cónico de tierra).
- **¿Ya existe?** «oven kiln furnace fire pit» → `flame` (lo usa hoy), `microwave`, `brick-wall-fire`: ninguno es un hoyo en la tierra.
- **Rasgos:** corte con la línea de suelo que sobresale por los dos lados; cono bajo el suelo; montículo de piñas tapadas encima.
- **Confusiones:** ice-cream-cone, martini, flame, cooking-pot.
- **Éxito:** se lee «algo enterrado que cuece», no helado ni copa.

## masonry-oven
- **Nombre y categoría:** `masonry-oven` · navigation (horno de mampostería sobre el suelo).
- **¿Ya existe?** igual que el anterior; `brick-wall-fire` es un muro de seguridad (firewall).
- **Rasgos:** cuerpo de obra sobre el suelo, boca en arco, vapor.
- **Confusiones:** house, tent, warehouse, brick-wall-fire.
- **Éxito:** horno, no casa ni almacén.

## stone-mill
- **Nombre y categoría:** `stone-mill` · navigation (etapa Molienda con tahona).
- **¿Ya existe?** «mill millstone grind wheel stone» → `cog` (lo usa hoy), `stone`, `ferris-wheel`: el engrane es maquinaria, no tahona.
- **Rasgos:** rueda de piedra en la fosa, vara que la une al poste del centro.
- **Confusiones:** cog, ferris-wheel, disc, tractor.
- **Éxito:** rueda que muele unida a un poste, no disco ni rueda de feria.

## fermenting
- **Nombre y categoría:** `fermenting` · status (ya existe en Uva, a trazo 1.5, con burbujas animadas).
- **¿Ya existe?** sí: se adapta a trazo 2, no se rediseña. `barrel` (lo usa hoy la app) se lee barrica de vino.
- **Confusiones:** barrel, database, trash, cylinder (y pastel de capas, vista al renderizar a trazo 2).
- **Éxito:** tina con burbujas, no base de datos ni pastel.
