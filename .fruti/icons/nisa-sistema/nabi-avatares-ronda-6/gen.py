import sys
S=sys.argv[1]
INK='#052A76'
FONDOS=[('Grafito','#8E929C'),('Azul real','#052A76'),('Azul medio','#3D67AE'),('Cian','#0A9BBE'),('Verde','#006D53'),('Verde claro','#2E9A2A'),('Pera','#A9B91C'),('Naranja','#E07B00'),('Café','#553739'),('Morado','#3D0066')]
def hx(h): h=h.lstrip('#'); return [int(h[i:i+2],16) for i in (0,2,4)]
def mix(a,b,t): A,B=hx(a),hx(b); return '#'+''.join(f'{round(x*t+y*(1-t)):02X}' for x,y in zip(A,B))
light=lambda c,t: mix('#FFFFFF',c,t); dark=lambda c,t: mix('#000000',c,t)
# geometría (caja 128): cabeza centrada en 64,52; hombros con hueco de cuello
SH='M18 132 C18 106 38 92 64 92 C90 92 110 106 110 132Z'
HEAD=(64,53,21)
HAIR_H='M42.5 52 C41 33 51 25.5 64.5 25.5 C79 25.5 88 33.5 85.6 51 C83.4 43.5 77.5 39.5 69 40.5 C60 41.5 52 40 46.5 36 C44.5 40.5 43.5 46 42.5 52Z'
HAIR_M_BACK='M39.5 58 C36.5 32 49 23.5 64 23.5 C79 23.5 91.5 32 88.5 58 C89 67 90.5 75 88.6 80.5 C86.6 85.5 80.6 86.2 77.4 82.4 L50.6 82.4 C47.4 86.2 41.4 85.5 39.4 80.5 C37.5 75 39 67 39.5 58Z'
HAIR_M_TOP='M42.6 51 C43 38 52 31 64 31 C70 31 75 33 79 37 C76 41 69 44 60 45 C53 46 47 48 42.6 51Z'
def glasses(c,w=2.2):
    return f'<g fill="none" stroke="{c}" stroke-width="{w}"><rect x="47.5" y="49" width="13" height="10" rx="5"/><rect x="67.5" y="49" width="13" height="10" rx="5"/><path d="M60.5 52.5 Q64 50.5 67.5 52.5"/></g>'
def figA(var,bg):  # silueta monocroma tipo Contactos
    f='#FFFFFF'; cut=mix(bg,'#FFFFFF',0.0)
    s=f'<path d="{SH}" fill="{f}" fill-opacity=".92"/>'
    if var[0]=='m': s+=f'<path d="{HAIR_M_BACK}" fill="{f}" fill-opacity=".92"/>'
    s+=f'<circle cx="{HEAD[0]}" cy="{HEAD[1]}" r="{HEAD[2]}" fill="{f}"/>'
    if var[0]=='h': s+=f'<path d="{HAIR_H}" fill="{f}"/>'
    if var[1]: s+=glasses(bg)
    return s
def figB(var,bg):  # retrato a dos tonos: cara y hombros claros, cabello oscuro, rasgos mínimos
    face='#FFFFFF'; hair=dark(bg,.55); feat=dark(bg,.62)
    s=f'<path d="{SH}" fill="{face}" fill-opacity=".94"/>'
    if var[0]=='m': s+=f'<path d="{HAIR_M_BACK}" fill="{hair}"/>'
    s+=f'<circle cx="64" cy="53" r="21" fill="{face}"/>'
    s+=f'<path d="{HAIR_H if var[0]=="h" else HAIR_M_TOP}" fill="{hair}"/>'
    s+=f'<circle cx="56.5" cy="55" r="1.9" fill="{feat}"/><circle cx="71.5" cy="55" r="1.9" fill="{feat}"/>'
    s+=f'<path d="M64.5 57 L62.2 63.4 L65.4 63.6" fill="none" stroke="{feat}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M60.5 67.8 Q64 69.6 67.5 67.8" fill="none" stroke="{feat}" stroke-width="1.6" stroke-linecap="round"/>'
    if var[1]: s+=glasses(feat,1.8).replace('y="49"','y="50"')
    return s
def av(fig,var,bg,size,uid):
    g=f'g{uid}'; k=f'k{uid}'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}" role="img" aria-label="Avatar"><defs>'
            f'<linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{light(bg,.22)}"/><stop offset="1" stop-color="{dark(bg,.08)}"/></linearGradient>'
            f'<clipPath id="{k}"><circle cx="64" cy="64" r="64"/></clipPath></defs><g clip-path="url(#{k})"><rect width="128" height="128" fill="url(#{g})"/><g transform="translate(64 78) scale(1.17) translate(-64 -78)">{fig(var,bg)}</g></g></svg>')
VARS=[(('h',False),'Hombre'),(('h',True),'Hombre con lentes'),(('m',False),'Mujer'),(('m',True),'Mujer con lentes')]
n=[0]
def u(): n[0]+=1; return n[0]
D=[('A','Silueta','Como Contactos de iOS: una sola figura blanca sobre un degradado del color elegido. Sin rasgos: hombre y mujer se distinguen solo por la silueta del cabello; los lentes son el único corte. Sobria, atemporal.',figA),
   ('B','Retrato mínimo','La misma geometría a dos tonos: cara clara, cabello en un tono profundo del fondo y rasgos mínimos (ojos, nariz, boca) de 1.6 px.',figB)]
html=''
for k,nm,t,fig in D:
    big=''.join(f'<div class="u">{av(fig,v,FONDOS[i][1],132,u())}<span>{lab}</span></div>' for (v,lab),i in zip(VARS,[1,4,9,2]))
    grid=''.join(f'<div class="rw"><span class="lb">{lab}</span>'+''.join(f'<span title="{fn}">{av(fig,v,bg,46,u())}</span>' for fn,bg in FONDOS)+'</div>' for v,lab in VARS)
    sizes=''.join(f'<span class="sz">{av(fig,VARS[2][0],FONDOS[1][1],z,u())}<i>{z}</i></span>' for z in (64,40,32,24))
    html+=f'<section><h2>{k} · {nm}</h2><p>{t}</p><div class="big">{big}</div>{grid}<div class="rw"><span class="lb">Tamaños</span>{sizes}</div></section>'
    for v,lab in VARS: open(f'{k}-{lab.lower().replace(" ","-")}.svg','w').write(av(fig,v,FONDOS[1][1],128,u()))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1100px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}p.i{{margin:0 0 6px;color:#535B70;max-width:960px}}
section{{border-top:1px solid #E2E5EC;padding:20px 0;display:grid;gap:12px}}h2{{margin:0;font-size:17px;font-stretch:125%;color:{INK}}}section p{{margin:0;color:#535B70;max-width:900px}}
.big{{display:flex;gap:34px;margin:6px 0 10px}}.u{{display:grid;justify-items:center;gap:8px;font-size:13px}}.u svg{{filter:drop-shadow(0 6px 14px rgba(5,42,118,.18))}}
.rw{{display:flex;gap:8px;align-items:center}}.rw svg{{display:block}}.lb{{width:150px;font-size:13px;color:#535B70}}.sz{{display:grid;justify-items:center;gap:2px;margin-right:14px}}.sz i{{font-style:normal;font-size:11px;color:#535B70}}
</style></head><body><h1>Nabi · avatares · ronda 6 · como si lo hubiera diseñado Apple</h1><p class="i">Geometría precisa, una sola figura por variante y fondo con degradado suave del color que elige el usuario. Hombre y mujer se distinguen por la silueta del cabello; los lentes son dos aros finos.</p>{html}</body></html>""")
print('ok')
