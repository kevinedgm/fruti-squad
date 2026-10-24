import sys,math
S=sys.argv[1]
r1=open('../nabi-avatares-ronda-1/gen.py').read()
exec(r1[:r1.index("GL={")])   # FONDOS, cr, tinta, muestra, INK, PERA, W
def mix(a,b,t):
    a=a.lstrip('#'); b=b.lstrip('#'); return '#'+''.join(f'{round(int(a[i:i+2],16)*t+int(b[i:i+2],16)*(1-t)):02X}' for i in (0,2,4))
COAT='M12 132 C12 100 34 86 64 86 C94 86 116 100 116 132Z'
LAPEL='M50 89 L64 112 L78 89'
HAIR={
 'corto':  ('', 'M43 55 C41 32 87 32 85 55 C80 46 72 42 64 42 C56 42 48 46 43 55Z', ''),
 'largo':  ('M41 58 C37 28 91 28 87 58 L89 88 C78 93 50 93 39 88Z', 'M43 56 C42 32 86 32 85 56 C78 45 70 41 60 43 C52 45 46 50 43 56Z', ''),
 'chongo': ('', 'M43 55 C41 34 87 34 85 55 C80 46 72 42 64 42 C56 42 48 46 43 55Z', '<circle cx="64" cy="30" r="10" fill="{F}"/>'),
 'rizado': ('', '', ''.join(f'<circle cx="{64+23*math.cos(math.radians(a)):.1f}" cy="{52+21*math.sin(math.radians(a)):.1f}" r="8.5" fill="{{F}}"/>' for a in range(180,361,30))),
 'lentes': ('', 'M44 52 C44 34 84 34 84 52 C79 44 71 41 64 41 C57 41 49 44 44 52Z', '<g fill="none" stroke="{F}" stroke-width="3"><circle cx="56" cy="57" r="6"/><circle cx="72" cy="57" r="6"/><path d="M62 57 H66"/></g>'),
 'barba':  ('', 'M44 52 C44 34 84 34 84 52 C79 44 71 41 64 41 C57 41 49 44 44 52Z', '<path d="M45 58 C45 80 83 80 83 58 C79 67 72 70 64 70 C56 70 49 67 45 58Z" fill="{F}"/>'),
}
def geo(v,bg):
    F=tinta(bg); M=muestra(bg,F); back,cap,extra=HAIR[v]
    s=''
    if back: s+=f'<path d="{back}" fill="{F}"/>'
    s+=f'<path d="{COAT}" fill="{F}"/><rect x="57" y="70" width="14" height="20" rx="4" fill="{mix(F,bg,.62)}"/>'
    s+=f'<path d="{LAPEL}" fill="none" stroke="{bg}" stroke-width="3.5" stroke-linejoin="round"/><circle cx="90" cy="106" r="5.5" fill="{M}"/>'
    s+=f'<circle cx="64" cy="56" r="20" fill="{mix(F,bg,.62)}"/>'
    if cap: s+=f'<path d="{cap}" fill="{F}"/>'
    s+=extra.replace('{F}',F)
    return s
def linea(v,bg):
    F=tinta(bg); M=muestra(bg,F); back,cap,extra=HAIR[v]; st=f'fill="none" stroke="{F}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"'
    s=''
    if back: s+=f'<path d="{back}" fill="{F}"/>'
    s+=f'<path d="M16 132 C16 102 36 90 64 90 C92 90 112 102 112 132" {st}/><path d="{LAPEL}" {st}/><path d="M58 76 V90 M70 76 V90" {st}/><circle cx="90" cy="106" r="5" fill="{M}"/>'
    s+=f'<circle cx="64" cy="56" r="20" fill="{bg}" stroke="{F}" stroke-width="3.5"/>'
    if cap: s+=f'<path d="{cap}" fill="{F}"/>'
    s+=extra.replace('{F}',F).replace(f'fill="{F}"/>',f'fill="{F}"/>')
    return s
def av(fn,v,bg,size,name=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}" role="img" aria-label="{name}"><defs><clipPath id="c"><circle cx="64" cy="64" r="64"/></clipPath></defs><g clip-path="url(#c)"><rect width="128" height="128" fill="{bg}"/>{fn(v,bg)}</g></svg>'
V=list(HAIR); BGS=[0,3,5,8,6,2]
C=[('A','Geométrica','Formas planas: cabeza, cabello y bata como piezas sólidas en dos tonos de una sola tinta. La bata de laboratorio y su solapa dicen dónde trabaja; el pocillo pera es el gafete.',geo),
   ('B','Línea','Las mismas personas en un solo trazo redondeado, con cabello sólido. Más ligera y editorial; se apoya en el fondo.',linea)]
rows=''
for k,n,t,fn in C:
    people=''.join(f'<div class="u">{av(fn,v,FONDOS[BGS[i]][1],80)}<span>{v}</span></div>' for i,v in enumerate(V))
    sizes=''.join(f'<span class="sz">{av(fn,"chongo",INK,z)}{z}</span>' for z in (40,32,24))
    picker=''.join(f'<span class="sw{" on" if j==0 else ""}">{av(fn,"chongo",bg,40)}</span>' for j,(nm,bg) in enumerate(FONDOS))
    rows+=f'<section><h2>{k} · {n}</h2><p>{t}</p><div class="users">{people}</div><div class="row"><div class="sizes">{sizes}</div><div class="pick"><span class="ov">Elige el fondo</span><div class="sws">{picker}</div></div></div></section>'
    for v in V: open(f'{k}-{v}.svg','w').write(av(fn,v,INK,128))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1100px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}p.i{{margin:0 0 6px;color:#535B70;max-width:960px}}
section{{border-top:1px solid #E2E5EC;padding:20px 0;display:grid;gap:12px}}h2{{margin:0;font-size:17px;font-stretch:125%;color:{INK}}}section p{{margin:0;color:#535B70;max-width:880px}}
.users{{display:flex;gap:26px}}.u{{display:grid;justify-items:center;gap:6px;font-size:12px;color:#535B70}}.row{{display:flex;gap:40px;align-items:end}}
.sizes{{display:flex;gap:14px;align-items:end}}.sz{{display:grid;justify-items:center;gap:4px;font-size:11px;color:#535B70}}
.ov{{font:600 11px Archivo;letter-spacing:.08em;text-transform:uppercase;color:#535B70}}.pick{{display:grid;gap:8px}}.sws{{display:flex;gap:8px}}.sw{{border-radius:50%;padding:2px;border:2px solid transparent;display:block}}.sw svg{{display:block}}.sw.on{{border-color:{INK}}}
</style></head><body><h1>Nabi · avatares · ronda 2 · forma humana</h1><p class="i">Bustos con bata de laboratorio. Seis personas para mostrar la variedad posible; la figura es fija y el usuario solo cambia el fondo. Figura en blanco o azul según el fondo; el gafete pera solo donde se distingue.</p>{rows}</body></html>""")
print('ok')
