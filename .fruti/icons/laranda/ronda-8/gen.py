# Laranda · ronda 8 · paleta intensa y neutra en género (usuario: «colores más intensos, para hombres y mujeres»).
# Conjunto validado con CVD: violeta intenso, naranja de acento, oro reservar, verde éxito, rojo error, sobre hueso frío.
import sys
S=sys.argv[1]
INK='#15121C'; FONDO='#F6F4EF'; ARENA='#EAE6DE'; SUAVE='#4F4B57'
exec(open('../ronda-5/gen.py').read().split("fr=S+'/fuentes/Fraunces")[0].replace("S=sys.argv[1];","S=sys.argv[1] if False else S;").replace("INK='#1C1917'; CREMA='#FAF8F5'",f"INK='{INK}'; CREMA='{FONDO}'"))
PAL=[('Violeta intenso','#5B3BB5','#4A2DA8'),('Naranja (acento)','#E0611A','#F2C9B2'),('Oro (solo reservar)','#D9A400',None),('Verde (éxito)','#0E8F5E',None),('Rojo (error)','#A8202F',None),('Tinta',INK,None),('Hueso',FONDO,None),('Arena',ARENA,None)]
VIO2='#5B3BB5'; NAR='#E0611A'; NART='#F2C9B2'; LILA2='#C4B5F0'; NIEBLA2='#ECE7FA'
def flor2(vio,acc,k=INK,f=FONDO):
    s=color(flor(3.2,(8,7),k,f),vio)
    extra=f'<path d="M70 20 C78 14 92 18 96 30 C98 40 90 48 80 46 C72 44 66 32 70 20Z" fill="{acc}" transform="translate(9 6)"/>'
    return s.replace('<path d="M60 46',extra+'<path d="M60 46',1)
def app2(vio,acc,r=112):
    body=flor2(LILA2,acc,FONDO,vio).split(">",1)[1].rsplit("</svg>",1)[0]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="{r}" fill="{vio}"/><g fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(32 32) scale(3.5)">{body}</g></svg>'
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
.sub{{color:{SUAVE};margin:0 0 14px}} .tag{{font:400 12px MR;color:{SUAVE}}} h2{{font:700 16px MR;margin:0}} svg{{display:block}}
.g{{display:grid;gap:16px;margin-bottom:16px}} .c2{{grid-template-columns:1fr 1fr}} .c3{{grid-template-columns:repeat(3,1fr)}}
.celda{{background:{FONDO};border:1px solid {ARENA};border-radius:14px;padding:16px;display:grid;gap:12px;align-content:start;min-width:0}}
.sw{{display:grid;grid-template-columns:repeat(8,1fr);gap:8px}} .sw div{{display:grid;gap:3px;font-size:11px}} .sw i{{display:block;height:44px;border-radius:8px;border:1px solid rgba(0,0,0,.08)}} .sw code{{font-size:10px;color:{SUAVE}}}
.lock{{display:flex;align-items:center;gap:10px}} .lock>span{{display:block;width:84px;height:84px}} .lock svg{{width:100%;height:100%}} .wm{{font:600 46px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 100}}
.f{{display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap}} .f span{{display:block;overflow:hidden}} .f svg{{width:100%;height:100%}}
.ui{{background:#fff;border:1px solid {ARENA};border-radius:12px;padding:14px;display:grid;gap:10px}} .ui h3{{margin:0;font:700 18px FR;font-variation-settings:"opsz" 72,"SOFT" 100}} .ui p{{margin:0;color:{SUAVE}}}
.chip{{display:inline-flex;align-items:center;gap:6px;font-weight:600;font-size:12px;padding:4px 10px;border-radius:999px}} .chip span{{width:14px;height:14px;display:block}} .chip svg{{width:100%;height:100%}}
.btn{{display:inline-block;background:#D9A400;color:{INK};font-weight:700;padding:9px 14px;border-radius:10px}} .btn2{{display:inline-block;background:{VIO2};color:#fff;font-weight:700;padding:9px 14px;border-radius:10px}} .lnk{{color:{NAR};font-weight:700}}
.est{{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;font-weight:600}} .est span{{padding:4px 10px;border-radius:6px;color:#fff}}
.oscuro{{background:{INK};color:{FONDO};border-color:{INK}}} .oscuro .ui{{background:#221E2E;border-color:#2E2940;color:{FONDO}}} .oscuro .ui p{{color:#B9B4C4}} .oscuro .tag{{color:#B9B4C4}}
.banda{{height:58px;border-radius:10px;display:flex;align-items:center;padding:0 14px;font:600 16px FR;font-variation-settings:"opsz" 72,"SOFT" 100}}'''
sw=''.join(f'<div><i style="background:{h}"></i><b>{n}</b><code>{h}</code></div>' for n,h,_ in PAL)
html=f'''<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 8 · paleta intensa, neutra en género. Validada: todas las parejas se distinguen con visión normal (ΔE ≥ 15.7) y bajo daltonismo (≥ 7.4 con icono y texto en los estados). Fondo hueso frío en vez de crema; tinta más fría.</p>
<div class="celda"><h2>Paleta</h2><div class="sw">{sw}</div><span class="tag">Violeta: #5B3BB5 para acción y marca; #4A2DA8 para presionado y texto grande. Naranja: acento de marca (lóbulo que se separa, enlaces, destacados, ilustración). Oro solo en Reservar. Lila y niebla se recalculan desde el nuevo violeta: #C4B5F0 y #ECE7FA.</span></div>
<div class="g c2">
<div class="celda"><h2>Marca</h2><div class="lock"><span>{flor2(VIO2,NAR)}</span><span class="wm">laranda</span></div><div class="f"><span style="width:64px;height:64px">{flor2(VIO2,NAR)}</span><span style="width:40px;height:40px">{flor2(VIO2,NAR)}</span><span style="width:72px;height:72px">{app2(VIO2,NAR)}</span><span style="width:48px;height:48px">{app2(VIO2,NAR)}</span><span style="width:44px;height:44px;border-radius:50%">{app2(VIO2,NAR,256)}</span><span style="width:48px;height:48px">{app2('#4A2DA8',NAR)}</span></div><div class="banda" style="background:{VIO2};color:#fff">Tu oficio, en flor.</div><div class="banda" style="background:{NART};color:{INK}">Your craft, in bloom.</div></div>
<div class="celda"><h2>Interfaz · claro</h2><div class="ui"><h3>Andrés Cortés</h3><div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip" style="background:{NIEBLA2};color:{VIO2}"><span>{silueta(VIO2,NIEBLA2)}</span>Barbería</span><span class="chip" style="background:{NART};color:{INK}"><span>{silueta(NAR,NART)}</span>Afeitado clásico</span></div><p>Corte, barba y navaja. Centro, Oaxaca. Lunes a sábado.</p><div><span class="btn">Reservar</span> &nbsp; <span class="btn2">Ver agenda</span></div><p>Próximo espacio: <b style="color:{INK}">vie 24 oct · 16:00</b> · <span class="lnk">ver todos</span></p></div><div class="est"><span style="background:#0E8F5E">✓ Folio emitido</span><span style="background:#A8202F">✕ Cancelada</span><span style="background:#D9A400;color:{INK}">Reservar</span><span style="background:{NAR}">Nuevo</span></div></div>
</div>
<div class="g c2">
<div class="celda oscuro"><h2>Interfaz · oscuro</h2><div class="ui"><h3>Laura Méndez</h3><div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip" style="background:#2E2940;color:{LILA2}"><span>{silueta(LILA2,'#2E2940')}</span>Podología</span><span class="chip" style="background:#3A2A22;color:#F2A074"><span>{silueta('#F2A074','#3A2A22')}</span>Pedicure</span></div><p>Consulta y tratamiento. Reforma, Oaxaca.</p><div><span class="btn">Reservar</span> &nbsp; <span class="btn2" style="background:{LILA2};color:{INK}">Ver agenda</span></div><p>Próximo espacio: <b>jue 23 oct · 11:00</b> · <span class="lnk" style="color:#F2A074">ver todos</span></p></div><span class="tag">en oscuro el violeta sube a lila #C4B5F0 y el naranja a #F2A074 para contraste</span></div>
<div class="celda"><h2>Antes y después</h2><div class="f"><span style="width:120px;height:120px">{color(flor(3.2,(8,7)),'#6B4FA0')}</span><span style="width:120px;height:120px">{flor2(VIO2,NAR)}</span></div><div class="sw" style="grid-template-columns:repeat(4,1fr)"><div><i style="background:#6B4FA0"></i><b>antes</b><code>#6B4FA0</code></div><div><i style="background:#B8A9E0"></i><b>antes</b><code>#B8A9E0</code></div><div><i style="background:{VIO2}"></i><b>ahora</b><code>{VIO2}</code></div><div><i style="background:{NAR}"></i><b>ahora</b><code>{NAR}</code></div></div><span class="tag">Contrastes: violeta/hueso 7.0:1 · naranja/hueso 3.2:1 (gráfico y texto grande; texto chico en tinta) · verde/hueso 3.7:1 · rojo/hueso 6.6:1 · oro con texto en tinta 8.2:1</span></div>
</div>'''
open('banco.html','w').write(html); print('ok')
