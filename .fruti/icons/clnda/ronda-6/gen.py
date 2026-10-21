# CLNDA · ronda 6: paletas sobrias para C1. Cada paleta: fondo, tinta, un acento (llave y cursor) y su versión sobre oscuro.
import sys
S=sys.argv[1]
def L(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def C(a,b): x,y=L(a),L(b); return (max(x,y)+.05)/(min(x,y)+.05)
P=[('1 · Grafito y cobre','#f4f1ec','#1c1b1f','#b4541f','#e08a5a','Cálida y artesanal: el cobre es el único color.'),
   ('2 · Hueso y bosque','#f5f3ed','#15201c','#1e5c47','#6fbf9f','Verde profundo, serena; se aleja de todo lo tecnológico azul.'),
   ('3 · Marfil y petróleo','#f3f3f0','#111a22','#1c4a5e','#6fb3cc','Azul oscuro y gris: la más corporativa de las cinco.'),
   ('4 · Niebla y ciruela','#f5f4f7','#1b181f','#5a3d73','#b79ad1','Morado apagado: creativa sin ser ruidosa.'),
   ('5 · Monocromo','#f4f4f2','#1a1a1a','#8a8a86','#9a9a96','Solo tinta y gris: la llave en gris, el dato en tinta. Lo más minimalista.')]
BR='M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
def sym(ll,pt): return svg(f'<path d="{BR}" stroke="{ll}" stroke-width="7" transform="translate(-3 0)"/><circle cx="46" cy="32" r="6.5" fill="{pt}"/>')
def app(bg,ll,pt): return svg(f'<rect width="512" height="512" rx="112" fill="{bg}"/><g transform="translate(80 80) scale(5.5)">{sym(ll,pt).split(">",1)[1].rsplit("</svg>",1)[0]}</g>','0 0 512 512')
sg=S+'/fuentes/SpaceGrotesk[wght].ttf'
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}}
body{{margin:0;padding:28px;background:#fff;color:#1a1a1a;font:14px/1.4 SG,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
.sub{{color:#666;margin:0 0 16px}} .p{{display:grid;grid-template-columns:260px 1fr 1fr;gap:0;border:1px solid #e5e5e5;border-radius:12px;overflow:hidden;margin-bottom:16px}}
.p>div{{padding:18px;display:grid;gap:10px;align-content:start;min-width:0}} h2{{font:700 17px SG;margin:0}} .tag{{font:400 12px;color:#666}}
.sw{{display:flex;gap:8px}} .sw i{{display:block;width:44px;height:44px;border-radius:8px;border:1px solid rgba(0,0,0,.08)}}
.fila{{display:flex;gap:14px;align-items:center}} .fila span{{display:block}} .fila svg{{width:100%;height:100%}}
.wm{{display:flex;align-items:center;gap:10px}} .wm svg{{width:36px;height:36px}} .wm b{{font:700 32px SG;letter-spacing:-.02em}} .cur{{display:inline-block;width:.6em;height:1em;border-radius:3px;vertical-align:-.12em;margin-left:.1em}}
.num{{font-family:ui-monospace,monospace;font-size:12px}}'''
rows=''
for name,bg,ink,acc,accd,nota in P:
    rows+=f'''<div class="p"><div style="background:#fff"><h2>{name}</h2><div class="sw"><i style="background:{bg}"></i><i style="background:{ink}"></i><i style="background:{acc}"></i><i style="background:{accd}"></i></div><span class="tag">{bg} · {ink} · {acc} · sobre oscuro {accd}</span><span class="tag">{nota}</span><span class="tag num">acento/fondo {C(acc,bg):.1f}:1 · tinta/fondo {C(ink,bg):.1f}:1 · acento claro/tinta {C(accd,ink):.1f}:1</span></div>
<div style="background:{bg};color:{ink}"><div class="fila"><span style="width:96px;height:96px">{sym(acc,ink)}</span><span style="width:24px;height:24px">{sym(acc,ink)}</span><span style="width:16px;height:16px">{sym(acc,ink)}</span><span style="width:72px;height:72px">{app(bg,acc,ink)}</span></div><div class="wm">{sym(acc,ink)}<b>CLNDA<span class="cur" style="background:{acc}"></span></b></div></div>
<div style="background:{ink};color:{bg}"><div class="fila"><span style="width:96px;height:96px">{sym(accd,bg)}</span><span style="width:24px;height:24px">{sym(accd,bg)}</span><span style="width:16px;height:16px">{sym(accd,bg)}</span><span style="width:72px;height:72px">{app(ink,accd,bg)}</span></div><div class="wm">{sym(accd,bg)}<b style="color:{bg}">CLNDA<span class="cur" style="background:{accd}"></span></b></div></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">CLNDA · ronda 6 · cinco paletas sobrias para C1. Columna clara y columna oscura; un solo acento en la llave y en el cursor; el dato siempre en tinta.</p>{rows}')
print('ok')
