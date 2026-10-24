import sys
S=sys.argv[1]
r1=open('../nabi-avatares-ronda-1/gen.py').read()
exec(r1[:r1.index("GL={")])   # FONDOS, cr, tinta, muestra, INK, PERA, W
FONDOS=[('Gris','#D9DCE3')]+FONDOS
INKL='#121826'
def col(bg): return W if cr(W,bg)>=cr(INKL,bg) else INKL
def L(d,c,w=4.2): return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
NARIZ='M88 50 C82 44 72 45 68 52 L59 80 L68 81.5'
def A(bg):  # fiel a la referencia
    c=col(bg); return L('M38 51 Q46 43 55 49',c)+f'<circle cx="47" cy="58" r="3.4" fill="{c}"/><circle cx="78" cy="58" r="3.4" fill="{c}"/>'+L(NARIZ,c)+L('M57 93 L71 92',c)
def B(bg):  # ojos de pocillo; el derecho es la muestra
    c=col(bg); m=PERA if cr(PERA,bg)>=2.2 else c
    return L('M38 50 Q46 43 55 48',c)+f'<circle cx="47" cy="59" r="5.2" fill="{c}"/><circle cx="78" cy="59" r="5.2" fill="{m}"/>'+L(NARIZ,c)+L('M57 93 L71 92',c)
def C(bg):  # sonrisa: cejas arqueadas, boca curva
    c=col(bg); return L('M38 51 Q46 43 55 49',c)+L('M74 49 Q82 43 90 50',c)+f'<circle cx="47" cy="58" r="3.4" fill="{c}"/><circle cx="81" cy="58" r="3.4" fill="{c}"/>'+L('M66 54 L59 80 L68 81.5',c)+L('M54 91 Q63 98 73 90',c)
def D(bg):  # lentes de laboratorio
    c=col(bg); m=PERA if cr(PERA,bg)>=2.2 else c
    return L('M37 46 L53 44',c,3.6)+L('M73 44 L89 46',c,3.6)+f'<circle cx="46" cy="59" r="10.5" fill="none" stroke="{c}" stroke-width="3.6"/><circle cx="80" cy="59" r="10.5" fill="none" stroke="{c}" stroke-width="3.6"/>'+L('M56.5 58 Q63 54 69.5 58',c,3.6)+f'<circle cx="46" cy="60" r="3" fill="{c}"/><circle cx="80" cy="60" r="3" fill="{m}"/>'+L('M66 66 L60 82 L68 83',c)+L('M57 95 L71 94',c)
def av(fn,bg,size):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}" role="img" aria-label="Avatar"><circle cx="64" cy="64" r="64" fill="{bg}"/><g transform="translate(64 66) scale(1.22) translate(-63 -69)">{fn(bg)}</g></svg>'
V=[('A','Fiel','La cara de la referencia: una ceja suelta, la otra baja y se vuelve nariz, dos ojos de punto y una boca corta.',A),
   ('B','Pocillos','Los ojos son pocillos; el derecho es la muestra pera cuando el fondo la deja ver. Une la cara con el símbolo de Nabi.',B),
   ('C','Sonrisa','Dos cejas arqueadas, nariz angular aparte y una boca que sonríe. Más amable.',C),
   ('D','Lentes','Lentes de laboratorio redondos con un ojo pera. La más propia del oficio.',D)]
rows=''
for k,n,t,fn in V:
    sws=''.join(f'<span class="sw{" on" if j==0 else ""}" title="{nm}">{av(fn,bg,52)}</span>' for j,(nm,bg) in enumerate(FONDOS))
    sizes=''.join(f'<span class="sz">{av(fn,FONDOS[0][1],z)}{z}</span>' for z in (96,40,32,24))
    rows+=f'<section><div class="hd"><h2>{k} · {n}</h2><p>{t}</p></div><div class="row"><div class="sizes">{sizes}</div><div class="sws">{sws}</div></div></section>'
    open(f'{k}.svg','w').write(av(fn,FONDOS[0][1],128))
ctx=''.join(f'<div class="li">{av(B,FONDOS[i][1],32)}<span><b>{n}</b> {a}</span></div>' for n,a,i in [('Jorge Hernández','capturó <span class="m">0.0124 mg/L</span> · Plomo',4),('Óscar Zárate','envió el lote <span class="m">L-2026-10-147</span> a revisión',9),('Mariana Ruiz','liberó <span class="m">NN-26-00417</span>',1)])
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}@font-face{{font-family:'Plex';src:url('file://{S}/fuentes/IBMPlexMono.ttf')}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1180px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}p.i{{margin:0 0 6px;color:#535B70;max-width:980px}}
section{{border-top:1px solid #E2E5EC;padding:18px 0;display:grid;gap:12px}}.hd{{display:flex;gap:16px;align-items:baseline}}h2{{margin:0;font-size:17px;font-stretch:125%;color:{INK};white-space:nowrap}}.hd p{{margin:0;color:#535B70}}
.row{{display:flex;gap:30px;align-items:center}}.sizes{{display:flex;gap:12px;align-items:end}}.sz{{display:grid;justify-items:center;gap:4px;font-size:11px;color:#535B70}}.sws{{display:flex;gap:6px;flex-wrap:wrap;max-width:720px}}.sw{{border-radius:50%;padding:2px;border:2px solid transparent;display:block}}.sw svg{{display:block}}.sw.on{{border-color:{INK}}}
.ctx{{border-top:1px solid #E2E5EC;padding-top:14px;display:grid;gap:10px}}.li{{display:flex;gap:12px;align-items:center}}.m{{font-family:Plex,monospace;font-feature-settings:"zero"}}
</style></head><body><h1>Nabi · avatares · ronda 4 · la cara mínima</h1><p class="i">Una sola cara para todos, de pocos trazos, como la de Notion. El usuario solo elige el fondo: gris por defecto y los diez colores de Nisa Nabani. La línea cambia sola a blanco o tinta según el fondo.</p>{rows}<div class="ctx">{ctx}</div></body></html>""")
print('ok')
