# MedicalManik · Manual de identidad 2026

Pedido del usuario (2026-10-31): un artifact nuevo que reemplace al manual anterior en PDF (22 págs., «Manual de identidad»), siguiendo su estructura y documentando toda la marca con sus productos.

Publicado: https://claude.ai/artifact/9CXk9mHzwGdy8bow3Q9VsV · `python3 gen.py <dir>` → `manual.html` (sin skeleton; imágenes como data URI). El PDF anterior no se versiona.

## Estructura (sigue al anterior y suma lo nuevo)
Portada · Índice · Introducción (acerca de, valores) · Arquitectura de marca (nuevo) · Logotipo (primario, construcción, área de seguridad, variaciones, usos incorrectos) · Paleta (comunicación, texto sobre color, interfaz y productos) · Tipografía · Personalidad y tono · Ecosistema Manik (nuevo) · manik, el directorio (antes «Mi Médico Manik») · Manik IA (nuevo) · Iconografía · Generación de contenido · Gimmick (Manix) · Aplicaciones (firma de correo) · Cambios y pendientes.

## Logotipo
La palabra MedicalManik se extrajo en vector del PDF anterior (pág. 8, versión azul; está trazada en **Filson Pro**). Nuevos archivos en `../final/svg/`: `medicalmanik-palabra.svg`, `medicalmanik-logotipo.svg` (color), `-blanco.svg`, `-1tinta.svg`, con las proporciones del manual anterior (sello 54, separación 8, palabra 29 de alto).

## Cambios respecto al anterior [propuesta, ver tabla en el manual]
Sello sólido como principal (degradado solo para fondos de comunicación) · azul unificado en #234899 (el anterior decía #23439C; 1.04:1) · retiradas 4 combinaciones de texto sin contraste (blanco sobre cian 1.90, lavanda 2.83, lima 1.33; cian sobre blanco 1.79) · submarca «Mi Médico Manik» → directorio manik · Ecosistema y Administración documentados · IA «sugiere» (antes «recomendar tratamientos») · Filson Pro/Scandia en comunicación y Urbanist/Atkinson en apps · ejemplo de tono repetido corregido · Manix no es la voz de la IA · firma de correo con datos de ejemplo (el anterior tenía datos de una persona real) · fotos de banco no reproducidas.

## Decisiones tomadas por Claude a pedido del usuario (2026-10-31: «tú analiza y decide»)
- **Tipografía única: Urbanist + Atkinson** en toda la marca. Filson Pro solo dentro del logotipo (ya en vector); Scandia se retira. Motivo: licencias comerciales vs. fuentes libres que cualquiera del equipo usa; Atkinson ya es la letra de las apps; una sola pareja entre comunicación y producto. Impresos actuales hasta agotarse.
- **Degradado solo como fondo** de comunicación, fórmula `linear-gradient(120deg,#234899 0%,#3E7CC6 55%,#5FC9D8 100%)`; nunca en el sello, botones, texto, íconos ni apps; texto y logo sobre el lado azul (blanco sobre el cian 1.9:1). En redes el sello va sólido.
- **Plantillas de correo** documentadas en Aplicaciones (reglas, 3 muestras, tabla de 11) y actualizadas: Urbanist en vez de Sora y logotipo oficial en la cabecera. Dominio unificado a `medicalmanik.com` como en las plantillas (sin confirmar).

## Pendientes
Dominios · fotografía e ilustración propias · probar correos en Gmail, Outlook y Apple Mail.

## Verificación
Playwright 1300 y 390 px con Urbanist y Atkinson locales: sin desbordes de página ni errores; todas las imágenes cargan. Corregido en prueba: párrafos con negritas que se partían en renglones.

## Puesta al día (2026-11-05)
Pedido: «ponlo al día y resume las secciones de producto con enlace».
- Nueva tabla «Dónde vive cada regla» en Arquitectura: este manual manda en lo compartido; cada producto en su documento (Ecosistema DS 28z6yfie6L8btocL8QBZi9, manual del directorio PNtPN4fEMSdEyVKTKwxAM7, DS del directorio MTg2EAZVsJKZJRFCWGvAuj, Manik IA LYq9oKz49WMM2ihwALM1WL).
- Ecosistema y directorio resumidos con enlace; se retiran del manual los detalles que ya viven en su documento (panel de usuario, ids de máscara).
- Del manual del directorio (4 nov): «Manik» con mayúscula en textos y «manik» en el logotipo; leyenda «Encuentra a tu médico cerca de ti.»; «luz, no color»; estrella #E3A21C (antes #F2B33D).
- Tipografía: excepción vigente Urbanist + Onest en el directorio [por confirmar como permanente]; contradice la regla de pareja única del 31 oct, se declara en vez de ocultarla.
- No incorporadas: Administración r1, pantalla principal de Administración y documentos de Expediente siguen como propuesta sin aprobación.
- Verificación: Playwright 1300 y 390 px, sin desbordes, sin errores, todas las imágenes cargan; 8 enlaces a los documentos.

## Superficies e interfaz (2026-11-05)
Pedido: «el diseño de superficies para todo el ecosistema (colores de superficies, acentos, semánticos, bordes de botones, inputs) en este manual».
- Sección nueva `#superficies` después de Paleta, generada por `superficies.py` desde `design-system/project/tokens.json` (apps), `directorio-ds/project/tokens.json` y el `:root` de `manik-ia/manual.html`. El manual no guarda valores propios: si cambia un token, se regenera.
- Muestras vivas (botones primario, secundario, terciario y destructivo; campo en reposo, foco, error y solo lectura; estados), 6 reglas, tabla de roles por familia con contrastes calculados.
- Huecos declarados: el directorio no define aviso, error ni información (propuesta: heredar de las apps), no tiene campo fuera del buscador; nadie define deshabilitado (pendiente, no se inventa).
- Diferencias con el mismo rol: borde de control #858EA5 vs #6B7590, foco 2 vs 3 px, éxito suave, borde decorativo. Por decidir: unificar o dejar por familia.

## Controles, formularios y diálogos (2026-11-05, aprobado)
- `superficies.py` suma a la tabla: deshabilitado (surface-soft + line + muted), fondo del diálogo (`scrim`) y compactos (`control-height-compact`); el hueco «deshabilitado» queda solo para el directorio.
- Subsección «Controles, formularios y diálogos» con 6 reglas y enlace al sistema de diseño; las medidas viven allá.
