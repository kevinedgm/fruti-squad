# Manual de marca · Directorio Manik (consolida el DS del directorio + decisiones aprobadas hasta 2026-11-04).
# Uso: python3 gen.py → manual.html. Logotipos, símbolo y avatares: archivos reales embebidos. Datos de médicos: de ejemplo.
import os, re, json, base64, math, html
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
TOK = json.load(open(os.path.join(M, 'directorio-ds/project/tokens.json')))
C = {t['name']: (t['value'] if isinstance(t['value'], str) else list(t['value'].values())[0]) for t in TOK['color']['tokens']}
USO = {t['name']: t.get('usage', '') for t in TOK['color']['tokens']}
for _ in range(4):
    C = {k: (C[v[1:-1]] if isinstance(v, str) and v.startswith('{') else v) for k, v in C.items()}
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
L = '/root/.cache/fruti-uva/package/icons/'
def ico(n, size=20, color='currentColor', sw=2):
    inner = ''.join(re.findall(r'<(?:path|circle|rect|line|polyline|ellipse|polygon)[^>]*/>', open(L + n + '.svg').read()))
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{inner}</svg>'
def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return f'{(la + .05) / (lb + .05):.1f}'
e = html.escape
IMG = {k: uri(f'manik-final/svg/{k}.svg') for k in ['simbolo', 'simbolo-1tinta', 'simbolo-blanco', 'logotipo', 'logotipo-vertical', 'logotipo-endoso', 'logotipo-blanco', 'logotipo-1tinta', 'app-icon', 'favicon']}
AV = {k: uri(f'directorio-ds/avatares/avatar-{k}.svg') for k in ['mujer', 'hombre', 'neutro']}
MM_LOGO = uri('final/svg/medicalmanik-logotipo.svg'); ECO = uri('final/svg/ecosistema.svg')
IMPULSA = 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, 'directorio-ds/ecosistema/sello-impulsa.svg'), 'rb').read()).decode()

# ---------- Color: grupos con contraste calculado
GRUPOS = [
 ('Base de lectura', [('bruma', None), ('blanco', None), ('tinta', 'blanco'), ('muted', 'blanco'), ('linea', None), ('linea-control', 'blanco')]),
 ('Marca y acción', [('cian', 'blanco'), ('cian-ui', 'blanco'), ('cian-ui-hover', 'blanco'), ('focus', 'blanco')]),
 ('Luz', [('luz-cian', None), ('luz-calida', None), ('foto-inicio', None), ('foto-fin', None)]),
 ('Categorías y sellos', [('categoria-cian', None), ('categoria-calida', None), ('categoria-azul', None), ('icono-calido', 'categoria-calida')]),
 ('Estados y detalles', [('estrella', 'blanco'), ('exito', 'blanco'), ('exito-suave', None), ('on-exito-suave', 'exito-suave'), ('texto-calido', 'luz-calida')]),
 ('Reservados', [('azul-medicalmanik', 'blanco')]),
]
def swatch(n, sobre):
    v = C.get(n)
    if not v: return ''
    oscuro = lum(v) < .35
    ratio = f'<span class="ra">{cr(v, C[sobre])}:1 sobre {sobre}</span>' if sobre else f'<span class="ra">Tinta encima {cr(C["tinta"], v)}:1</span>'
    return (f'<figure class="sw"><span class="chip" style="background:{v};color:{"#fff" if oscuro else C["tinta"]}"><b>{n}</b><code>{v.upper()}</code></span>'
            f'<figcaption>{e(USO.get(n, ""))}{ratio}</figcaption></figure>')
COLOR = ''.join(f'<div class="grupo"><h3>{g}</h3><div class="sws">{"".join(swatch(n, s) for n, s in items)}</div></div>' for g, items in GRUPOS)

# ---------- Sellos de categoría (aprobados, categorias/r02)
CATS = [('scan-face', 'Piel', 'Dermatología'), ('brain', 'Salud mental', 'Psicología y psiquiatría'), ('apple', 'Alimentación', 'Nutrición'),
        ('flower-2', 'Salud íntima', 'Ginecología y urología'), ('baby', 'Niñas y niños', 'Pediatría'), ('stethoscope', 'Chequeo general', 'Medicina general')]
TRI = [('categoria-cian', 'cian-ui'), ('categoria-calida', 'icono-calido'), ('categoria-azul', 'tinta')]
def sello(k, c, tam, pre):
    f, t = TRI[k % 3]; F, T = C[f], C[t]
    ley = f'{c[1].upper()} · {c[2].upper()} · '; rep = max(1, round(314 / (len(ley) * 8.0)))
    sub = lambda x, w: ico(c[0], w, T).replace('<svg ', f'<svg x="{x}" y="{x}" ')
    comp = tam < 104
    cuerpo = (f'<circle cx="70" cy="70" r="50" fill="#fff"/><circle cx="70" cy="70" r="50" fill="none" stroke="{T}" stroke-width="2" stroke-dasharray="2.5 4"/>{sub(43, 54)}' if comp else
              f'<circle cx="70" cy="70" r="37" fill="#fff"/><circle cx="70" cy="70" r="37" fill="none" stroke="{T}" stroke-width="1.5" stroke-dasharray="2 3.2"/>'
              f'<text font-family="Onest,sans-serif" font-size="11" font-weight="600" letter-spacing="1.4" fill="{T}"><textPath href="#a-{pre}{k}" textLength="312" lengthAdjust="spacing">{ley * rep}</textPath></text>{sub(52, 36)}')
    return (f'<div class="scat"><svg width="{tam}" height="{tam}" viewBox="0 0 140 140" aria-hidden="true"><defs><path id="a-{pre}{k}" d="M70,70 m-50,0 a50,50 0 1,1 100,0 a50,50 0 1,1 -100,0"/></defs>'
            f'<circle cx="70" cy="70" r="68" fill="{F}"/><circle cx="70" cy="70" r="63" fill="none" stroke="{T}" stroke-width="1.5"/>{cuerpo}</svg><b>{c[1]}</b><small>{c[2]}</small></div>')
SELLOS = ''.join(sello(k, c, 132, 'g') for k, c in enumerate(CATS))
ESCALA = ''.join(f'<figure>{sello(0, CATS[0], w, "e" + str(w))}<figcaption>{t} · {w} px</figcaption></figure>' for w, t in ((88, 'Compacto · celular'), (112, 'Mediano · tableta'), (132, 'Grande · escritorio')))

# ---------- Componentes de muestra (estáticos)
FICHA = f'''<article class="fm"><div class="fmi"><div class="face"><img src="{AV['mujer']}" alt="Sin foto: Dra. Mariana Soto"></div><div class="who"><h4>Dra. Mariana Soto</h4><p class="spec">Dermatóloga · acné y lunares</p>
<p class="ced">{ico('badge-check', 16, C['on-exito-suave'])}<span><span class="nw">Céd. Prof. 10234567</span> · <span class="nw">Céd. Esp. 11876543</span></span></p><p class="meta"><b aria-hidden="true">★</b> 4.9 · 312 opiniones</p></div>
<div class="cons"><div class="co"><span class="l1">Angelópolis · <span class="nw">1.8 km · <b>$900</b></span></span><span class="btn pri">Agendar</span><span class="l2">{ico('calendar-check', 16, C['cian-ui'])}<span class="nw">Agenda en Manik</span> <span class="nw">· Hoy, 16:30</span></span><span class="alt">{ico('phone', 16)}o llama al <span class="nw">222 555 0140</span></span></div>
<div class="co"><span class="l1">Centro · <span class="nw">5.2 km · <b>$700</b></span></span><span class="btn sec">Llamar</span><span class="l2">{ico('phone', 16, C['cian-ui'])}<span class="nw">Por teléfono</span> <span class="nw">· 222 555 0141</span></span></div></div></div></article>'''
PROMO = f'''<div class="promo"><span class="pimg"></span><span class="ptx"><span class="etq">Patrocinado</span><b>Revisión de lunares a $650</b><small>Clínica Dermalia · hasta el 30 de noviembre · <span class="nw">con Impulsa Manik</span></small></span></div>'''
HORAS = '<div class="dias">' + ''.join(f'<span class="d{" on" if i == 0 else ""}{" off" if n == 0 else ""}"><small>{a}</small><b>{b}</b><small>{"sin lugar" if n == 0 else f"{n} lugares"}</small></span>' for i, (a, b, n) in enumerate([('Hoy', '4', 7), ('Mañana', '5', 6), ('Vie', '6', 3), ('Sáb', '7', 0)])) + '</div><div class="horas">' + ''.join(f'<span>{h}</span>' for h in ['16:30', '17:00', '17:30', '18:30', '19:00', '19:30']) + '</div>'

VOZ = [('«Encuentra a tu médico cerca de ti.»', '«Directorio de profesionales de la salud»'), ('«Hoy tiene espacio a las 11:30»', '«Disponibilidad en el slot 11:30»'),
       ('«Agenda en Manik» (la cita es presencial)', '«En línea» o «Cita en línea»: se confunde con videoconsulta'), ('«Te mandamos un recordatorio un día antes»', '«Su cita ha sido registrada exitosamente en el sistema»'),
       ('«Miércoles 4 de noviembre, 17:00»', '«4/11 17:00» (en México y EUA se lee distinto)'), ('«Ese horario se acaba de ocupar. Elige otro; tus datos se quedan como están.»', '«Error 409: conflicto de reserva»'),
       ('«¿Cómo te fue con el Dr. Díaz?»', '«¿Cómo te fue con Dr. Mario?»'), ('«312 pacientes opinaron sobre la Dra. Soto»', '«¡Los mejores doctores!»')]
VOZ_T = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in VOZ)

NAV = [('esencia', 'Esencia'), ('marca', 'Marca'), ('color', 'Color'), ('tipografia', 'Tipografía'), ('forma', 'Forma y espacio'), ('iconos', 'Iconos y sellos'),
       ('fotografia', 'Fotografía'), ('voz', 'Voz'), ('componentes', 'Componentes'), ('reglas', 'Reglas del producto'), ('accesibilidad', 'Accesibilidad'), ('pendientes', 'Pendientes')]
NAVH = ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in NAV)

CSS = f'''
/* Manual: índice fijo a la izquierda en escritorio, arriba en celular; secciones en columna de lectura. Tema claro único (decisión de marca). */
:root{{--bruma:{C['bruma']};--blanco:#fff;--lavado:{C['lavado']};--tinta:{C['tinta']};--muted:{C['muted']};--linea:{C['linea']};--cian:{C['cian']};--cian-ui:{C['cian-ui']};
--luz-cian:{C['luz-cian']};--luz-calida:{C['luz-calida']};--estrella:{C['estrella']};--on-exito-suave:{C['on-exito-suave']};--exito-suave:{C['exito-suave']};--texto-calido:{C['texto-calido']};--foto-inicio:{C['foto-inicio']};--foto-fin:{C['foto-fin']};
--display:"Urbanist",ui-sans-serif,system-ui,sans-serif;--sans:"Onest",ui-sans-serif,system-ui,sans-serif;color-scheme:light}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{margin:0;background:var(--bruma);color:var(--tinta);font:16px/1.6 var(--sans)}}
a{{color:var(--cian-ui)}}a:focus-visible,button:focus-visible{{outline:3px solid var(--cian-ui);outline-offset:2px}}
h1,h2,h3,h4{{margin:0;text-wrap:balance}}p{{margin:0}}code{{font:500 13px ui-monospace,SFMono-Regular,Menlo,monospace;overflow-wrap:anywhere}}
.nw{{white-space:nowrap}}
.wrap{{max-width:1240px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.portada{{background:radial-gradient(60% 80% at 8% 0%,var(--luz-cian),transparent 70%),radial-gradient(50% 70% at 95% 20%,var(--luz-calida),transparent 70%),var(--bruma)}}
.portada .wrap{{padding-block:28px 56px;display:grid;gap:28px}}
.portada .logo{{height:34px;width:auto}}.portada h1{{font:300 clamp(44px,9vw,92px)/1 var(--display);letter-spacing:-.04em;max-width:12ch}}.portada h1 b{{font-weight:600}}
.portada .lead{{font-size:19px;color:var(--muted);max-width:56ch}}.portada .meta{{display:flex;flex-wrap:wrap;gap:8px}}.portada .meta span{{background:#fff;border-radius:999px;padding:4px 12px;font-size:13px;color:var(--muted)}}
.cuerpo{{display:grid;grid-template-columns:minmax(0,1fr);gap:0;padding-block:8px 64px}}.cuerpo>*{{min-width:0}}
@media (min-width:1024px){{.cuerpo{{grid-template-columns:200px minmax(0,1fr);gap:48px}}}}
nav.indice{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bruma);border-bottom:1px solid var(--linea);margin:0 calc(-1 * max(16px,env(safe-area-inset-left,0px)));padding:8px max(16px,env(safe-area-inset-left,0px))}}
nav.indice ul{{list-style:none;margin:0;padding:0;display:flex;gap:6px;overflow-x:auto;scrollbar-width:none}}
nav.indice a{{display:inline-flex;align-items:center;min-height:36px;padding:0 12px;border-radius:999px;background:#fff;border:1px solid var(--linea);color:var(--tinta);text-decoration:none;font-size:14px;white-space:nowrap}}
@media (min-width:1024px){{nav.indice{{margin:0;padding:24px 0;border:0;top:0;align-self:start;max-height:100vh;overflow:auto}}nav.indice ul{{flex-direction:column;overflow:visible}}nav.indice a{{background:none;border:0;padding:0 8px;min-height:32px}}nav.indice a:hover{{background:#fff}}}}
section.s{{display:grid;grid-template-columns:minmax(0,1fr);gap:20px;padding-block:40px;border-bottom:1px solid var(--linea);scroll-margin-top:64px;min-width:0}}
.s>h2{{font:300 clamp(32px,5vw,48px)/1.05 var(--display);letter-spacing:-.03em}}.s>h2 b{{font-weight:600}}
.s .intro{{font-size:18px;color:var(--muted);max-width:62ch}}.s h3{{font:600 20px/1.2 var(--display)}}
.ey{{font:600 12px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--cian-ui)}}
.grid2{{display:grid;gap:16px}}@media (min-width:760px){{.grid2{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.grid3{{display:grid;gap:16px}}@media (min-width:760px){{.grid3{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
.card{{background:#fff;border:1px solid var(--linea);border-radius:24px;padding:20px;display:grid;gap:10px;min-width:0}}.card p{{color:var(--muted)}}
.lista{{margin:0;padding-left:20px;display:grid;gap:6px;max-width:68ch}}.lista b{{font-weight:600}}
.fam{{display:grid;gap:12px}}@media (min-width:760px){{.fam{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
.fam .card img{{width:40px;height:40px}}
/* Marca */
.lienzo{{border-radius:24px;display:grid;place-items:center;padding:28px;min-height:150px;border:1px solid var(--linea)}}.lienzo img{{max-height:72px;width:auto;max-width:100%}}
.lienzo.claro{{background:#fff}}.lienzo.bruma{{background:var(--bruma)}}.lienzo.oscuro{{background:var(--tinta);border-color:var(--tinta)}}.lienzo.luz{{background:linear-gradient(160deg,var(--luz-cian),var(--luz-calida))}}
.pie{{font-size:13px;color:var(--muted);margin-top:6px}}
.respeto{{position:relative;display:inline-grid;place-items:center;padding:22px;background:repeating-linear-gradient(45deg,var(--luz-cian) 0 6px,#fff 6px 12px);border-radius:12px}}.respeto img{{height:88px;display:block;background:#fff}}
.mal{{display:grid;gap:12px}}@media (min-width:640px){{.mal{{grid-template-columns:repeat(4,minmax(0,1fr))}}}}
.mal figure{{margin:0;background:#fff;border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:8px;justify-items:center;text-align:center;font-size:13px;color:var(--muted)}}.mal img{{height:40px;width:auto}}
.mal .x{{font:700 12px var(--sans);color:#B42318;letter-spacing:.06em}}
/* Color */
.grupo{{display:grid;gap:10px}}.sws{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}}
.sw{{margin:0;display:grid;gap:6px}}.sw .chip{{border-radius:18px;min-height:96px;padding:12px 14px;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;border:1px solid rgba(20,33,61,.08)}}.sw .chip b{{font:600 15px var(--display)}}
.sw figcaption{{font-size:13px;line-height:18px;color:var(--muted);display:grid;gap:4px}}.sw .ra{{font-weight:600;color:var(--tinta);font-variant-numeric:tabular-nums}}
.halo{{border-radius:24px;min-height:160px;background:radial-gradient(60% 90% at 0% 0%,var(--luz-cian),transparent 70%),radial-gradient(60% 80% at 100% 20%,var(--luz-calida),transparent 70%),var(--bruma);border:1px solid var(--linea);display:grid;place-items:center;padding:20px;text-align:center;color:var(--muted)}}
/* Tipografía */
.esp-u{{font:300 clamp(40px,7vw,72px)/1 var(--display);letter-spacing:-.035em}}.esp-u b{{font-weight:600}}
.esp-o{{font:400 17px/1.6 var(--sans);max-width:60ch}}
.escala{{display:grid;gap:10px}}.escala div{{display:grid;grid-template-columns:96px minmax(0,1fr);gap:12px;align-items:baseline;border-top:1px solid var(--linea);padding-top:10px}}.escala span{{font-size:13px;color:var(--muted)}}
.tab{{font-variant-numeric:tabular-nums}}
/* Forma */
.radios{{display:flex;flex-wrap:wrap;gap:14px;align-items:end}}.radios figure{{margin:0;display:grid;gap:6px;justify-items:center;font-size:13px;color:var(--muted)}}.radios span{{display:block;width:72px;height:72px;background:var(--luz-cian);border:1.5px solid var(--cian-ui)}}
.esp{{display:grid;gap:8px}}.esp div{{display:grid;grid-template-columns:80px minmax(0,1fr) 1.2fr;gap:12px;align-items:center;font-size:14px}}.esp i{{display:block;height:14px;background:var(--cian-ui);border-radius:4px}}.esp small{{color:var(--muted)}}
/* Sellos */
.sellos{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}@media (min-width:760px){{.sellos{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}@media (min-width:1200px){{.sellos{{grid-template-columns:repeat(6,minmax(0,1fr))}}}}
.scat{{display:grid;justify-items:center;gap:4px;text-align:center}}.scat svg{{max-width:100%;height:auto;margin-bottom:6px}}.scat b{{font:600 16px/1.2 var(--display)}}.scat small{{font-size:13px;color:var(--muted)}}
.escl{{display:flex;flex-wrap:wrap;gap:28px;align-items:end}}.escl figure{{margin:0}}.escl figcaption{{font-size:13px;color:var(--muted);text-align:center;margin-top:6px}}
.ics{{display:flex;flex-wrap:wrap;gap:10px}}.ics span{{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--linea);border-radius:999px;padding:6px 14px 6px 10px;font-size:14px;color:var(--tinta)}}.ics svg{{color:var(--cian-ui)}}
/* Fotografía */
.fotos{{display:flex;flex-wrap:wrap;gap:16px;align-items:end}}.fotos figure{{margin:0;display:grid;gap:6px;width:120px;font-size:13px;color:var(--muted)}}.face{{border-radius:20px;aspect-ratio:3/4;overflow:hidden;background:linear-gradient(160deg,var(--foto-inicio),var(--foto-fin))}}.face img{{width:100%;height:100%;object-fit:cover;display:block}}
.marcafoto{{border-radius:28px;aspect-ratio:4/5;max-width:300px;background:linear-gradient(160deg,var(--foto-inicio),var(--foto-fin));display:grid;place-items:end start;padding:16px;color:var(--muted);font-size:13px;position:relative}}
.marcafoto .fl{{position:absolute;left:14px;top:18px;background:#fff;border-radius:16px;padding:8px 12px;font-size:13px;box-shadow:0 10px 26px rgba(20,33,61,.14)}}.marcafoto .fl b{{display:block;font:600 14px var(--display);color:var(--tinta)}}
/* Voz */
table.voz{{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--linea);border-radius:20px;overflow:hidden;font-size:15px}}table.voz th,table.voz td{{text-align:left;padding:12px 14px;border-bottom:1px solid var(--linea);vertical-align:top}}table.voz th{{font:600 13px var(--sans);letter-spacing:.06em;text-transform:uppercase}}
table.voz td:first-child{{color:var(--on-exito-suave)}}table.voz td:last-child{{color:#9B2C1F}}.tw{{overflow-x:auto}}
/* Componentes */
.muestra{{background:#fff;border:1px solid var(--linea);border-radius:24px;padding:20px;display:grid;gap:14px;min-width:0}}.muestra>.et{{font:600 12px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.btnrow{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;font:600 16px/20px var(--sans);min-height:48px;padding:0 22px;white-space:nowrap}}.btn.pri{{background:var(--cian-ui);color:#fff}}.btn.sec{{background:#fff;color:var(--cian-ui);border:1.5px solid var(--cian-ui)}}.btn.osc{{background:var(--tinta);color:#fff}}.btn.txt{{color:var(--tinta);text-decoration:underline;text-underline-offset:3px;padding:0 4px}}
.fm{{container-type:inline-size;max-width:420px}}.fmi{{border:1px solid var(--linea);border-radius:24px;padding:14px;display:grid;gap:12px;grid-template-columns:72px minmax(0,1fr);align-items:start;background:#fff}}
.fmi .face{{border-radius:16px}}.who{{display:grid;gap:4px;min-width:0}}.who h4{{font:600 20px/24px var(--display)}}.spec{{color:var(--muted);font-size:15px}}
.ced{{display:flex;gap:6px;align-items:flex-start;font-size:13px;line-height:18px;color:var(--muted);font-variant-numeric:tabular-nums}}.ced svg{{flex:none;margin-top:1px}}
.meta{{font-size:14px}}.meta b{{color:var(--estrella);font-weight:400}}
.cons{{grid-column:1/-1;border:1px solid var(--linea);border-radius:18px}}.co{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 12px;align-items:center;padding:12px 14px}}.co+.co{{border-top:1px solid var(--linea)}}
.co .l1{{font-size:15px;font-weight:600}}.co .l1 b{{font:600 17px var(--display)}}.co .l2{{display:flex;flex-wrap:wrap;align-items:center;gap:0 6px;font-size:14px;color:var(--muted)}}.co .btn{{grid-column:2;grid-row:1/3;min-height:44px;min-width:92px;padding:0 16px}}
.co .alt{{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;text-decoration:underline;text-underline-offset:3px;min-height:36px}}
.dias{{display:flex;gap:8px;overflow-x:auto}}.dias .d{{flex:none;display:grid;justify-items:center;gap:2px;min-width:76px;padding:8px 10px;border:1.5px solid var(--linea);border-radius:14px}}.dias .d b{{font:600 17px var(--display)}}.dias .d small{{font-size:12px;color:var(--muted)}}
.dias .on{{background:var(--tinta);border-color:var(--tinta);color:#fff}}.dias .on small{{color:#C7D2E4}}.dias .off{{opacity:.5}}
.horas{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;max-width:360px}}.horas span{{display:grid;place-items:center;min-height:44px;border:1.5px solid var(--cian-ui);color:var(--cian-ui);border-radius:999px;font-weight:600;font-variant-numeric:tabular-nums}}
.promo{{display:grid;background:#fff;border:1.5px dashed #6B7590;border-radius:24px;overflow:hidden;max-width:620px}}.pimg{{display:block;aspect-ratio:357/104;background:linear-gradient(120deg,var(--luz-cian),#9FDCE5 55%,var(--luz-calida))}}
.ptx{{display:grid;gap:4px;padding:12px 16px 14px}}.ptx b{{font:600 18px/1.25 var(--display)}}.ptx small{{color:var(--muted);font-size:14px}}
.etq{{justify-self:start;font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--texto-calido);background:var(--luz-calida);border-radius:999px;padding:3px 10px}}
@container (min-width:400px){{.fmi{{grid-template-columns:110px minmax(0,1fr)}}.fmi .face{{grid-row:1/3}}.cons{{grid-column:2}}}}
.impulsa{{display:flex;gap:12px;align-items:center;background:#fff;border:1px solid var(--linea);border-radius:18px;padding:12px 14px;font-size:14px;color:var(--muted);max-width:620px}}.impulsa img{{width:32px;height:32px;flex:none}}.impulsa b{{color:var(--tinta)}}
/* Reglas */
.reglas{{display:grid;gap:14px}}@media (min-width:860px){{.reglas{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.regla h3{{display:flex;align-items:center;gap:10px}}.regla h3 svg{{color:var(--cian-ui)}}
.estado{{font-size:12px;font-weight:600;border-radius:999px;padding:2px 10px;background:var(--exito-suave);color:var(--on-exito-suave)}}.estado.p{{background:var(--luz-calida);color:var(--texto-calido)}}
footer{{padding-block:28px 48px;color:var(--muted);font-size:14px;display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center}}footer img{{height:22px}}
'''

def S(id_, ey, titulo, intro, cuerpo):
    return f'<section class="s" id="{id_}" aria-labelledby="h-{id_}"><span class="ey">{ey}</span><h2 id="h-{id_}">{titulo}</h2>{f"<p class=intro>{intro}</p>" if intro else ""}{cuerpo}</section>'

SECCIONES = [
S('esencia', '01 · Esencia', 'Tu médico, <b>a la mano</b>.', 'Manik es lo que conoce el paciente: un directorio para encontrar médico, ver cuánto cuesta y agendar. La consulta es presencial; buscar y agendar es gratis.',
  f'''<div class="grid2"><div class="card"><h3>Para quién</h3><p>Pacientes de México y Centroamérica que buscan médico, muchas veces sin saber a qué especialista ir. El 70 % entra desde el celular.</p></div>
  <div class="card"><h3>Cómo se nombra</h3><p>En textos, «Manik» con mayúscula, sin «Mi» ni «Directorio» delante. En el logotipo, «manik». Se respalda con «de MedicalManik».</p></div></div>
  <h3>Fundamentos</h3><ul class="lista"><li><b>El paciente decide rápido.</b> Cada pantalla responde primero quién, dónde, cuándo y cuánto cuesta.</li><li><b>Luz, no color.</b> Bruma y blanco dominan; la luz cian y la cálida dan ambiente; tinta para leer; cian de interfaz para lo que se toca.</li>
  <li><b>Confianza demostrable.</b> Cédulas con número, opiniones solo de citas agendadas y precios a la vista.</li><li><b>Personas reales.</b> Médicos con su foto o su silueta; nada de bancos de imágenes.</li></ul>
  <h3>La familia MedicalManik</h3><div class="fam"><div class="card"><img src="{MM_LOGO}" alt="" style="width:auto;height:30px;max-width:100%"><b>MedicalManik</b><p>La empresa y el sello madre. Aparece como respaldo: «de MedicalManik».</p></div>
  <div class="card"><img src="{IMG['app-icon']}" alt=""><b>Manik · directorio</b><p>Para pacientes. Urbanist y Onest, luz cian y cálida. Este manual.</p></div>
  <div class="card"><img src="{ECO}" alt=""><b>Ecosistema Manik</b><p>Herramientas para clínicas («Producto Manik»: Expediente, Agenda, Impulsa…). Su propio sistema; comparten Urbanist, el cian del pin y la luz en marca.</p></div></div>'''),
S('marca', '02 · Marca', 'Símbolo y <b>logotipo</b>', 'El símbolo es la línea de pulso de la familia (una M que es un latido) en un cuadro con punta de pin: «aquí, cerca de ti». Se usan siempre los archivos; nunca se redibuja ni se reescribe con fuente.',
  f'''<div class="grid3"><div><div class="lienzo claro"><img src="{IMG['logotipo']}" alt="Logotipo manik"></div><p class="pie">Horizontal · uso principal</p></div>
  <div><div class="lienzo bruma"><img src="{IMG['logotipo-vertical']}" alt="Logotipo manik vertical" style="max-height:110px"></div><p class="pie">Vertical · espacios cuadrados</p></div>
  <div><div class="lienzo luz"><img src="{IMG['logotipo-endoso']}" alt="Logotipo manik de MedicalManik"></div><p class="pie">Con respaldo «de MedicalManik»</p></div>
  <div><div class="lienzo oscuro"><img src="{IMG['logotipo-blanco']}" alt="Logotipo manik en blanco"></div><p class="pie">Blanco · sobre tinta o foto oscura</p></div>
  <div><div class="lienzo claro"><img src="{IMG['logotipo-1tinta']}" alt="Logotipo manik a una tinta"></div><p class="pie">Una tinta · impresión, bordado, sello</p></div>
  <div><div class="lienzo bruma" style="gap:18px;grid-auto-flow:column"><img src="{IMG['simbolo']}" alt="Símbolo" style="max-height:56px"><img src="{IMG['app-icon']}" alt="Ícono de app" style="max-height:56px"><img src="{IMG['favicon']}" alt="Favicon" style="max-height:32px"></div><p class="pie">Símbolo · ícono de app · favicon</p></div></div>
  <div class="grid2"><div class="card"><h3>Área de respeto y tamaño mínimo</h3><div><span class="respeto"><img src="{IMG['simbolo']}" alt=""></span></div><p>Un cuarto del ancho del símbolo libre por cada lado. Mínimo 24 px en pantalla y 8 mm impreso. Sin degradados en el sello: un solo color para imprimir, bordar y sellar.</p></div>
  <div class="card"><h3>El logotipo</h3><p>«manik» en Sora 600 con espaciado −0.04 em, convertido a trazos. Va en minúsculas porque es un nombre cercano, no una institución.</p></div></div>
  <h3>Así no</h3><div class="mal"><figure><img src="{IMG['logotipo']}" alt="" style="transform:scaleX(1.5)"><span class="x">NO</span>Estirar o deformar</figure><figure><img src="{IMG['logotipo']}" alt="" style="filter:hue-rotate(140deg)"><span class="x">NO</span>Cambiar colores</figure>
  <figure><img src="{IMG['logotipo']}" alt="" style="transform:rotate(-12deg)"><span class="x">NO</span>Girar</figure><figure><span style="font:800 28px Arial,sans-serif;color:var(--tinta)">Manik</span><span class="x">NO</span>Reescribir con otra fuente</figure></div>'''),
S('color', '03 · Color', 'Luz, <b>no color</b>', 'Bruma y blanco dominan; la luz da ambiente; la tinta se lee; el cian de interfaz marca lo que se toca. El cian del pin es de marca: nunca en botones (3.3:1 con blanco). Contrastes calculados con los valores del sistema.',
  f'''{COLOR}<div class="halo">Halos de marca: luz cian arriba a la izquierda, luz cálida a la derecha, sobre bruma. La luz vive en fondos y fotografía, nunca en el sello.</div>
  <ul class="lista"><li><b>Tema claro único</b>, por decisión de marca.</li><li><b>La estrella</b> nunca va sola: el número va escrito en tinta.</li><li><b>Sellos de categoría:</b> rotan cian, cálido y tinta (nunca <code>azul-medicalmanik</code>, que es solo para «de MedicalManik»).</li><li><b>El violeta de Impulsa</b> solo vive dentro de su sello.</li></ul>'''),
S('tipografia', '04 · Tipografía', 'Urbanist para hablar, <b>Onest para decidir</b>', 'Dos familias de Google Fonts. Urbanist ligera y grande dice la idea; la palabra clave va en 600. Onest lleva todo lo demás: el paciente escanea y decide.',
  f'''<div class="card"><span class="ey">Primaria · Urbanist 300 / 600</span><p class="esp-u" style="color:var(--tinta)">Encuentra a tu médico <b>cerca de ti</b>.</p></div>
  <div class="card"><span class="ey">Secundaria · Onest 400–700</span><p class="esp-o" style="color:var(--tinta)">Mira cuánto cuesta antes de ir y agenda sin pagar nada. La consulta es en el consultorio del médico; pagas ahí.</p><p class="tab" style="color:var(--tinta);font-weight:600">Hoy, 16:30 · $900 · 222 555 0140 · Céd. Prof. 10234567</p><p class="pie">Horarios, precios, teléfonos y cédulas con cifras tabulares.</p></div>
  <div class="escala"><div><span>Titular · 300</span><b style="font:300 44px/1 var(--display);letter-spacing:-.035em">Busca por <b style="font-weight:600">lo que sientes</b></b></div><div><span>Nombre · 600</span><b style="font:600 20px var(--display)">Dra. Mariana Soto</b></div>
  <div><span>Precio · 600</span><b style="font:600 22px var(--display)">$900</b></div><div><span>Texto · 17 px</span><span style="font-size:17px;color:var(--tinta)">Dermatóloga · acné y lunares</span></div><div><span>Dato · 13 px</span><span style="font-size:13px;color:var(--muted)">Céd. Prof. 10234567 · Céd. Esp. 11876543</span></div></div>
  <p class="pie">Carga: <code>family=Urbanist:wght@300..700&amp;family=Onest:wght@400..700&amp;display=swap</code>.</p>'''),
S('forma', '05 · Forma y espacio', 'Píldora para <b>lo que se toca</b>', 'Buscador, botones, horarios, chips y atajos van en píldora. Lo demás se separa con borde fino y aire; la sombra solo en el buscador, la ficha al pasar el cursor y las tarjetas flotantes.',
  '<div class="radios">' + ''.join(f'<figure><span style="border-radius:{t["value"]}"></span>{t["name"].replace("radius-", "")} · {t["value"]}</figure>' for t in TOK['radius']['tokens']) + '</div>'
  + '<div class="esp">' + ''.join(f'<div><code>{t["name"]}</code><span><i style="width:{int(t["value"][:-2]) * 3}px"></i></span><small>{t["value"]} · {e(t["usage"])}</small></div>' for t in TOK['spacing']['tokens']) + '</div>'
  + '<p class="pie">Controles de 42 a 60 px; botones de cierre e iconos de 44 px; ancho máximo 1280 px. Cortes: celular &lt; 640 · tableta 640–1023 · escritorio ≥ 1024.</p>'),
S('iconos', '06 · Iconos y sellos', 'Sellos <b>con identidad</b>', 'Lucide, trazo 2, en cian de interfaz. Las categorías de «Busca por lo que sientes» son sellos circulares: doble anillo, pictograma y la categoría escrita en el arco.',
  f'''<div class="ics">{"".join(f"<span>{ico(n, 18)}{t}</span>" for n, t in [("search", "Buscar"), ("map-pin", "Dónde"), ("calendar-check", "Agenda en Manik"), ("phone", "Por teléfono"), ("badge-check", "Verificado"), ("clock", "Horario")])}</div>
  <div class="sellos">{SELLOS}</div><h3>Tres tamaños</h3><p class="intro" style="font-size:16px">Por debajo de 104 px la leyenda del arco quedaría en menos de 8 px: el compacto la quita y agranda el pictograma. El nombre y la especialidad siempre van como texto debajo.</p><div class="escl">{ESCALA}</div>'''),
S('fotografia', '07 · Fotografía', 'Personas <b>reales</b>', 'Retratos 3:4 que sube cada médico, con luz natural y fondo claro. Sin foto, una silueta de médica, médico o neutra sobre el degradado de foto.',
  f'''<div class="fotos">{"".join(f'<figure><div class="face"><img src="{AV[k]}" alt="Silueta {t}"></div>Silueta · {t}</figure>' for k, t in [("mujer", "médica"), ("hombre", "médico"), ("neutro", "neutra")])}
  <div class="marcafoto"><span class="fl"><b>Dra. Mariana Soto</b>Hoy, 16:30 · Agenda en Manik</span>Foto de marca 4:5 · personas cuidándose, México real (pendiente)</div></div>
  <ul class="lista"><li><b>Retratos:</b> mínimo 900 × 1200 px; WebP a 176 × 234 en la ficha de celular (≤ 20 KB) y 480 × 640 en el perfil.</li><li><b>Foto de marca:</b> 4:5 desde tableta; puede llevar tarjetas flotantes de la interfaz, que nunca tapan caras.</li><li><b>Banners de promociones:</b> 16:9 original; en la lista se recorta la franja central 357:104, como en Impulsa.</li></ul>'''),
S('voz', '08 · Voz', 'Clara, de tú, <b>sin tecnicismos</b>', 'Como una persona que conoce buenos médicos y te ayuda a llegar con uno. Fechas en palabras; médicos con título y apellido; errores que dicen qué hacer.',
  f'<div class="tw"><table class="voz"><thead><tr><th>Así sí</th><th>Así no</th></tr></thead><tbody>{VOZ_T}</tbody></table></div>'),
S('componentes', '09 · Componentes', 'Las piezas <b>clave</b>', 'Muestras estáticas de los componentes aprobados. El design system del directorio tiene sus versiones vivas, sus estados y sus reglas.',
  f'''<div class="muestra"><span class="et">Botones</span><div class="btnrow"><span class="btn pri">Agendar</span><span class="btn sec">Llamar</span><span class="btn osc">Buscar</span><span class="btn txt">Ver perfil</span></div><p class="pie">Una sola acción principal por vista. «Buscar» va en tinta y solo en el buscador.</p></div>
  <div class="grid2"><div class="muestra"><span class="et">Ficha del médico (resultados)</span>{FICHA}<p class="pie">Precio, forma de agendar y acción son de cada consultorio. Máximo 2 visibles.</p></div>
  <div class="muestra"><span class="et">Agenda tu cita (perfil)</span>{HORAS}<p class="pie">Tocar una hora lleva directo a «Confirma tu cita». Días sin lugar, apagados y con texto.</p></div></div>
  <div class="muestra"><span class="et">Promoción patrocinada (Impulsa)</span>{PROMO}<div class="impulsa"><img src="{IMPULSA}" alt=""><span><b>Promoción publicada con Impulsa Manik</b>, la herramienta de campañas del ecosistema Manik.</span></div><p class="pie">Nunca en la 1.ª posición; máximo 1 cada 5 resultados. «Patrocinado» siempre primero.</p></div>'''),
S('reglas', '10 · Reglas del producto', 'Decisiones <b>aprobadas</b>', 'Lo que no cambia sin volver a aprobar. Cada regla tiene su ronda en el repositorio (carpeta <code>directorio-ds/</code>).',
  '<div class="reglas">' + ''.join(f'<div class="card regla"><h3>{ico(i, 20)}{t}</h3><ul class="lista">{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for i, t, xs in [
   ('search', 'Inicio', ['Leyenda: «Encuentra a tu médico cerca de ti.»', 'Sin cuenta de paciente: no hay «Entrar».', 'Orden: buscador → lo que sientes → con lugar hoy → resuelve tus dudas → cómo funciona → confianza → ¿eres médico?']),
   ('badge-check', 'Confianza', ['Cédulas con número: «Céd. Prof. · Céd. Esp.».', 'Sin opiniones, ni calificación ni etiqueta.', 'Solo opina quien tuvo cita agendada en Manik.']),
   ('map-pin', 'Consultorios', ['Precio, horarios y forma de agendar son de cada consultorio.', 'Se publica solo con dirección, precio y forma de agendar.', '«Agenda en Manik» (presencial) o «Por teléfono».']),
   ('scan-face', 'Perfil del médico', ['Sección sin datos, no aparece.', 'Barra de secciones solo con 4 o más.', 'Formación desde las cédulas verificadas (título, institución, año).']),
   ('calendar-check', 'Agendar', ['Hora → nombre y celular → Confirmar: 2 toques.', 'Confirmación inmediata; si la hora se ocupa, aviso y horas cercanas.', '«Agendar» de la ficha lleva al perfil, con su consultorio elegido.']),
   ('clock', 'La cita', ['Confirmación y recordatorio por mensaje con enlace; sin cuenta.', 'Cambiar o cancelar hasta 24 h antes; luego, llamar.', 'El enlace vence al terminar el día siguiente a la cita.']),
   ('message-circle-heart', 'Preguntas y artículos', ['Cualquiera pregunta (con correo); solo responden médicos del expediente Manik.', 'La pregunta pasa por un filtro; si no, correo con el motivo.', 'Artículos de médicos con portada y autor.']),
   ('shield-check', 'Promociones (Impulsa)', ['Banner 357:104 en la lista; 16:9 en su página.', '«Patrocinado» primero; «con Impulsa Manik» al final.', 'El precio con promoción llega hasta la cita.'])]) + '</div>'),
S('accesibilidad', '11 · Accesibilidad', 'WCAG 2.2 <b>AA</b>', None,
  '<ul class="lista"><li>Texto 4.5:1 en su fondo; gráficos e iconos 3:1.</li><li>Controles de 42 px o más; nada interactivo por debajo de 24 px.</li><li>Foco visible de 3 px en cian de interfaz.</li><li>Estados con icono y texto, nunca solo color.</li><li>Lo decorativo (leyendas de sellos, banners, foto de marca) se oculta al lector de pantalla; el texto real va aparte.</li><li>Se respeta «reducir movimiento».</li></ul>'),
S('pendientes', '12 · Pendientes', 'Por <b>decidir</b>', None,
  '<ul class="lista"><li>Formato de precio: «$900» o «MXN 900» (en Centroamérica «$» puede ser dólar).</li><li>Canal de mensajes: SMS, WhatsApp o ambos.</li><li>Foto de marca definitiva.</li><li>Aviso de publicidad en salud (COFEPRIS) en promociones: verificar con el área legal.</li><li>Etiqueta común de verificación para Centroamérica («Registro verificado»).</li><li>Página «Conoce Impulsa» para médicos.</li><li>Escala de espacio: confirmar con desarrollo.</li></ul>'),
]

html_out = f'''<title>Manual de marca Manik</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Onest:wght@400..700&display=swap">
<style>{CSS}</style>
<script>document.documentElement.lang='es'</script>
<header class="portada"><div class="wrap"><img class="logo" src="{IMG['logotipo-endoso']}" alt="manik de MedicalManik"><h1>Manual de marca del <b>directorio</b></h1>
<p class="lead">Cómo se ve, cómo habla y cómo funciona Manik, el directorio para pacientes. Reúne el sistema de diseño y todas las decisiones aprobadas al 4 de noviembre de 2026.</p>
<div class="meta"><span>Versión 3 · noviembre 2026</span><span>Celular primero (70 %)</span><span>WCAG 2.2 AA</span><span>Datos de médicos: de ejemplo</span></div></div></header>
<div class="wrap cuerpo"><nav class="indice" aria-label="Secciones del manual"><ul>{NAVH}</ul></nav><main>{"".join(SECCIONES)}</main></div>
<footer class="wrap"><img src="{IMG['logotipo-1tinta']}" alt="manik"><span>de MedicalManik</span><span>Fuente: design system «Directorio Manik» y rondas aprobadas en el repositorio.</span></footer>'''
open(os.path.join(D, 'manual.html'), 'w').write(html_out)
print('ok', len(html_out) // 1024, 'KB')
