# Directorio Manik · avatares sin foto (decisión del usuario 2026-11-04: silueta de médico, mujer u hombre; neutra si no se sabe).
# 3:4 (120 × 160), sobre el degradado foto-inicio → foto-fin; silueta en un solo tono; bata con solapas y estetoscopio.
# Uso: python3 avatares.py → avatares/avatar-{mujer,hombre,neutro}.svg
import os
D = os.path.dirname(os.path.abspath(__file__))
F0, F1, SIL, LINEA = '#CDEEF2', '#FBE7C9', '#93AAB9', '#E9F3F3'
def svg(nombre, pelo, cuerpo_extra):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 160" role="img" aria-label="Sin foto">'
            f'<defs><linearGradient id="g-{nombre}" x1="0" y1="0" x2="0.6" y2="1"><stop offset="0" stop-color="{F0}"/><stop offset="1" stop-color="{F1}"/></linearGradient></defs>'
            f'<rect width="120" height="160" fill="url(#g-{nombre})"/>'
            f'{pelo}'
            f'<path d="M60 96c-11 0-20-10-20-24s9-24 20-24 20 10 20 24-9 24-20 24Z" fill="{SIL}"/>'
            f'<path d="M52 92h16v14H52z" fill="{SIL}"/>'
            f'<path d="M10 160c0-34 20-54 50-54s50 20 50 54Z" fill="{SIL}"/>'
            f'<path d="M50 106 60 128 70 106" fill="none" stroke="{LINEA}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M60 128V160" stroke="{LINEA}" stroke-width="3"/>'
            f'{cuerpo_extra}</svg>')
EST = f'<path d="M44 108c-4 14 0 26 10 30" fill="none" stroke="{LINEA}" stroke-width="2.6" stroke-linecap="round"/><circle cx="56" cy="139" r="3.4" fill="{LINEA}"/>'
PELO_M = f'<path d="M36 74c-2-26 10-40 24-40s26 14 24 40l4 30c-6 5-16 6-28 6s-22-1-28-6Z" fill="#7F97A7"/>'
PELO_H = f'<path d="M40 66c-1-14 8-22 20-22s21 8 20 22c-4-6-10-9-20-9s-16 3-20 9Z" fill="#7F97A7"/>'
os.makedirs(os.path.join(D, 'avatares'), exist_ok=True)
for n, pelo in (('mujer', PELO_M), ('hombre', PELO_H), ('neutro', '')):
    open(os.path.join(D, 'avatares', f'avatar-{n}.svg'), 'w').write(svg(n, pelo, EST))
print('ok')
