# Manik · paquete final (directorio de pacientes)

«Manik» a secas, en minúsculas. Lema: «Tu médico, a la mano». Respaldo: «de MedicalManik».
Origen del nombre: Manik' es el séptimo día del Tzolk'in; su glifo es una mano semiempuñada.

## Archivos
- `svg/simbolo.svg`: la M de pulso de la familia en un pin cian (#009BB0).
- `svg/simbolo-1tinta.svg` (currentColor, línea calada) y `svg/simbolo-blanco.svg` (sobre fondos oscuros).
- `svg/logotipo.svg`, `logotipo-blanco.svg`, `logotipo-1tinta.svg`, `logotipo-endoso.svg` («de MedicalManik»), `logotipo-vertical.svg`. Texto en Sora 600 convertido a trazos.
- `svg/app-icon.svg` (1024, sello sobre blanco) y `svg/favicon.svg`.
- `png/<archivo>-{16,32,64,128,512}.png` con transparencia. `tema.json` con colores y contrastes.
- `python3 gen.py <Sora[wght].ttf> <carpeta temporal>` regenera todo; `lamina.png` es la vista general.

## Reglas
1. La línea de pulso es la misma de toda la familia; la punta del pin es el único rasgo propio.
2. Cian Manik (#009BB0) es para el sello y áreas grandes de marca. Botones, enlaces y texto en cian usan #00788A (5.2:1 con blanco).
3. Sin degradados: el sello es de un solo color para imprimir, bordar y sellar.
4. El azul MedicalManik solo aparece en el respaldo «de MedicalManik».
5. Estrellas de calificación en #F2B33D; el número junto a ellas va en tinta.

## Pendiente
- Revisar registro de marca y disponibilidad de manik.mx.
- A 24 px el pin todavía puede recordar un globo de chat: validar en teléfono.
