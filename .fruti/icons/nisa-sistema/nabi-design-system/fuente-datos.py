# NisaLab · la fuente de datos pasa de IBM Plex Mono a Google Sans Code (decisión 2026-11-05: la que ya usa bitácoras en producción).
# Comprobado antes de cambiar: cifras de ancho fijo (todas 20.4 px a 34 px), cero con barra de fábrica, pesos 300–800, tiene µ ± ≤ ≥ °.
# Uso: python3 fuente-datos.py <carpeta del design system>. Idempotente.
import sys, glob, os
root = sys.argv[1]
REEMPLAZOS = [
 ('- **IBM Plex Mono** (`datos`). Para valores y resultados de análisis. Cifras de ancho fijo, para que las columnas se alineen solas; cero con barra (`font-feature-settings: "zero"`) para no confundir 0 con O; tiene µ, ±, ×, ≤, ≥, ° y superíndices.',
  '- **Google Sans Code** (`datos`). Para valores y resultados de análisis. Cifras de ancho fijo, para que las columnas se alineen solas; cero con barra de fábrica para no confundir 0 con O; tiene µ, ±, ×, ≤, ≥ y °. Es la que ya usa bitácoras en producción.'),
 ('- **IBM Plex Mono** se conserva aunque el manual no la incluye: el manual no cubre datos tabulares y Poppins no alinea cifras en columna.',
  '- **Google Sans Code** se usa aunque el manual de Nisa Nabani no la incluye: el manual no cubre datos tabulares y Poppins no alinea cifras en columna.'),
 ('`IBM Plex Mono:wght@400;500;600`', '`Google Sans Code:wght@400;500;600`'),
 ('IBM Plex Mono con cero con barra (font-feature-settings: \\"zero\\").', 'Google Sans Code: cifras de ancho fijo y cero con barra de fábrica.'),
 ('IBM+Plex+Mono:wght@400;500;600', 'Google+Sans+Code:wght@400;500;600'),
 ('\\"IBM Plex Mono\\"', '\\"Google Sans Code\\"'),
 ('"IBM Plex Mono"', '"Google Sans Code"'),
 ('IBM Plex Mono', 'Google Sans Code'),
 ('Plex Mono', 'Google Sans Code'),
]
fs = [os.path.join(root, f) for f in ('tokens.json', 'README.md', 'valores.md', 'modulos.md')] + glob.glob(os.path.join(root, 'components', '*', '*.*'))
for f in fs:
    if not os.path.exists(f): continue
    s = open(f).read(); s2 = s
    for a, b in REEMPLAZOS: s2 = s2.replace(a, b)
    if s2 != s: open(f, 'w').write(s2); print('ok', os.path.relpath(f, root))
