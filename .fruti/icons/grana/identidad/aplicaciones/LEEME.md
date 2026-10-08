# Grana · aplicaciones

Generadas por `gen.py` a partir del símbolo A5, el wordmark W2, la paleta (`../color/paleta.json`) y el gesto «la impresión». Para regenerar: `python gen.py <ruta a InstrumentSans[wdth,wght].ttf>` y, después, renderizar los PNG.

| Archivo | Uso |
|---|---|
| `favicon.svg` | Favicon: versión de 16 px; tinta y tinte cambian con el tema del navegador |
| `png/favicon.ico`, `png/favicon-{16,32,48}.png` | Respaldo de favicon |
| `png/apple-touch-icon.png` | iOS (180 px, fondo cera) |
| `png/icon-{192,512}.png`, `png/icon-maskable-{192,512}.png` | Docs instalables (PWA) |
| `avatar-{claro,oscuro}.svg`, `png/avatar-{claro,oscuro}-{460,512,1024}.png` | GitHub y npm |
| `readme-cabecera-{claro,oscuro}.svg` | Cabecera del README: W2 + lema; reproduce «la impresión» una vez |
| `tarjeta-redes-{claro,oscuro}.svg`, `png/tarjeta-redes-{claro,oscuro}-1280x640.png` | Vista previa social de GitHub y Open Graph |

## README

```html
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/marca/readme-cabecera-oscuro.svg">
    <img src="assets/marca/readme-cabecera-claro.svg" alt="Grana: the only bug you'll want in your UI." width="560">
  </picture>
</p>
```

## Docs

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

Todo el texto de los SVG está convertido a trazados: no depende de tener Instrument Sans instalada.
