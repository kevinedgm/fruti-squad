# Serie · categorías de servicios

Marco común para que todas las categorías de la app se lean como una familia en la cuadrícula.

- **Variante:** object (sin personaje): la mano del oficio y su herramienta. 1:1, fondo transparente.
- **Sin manos flotantes:** la mano entra desde la esquina inferior derecha con el antebrazo cortado por el borde real (en «Uñas», la mano de la clienta entra además por la izquierda).
- **Señal de categoría:** la herramienta, en diagonal y centrada. El amarillo #F8BC32 va **solo en la parte que identifica el oficio**; 2–3 marcas cinéticas negras junto a la herramienta.
- **Escala pareja:** las manos ocupan lo mismo en todas las tarjetas.
- **Tamaño mínimo:** 96 px (engrosar la tinta al vectorizar se probó y se descartó: tapa el acento y funde detalles).
- La versión con persona (`estilista-persona`) queda como alternativa para piezas grandes (hero, onboarding).

## Prompt
Pegar la base y añadir la línea de la categoría. Pedir varias en una hoja 2×2 ahorra rondas: `parte-hoja.py` las separa.

```
Ilustración doodle plana, vector-ready, icono-ilustración para una categoría de una app de reservas de servicios. Sin personaje completo: solo la mano (o manos) y el objeto del oficio. La mano entra desde la esquina inferior derecha, con el antebrazo cortado exactamente por el borde de la imagen (nunca una mano flotante), y sostiene el objeto en diagonal, centrado. Mano un poco grande y expresiva, dedos simples, juntos y legibles, uñas sin pintar salvo que se indique.

Estilo: contorno negro #111111 grueso, uniforme y redondeado, curvas orgánicas; piel y superficies en blanco cálido #FFFDF5; masas sólidas en negro; un solo acento amarillo #F8BC32 (donde se indica abajo). Dos o tres marcas cinéticas cortas negras junto al objeto.

Reglas: fondo transparente; colores planos; sin degradados, sombras, texturas, texto ni símbolos; sin accesorios (anillos, relojes, pulseras); sin fondo ni muebles; detalle bajo; margen uniforme. PNG cuadrado 1024×1024.

Tema:
```

## Hechas
| Categoría | Tema (línea del prompt) | Acento |
|---|---|---|
| estilista | mano con tijeras de peluquería abiertas, pulgar y un dedo en los aros | aros |
| unas | mano relajada desde la izquierda; otra mano le pinta la uña del índice con el pincel del esmalte | uñas pintadas + punta del pincel |
| barberia | mano con navaja de barbero clásica abierta | mango |
| tatuajes | mano con máquina de tatuar clásica de bobinas, aguja hacia abajo | bobinas |
