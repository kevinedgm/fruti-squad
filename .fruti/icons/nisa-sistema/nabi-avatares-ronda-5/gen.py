import sys
S=sys.argv[1]
r4=open('../nabi-avatares-ronda-4/gen.py').read()
exec(r4[:r4.index("V=[")])   # FONDOS (gris + 10), col, L, A, INK...
HOMBRE='M0 0 H128 V27 C116 31 104 23 90 26 C78 29 70 21 56 25 C42 29 30 22 18 27 C10 30 4 29 0 31Z'
MUJER_TOP='M0 0 H128 V32 C112 22 90 18 66 30 C48 20 22 22 0 32Z'
MUJER_LADOS='M0 30 C14 27 23 36 25 54 C27 82 20 106 12 128 H0Z M128 30 C114 27 105 36 103 54 C101 82 108 106 116 128 H128Z'
def pelo(bg):
    c=col(bg)
    if c!=W: return INKL
    h=bg.lstrip('#'); return '#'+''.join(f'{round(int(h[i:i+2],16)*0.48):02X}' for i in (0,2,4))
def lentes(c): # en coordenadas de la cara A
    return f'<g fill="none" stroke="{c}" stroke-width="3.2"><circle cx="47" cy="58" r="10"/><circle cx="78" cy="58" r="10"/><path d="M57 57 Q62.5 53.5 68 57" stroke-linecap="round"/></g>'
def av(var,bg,size,uid):
    c=col(bg); hc=pelo(bg); hair=f'<path d="{HOMBRE}" fill="{hc}"/>' if var[0]=='h' else f'<path d="{MUJER_TOP} {MUJER_LADOS}" fill="{hc}"/>'
    face=A(bg)+(lentes(c) if var[1] else '')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}" role="img" aria-label="Avatar">'
            f'<defs><clipPath id="k{uid}"><circle cx="64" cy="64" r="64"/></clipPath></defs><g clip-path="url(#k{uid})"><rect width="128" height="128" fill="{bg}"/>{hair}'
            f'<g transform="translate(64 68) scale(1.2) translate(-63 -66)">{face}</g></g></svg>')
VARS=[(('h',False),'Hombre'),(('h',True),'Hombre con lentes'),(('m',False),'Mujer'),(('m',True),'Mujer con lentes')]
uid=[0]
def nx(): uid[0]+=1; return uid[0]
big=''.join(f'<div class="u">{av(v,FONDOS[0][1],120,nx())}<span>{n}</span></div>' for v,n in VARS)
grid=''.join(f'<div class="rw"><span class="lb">{n}</span>'+''.join(f'<span title="{fn}">{av(v,bg,46,nx())}</span>' for fn,bg in FONDOS)+'</div>' for v,n in VARS)
sizes=''.join(f'<div class="rw"><span class="lb">{n}</span>'+''.join(f'<span class="sz">{av(v,FONDOS[1][1],z,nx())}<i>{z}</i></span>' for z in (48,40,32,24))+'</div>' for v,n in VARS)
ctx=''.join(f'<div class="li">{av(v,FONDOS[i][1],32,nx())}<span><b>{n}</b> {a}</span></div>' for v,n,a,i in [(('h',True),'Jorge Hernández','capturó <span class="m">0.0124 mg/L</span> · Plomo',4),(('m',False),'Lucía Méndez','envió el lote <span class="m">L-2026-10-147</span> a revisión',9),(('m',True),'Mariana Ruiz','liberó <span class="m">NN-26-00417</span>',1),(('h',False),'Óscar Zárate','rechazó la muestra <span class="m">NN-26-00412</span>',8)])
for (v,n) in VARS: open(f'{n.lower().replace(" ","-")}.svg','w').write(av(v,FONDOS[0][1],128,nx()))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}@font-face{{font-family:'Plex';src:url('file://{S}/fuentes/IBMPlexMono.ttf')}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1100px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}p.i{{margin:0 0 18px;color:#535B70;max-width:960px}}
.big{{display:flex;gap:36px;margin-bottom:20px}}.u{{display:grid;justify-items:center;gap:8px;font-size:13px}}
h2{{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#535B70;margin:18px 0 8px;border-top:1px solid #E2E5EC;padding-top:14px}}
.rw{{display:flex;gap:8px;align-items:center;margin:6px 0}}.rw svg{{display:block}}.lb{{width:150px;font-size:13px;color:#535B70}}.sz{{display:grid;justify-items:center;gap:2px;margin-right:12px}}.sz i{{font-style:normal;font-size:11px;color:#535B70}}
.li{{display:flex;gap:12px;align-items:center;margin:8px 0}}.m{{font-family:Plex,monospace;font-feature-settings:"zero"}}
</style></head><body><h1>Nabi · avatares · ronda 5 · cara A en cuatro variantes</h1><p class="i">La misma cara mínima, con cabello para distinguir hombre y mujer y lentes opcionales. El cabello es una masa sólida recortada por el círculo: tinta sobre fondos claros y un tono más oscuro del propio fondo sobre los oscuros. El usuario solo elige el fondo.</p>
<div class="big">{big}</div><h2>Los once fondos</h2>{grid}<h2>Tamaños</h2>{sizes}<h2>En la actividad del sistema</h2>{ctx}</body></html>""")
print('ok')
