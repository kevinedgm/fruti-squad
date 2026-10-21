# CLNDA · ronda 8: tres maneras de combinar índigo (1) y lima (5) en C1.
import sys
S=sys.argv[1]
BG='#f5f6fb'; INK='#0e0f1c'; IND='#4338ca'; INDD='#8b8cf8'; LIMA='#c6f23d'; OLIVA='#4d7c0f'
def L(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def C(a,b): x,y=L(a),L(b); return (max(x,y)+.05)/(min(x,y)+.05)
BR='M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
def sym(ll,pt): return svg(f'<path d="{BR}" stroke="{ll}" stroke-width="7" transform="translate(-3 0)"/><circle cx="46" cy="32" r="6.5" fill="{pt}"/>')
def app(bg,ll,pt): return svg(f'<rect width="512" height="512" rx="112" fill="{bg}"/><g transform="translate(80 80) scale(5.5)">{sym(ll,pt).split(">",1)[1].rsplit("</svg>",1)[0]}</g>','0 0 512 512')
# A · índigo lleva la llave; lima es el dato (solo en oscuro). En claro el dato vuelve a tinta y la lima vive en la interfaz.
# B · lima lleva la llave en oscuro, índigo la lleva en claro: un color por modo; el dato siempre en tinta/papel.
# C · índigo la llave en ambos modos; lima solo en el cursor del logotipo y en acentos de interfaz.
O=[('A · índigo llave, lima dato',   (INDD,LIMA,LIMA), (IND,INK,IND),  'La lima es el dato: en oscuro brilla; en claro el dato vuelve a tinta y la lima queda para la interfaz (botones, enlaces, gráficas).'),
   ('B · un color por modo',         (LIMA,BG,LIMA),   (IND,INK,IND),  'Oscuro: lima. Claro: índigo. El símbolo es el mismo; el color cambia con el tema, como un IDE.'),
   ('C · índigo marca, lima cursor', (INDD,BG,LIMA),   (IND,INK,OLIVA),'Índigo es la marca en ambos modos; la lima aparece solo en el cursor del logotipo y en la interfaz. La más estable.')]
sg=S+'/fuentes/SpaceGrotesk[wght].ttf'; jb=S+'/fuentes/JetBrainsMono.ttf'
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}} @font-face{{font-family:JB;src:url("file://{jb}");font-weight:100 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 SG,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
.sub{{color:#666;margin:0 0 16px}} .p{{display:grid;grid-template-columns:230px 1fr 1fr;border:1px solid #e5e5e5;border-radius:12px;overflow:hidden;margin-bottom:16px}}
.p>div{{padding:18px;display:grid;gap:12px;align-content:start;min-width:0}} h2{{font:700 17px SG;margin:0}} .tag{{font:400 12px;color:#666}} .num{{font-family:JB,monospace;font-size:11px}}
.sw{{display:flex;gap:8px}} .sw i{{display:block;width:40px;height:40px;border-radius:8px;border:1px solid rgba(0,0,0,.08)}}
.fila{{display:flex;gap:14px;align-items:center}} .fila span{{display:block}} .fila svg{{width:100%;height:100%}}
.wm{{display:flex;align-items:center;gap:10px}} .wm svg{{width:36px;height:36px}} .wm b{{font:700 32px SG;letter-spacing:-.02em}} .cur{{display:inline-block;width:.6em;height:1em;border-radius:3px;vertical-align:-.12em;margin-left:.1em}}
.ui{{display:flex;gap:10px;align-items:center;font:500 13px SG}} .btn{{padding:7px 12px;border-radius:7px;font-weight:700}} .lnk{{text-decoration:underline}}
.gh{{display:flex;gap:10px;align-items:center;background:#0d1117;color:#e6edf3;padding:10px;border-radius:8px;font:13px system-ui}} .gh span{{width:36px;height:36px;border-radius:50%;overflow:hidden;display:block}} .gh b{{display:block}} .gh small{{color:#8b949e}}
.firma{{font:500 12px JB;display:flex;align-items:center;gap:6px;opacity:.8}} .firma svg{{width:14px;height:14px}}'''
rows=''
for name,(dl,dp,dc),(ll,lp,lc),nota in O:
    rows+=f'''<div class="p"><div><h2>{name}</h2><div class="sw"><i style="background:{INK}"></i><i style="background:{BG}"></i><i style="background:{IND}"></i><i style="background:{LIMA}"></i></div><span class="tag">{nota}</span><span class="num">oscuro: llave/fondo {C(dl,INK):.1f}:1 · dato/fondo {C(dp,INK):.1f}:1<br>claro: llave/fondo {C(ll,BG):.1f}:1 · cursor/fondo {C(lc,BG):.1f}:1</span></div>
<div style="background:{INK};color:{BG}"><div class="fila"><span style="width:96px;height:96px">{sym(dl,dp)}</span><span style="width:24px;height:24px">{sym(dl,dp)}</span><span style="width:16px;height:16px">{sym(dl,dp)}</span><span style="width:72px;height:72px">{app(INK,dl,dp)}</span></div><div class="wm">{sym(dl,dp)}<b style="color:{BG}">CLNDA<span class="cur" style="background:{dc}"></span></b></div>
<div class="ui"><span class="btn" style="background:{LIMA};color:{INK}">Ver trabajo</span><span class="btn" style="background:{INDD};color:{INK}">Contacto</span><span class="lnk" style="color:{LIMA}">clnda.studio</span></div><div class="gh"><span>{app(INK,dl,dp)}</span><div><b>clnda-studio</b><small>Software y ciencia de datos · Oaxaca</small></div></div></div>
<div style="background:{BG};color:{INK}"><div class="fila"><span style="width:96px;height:96px">{sym(ll,lp)}</span><span style="width:24px;height:24px">{sym(ll,lp)}</span><span style="width:16px;height:16px">{sym(ll,lp)}</span><span style="width:72px;height:72px">{app(BG,ll,lp)}</span></div><div class="wm">{sym(ll,lp)}<b>CLNDA<span class="cur" style="background:{lc}"></span></b></div>
<div class="ui"><span class="btn" style="background:{IND};color:#fff">Ver trabajo</span><span class="btn" style="background:{LIMA};color:{INK}">Contacto</span><span class="lnk" style="color:{IND}">clnda.studio</span></div><div class="firma">{sym(ll,lp)}hecho por CLNDA Studio</div></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">CLNDA · ronda 8 · índigo + lima: tres repartos. Oscuro primero. Debajo de cada lockup, cómo se ven los dos colores en botones, enlace, avatar de GitHub y firma.</p>{rows}')
print('ok')
