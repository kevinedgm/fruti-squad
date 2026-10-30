# NisaLab · símbolos, ronda 2: solo opciones que pasan seis pruebas de riesgo.
# Uso: python3 gen.py [carpeta-fuentes] → simbolos.html y svg/
import os, sys

H = os.path.dirname(os.path.abspath(__file__))
AZ, PE, W = '#052A76', '#C2D225', '#FFFFFF'

def petri(a=AZ, p=PE):  # caja de Petri vista desde arriba con tres colonias
    return (f'<circle cx="50" cy="50" r="42" fill="none" stroke="{a}" stroke-width="10"/>'
            f'<circle cx="37" cy="38" r="9" fill="{a}"/><circle cx="61" cy="57" r="14" fill="{p}"/><circle cx="36" cy="66" r="6" fill="{a}"/>')
def gel(a=AZ, p=PE):  # dos carriles de electroforesis con bandas a distinta altura
    lanes = ''.join(f'<rect x="{x}" y="4" width="38" height="92" rx="12" fill="none" stroke="{a}" stroke-width="8"/>' for x in (6, 56))
    bands = (f'<rect x="16" y="22" width="18" height="9" rx="4.5" fill="{a}"/><rect x="16" y="62" width="18" height="9" rx="4.5" fill="{a}"/>'
             f'<rect x="66" y="40" width="18" height="11" rx="5.5" fill="{p}"/><rect x="66" y="74" width="18" height="9" rx="4.5" fill="{a}"/>')
    return lanes + bands
def colonia(a=AZ, p=PE):  # células agrupadas, una destacada
    return (f'<circle cx="34" cy="62" r="24" fill="{a}"/><circle cx="68" cy="36" r="22" fill="{p}"/><circle cx="72" cy="76" r="14" fill="{a}"/>'
            f'<circle cx="32" cy="22" r="11" fill="{a}"/>')

C = [
    ('Petri', petri, 'La caja de Petri vista desde arriba, con tres colonias; la que creció es pera. Es el objeto más reconocible de un laboratorio de calidad y casi ningún software lo usa como marca.'),
    ('Gel', gel, 'Dos carriles de electroforesis con bandas a distinta altura: comparar muestras y ver el resultado. Es el patrón visual del análisis.'),
    ('Colonia', colonia, 'Cuatro células agrupadas, una en pera: lo vivo que el laboratorio detecta y cuenta. Es la más orgánica y la más cálida.'),
]
PRUEBAS = ['No es un ícono común de interfaz', 'No se confunde con algo con otra carga', 'Se lee a 16 px', 'No se parece a Nisa, al matraz ni a las divisiones', 'Significado de laboratorio en una frase', 'Funciona a una tinta']

def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 108 108">{body}</svg>'
def inl(s, h):
    return s.replace('<svg ', f'<svg style="height:{h}px;width:auto;display:block" aria-hidden="true" ', 1)

os.makedirs(os.path.join(H, 'svg'), exist_ok=True)
cards = ''
for i, (nom, fn, que) in enumerate(C, 1):
    s = svg(fn())
    open(os.path.join(H, 'svg', f'{i}-{nom.lower()}.svg'), 'w').write(s)
    tinta = svg(fn('#141B33', '#141B33'))
    blanco = svg(fn(W, PE))
    checks = ''.join(f'<li>{t}</li>' for t in PRUEBAS)
    cards += (f'<article><div class="big">{inl(s, 150)}</div><h2>{nom}</h2><p>{que}</p>'
              f'<div class="lk">{inl(s, 52)}<div><span class="wm"><b>Nisa</b>Lab</span><small>de Nisa Nabani</small></div></div>'
              f'<div class="sm"><span class="tile">{inl(blanco, 34)}</span>{inl(tinta, 32)}{inl(s, 24)}{inl(s, 16)}</div>'
              f'<ul class="ok">{checks}</ul></article>')

F = sys.argv[1] if len(sys.argv) > 1 else None
fuentes = ('<style>' + ''.join(f"@font-face{{font-family:Poppins;src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 600, 700)) + '</style>'
           if F else '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap">')
html = f'''<title>NisaLab · símbolos 2</title>
<meta name="claude:viewport-fit-sides" content="cover">
{fuentes}
<style>
/* Tres opciones que pasan seis pruebas: blanco, tinta y azul real; Poppins como en el manual. */
:root{{--az:{AZ};--fg:#141B33;--muted:#535B70;--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{margin:0;background:#fff;color:var(--fg);font:16px/1.5 Poppins,system-ui,sans-serif;padding-block:0 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1120px;margin:0 auto}} header{{padding:40px 0 22px;display:grid;gap:8px}} h1{{margin:0;font:700 clamp(28px,5vw,42px)/1.1 Poppins,sans-serif;letter-spacing:-.02em}} header p{{margin:0;color:var(--muted);max-width:74ch}}
.g{{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}}
article{{border:1px solid var(--line);border-radius:20px;padding:18px;display:grid;gap:8px;align-content:start}} .big{{display:grid;place-items:center;background:var(--sunk);border-radius:16px;height:200px}}
h2{{margin:6px 0 0;font:700 22px/1.2 Poppins,sans-serif}} article p{{margin:0;font-size:14px;color:var(--muted);line-height:1.5}}
.lk{{display:flex;align-items:center;gap:12px;margin-top:6px}} .wm{{font-size:26px;color:var(--az);line-height:1;display:block}} .wm b{{font-weight:700}} .lk small{{font-size:12px;color:var(--muted)}}
.sm{{display:flex;align-items:center;gap:14px;margin-top:4px}} .tile{{display:grid;place-items:center;width:48px;height:48px;border-radius:12px;background:var(--az)}}
.ok{{list-style:none;margin:6px 0 0;padding:12px 14px;background:#EEF4D6;border-radius:12px;display:grid;gap:4px;font-size:13px}} .ok li::before{{content:"✓ ";color:#3D5A00;font-weight:700}}
.nota{{margin-top:22px;background:var(--sunk);border-radius:16px;padding:16px 18px;font-size:14px;color:var(--muted)}}
</style>
<main><header><h1>Tres símbolos que pasan las seis pruebas</h1><p>De unas quince ideas, solo estas tres pasaron todas las pruebas. Las demás fallaron en alguna: la cubeta parece una batería, los portaobjetos parecen el ícono de copiar, la pipeta parece un signo de alerta y el pocillo con muestra parece un ojo.</p></header>
<div class="g">{cards}</div>
<p class="nota">Lo que no puedo comprobar desde aquí: el registro de marca en el IMPI. Un símbolo abstracto y propio como estos suele registrarse mejor que un ícono genérico, pero eso lo confirma una búsqueda legal.</p></main>'''
open(os.path.join(H, 'simbolos.html'), 'w').write(html)
print('ok')
