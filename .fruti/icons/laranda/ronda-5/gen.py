# Laranda · ronda 5 · desarrollo de B (campana de frente, línea en tinta): lóbulo que se separa, tres pesos de línea y desfase,
# silueta sólida para 16 px, wordmark con brote en la l, app icon, avatar y sello.
import sys,math
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIO='#6B4FA0'; LILA='#B8A9E0'; NIEBLA='#EDE9F7'; ORO='#C9A227'
def svg(body,vb='0 0 128 128'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# cinco lóbulos como trazos abiertos (a mano), con huecos entre ellos; el lóbulo 1 (arriba a la derecha) se separa
LOBOS=[('M60 46 C54 30 40 26 34 36 C28 46 38 56 50 56',0,0),            # arriba izquierda
       ('M68 44 C72 30 88 26 94 36 C100 46 90 56 78 58',4,-4),         # arriba derecha · el que se separa
       ('M80 66 C96 64 104 76 98 86 C92 94 78 92 72 80',0,0),           # derecha abajo
       ('M66 86 C70 100 60 110 50 104 C42 98 46 88 56 84',0,0),         # abajo
       ('M48 76 C34 82 22 74 26 62 C30 52 44 54 52 62',0,0)]            # izquierda
def mancha(off):
    dx,dy=off
    return f'<path d="M62 36 C50 26 36 34 40 50 C28 54 24 70 34 78 C42 86 54 84 60 76 C62 92 78 100 88 90 C96 82 92 70 84 64 C98 58 100 42 88 36 C80 30 70 32 62 36Z" fill="{VIO}" transform="translate({dx} {dy})"/>'
def flor(sw=3.2,off=(6,5),k=INK,f=CREMA,sep=True,con_mancha=True):
    b=mancha(off).replace(VIO,'@M@') if con_mancha else ''
    for i,(d,dx,dy) in enumerate(LOBOS):
        if not sep: dx=dy=0
        b+=f'<path d="{d}" stroke="{k}" stroke-width="{sw}" transform="translate({dx} {dy})"/>'
    b+=f'<circle cx="64" cy="68" r="4.5" fill="{f}" stroke="{k}" stroke-width="{sw*.8:.1f}"/>'
    return svg(b)
def color(s,m=VIO): return s.replace('@M@',m)
# silueta sólida para 16–32 px: cinco lóbulos redondos, el de arriba a la derecha separado, garganta vacía
def silueta(k=INK,f=CREMA):
    b=''
    for i in range(5):
        a=math.radians(-126+i*72); cx,cy=64+20*math.cos(a),66+20*math.sin(a)
        if i==1: cx+=5; cy-=5
        b+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="15" fill="{k}"/>'
    b+=f'<circle cx="64" cy="66" r="7" fill="{f}"/>'
    return svg(b)
def app(sw=3.2,r=112):
    body=color(flor(sw,(7,6),CREMA,VIO),LILA).split(">",1)[1].rsplit("</svg>",1)[0]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="{VIO}"/><g fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(32 32) scale(3.5)">{body}</g></svg>'
def app16(r=112): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="{VIO}"/><g transform="translate(64 64) scale(3)">{silueta(CREMA,VIO).split(">",1)[1].rsplit("</svg>",1)[0]}</g></svg>'
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'; jb=S+'/fuentes/JetBrainsMono.ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}} @font-face{{font-family:JB;src:url("file://{jb}");font-weight:100 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 16px MR;margin:0 0 8px}} .sub{{color:#57534E;margin:0 0 14px}} .tag{{font:400 12px MR;color:#57534E}}
.g{{display:grid;gap:16px;margin-bottom:16px}} .c3{{grid-template-columns:repeat(3,1fr)}} .c2{{grid-template-columns:1fr 1fr}}
.celda{{background:{CREMA};padding:16px;border-radius:14px;border:1px solid #F0EBE3;display:grid;gap:12px;align-content:start;min-width:0}} svg{{display:block}}
.f{{display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap}} .f span{{display:block}} .f svg{{width:100%;height:100%}}
.dark{{background:{INK};padding:8px;border-radius:8px;display:inline-flex;gap:8px;align-items:flex-end}}
.wm{{position:relative;display:inline-block;font:600 72px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 100;letter-spacing:-.01em}} .wm svg{{position:absolute;left:-6px;top:-30px;width:44px;height:44px}}
.wm2{{font:600 40px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 100}} .lock{{display:flex;align-items:center;gap:10px}} .lock>span{{display:block;width:64px;height:64px}} .lock svg{{width:100%;height:100%}}
.v{{display:grid;justify-items:center;gap:4px}} .v>span{{display:block;width:72px;height:72px}}
.folio{{background:#FBF9F4;border:1px solid #E7E1D6;border-radius:4px;padding:16px;font:12px/1.5 JB;color:{INK};display:grid;gap:6px;max-width:360px}} .folio .n{{font:600 15px FR}} .folio .sello{{width:56px;height:56px;justify-self:end;opacity:.9}} .folio .sello svg{{width:100%;height:100%}}
.btn{{display:inline-block;background:{ORO};color:{INK};font:700 14px MR;padding:10px 16px;border-radius:10px}}
.chip{{display:inline-flex;align-items:center;gap:6px;background:{NIEBLA};color:{VIO};font:600 12px MR;padding:4px 10px;border-radius:999px}} .chip span{{width:14px;height:14px;display:block}} .chip svg{{width:100%;height:100%}}'''
def inv(s): return s.replace(f'fill="{CREMA}"','fill="@F@"').replace(INK,CREMA).replace('@F@',INK)
V=[('B1 · línea fina, desfase corto',2.4,(5,4)),('B2 · línea media, desfase largo',3.2,(8,7)),('B3 · línea gruesa, desfase corto',4.2,(5,4))]
cells=''
for name,sw,off in V:
    s=color(flor(sw,off)); t=color(flor(sw,off,con_mancha=False)); d=inv(color(flor(sw,off),LILA))
    cells+=f'<div class="celda"><h2>{name}</h2><div class="f"><span style="width:180px;height:180px">{s}</span><span style="width:110px;height:110px">{t}</span></div><div class="f"><span style="width:64px;height:64px">{s}</span><span style="width:40px;height:40px">{s}</span><span style="width:32px;height:32px">{s}</span><span class="dark"><span style="width:64px;height:64px">{d}</span><span style="width:32px;height:32px">{d}</span></span></div><div class="f"><span style="width:72px;height:72px">{app(sw)}</span><span style="width:48px;height:48px">{app(sw)}</span><span style="width:44px;height:44px;border-radius:50%;overflow:hidden">{app(sw,256)}</span></div></div>'
brote='<svg viewBox="0 0 44 44"><path d="M22 36 C20 26 14 22 10 14 C8 10 12 6 16 10 C20 14 22 22 22 30 M22 30 C24 22 30 16 36 14 C40 13 42 18 38 22 C34 26 28 30 22 36" stroke="'+INK+'" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>'
sil=silueta(); silv=silueta(VIO,CREMA)
page2=f'''<div class="g c2">
<div class="celda"><h2>Silueta para 16–32 px (derivada de B: cinco lóbulos, uno separado, garganta vacía)</h2><div class="f"><span style="width:96px;height:96px">{sil}</span><span style="width:48px;height:48px">{sil}</span><span style="width:32px;height:32px">{sil}</span><span style="width:16px;height:16px">{sil}</span><span style="width:32px;height:32px">{silv}</span><span style="width:16px;height:16px">{silv}</span><span class="dark"><span style="width:32px;height:32px">{inv(sil)}</span><span style="width:16px;height:16px">{inv(sil)}</span></span><span style="width:48px;height:48px">{app16()}</span><span style="width:40px;height:40px;border-radius:50%;overflow:hidden">{app16(256)}</span></div><span class="tag">favicon, avatar, chip de categoría, sello pequeño</span>
<div class="f"><span class="chip"><span>{silv}</span>Barbería</span><span class="chip"><span>{silv}</span>Uñas</span><span class="chip"><span>{silv}</span>Podología</span></div></div>
<div class="celda"><h2>Wordmark · Fraunces 600, caja baja; la l con brote solo en versión de marca</h2><div style="padding-top:28px"><span class="wm">{brote}laranda</span></div><div class="lock"><span>{color(flor(3.2,(6,5)))}</span><span class="wm2">laranda</span></div><div class="v"><span>{color(flor(3.2,(6,5)))}</span><span class="wm2">laranda</span></div><span class="tag">horizontal mín. 120 px · vertical mín. 80 px · en UI el wordmark va sin brote</span></div>
</div>
<div class="g c2">
<div class="celda"><h2>Folio · la flor como sello de «folio emitido»</h2><div class="folio"><span class="n">laranda</span><span>FOLIO LR-2026-00417</span><span>Corte y color · Mariana R. · 22 oct 2026 · $650.00</span><span>Pagado · tarjeta</span><span class="sello">{color(flor(3.2,(0,0),con_mancha=False))}</span></div><span class="tag">papel crema, tinta; wordmark monocromo; folio en mono</span></div>
<div class="celda"><h2>Cabecera de perfil · categoría con color + icono + texto, botón Reservar en oro</h2><div style="display:grid;gap:10px"><div style="display:flex;gap:12px;align-items:center"><span style="width:56px;height:56px;border-radius:50%;background:#D8CFC2;display:block"></span><div><b style="font:700 18px MR">Mariana Ruiz</b><br><span class="chip"><span>{silv}</span>Colorista</span></div></div><span class="btn">Reservar</span><div class="f"><span style="width:28px;height:28px">{silv}</span><span class="tag">Perfil publicado · florece</span></div></div><span class="tag">el oro solo aquí; la flor como estado</span></div>
</div>'''
open('muestra.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 5 · desarrollo de B con línea en tinta: lóbulo que se separa, tres pesos de línea y desfase de mancha, silueta para 16 px, wordmark con brote, app icon, avatar, chip, folio y cabecera.</p><div class="g c3">{cells}</div>{page2}')
print('ok')
