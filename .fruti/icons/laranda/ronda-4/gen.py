# Laranda · ronda 4 · dibujada (referencias del usuario): línea de tinta suelta + mancha plana de color desfasada, estilo impresión mal registrada.
# La jacaranda es una campana (corola tubular con cinco lóbulos), no una margarita.
import sys
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIO='#6B4FA0'; LILA='#B8A9E0'
def svg(body,vb='0 0 128 128'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · la campana de lado: tubo que se ensancha en una boca de cinco lóbulos; mancha violeta desfasada
CAMPANA_LINE='M46 22 C40 34 38 50 44 66 C48 78 56 88 66 94 M70 20 C76 34 82 50 84 68 C85 80 82 90 76 96 M66 94 C60 100 54 104 50 110 C58 108 64 104 70 102 C74 108 80 110 86 110 C82 104 80 100 80 96 C86 96 92 94 96 90 C90 90 86 88 82 86 M46 22 C50 16 56 14 62 14 C68 14 72 16 70 20 M58 14 C56 10 54 8 50 6 M46 66 C50 70 56 72 62 70'
CAMPANA_FILL='M50 28 C44 44 44 60 52 76 C58 88 68 96 80 94 C90 90 92 74 88 58 C84 42 78 28 70 22 C64 18 54 20 50 28Z'
def campana(k=INK,f=CREMA,c=VIO,lila=LILA,off=(5,4)):
    dx,dy=off
    return svg(f'<path d="{CAMPANA_FILL}" fill="{c}" transform="translate({dx} {dy})"/><path d="{CAMPANA_LINE}" stroke="{k}" stroke-width="3.2"/>')
# B · la campana de frente: cinco lóbulos sueltos alrededor de la garganta (el punto vacío); mancha desfasada
FRENTE_LINE='M64 34 C58 22 44 20 36 30 C30 38 36 50 48 54 M48 54 C36 54 24 60 24 72 C24 82 36 86 48 80 M48 80 C42 92 48 106 60 106 C70 106 76 96 70 84 M70 84 C80 94 96 90 100 78 C102 70 94 62 82 62 M82 62 C94 56 96 42 86 34 C78 28 68 30 64 40 M60 62 C58 58 62 54 66 56 C70 58 68 64 64 66 M56 70 C58 74 64 74 66 70'
FRENTE_FILL='M62 28 C48 22 36 32 40 48 C28 50 22 64 30 76 C36 86 50 88 58 80 C60 96 76 104 86 94 C94 86 90 74 82 68 C96 62 98 44 86 36 C78 30 68 32 62 28Z'
def frente(k=INK,f=CREMA,c=VIO,lila=LILA,off=(6,5)):
    dx,dy=off
    return svg(f'<path d="{FRENTE_FILL}" fill="{c}" transform="translate({dx} {dy})"/><path d="{FRENTE_LINE}" stroke="{k}" stroke-width="3.2"/><circle cx="63" cy="64" r="4" fill="{f}" stroke="{k}" stroke-width="2.4"/>')
# C · la campana que cae: dos campanas, una entera y otra chica que se desprende (el rasgo del brief), con una sola mancha
CAE_LINE='M40 30 C34 44 36 62 46 78 C52 88 60 96 70 100 M62 26 C70 40 76 58 76 76 C76 86 74 94 70 100 M70 100 C64 106 60 110 58 116 C64 114 68 110 72 108 C76 112 82 114 88 112 C84 108 82 104 82 100 M40 30 C44 24 50 20 56 20 C60 20 64 22 62 26 M84 28 C92 36 96 48 94 60 M100 24 C106 34 108 46 104 58 M94 60 C92 66 96 70 100 68 C104 66 106 62 104 58 M84 28 C88 22 96 20 100 24'
CAE_FILL='M46 36 C40 52 40 70 50 86 C56 96 66 104 78 102 C88 98 90 82 86 66 C82 50 76 36 68 30 C62 26 52 28 46 36Z'
def cae(k=INK,f=CREMA,c=VIO,lila=LILA,off=(5,4)):
    dx,dy=off
    return svg(f'<path d="{CAE_FILL}" fill="{c}" transform="translate({dx} {dy})"/><path d="M90 32 C96 40 100 52 98 62 C96 70 90 70 88 62 C86 52 86 40 90 32Z" fill="{lila}" transform="translate(4 3)"/><path d="{CAE_LINE}" stroke="{k}" stroke-width="3.2"/>')
# versión 16–32 px: silueta sólida de la campana, sin línea, con la garganta vacía
def chica(k=INK,f=CREMA,c=None,lila=None,off=None):
    k=c or k
    return svg(f'<path d="M50 24 C40 44 40 64 52 84 C60 96 72 104 84 100 C94 94 94 74 88 56 C84 40 78 26 70 20 C64 16 54 18 50 24Z" fill="{k}"/><circle cx="68" cy="60" r="7" fill="{f}"/>')
T={'A · la campana de lado':campana,'B · la campana de frente':frente,'C · la campana que cae':cae}
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 16px MR;margin:0 0 8px}} .sub{{color:#57534E;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:20px}}
.celda{{background:{CREMA};padding:16px;border-radius:14px;border:1px solid #F0EBE3;display:grid;gap:12px;align-content:start}} svg{{display:block}}
.big{{display:flex;gap:14px;align-items:flex-end}} .big span{{display:block}} .big svg{{width:100%;height:100%}}
.s{{display:flex;gap:10px;align-items:flex-end}} .s span{{display:block}} .s svg{{width:100%;height:100%}}
.dark{{background:{INK};padding:8px;border-radius:8px;display:inline-flex;gap:8px;align-items:flex-end}}
.lock{{display:flex;align-items:center;gap:8px}} .lock svg{{width:56px;height:56px}} .f1{{font:600 38px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 100}}
.app{{display:flex;gap:14px;align-items:flex-end}} .app span{{display:block;overflow:hidden}} .app svg{{width:100%;height:100%}}
.tag{{font:400 12px MR;color:#57534E}}
.chica{{background:{CREMA};padding:16px;border-radius:14px;border:1px solid #F0EBE3;display:flex;gap:16px;align-items:center}} .chica span{{display:block}} .chica svg{{width:100%;height:100%}}'''
def inv(s): return s.replace(f'fill="{CREMA}"','fill="@F@"').replace(INK,CREMA).replace('@F@',INK)
def app(fn,r=112):
    body=fn(CREMA,VIO,LILA,'#9f8fd0').split(">",1)[1].rsplit("</svg>",1)[0]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="{VIO}"/><g fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(32 32) scale(3.5)">{body}</g></svg>'
cells=''
for name,fn in T.items():
    s=fn(); d=inv(fn(INK,CREMA,LILA,'#9f8fd0'))
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big"><span style="width:200px;height:200px">{s}</span><span style="width:120px;height:120px">{fn(INK,CREMA,INK,INK,(0,0))}</span></div><div class="s"><span style="width:64px;height:64px">{s}</span><span style="width:40px;height:40px">{s}</span><span class="dark"><span style="width:64px;height:64px">{d}</span></span></div><div class="app"><span style="width:72px;height:72px">{app(fn)}</span><span style="width:48px;height:48px">{app(fn)}</span><span style="width:44px;height:44px;border-radius:50%">{app(fn,256)}</span></div><div class="lock">{s}<span class="f1">laranda</span></div><span class="tag">color desfasado · una tinta · 64 y 40 px · sobre tinta · app icon · lockup Fraunces</span></div>'
ch=f'<div class="chica"><b>Versión 16–32 px (silueta de la campana, sin línea)</b><span style="width:48px;height:48px">{chica()}</span><span style="width:32px;height:32px">{chica()}</span><span style="width:16px;height:16px">{chica()}</span><span style="width:48px;height:48px">{chica(VIO,CREMA)}</span><span style="width:16px;height:16px">{chica(VIO,CREMA)}</span><span class="dark"><span style="width:32px;height:32px">{inv(chica())}</span><span style="width:16px;height:16px">{inv(chica())}</span></span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 4 · dibujada: línea de tinta suelta y mancha plana de violeta desfasada, como impresión mal registrada. La jacaranda como campana. Tres encuadres y una silueta para tamaños chicos.</p><div class="fila">{cells}</div>{ch}')
print('ok')
