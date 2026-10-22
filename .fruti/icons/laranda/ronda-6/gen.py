# Laranda · ronda 6 · tipografía: cuatro pares (primaria de marca + secundaria de interfaz) probados con B2 y con pantallas reales.
import sys
sys.path.insert(0,'../ronda-5')
S=sys.argv[1]; INK='#1C1917'; CREMA='#FAF8F5'; VIO='#6B4FA0'; LILA='#B8A9E0'; NIEBLA='#EDE9F7'; ORO='#C9A227'; ARENA='#F0EBE3'; SUAVE='#57534E'
import importlib.util
spec=importlib.util.spec_from_file_location('r5','../ronda-5/gen.py'); 
# reutilizar la flor B2 sin ejecutar el banco: copiamos las funciones necesarias
exec(open('../ronda-5/gen.py').read().split("fr=S+'/fuentes/Fraunces")[0].replace("S=sys.argv[1];","S=sys.argv[1] if False else S;"))
B2=color(flor(3.2,(8,7))); B2t=color(flor(3.2,(0,0),con_mancha=False)); SIL=silueta(VIO,CREMA)
F={'FR':'Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf','LO':'Lora.ttf','BR':'BricolageGrotesque[opsz,wdth,wght].ttf','NR':'Newsreader%5Bopsz,wght%5D.ttf',
   'MR':'Manrope[wght].ttf','DM':'DMSans.ttf','AT':'Atkinson.ttf','ON':'Onest.ttf','IS':'InstrumentSans[wdth,wght].ttf','PM':'IBMPlexMono.ttf'}
faces=''.join(f'@font-face{{font-family:{k};src:url("file://{S}/fuentes/{v}");font-weight:100 900}}' for k,v in F.items())
P=[('1 · Fraunces + Manrope','FR','MR','"opsz" 72,"SOFT" 100','Editorial cálida y una sans redonda de herramienta. Es el par que el brief recomienda.'),
   ('2 · Fraunces + Atkinson Hyperlegible Next','FR','AT','"opsz" 72,"SOFT" 100','La misma marca con la sans más legible que existe para móvil y sol; letras que no se confunden (l/I/1).'),
   ('3 · Lora + DM Sans','LO','DM','','Serif más clásica y tranquila; DM Sans es neutra y muy de producto. Menos personalidad, más seguridad.'),
   ('4 · Bricolage Grotesque + Onest','BR','ON','"opsz" 96','Sin serif: el carácter lo pone Bricolage, con algo de dibujo en las curvas, y Onest es limpia. Más moderno, menos artesanal.')]
css=f'''{faces}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 MR,system-ui,sans-serif;width:1200px;box-sizing:border-box}}
.sub{{color:{SUAVE};margin:0 0 14px}} .tag{{font:400 12px MR;color:{SUAVE}}}
.par{{display:grid;grid-template-columns:300px 1fr 1fr;gap:16px;background:{CREMA};border:1px solid {ARENA};border-radius:14px;padding:16px;margin-bottom:16px}}
.par>div{{display:grid;gap:10px;align-content:start;min-width:0}} h2{{font:700 16px MR;margin:0}} svg{{display:block}}
.lock{{display:flex;align-items:center;gap:10px}} .lock>span{{display:block;width:60px;height:60px}} .lock svg{{width:100%;height:100%}}
.wm{{font-size:46px;line-height:1;letter-spacing:-.01em;font-weight:600}}
.tl{{font-size:22px;line-height:1.2;font-weight:600}} .tl i{{font-style:italic;font-weight:400;color:{SUAVE}}}
.ui{{background:#fff;border:1px solid {ARENA};border-radius:12px;padding:14px;display:grid;gap:10px}} .ui h3{{margin:0;font-size:20px;font-weight:700}} .ui p{{margin:0;font-size:14px;color:{SUAVE}}} .ui .num{{font-size:15px;font-variant-numeric:tabular-nums}}
.chip{{display:inline-flex;align-items:center;gap:6px;background:{NIEBLA};color:{VIO};font-weight:600;font-size:12px;padding:4px 10px;border-radius:999px}} .chip span{{width:14px;height:14px;display:block}} .chip svg{{width:100%;height:100%}}
.btn{{display:inline-block;background:{ORO};color:{INK};font-weight:700;font-size:14px;padding:10px 16px;border-radius:10px}}
.folio{{background:#FBF9F4;border:1px solid #E7E1D6;border-radius:4px;padding:12px;font:12px/1.5 PM;display:grid;gap:4px}} .folio b{{font-size:15px}}
.small{{font-size:12px;color:{SUAVE}}} .alf{{font-size:13px;color:{SUAVE};letter-spacing:.02em;word-break:break-all}}'''
rows=''
for name,p,s,fvs,nota in P:
    st=f'font-family:{p};'+(f'font-variation-settings:{fvs};' if fvs else '')
    rows+=f'''<div class="par"><div><h2>{name}</h2><span class="tag">{nota}</span><div class="lock"><span>{B2}</span><span class="wm" style="{st}">laranda</span></div><div class="tl" style="{st}">Tu oficio, en flor.<br><i>Your craft, in bloom.</i></div><div class="alf" style="font-family:{s}">abcdefghijklmnñopqrstuvwxyz 0123456789 Il1 · ¿Cuándo? ¡Listo! · 10:30 · $650.00</div></div>
<div><div class="ui" style="font-family:{s}"><div style="display:flex;gap:10px;align-items:center"><span style="width:44px;height:44px;border-radius:50%;background:#D8CFC2;display:block"></span><div><h3 style="{st}">Mariana Ruiz</h3><span class="chip"><span>{SIL}</span>Colorista</span></div></div><p>Corte, color y tratamientos. Col. Reforma, Oaxaca. Atiende de martes a sábado.</p><div class="num">Próximo espacio: <b>jue 23 oct · 10:30</b> · desde <b>$650</b></div><span class="btn">Reservar</span><p class="small">★ 4.9 · 128 reseñas · responde en 1 h</p></div><span class="tag">cabecera de perfil: título en primaria, todo lo demás en secundaria</span></div>
<div><div class="folio"><b style="{st}">laranda</b>FOLIO LR-2026-00417<br>Corte y color · Mariana R.<br>22 oct 2026 · 10:30 · $650.00<br>Pagado · tarjeta ····4821</div><div class="ui" style="font-family:{s}"><h3 style="{st};font-size:17px">Tu perfil ya está publicado</h3><p>Compártelo por WhatsApp o Instagram. Cada reserva te llega aquí y al correo.</p><div style="display:flex;gap:8px;align-items:center"><span style="width:22px;height:22px;display:block">{SIL}</span><span class="small" style="color:{VIO};font-weight:600">Florece</span></div></div><span class="tag">folio en IBM Plex Mono (fijo por el brief); aviso de estado</span></div></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · ronda 6 · tipografía. Cuatro pares (primaria de marca y títulos + secundaria de interfaz y cuerpo), cada uno con el lockup B2, el tagline bilingüe, el alfabeto de la secundaria, una cabecera de perfil, un folio y un aviso.</p>{rows}')
print('ok')
