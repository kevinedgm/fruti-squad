# Laranda · ronda 7 · color de acento. Tres candidatos junto al violeta y a los tres colores reservados (oro, salvia, terracota),
# en la flor B2 (la mancha del lóbulo que se separa), en interfaz y en ilustración.
import sys
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIO='#6B4FA0'; LILA='#B8A9E0'; NIEBLA='#EDE9F7'; ORO='#C9A227'; SALVIA='#4F7A5B'; TERRA='#B4452F'; ARENA='#F0EBE3'; SUAVE='#57534E'
exec(open('../ronda-5/gen.py').read().split("fr=S+'/fuentes/Fraunces")[0].replace("S=sys.argv[1];","S=sys.argv[1] if False else S;"))
def L(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def C(a,b): x,y=L(a),L(b); return (max(x,y)+.05)/(min(x,y)+.05)
# flor B2 con segunda mancha: el lóbulo que se separa lleva el acento
def flor_acento(acc):
    s=color(flor(3.2,(8,7)))
    extra=f'<path d="M70 20 C78 14 92 18 96 30 C98 40 90 48 80 46 C72 44 66 32 70 20Z" fill="{acc}" transform="translate(9 6)"/>'
    return s.replace('<path d="M60 46',extra+'<path d="M60 46',1)
A=[('1 · Durazno (acento de relleno)','#F2B48C','#F9DCC8','Claro y cálido. Vive en manchas, fondos de sección, ilustración y chips; el texto encima siempre en tinta. No compite con oro, salvia ni terracota porque no es un color de texto.'),
   ('2 · Coral (acento vivo)','#E0674B','#F7C9BC','Expresivo y moderno junto al violeta. Problema: se parece al terracota de error (ΔE 12); para usarlo habría que oscurecer el error a ladrillo #8A2E1E.'),
   ('3 · Cielo (acento frío)','#3F86C9','#CFE1F5','El cielo detrás de la jacaranda. Pasa contra todos los reservados; es el único que puede ir como texto sobre crema. Enfría la paleta.')]
fr=S+'/fuentes/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf'; mr=S+'/fuentes/Manrope[wght].ttf'
css=f'''@font-face{{font-family:FR;src:url("file://{fr}");font-weight:100 900}} @font-face{{font-family:MR;src:url("file://{mr}");font-weight:200 800}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
.sub{{color:{SUAVE};margin:0 0 14px}} .tag{{font:400 12px MR;color:{SUAVE}}} h2{{font:700 16px MR;margin:0}} svg{{display:block}}
.op{{display:grid;grid-template-columns:260px 1fr 1fr;gap:16px;background:{CREMA};border:1px solid {ARENA};border-radius:14px;padding:16px;margin-bottom:16px}} .op>div{{display:grid;gap:10px;align-content:start;min-width:0}}
.sw{{display:flex;gap:6px}} .sw i{{display:block;width:34px;height:34px;border-radius:8px;border:1px solid rgba(0,0,0,.08)}}
.lock{{display:flex;align-items:center;gap:10px}} .lock>span{{display:block;width:72px;height:72px}} .lock svg{{width:100%;height:100%}} .wm{{font:600 40px/1 FR;font-variation-settings:"opsz" 72,"SOFT" 100}}
.ui{{background:#fff;border:1px solid {ARENA};border-radius:12px;padding:14px;display:grid;gap:10px}} .ui h3{{margin:0;font:700 18px FR;font-variation-settings:"opsz" 72,"SOFT" 100}} .ui p{{margin:0;color:{SUAVE}}}
.chip{{display:inline-flex;align-items:center;gap:6px;font-weight:600;font-size:12px;padding:4px 10px;border-radius:999px;color:{INK}}} .chip span{{width:14px;height:14px;display:block}} .chip svg{{width:100%;height:100%}}
.btn{{display:inline-block;background:{ORO};color:{INK};font-weight:700;padding:9px 14px;border-radius:10px}} .est{{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;font-weight:600}} .est span{{padding:4px 10px;border-radius:6px;color:#fff}}
.num{{font-family:ui-monospace,monospace;font-size:11px;color:{SUAVE}}} .banda{{height:54px;border-radius:10px;display:flex;align-items:center;padding:0 14px;font:600 15px FR;font-variation-settings:"opsz" 72,"SOFT" 100}}'''
rows=''
for name,acc,tint,nota in A:
    sil=silueta(acc,CREMA) if C(acc,CREMA)>=3 else silueta(VIO,CREMA)
    rows+=f'''<div class="op"><div><h2>{name}</h2><span class="tag">{nota}</span><div class="sw"><i style="background:{CREMA}"></i><i style="background:{INK}"></i><i style="background:{VIO}"></i><i style="background:{LILA}"></i><i style="background:{acc}"></i><i style="background:{tint}"></i></div><span class="num">acento/crema {C(acc,CREMA):.1f}:1 · tinta/acento {C(INK,acc):.1f}:1 · acento/violeta {C(acc,VIO):.1f}:1</span><div class="est"><span style="background:{ORO};color:{INK}">Reservar</span><span style="background:{SALVIA}">Folio emitido</span><span style="background:{TERRA}">Cancelada</span><span style="background:{acc};color:{INK if C(INK,acc)>=4.5 else '#fff'}">acento</span></div></div>
<div><div class="lock"><span>{flor_acento(acc)}</span><span class="wm">laranda</span></div><div class="banda" style="background:{tint};color:{INK}">Tu oficio, en flor.</div><div class="ui"><h3>Mariana Ruiz</h3><div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip" style="background:{tint}"><span>{silueta(VIO,tint)}</span>Colorista</span><span class="chip" style="background:{NIEBLA};color:{VIO}"><span>{silueta(VIO,NIEBLA)}</span>Uñas</span></div><p>Corte, color y tratamientos. Col. Reforma, Oaxaca.</p><span class="btn">Reservar</span></div></div>
<div><div class="ui"><h3>Tu perfil ya está publicado</h3><p>Compártelo por WhatsApp o Instagram.</p><div style="display:flex;gap:8px;align-items:center"><span style="width:26px;height:26px;display:block">{sil}</span><b style="color:{acc if C(acc,CREMA)>=4.5 else INK}">Florece</b></div></div><div class="ui" style="background:{tint};border-color:{tint}"><h3>Primera reseña</h3><p style="color:{INK}">«Me atendió puntual y el color quedó justo como lo pedí.»</p><span class="tag">fondo de sección en el tono claro del acento</span></div></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 7 · color de acento. Cada candidato con el violeta y los tres reservados (oro reservar, salvia éxito, terracota error), en la flor B2 como mancha del lóbulo que se separa, en chips, banda y fondo de sección.</p>{rows}')
print('ok')
