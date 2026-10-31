# MedicalManik · Manual de identidad 2026

Pedido del usuario (2026-10-31): un artifact nuevo que reemplace al manual anterior en PDF (22 págs., «Manual de identidad»), siguiendo su estructura y documentando toda la marca con sus productos.

Publicado: https://claude.ai/artifact/9CXk9mHzwGdy8bow3Q9VsV · `python3 gen.py <dir>` → `manual.html` (sin skeleton; imágenes como data URI). El PDF anterior no se versiona.

## Estructura (sigue al anterior y suma lo nuevo)
Portada · Índice · Introducción (acerca de, valores) · Arquitectura de marca (nuevo) · Logotipo (primario, construcción, área de seguridad, variaciones, usos incorrectos) · Paleta (comunicación, texto sobre color, interfaz y productos) · Tipografía · Personalidad y tono · Ecosistema Manik (nuevo) · manik, el directorio (antes «Mi Médico Manik») · Manik IA (nuevo) · Iconografía · Generación de contenido · Gimmick (Manix) · Aplicaciones (firma de correo) · Cambios y pendientes.

## Logotipo
La palabra MedicalManik se extrajo en vector del PDF anterior (pág. 8, versión azul; está trazada en **Filson Pro**). Nuevos archivos en `../final/svg/`: `medicalmanik-palabra.svg`, `medicalmanik-logotipo.svg` (color), `-blanco.svg`, `-1tinta.svg`, con las proporciones del manual anterior (sello 54, separación 8, palabra 29 de alto).

## Cambios respecto al anterior [propuesta, ver tabla en el manual]
Sello sólido como principal (degradado solo para fondos de comunicación) · azul unificado en #234899 (el anterior decía #23439C; 1.04:1) · retiradas 4 combinaciones de texto sin contraste (blanco sobre cian 1.90, lavanda 2.83, lima 1.33; cian sobre blanco 1.79) · submarca «Mi Médico Manik» → directorio manik · Ecosistema y Administración documentados · IA «sugiere» (antes «recomendar tratamientos») · Filson Pro/Scandia en comunicación y Urbanist/Atkinson en apps · ejemplo de tono repetido corregido · Manix no es la voz de la IA · firma de correo con datos de ejemplo (el anterior tenía datos de una persona real) · fotos de banco no reproducidas.

## Pendientes
Tipografías de comunicación (¿unificar?) · uso del degradado · dominios · fotografía e ilustración propias.

## Verificación
Playwright 1300 y 390 px con Urbanist y Atkinson locales: sin desbordes de página ni errores; todas las imágenes cargan. Corregido en prueba: párrafos con negritas que se partían en renglones.
