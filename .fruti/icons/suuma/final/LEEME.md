# SUUMA · paquete final

Símbolo: la doble U anidada (una u fina en cadmio dentro de la u de la palabra). Wordmark «suma» en Bricolage Grotesque 600, opsz 96, caja baja, tracking −1 %, en trazados. Interfaz: Onest. Color: tinta #121212, blanco #FFFFFF, papel #F5F4F0, cadmio #FFD400 (nunca texto). Manual: https://claude.ai/artifact/3CdHEhfrwNCkxAo6XkB3j6

- `gen.py`: `python3 gen.py <scratchpad>` regenera `svg/` y `tema.json` (usa `fuentes/BricolageGrotesque[opsz,wdth,wght].ttf` instanciada en `/tmp/suuma-bric600.ttf`).
- `svg/`: simbolo (-tinta, -blanco, -blanco-tinta), wordmark (-tinta, -oscuro), lockup-h (-oscuro, -tinta), lockup-v (-oscuro), app-icon (-cadmio, -claro, -maskable), avatar, favicon (cambia con prefers-color-scheme), tarjeta-redes.
- `png/`: icon-1024/512/192, icon-maskable-512, icon-cadmio-512, icon-claro-512, avatar-512, simbolo-512 (-tinta, -blanco), favicon-16/32/48 + favicon.ico, wordmark y lockups a 240 px, tarjeta-redes 1200×630.
- `tema.json`: colores, tipografía, reglas. `pruebas.md`: contrastes WCAG. `lamina.png`: control visual.
