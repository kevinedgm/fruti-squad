# CLNDA · ronda 5: desarrollo de C1 (llave rosa, punto tinta): símbolo afinado, versión chica, app icon, logotipo, paleta y contexto.
import sys
S=sys.argv[1]; INK='#17141a'; PAPEL='#f6f1e8'; ROSA='#e4007c'; TURQ='#00a3a8'; AMAR='#ffd400'; ROSA_D='#ff5fb0'
def svg(body,vb='0 0 64 64'): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
BR='M40 10 H36 a8 8 0 0 0 -8 8 V26 a6 6 0 0 1 -6 6 a6 6 0 0 1 6 6 V46 a8 8 0 0 0 8 8 H40'
def simbolo(llave=ROSA,punto=INK,sw=7,dx=-3,r=6.5): return svg(f'<path d="{BR}" stroke="{llave}" stroke-width="{sw}" transform="translate({dx} 0)"/><circle cx="46" cy="32" r="{r}" fill="{punto}"/>')
# versión chica: trazo más grueso, punto más grande, sin los ganchos cortos
BR16='M38 10 H36 a9 9 0 0 0 -9 9 V25 a7 7 0 0 1 -7 7 a7 7 0 0 1 7 7 V45 a9 9 0 0 0 9 9 H38'
def simbolo16(llave=ROSA,punto=INK): return svg(f'<path d="{BR16}" stroke="{llave}" stroke-width="9" transform="translate(-3 0)"/><circle cx="46" cy="32" r="8" fill="{punto}"/>')
def appicon(fondo=PAPEL,llave=ROSA,punto=INK,r=112): return svg(f'<rect width="512" height="512" rx="{r}" fill="{fondo}"/><g transform="translate(80 80) scale(5.5)">{simbolo(llave,punto).split(">",1)[1].rsplit("</svg>",1)[0]}</g>','0 0 512 512')
sg=S+'/fuentes/SpaceGrotesk[wght].ttf'; jb=S+'/fuentes/JetBrainsMono.ttf'; sy=S+'/fuentes/Syne[wght].ttf'; un=S+'/fuentes/Unbounded[wght].ttf'
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}} @font-face{{font-family:JB;src:url("file://{jb}");font-weight:100 800}} @font-face{{font-family:SY;src:url("file://{sy}");font-weight:400 800}} @font-face{{font-family:UN;src:url("file://{un}");font-weight:200 900}}
body{{margin:0;padding:28px;background:{PAPEL};color:{INK};font:14px/1.4 SG,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 10px}} h3{{font:700 14px SG;margin:0 0 6px}} .sub{{color:#5b5560;margin:0 0 14px}} .tag{{font:400 12px SG;color:#5b5560}}
.g{{display:grid;gap:18px;margin-bottom:22px}} .c2{{grid-template-columns:1fr 1fr}} .c3{{grid-template-columns:repeat(3,1fr)}}
.celda{{background:#fff;padding:16px;border-radius:12px;border:1px solid #e3ddd1;display:grid;gap:10px;align-content:start;min-width:0}} svg{{display:block}}
.fila{{display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap}} .fila span{{display:block}} .fila svg{{width:100%;height:100%}}
.dark{{background:{INK};padding:12px;border-radius:8px;display:inline-flex;gap:12px;align-items:flex-end}}
.wm{{display:flex;align-items:center;gap:12px}} .wm svg{{width:44px;height:44px}} .wm b{{font-size:40px;letter-spacing:-.02em}} .sgf{{font:700 40px SG}} .syf{{font:800 40px SY;letter-spacing:.01em}} .jbf{{font:700 40px JB}} .unf{{font:700 36px UN}}
.cur{{display:inline-block;width:.6em;height:1em;background:{ROSA};border-radius:3px;vertical-align:-.12em;margin-left:.1em}}
.sw{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}} .sw div{{display:grid;gap:4px;font-size:12px}} .sw i{{display:block;height:48px;border-radius:8px;border:1px solid #e3ddd1}}
.gh{{display:flex;gap:12px;align-items:center;background:#0d1117;color:#e6edf3;padding:14px;border-radius:10px;font:14px system-ui}} .gh span{{width:48px;height:48px;border-radius:50%;overflow:hidden;display:block}} .gh b{{display:block;font-size:16px}} .gh small{{color:#8b949e}}
.tarjeta{{background:{INK};color:{PAPEL};border-radius:10px;padding:18px;aspect-ratio:1.75;display:grid;align-content:space-between}} .tarjeta .wm b{{color:{PAPEL};font:700 26px SG}} .tarjeta .wm svg{{width:30px;height:30px}} .tarjeta small{{font:400 11px JB;color:#b9b3bd}}
.firma{{font:500 13px JB;color:#5b5560;display:flex;align-items:center;gap:6px;border-top:1px solid #e3ddd1;padding-top:10px}} .firma svg{{width:16px;height:16px}}
.web{{border:1px solid #e3ddd1;border-radius:10px;overflow:hidden}} .web .bar{{display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid #e3ddd1;font:700 15px SG}} .web .bar svg{{width:24px;height:24px}} .web .bar nav{{margin-left:auto;font:400 13px SG;color:#5b5560;display:flex;gap:14px}} .web .hero{{padding:22px 14px;font:700 26px/1.1 SG;letter-spacing:-.02em}} .web .hero em{{font-style:normal;color:{ROSA}}}'''
def dark(s): return s.replace(INK,'@I@').replace(ROSA,ROSA_D).replace('@I@',PAPEL)
sym=simbolo(); sym_t=simbolo(INK,INK); sym16=simbolo16()
html=f'''<!doctype html><meta charset="utf-8"><style>{css}</style>
<p class="sub">CLNDA · ronda 5 · desarrollo de C1: la llave en rosa y el dato en tinta. Símbolo afinado, versión chica, app icon, logotipo, paleta y contexto.</p>
<div class="g c3">
<div class="celda"><h2>Símbolo</h2><div class="fila"><span style="width:120px;height:120px">{sym}</span><span style="width:120px;height:120px">{sym_t}</span><span class="dark"><span style="width:96px;height:96px">{dark(sym)}</span><span style="width:96px;height:96px">{dark(sym_t)}</span></span></div><span class="tag">color · una tinta · sobre tinta (rosa claro {ROSA_D} para contraste)</span></div>
<div class="celda"><h2>Versión chica (16–24 px)</h2><div class="fila"><span style="width:120px;height:120px">{sym16}</span><span style="width:32px;height:32px">{sym}</span><span style="width:24px;height:24px">{sym16}</span><span style="width:16px;height:16px">{sym16}</span><span class="dark"><span style="width:24px;height:24px">{dark(sym16)}</span><span style="width:16px;height:16px">{dark(sym16)}</span></span></div><span class="tag">trazo más grueso y punto mayor; de 32 px en adelante, el símbolo normal</span></div>
<div class="celda"><h2>App icon</h2><div class="fila"><span style="width:120px;height:120px">{appicon()}</span><span style="width:120px;height:120px">{appicon(ROSA,PAPEL,INK)}</span><span style="width:120px;height:120px">{appicon(INK,ROSA_D,PAPEL)}</span></div><span class="tag">papel · rosa · tinta. Recomiendo papel: el rosa queda en la llave</span></div>
</div>
<div class="g c2">
<div class="celda"><h2>Logotipo · opciones</h2>
<div class="wm">{sym}<b class="sgf">CLNDA<span class="cur"></span></b></div><span class="tag">1 · Space Grotesk 700 con cursor de bloque (de la E)</span>
<div class="wm">{sym}<b class="syf">CLNDA</b></div><span class="tag">2 · Syne 800: más ancha, más estudio creativo</span>
<div class="wm">{sym}<b class="jbf">CLNDA_</b></div><span class="tag">3 · JetBrains Mono 700 con guion bajo: más código</span>
<div class="wm">{sym}<b class="unf">CLNDA</b></div><span class="tag">4 · Unbounded 700: redonda, de fiesta</span></div>
<div class="celda"><h2>Paleta</h2><div class="sw"><div><i style="background:{PAPEL}"></i><b>papel</b>{PAPEL}</div><div><i style="background:{INK}"></i><b>tinta</b>{INK}</div><div><i style="background:{ROSA}"></i><b>rosa</b>{ROSA}</div><div><i style="background:{TURQ}"></i><b>turquesa</b>{TURQ}</div><div><i style="background:{AMAR}"></i><b>amarillo</b>{AMAR}</div></div>
<p class="tag">Rosa es el color de marca y va solo en la llave y el cursor. Turquesa y amarillo son color de fiesta para ilustración, gráficas y fondos de redes; nunca en el símbolo. Rosa sobre papel 4.1:1 (gráfico sí, texto chico no); tinta sobre papel 16:1; sobre tinta la llave usa {ROSA_D}.</p>
<h3>En contexto</h3>
<div class="gh"><span>{appicon(ROSA,PAPEL,INK,256)}</span><div><b>clnda-studio</b><small>Soluciones en software y ciencia de datos · Oaxaca</small></div></div>
<div class="firma">{sym}hecho por CLNDA Studio</div></div>
</div>
<div class="g c2">
<div class="tarjeta"><div class="wm">{dark(sym)}<b>CLNDA<span class="cur" style="background:{ROSA_D}"></span></b></div><div><small>Kevin · software y ciencia de datos<br>hola@clnda.studio · clnda.studio</small></div></div>
<div class="web"><div class="bar">{sym}CLNDA Studio<nav><span>Trabajo</span><span>Estudio</span><span>Contacto</span></nav></div><div class="hero">Diseñamos soluciones<br>en software y <em>datos</em>.</div></div>
</div>'''
open('muestra.html','w').write(html); print('ok')
