# Mesanda · paquete final de marca

Comandero local de CLNDA Studio (plano de mesas, órdenes con fotos, cuenta; gratis local + nube de pago). Ver `../menu-producto/brief.md`.

## Decisiones del usuario (2026-10-30)
- Nombre propio respaldado por CLNDA Studio: **Mesanda** (mesa + comanda, «la mesa anda»). Rondas: `../restaurante-nombres-r2`, `-r3`.
- Símbolo **H1 mesa con estela**: mesa redonda, tres sillas y estela de velocidad en lugar de la cuarta (`../mesanda-r1`, `-r2`).
- Color: **blanco, negro y acento amarillo señal**, por psicología del producto (atención, rapidez), sin asociaciones mexicanas ni naranja (`../mesanda-r3` a `-r6`).

## Color
| Token | Valor | Uso |
|---|---|---|
| negro | #0b0b0c | texto, mesas ocupadas, fondos de marca |
| blanco | #ffffff | fondo |
| amarillo | #facc15 | acción principal y «cuenta pedida»; texto encima siempre negro (12.8:1) |
| amarillo-texto | #7a5a00 | texto amarillo sobre blanco (6.4:1) |
| gris-fondo | #f4f4f5 | superficies secundarias |
Amarillo sobre blanco 1.5:1: nunca texto ni icono funcional; en el logotipo claro la estela es decorativa (logotipos exentos en WCAG 1.4.3/1.4.11).

## Decisiones mías (cambiables)
- Tipografía Manrope (800 marca en trazados, 400–700 interfaz).
- Debajo de 24 px, `simbolo-16` (dos líneas gruesas); sobre blanco, todo negro.

## Archivos
`svg/` símbolo (claro, oscuro, amarillo, negro, blanco, 16), favicon (cambia con el tema), app icons (negro y amarillo), lockups (claro, oscuro, amarillo, negro) y lockup con respaldo «de CLNDA Studio». `png/` app icons 512/192, símbolo 512, favicon 32. `tema.json`, `gen.py` (`python3 gen.py <carpeta con Manrope[wght].ttf>`), `png.cjs`, `lamina.html` / `lamina.png`.

## Pendiente
- Búsqueda fonética en MARCia (IMPI), clases 9 y 42.
