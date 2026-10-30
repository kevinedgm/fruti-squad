# NisaData · pantalla principal (panel), ronda 1 + paleta de datos v1.
# Datos de ejemplo. Paleta validada con validate_palette.js (skill dataviz); ver paleta.md.
# Uso: python3 gen.py <carpeta de fuentes> <íconos lucide> → panel.html
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..'); F, LU = sys.argv[1], sys.argv[2]
GR, MA = '#1F2532', '#FF8A1F'
# — paleta de datos NisaData v1 —
S1, S2, S3 = '#1d4ed8', '#9b3d8f', '#14b8a6'          # categórica: cobalto, ciruela, turquesa (máx. 3 series)
GRIS = '#9AA1B1'                                         # «Otros» y periodo anterior
ETAPA = {'No ingresada': '#CA8A04', 'En proceso': '#0284C7', 'Generando informe': '#7C3AED', 'Cancelada': '#DC2626'}  # estatus del laboratorio (marca)
def lucide(n, px=18):
    s = open(os.path.join(LU, n + '.svg')).read(); s = s[s.index('<svg'):]
    return re.sub(r'\s+', ' ', s).replace('width="24"', f'width="{px}"').replace('height="24"', f'height="{px}"').replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
_n = [0]
def area_ico(k):
    _n[0] += 1; u = f'-p{_n[0]}'
    s = open(os.path.join(NS, 'nisalab-areas-final', 'svg', k, 'icono-1tinta.svg')).read().strip()
    s = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', s)
    s = s.replace(f'id="i{k}"', f'id="i{k}{u}"').replace(f'url(#i{k})', f'url(#i{k}{u})')
    return s.replace('<svg ', '<svg width="16" height="16" aria-hidden="true" focusable="false" style="color:#646B80;flex:none" ', 1)
logo = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, 'nisadata-final', 'svg', 'logotipo-blanco.svg')).read().strip())
logo = logo.replace('<svg ', '<svg style="height:30px;width:auto;display:block" aria-label="NisaData" role="img" ', 1)
logo_m = logo.replace('height:30px', 'height:24px')

# — datos de ejemplo —
SEM = [f'S{n}' for n in range(33, 45)]
REC = [96, 104, 99, 112, 108, 118, 121, 115, 127, 124, 131, 138]
ENT = [92, 97, 101, 104, 109, 110, 117, 112, 118, 121, 122, 126]
WIP = [('No ingresada', 18), ('En proceso', 64), ('Generando informe', 22)]
CANC = 6
AREAS = [('aguas', 'Aguas', 41, 3.1), ('alimentos', 'Alimentos', 28, 4.6), ('bebidas', 'Bebidas alcohólicas', 19, 3.8), ('agricolas', 'Agrícolas', 11, 4.2), ('ambiental', 'Ambiental', 5, 2.9)]
META = 4.0

# — 1 · tendencia (líneas) —
W, Hh, L, R, T, B = 640, 250, 44, 124, 16, 30
ymin, ymax = 80, 140
X = lambda i: L + i * (W - L - R) / (len(SEM) - 1); Y = lambda v: T + (ymax - v) * (Hh - T - B) / (ymax - ymin)
grid = ''.join(f'<line x1="{L}" x2="{W - R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#E6E8EE"/><text x="{L - 8}" y="{Y(v) + 4:.1f}" text-anchor="end" class="ax">{v}</text>' for v in range(80, 141, 20))
xl = ''.join(f'<text x="{X(i):.1f}" y="{Hh - 8}" text-anchor="middle" class="ax">{s}</text>' for i, s in enumerate(SEM) if i % 2 == 0)
def linea(vals, col): return f'<path d="M' + ' L'.join(f'{X(i):.1f} {Y(v):.1f}' for i, v in enumerate(vals)) + f'" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
def fin(vals, col, txt, dy): i = len(vals) - 1; return f'<circle cx="{X(i):.1f}" cy="{Y(vals[i]):.1f}" r="4" fill="{col}" stroke="#fff" stroke-width="2"/><text x="{X(i) + 10:.1f}" y="{Y(vals[i]) + dy:.1f}" class="dl">{txt} {vals[i]}</text>'
hits = ''.join(f'<rect class="hit" x="{X(i) - (W - L - R) / 22:.1f}" y="{T}" width="{(W - L - R) / 11:.1f}" height="{Hh - T - B}" fill="transparent" tabindex="0" data-x="{X(i):.1f}" '
               f'data-tip="Semana {s[1:]}&#10;Recibidas {REC[i]}&#10;Entregadas {ENT[i]}"/>' for i, s in enumerate(SEM))
tend = (f'<svg viewBox="0 0 {W} {Hh}" class="ch ln" role="img" aria-label="Muestras recibidas y entregadas por semana, semanas 33 a 44">{grid}{xl}'
        f'<line x1="{L}" x2="{W - R}" y1="{Hh - B}" y2="{Hh - B}" stroke="#C9CED8"/><line class="cross" y1="{T}" y2="{Hh - B}" stroke="#8A93A8" stroke-dasharray="3 3" visibility="hidden"/>'
        f'{linea(REC, S1)}{linea(ENT, S2)}{fin(REC, S1, "Recibidas", -6)}{fin(ENT, S2, "Entregadas", 14)}{hits}</svg>')
tabla_t = '<table class="tv"><thead><tr><th>Semana</th><th>Recibidas</th><th>Entregadas</th></tr></thead><tbody>' + ''.join(f'<tr><td>{s}</td><td>{a}</td><td>{b}</td></tr>' for s, a, b in zip(SEM, REC, ENT)) + '</tbody></table>'

# — 2 · trabajo en curso por etapa (barras horizontales, colores de estatus) —
mx = max(v for _, v in WIP)
def barra(lbl, v, col, mxv, extra=''):
    return (f'<div class="br" tabindex="0" data-tip="{lbl}&#10;{v} muestras"><span class="bl">{extra}{lbl}</span>'
            f'<span class="bt"><i style="width:{v / mxv * 100:.1f}%;background:{col}"></i></span><span class="bv">{v}</span></div>')
wip = ''.join(barra(n, v, ETAPA[n], mx) for n, v in WIP) + f'<div class="sep"></div>' + barra('Cancelada', CANC, ETAPA['Cancelada'], mx)
# — 3 · carga por área (una serie: cobalto; el área se nombra, no se colorea) —
ma = max(a[2] for a in AREAS)
carga = ''.join(barra(n, v, S1, ma, area_ico(k)) for k, n, v, _ in AREAS)
# — 4 · tiempo de entrega vs meta (divergente desde la meta) —
dv = ''
for k, n, v, t in AREAS:
    d = t - META; w = abs(d) / 1.0 * 50; col = S1 if d <= 0 else S2; side = 'l' if d <= 0 else 'r'
    dv += (f'<div class="dvr" tabindex="0" data-tip="{n}&#10;{t:.1f} días · meta {META:.0f}&#10;{"+" if d > 0 else "−"}{abs(d):.1f} días"><span class="bl">{area_ico(k)}{n}</span>'
           f'<span class="dt"><span class="mid"></span><i class="{side}" style="width:{min(w, 50):.1f}%;background:{col}"></i></span><span class="bv">{t:.1f} d</span></div>')
# — tiles —
def tile(lbl, val, unit, delta, good, nota):
    ic = lucide('trending-up', 14) if delta.startswith('+') else lucide('trending-up', 14).replace('<svg ', '<svg style="transform:scaleY(-1)" ', 1)
    return (f'<div class="kp"><span class="kl">{lbl}</span><span class="kv">{val}<small>{unit}</small></span>'
            f'<span class="kd {"ok" if good else "bad"}">{ic}{delta}</span><span class="kn">{nota}</span></div>')
tiles = (tile('Muestras recibidas', '1,393', '', '+8.4 %', True, 'vs. 90 días anteriores')
         + tile('Tiempo de entrega', '3.6', 'días', '−0.4 días', True, 'meta 4 días')
         + tile('Entregadas a tiempo', '91', '%', '−2 pts', False, 'meta 95 %')
         + tile('Trabajo en curso', '104', 'muestras', '+12', False, '9 urgentes'))
def alerta(ic, cls, t, d): return f'<li><span class="ai {cls}">{lucide(ic, 16)}</span><div><b>{t}</b><span>{d}</span></div></li>'
alertas = ('<ul class="al">' + alerta('zap', 'urg', '3 urgentes con más de 48 h', 'Aguas 2 · Alimentos 1')
           + alerta('file-clock', 'warn', '7 informes atrasados', 'En «Generando informe» más de 2 días')
           + alerta('triangle-alert', 'bad', 'Alimentos fuera de meta', '4.6 días de entrega · meta 4')
           + alerta('wallet', 'neu', '$42,800 por cobrar vencido', '11 órdenes con más de 30 días') + '</ul>')
NAV = [('layout-dashboard', 'Panel', True), ('trending-up', 'Tendencias', False), ('flask-conical', 'Áreas', False), ('users', 'Clientes', False),
       ('shield-check', 'Calidad', False), ('wallet', 'Cobranza', False), ('file-text', 'Reportes', False)]
nav = ''.join(f'<a href="#" class="ni"{" aria-current=page" if a else ""}>{lucide(i)}<span>{n}</span></a>' for i, n, a in NAV)
ff = ''.join(f"@font-face{{font-family:'Poppins';src:url('file://{F}/Poppins-{w}.woff2');font-weight:{w}}}" for w in (400, 500, 600, 700)) + f"@font-face{{font-family:'IBM Plex Mono';src:url('file://{F}/IBMPlexMono.ttf')}}"
css = ff + f'''
:root{{--gr:{GR};--ma:{MA};--bg:#F2F4F8;--sf:#fff;--tx:#141B33;--mu:#535B70;--sub:#646B80;--ln:#DFE3EC;--s1:{S1};--s2:{S2};--s3:{S3}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font:400 14px/1.5 Poppins,system-ui,sans-serif}}
.app{{display:grid;grid-template-columns:232px 1fr;min-height:100vh}}
.sb{{background:var(--gr);color:#C9CED8;padding:22px 14px;display:flex;flex-direction:column;gap:22px;position:sticky;top:0;height:100vh}}
.sb nav{{display:flex;flex-direction:column;gap:2px}}.ni{{display:flex;align-items:center;gap:12px;color:#C9CED8;text-decoration:none;font:500 14px/20px Poppins;padding:9px 12px;border-radius:8px;position:relative}}
.ni:hover{{background:rgba(255,255,255,.06);color:#fff}}.ni[aria-current]{{background:rgba(255,255,255,.08);color:#fff}}.ni[aria-current]::before{{content:"";position:absolute;left:-14px;top:8px;bottom:8px;width:4px;border-radius:0 4px 4px 0;background:var(--ma)}}
.ni:focus-visible,[tabindex]:focus-visible,button:focus-visible{{outline:2px solid var(--s1);outline-offset:2px}}.sb .ni:focus-visible{{outline-color:#fff}}
.mn{{padding:24px 32px 40px;min-width:0}}.top{{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap;margin-bottom:20px}}
.top h1{{font:600 24px/32px Poppins;margin:0}}.top p{{margin:2px 0 0;color:var(--mu);font:400 13px 'IBM Plex Mono',monospace}}
.flt{{display:flex;gap:8px;flex-wrap:wrap}}.sel{{display:inline-flex;align-items:center;gap:8px;font:500 14px/20px Poppins;color:var(--tx);background:var(--sf);border:1px solid #858DA3;border-radius:8px;padding:9px 12px;min-height:40px;cursor:pointer}}.sel small{{color:var(--mu);font-weight:400}}
.kps{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-bottom:16px}}
.kp,.cd{{background:var(--sf);border:1px solid var(--ln);border-radius:12px;box-shadow:0 1px 2px rgba(20,27,51,.05)}}
.kp{{padding:16px 18px;display:flex;flex-direction:column;gap:2px}}.kl{{font:500 13px/18px Poppins;color:var(--mu)}}.kv{{font:600 32px/40px Poppins;letter-spacing:-.01em}}.kv small{{font:500 14px Poppins;color:var(--mu);margin-left:6px}}
.kd{{display:inline-flex;align-items:center;gap:4px;font:600 13px/18px Poppins}}.kd.ok{{color:#166534}}.kd.bad{{color:#991B1B}}.kn{{font-size:12px;color:var(--sub)}}
.gd{{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:16px}}.cd{{padding:18px 20px;min-width:0}}.c8{{grid-column:span 8}}.c4{{grid-column:span 4}}.c6{{grid-column:span 6}}
.ch-h{{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-bottom:10px}}.ch-h h2{{font:600 16px/22px Poppins;margin:0}}.ch-h p{{margin:2px 0 0;font-size:13px;color:var(--mu)}}
.lg{{display:flex;gap:14px;font-size:12px;color:var(--mu);flex-wrap:wrap}}.lg span{{display:inline-flex;align-items:center;gap:6px}}.lg i{{width:12px;height:3px;border-radius:2px;display:inline-block}}.lg i.sq{{width:10px;height:10px;border-radius:3px}}
.lnk{{font:500 13px Poppins;color:var(--s1);background:none;border:0;padding:4px;cursor:pointer;white-space:nowrap}}
.ch{{width:100%;height:auto;display:block}}.ax{{font:11px 'IBM Plex Mono',monospace;fill:#646B80}}.dl{{font:600 12px Poppins;fill:#141B33}}.cw{{overflow-x:auto}}.cw .ln{{min-width:520px}}
.br,.dvr{{display:grid;grid-template-columns:minmax(0,170px) 1fr 52px;align-items:center;gap:12px;padding:7px 0;border-radius:6px}}.br:hover .bt i,.dvr:hover .dt i{{filter:brightness(1.12)}}
.bl{{display:inline-flex;align-items:center;gap:8px;font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}.bt{{height:16px;display:block}}.bt i{{display:block;height:100%;border-radius:0 4px 4px 0;min-width:4px}}
.bv{{font:600 13px 'IBM Plex Mono',monospace;text-align:right}}.sep{{height:1px;background:var(--ln);margin:6px 0}}
.dt{{position:relative;height:16px;display:block}}.dt .mid{{position:absolute;left:50%;top:-4px;bottom:-4px;width:1.5px;background:#8A93A8}}.dt i{{position:absolute;top:0;height:100%}}.dt i.r{{left:50%;border-radius:0 4px 4px 0}}.dt i.l{{right:50%;border-radius:4px 0 0 4px}}
.ml{{display:flex;justify-content:space-between;font-size:11px;color:var(--sub);margin:4px 0 0;padding-left:182px;padding-right:64px}}
.al{{list-style:none;margin:0;padding:0}}.al li{{display:flex;gap:12px;padding:12px 0;border-top:1px solid var(--ln)}}.al li:first-child{{border-top:0}}.al b{{display:block;font-weight:600;font-size:14px}}.al span{{font-size:12px;color:var(--mu)}}
.ai{{width:30px;height:30px;border-radius:8px;display:grid;place-items:center;flex:none}}.ai.urg{{background:#C2D225;color:#052A76}}.ai.warn{{background:#FEF3C7;color:#713F12}}.ai.bad{{background:#FEE2E2;color:#991B1B}}.ai.neu{{background:#EEF1F6;color:#475467}}
.tv{{width:100%;border-collapse:collapse;font-size:13px}}.tv th{{text-align:left;color:var(--mu);font-weight:500;background:#EEF1F6;padding:6px 10px}}.tv td{{padding:6px 10px;border-top:1px solid var(--ln);font-family:'IBM Plex Mono',monospace}}
.tip{{position:fixed;pointer-events:none;background:var(--gr);color:#fff;font:500 12px/17px Poppins;padding:8px 10px;border-radius:8px;white-space:pre;box-shadow:0 8px 20px rgba(20,27,51,.25);z-index:9;display:none}}
.mt{{display:none}}.nota{{font-size:12px;color:var(--sub);margin-top:16px}}
@media (max-width:1100px){{.kps{{grid-template-columns:repeat(2,minmax(0,1fr))}}.c8,.c4,.c6{{grid-column:span 12}}}}
@media (max-width:760px){{.app{{grid-template-columns:1fr}}.sb{{display:none}}.mt{{display:flex;align-items:center;justify-content:space-between;background:var(--gr);padding:12px 16px;color:#fff}}
.mt button{{background:none;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:8px;min-height:40px;padding:0 12px;font:500 14px Poppins}}.mn{{padding:16px}}
.kps{{grid-template-columns:1fr 1fr;gap:10px}}.kv{{font-size:26px;line-height:32px}}.br,.dvr{{grid-template-columns:1fr 44px;gap:2px 8px}}.bl{{grid-column:1/-1}}.ml{{padding-left:0;padding-right:52px}}}}
'''
js = '''
const tip=document.querySelector('.tip');
function show(el,x,y){tip.textContent=el.dataset.tip.replace(/&#10;/g,'\\n');tip.style.display='block';const r=tip.getBoundingClientRect();
 tip.style.left=Math.min(window.innerWidth-r.width-8,x+14)+'px';tip.style.top=Math.max(8,y-r.height-12)+'px';}
document.querySelectorAll('[data-tip]').forEach(el=>{
 el.addEventListener('pointermove',e=>{show(el,e.clientX,e.clientY);cross(el,true)});
 el.addEventListener('pointerleave',()=>{tip.style.display='none';cross(el,false)});
 el.addEventListener('focus',()=>{const r=el.getBoundingClientRect();show(el,r.left+r.width/2,r.top);cross(el,true)});
 el.addEventListener('blur',()=>{tip.style.display='none';cross(el,false)});});
function cross(el,on){const c=el.closest('svg')?.querySelector('.cross');if(!c)return;c.setAttribute('x1',el.dataset.x);c.setAttribute('x2',el.dataset.x);c.setAttribute('visibility',on?'visible':'hidden');}
const b=document.querySelector('[data-tabla]');b.addEventListener('click',()=>{const t=document.getElementById('tabla-t'),g=document.getElementById('graf-t');const v=t.hidden;t.hidden=!v;g.hidden=v;b.textContent=v?'Ver gráfica':'Ver tabla';b.setAttribute('aria-pressed',v);});
'''
html = (f'<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NisaData · Panel</title><style>{css}</style><body>'
        f'<div class="mt">{logo_m}<button aria-label="Abrir menú">Menú</button></div>'
        f'<div class="app"><aside class="sb">{logo}<nav aria-label="Principal">{nav}</nav><a href="#" class="ni" style="margin-top:auto">{lucide("settings")}<span>Configuración</span></a></aside>'
        f'<main class="mn"><div class="top"><div><h1>Panel del laboratorio</h1><p>Actualizado hoy 09:42 · datos de NisaLab</p></div>'
        f'<div class="flt"><button class="sel">{lucide("calendar", 16)}<small>Periodo</small> Últimos 90 días {lucide("chevron-down", 16)}</button><button class="sel"><small>Área</small> Todas {lucide("chevron-down", 16)}</button></div></div>'
        f'<section class="kps" aria-label="Indicadores principales">{tiles}</section><div class="gd">'
        f'<section class="cd c8"><div class="ch-h"><div><h2>Muestras recibidas y entregadas</h2><p>Por semana · ¿estamos sacando lo que entra?</p></div>'
        f'<div style="display:flex;gap:12px;align-items:center"><div class="lg"><span><i style="background:var(--s1)"></i>Recibidas</span><span><i style="background:var(--s2)"></i>Entregadas</span></div><button class="lnk" data-tabla aria-pressed="false">Ver tabla</button></div></div>'
        f'<div id="graf-t" class="cw">{tend}</div><div id="tabla-t" hidden>{tabla_t}</div></section>'
        f'<section class="cd c4"><div class="ch-h"><div><h2>Requiere atención</h2><p>Lo que se sale de lo normal hoy</p></div></div>{alertas}</section>'
        f'<section class="cd c6"><div class="ch-h"><div><h2>Trabajo en curso por etapa</h2><p>Muestras abiertas hoy · colores de estatus de NisaLab</p></div></div>{wip}</section>'
        f'<section class="cd c6"><div class="ch-h"><div><h2>Carga por área</h2><p>Muestras en curso</p></div></div>{carga}</section>'
        f'<section class="cd c6"><div class="ch-h"><div><h2>Tiempo de entrega contra la meta</h2><p>Promedio por área · meta {META:.0f} días</p></div>'
        f'<div class="lg"><span><i class="sq" style="background:var(--s1)"></i>Más rápido</span><span><i class="sq" style="background:var(--s2)"></i>Más lento</span></div></div>{dv}'
        f'<div class="ml"><span>−1 día</span><span>meta</span><span>+1 día</span></div></section>'
        f'<section class="cd c6"><div class="ch-h"><div><h2>Qué más puede vivir aquí</h2><p>Siguientes vistas del menú (propuesta)</p></div></div><ul class="al">'
        + alerta('trending-up', 'neu', 'Tendencias', 'Volumen, tiempos y fuera de límite mes a mes') + alerta('flask-conical', 'neu', 'Áreas', 'El mismo panel filtrado por área')
        + alerta('users', 'neu', 'Clientes', 'Quién manda más muestras y quién crece') + alerta('shield-check', 'neu', 'Calidad', 'Parámetros fuera de límite, repeticiones, cancelaciones')
        + '</ul></section></div><p class="nota">Datos de ejemplo. Paleta de datos NisaData v1: cobalto, ciruela y turquesa para series; colores de estatus solo en gráficas de estatus; las áreas se nombran, no se colorean.</p></main></div>'
        f'<div class="tip" role="tooltip"></div><script>{js}</script></body></html>')
open(os.path.join(H, 'panel.html'), 'w').write(html); print('ok')
