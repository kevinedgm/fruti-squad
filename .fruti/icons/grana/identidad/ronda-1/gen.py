# Grana · identidad, ronda 1: tres conceptos de símbolo. Lienzo 48.
# Color del tema: --g-color-brand (por defecto carmín #a3123a). Estructura: currentColor (tinta).
import math
COLOR='var(--g-color-brand,#a3123a)'
def svg(id_,body,desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Grana" class="grana-{id_}">\n'
            f'  <!-- Grana · {desc} -->\n{body}</svg>\n')
V={}
# A · ARMAZÓN: cochinilla vista desde arriba. Capa de color desplazada (tinte) + estructura en tinta encima.
body_d='M24 9C31.5 9 36.5 15.5 36.5 25.5C36.5 35 31 41 24 41C17 41 11.5 35 11.5 25.5C11.5 15.5 16.5 9 24 9Z'
A=(f'  <path d="{body_d}" fill="{COLOR}" transform="translate(2.6 2.6)"/>\n'
   f'  <g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">\n'
   f'    <path d="{body_d}"/>\n'
   f'    <path d="M12.6 20.5Q24 23.5 35.4 20.5M11.8 28Q24 31 36.2 28M13.6 35Q24 37.8 34.4 35"/>\n'
   f'    <path d="M20.5 9.6 17.5 4.5M27.5 9.6 30.5 4.5"/>\n  </g>\n')
V['a-armazon']=(A,'armazón: la estructura en tinta es fija; el tinte del tema va detrás, desplazado como una impresión')
# B · G-GOTA: la «g» minúscula. Panza = cuerpo de la cochinilla (color, con bandas); asta en tinta; la cola termina en una gota de tinte.
B=(f'  <defs><mask id="grana-b-bandas"><rect width="48" height="48" fill="#fff"/><path d="M8 16.5H32M8 22.5H32" stroke="#000" stroke-width="2.4"/></mask></defs>\n'
   f'  <circle cx="20" cy="19.5" r="11" fill="{COLOR}" mask="url(#grana-b-bandas)"/>\n'
   f'  <path d="M34.5 9V30.5C34.5 38.5 29.5 42.5 22.5 42.5C18 42.5 15 41 13.2 38.6" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>\n'
   f'  <path d="M9.6 34.2C9.6 34.2 6.4 38.2 6.4 40.3A3.2 3.2 0 0 0 12.8 40.3C12.8 38.2 9.6 34.2 9.6 34.2Z" fill="{COLOR}"/>\n')
V['b-g-gota']=(B,'g-gota: la «g» de grana; su panza es la cochinilla con bandas y su cola suelta una gota de tinte')
# C · COMPONENTES: el cuerpo son cuatro píldoras apiladas (botones, campos) que forman el óvalo del insecto.
pills=[(16,10.5),(28,18.5),(30,26.5),(22,34.5)]
C=''.join(f'  <rect x="{24-w/2:g}" y="{y-3.5:g}" width="{w:g}" height="7" rx="3.5" fill="{COLOR}"/>\n' for w,y in pills)
C+=('  <path d="M20.5 6.5 17.5 2.8M27.5 6.5 30.5 2.8" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>\n'
    '  <circle cx="24" cy="42.5" r="2.6" fill="currentColor"/>\n')
V['c-componentes']=(C,'componentes: el insecto está hecho de cuatro píldoras apiladas, como botones y campos; antenas en tinta y una gota al final')
for k,(b,d) in V.items(): open(f'{k}.svg','w').write(svg(k,b,d))
# banco
TEMAS=[('carmín','#a3123a'),('azul','#2563eb'),('verde','#0f8a5f'),('violeta','#7c3aed'),('ámbar','#b45309')]
rows=''
for k in V:
    s=open(f'{k}.svg').read()
    sz=''.join(f'<span style="display:inline-flex;width:{max(z,40)+8}px;justify-content:center">{s.replace("<svg ",f"<svg width={z} height={z} ",1)}</span>' for z in (16,24,32,48,64,128))
    th=''.join(f'<span style="display:inline-flex;gap:6px;align-items:center;padding:6px 10px;border:1px solid #e5e5e5;border-radius:10px;--g-color-brand:{c};color:#1a1a1a">{s.replace("<svg ","<svg width=32 height=32 ",1)}<small>{n}</small></span>' for n,c in TEMAS)
    dk=f'<span style="display:inline-flex;padding:8px;border-radius:10px;background:#141414;color:#f5f5f5;--g-color-brand:#ff4d7a">{s.replace("<svg ","<svg width=48 height=48 ",1)}</span>'
    mono=f'<span style="display:inline-flex;padding:8px;--g-color-brand:currentColor;color:#1a1a1a">{s.replace("<svg ","<svg width=48 height=48 ",1)}</span>'
    rows+=f'<section style="padding:14px 18px;border-bottom:1px solid #eee"><b style="font:600 14px sans-serif">{k}</b><div style="display:flex;align-items:flex-end;gap:4px;margin:8px 0;color:#1a1a1a">{sz}</div><div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">{th}{dk}{mono}<small style="font:11px sans-serif;color:#666">oscuro · una tinta</small></div></section>'
open('banco.html','w').write(f'<html><body style="margin:0;background:#fafaf9;font:12px sans-serif">{rows}</body></html>')
