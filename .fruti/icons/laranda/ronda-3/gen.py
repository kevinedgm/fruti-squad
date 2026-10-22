# Laranda · ronda 3 · orgánica (usuario: «se ve muy rígido»). Curvas asimétricas, formas blandas, movimiento.
import sys,math
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIO='#6B4FA0'; LILA='#B8A9E0'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# A · el pétalo suelto: una sola forma blanda y asimétrica que se levanta; el punto vacío donde estaba unida
def petalo(k=INK,f=CREMA,k2=None):
    return svg(f'<path d="M30 54 C14 50 10 34 18 22 C25 12 42 8 50 14 C56 20 50 34 42 42 C38 46 36 52 30 54Z" fill="{k}"/><circle cx="25" cy="44" r="4.5" fill="{f}"/>')
# B · la yema: dos hojas blandas y asimétricas que se abren desde un mismo punto; el hueco entre ellas es el centro
def yema(k=INK,f=CREMA,k2=None):
    k2=k2 or k
    return svg(f'<path d="M31 56 C22 48 10 36 16 22 C20 12 30 14 31 26 C32 36 31 48 31 56Z" fill="{k}"/><path d="M33 56 C34 46 36 34 44 22 C50 14 58 18 54 30 C50 40 40 50 33 56Z" fill="{k2}"/><circle cx="32" cy="54" r="3" fill="{f}"/>')
# C · la forma partida: una forma blanda que se abre por una grieta curva; el trozo pequeño se separa; punto vacío en la grieta
def partida(k=INK,f=CREMA,k2=None):
    k2=k2 or k
    return svg(f'<path d="M30 56 C14 54 8 40 14 28 C19 18 30 14 38 20 C34 28 32 40 36 52 C34 55 32 56 30 56Z" fill="{k}"/><path d="M42 24 C50 30 52 44 44 50 C41 52 39 51 38 48 C36 40 38 30 42 24Z" fill="{k2}"/><circle cx="39" cy="36" r="3" fill="{f}"/>')
# D · el trazo que se abre: una curva blanda que sube y se abre, con un punto suelto al final (el brote que se desprende)
def trazo(k=INK,f=CREMA,k2=None):
    k2=k2 or k
    return svg(f'<path d="M14 50 C20 36 28 28 40 26 C46 25 50 28 50 32" stroke="{k}" stroke-width="9"/><circle cx="54" cy="18" r="6" fill="{k2}"/><circle cx="54" cy="18" r="2" fill="{f}"/>')
T={'A · el pétalo suelto':petalo,'B · la yema':yema,'C · la forma partida':partida,'D · el trazo que se abre':trazo}
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 16px MR;margin:0 0 8px}} .sub{{color:#57534E;margin:0 0 14px}}
.fila{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:20px}}
.celda{{background:{CREMA};padding:16px;border-radius:14px;border:1px solid #F0EBE3;display:grid;gap:12px;align-content:start}} svg{{display:block}}
.big{{display:flex;gap:14px;align-items:flex-end}} .big span{{display:block}} .big svg{{width:100%;height:100%}}
.s{{display:flex;gap:10px;align-items:flex-end}} .s span{{display:block}} .s svg{{width:100%;height:100%}}
.dark{{background:{INK};padding:8px;border-radius:8px;display:inline-flex;gap:8px;align-items:flex-end}}
.lock{{display:flex;align-items:center;gap:10px}} .lock svg{{width:44px;height:44px}} .f1{{font:600 36px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 100}} .f2{{font:600 34px/1 MR;letter-spacing:-.02em}}
.app{{display:flex;gap:14px;align-items:flex-end}} .app span{{display:block;overflow:hidden}} .app svg{{width:100%;height:100%}}
.tag{{font:400 12px MR;color:#57534E}}'''
def inv(s,bg=INK): return s.replace(f'fill="{CREMA}"','fill="@F@"').replace(INK,CREMA).replace('@F@',bg)
def app(fn,r=112): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="{VIO}"/><g fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(64 64) scale(6)">{fn(CREMA,VIO,LILA).split(">",1)[1].rsplit("</svg>",1)[0]}</g></svg>'
cells=''
for name,fn in T.items():
    s=fn(); c=fn(VIO,CREMA,LILA)
    cells+=f'<div class="celda"><h2>{name}</h2><div class="big"><span style="width:140px;height:140px">{s}</span><span style="width:140px;height:140px">{c}</span></div><div class="s"><span style="width:48px;height:48px">{s}</span><span style="width:32px;height:32px">{s}</span><span style="width:16px;height:16px">{s}</span><span class="dark"><span style="width:40px;height:40px">{inv(s)}</span><span style="width:16px;height:16px">{inv(s)}</span></span></div><div class="app"><span style="width:64px;height:64px">{app(fn)}</span><span style="width:48px;height:48px">{app(fn)}</span><span style="width:40px;height:40px;border-radius:50%">{app(fn,256)}</span></div><div class="lock">{c}<span class="f1">laranda</span></div><div class="lock">{c}<span class="f2">laranda</span></div><span class="tag">tinta · violeta y lila · 48, 32, 16 · sobre tinta · app icon · lockups</span></div>'
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 3 · orgánica: curvas asimétricas y formas blandas, sin flor literal. Cada concepto en tinta y en violeta + lila (dos tonos planos, sin degradado).</p><div class="fila">{cells}</div>')
print('ok')
