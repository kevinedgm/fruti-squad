# NisaLab · manual de marca (sistema y áreas). Uso: python3 gen-guia.py → guia.html
# Fuentes: ../nisalab-final (símbolo y logotipos), ../nisalab-colonia (construcción), ../nisalab-areas-final (áreas).
import json, os, re

H = os.path.dirname(os.path.abspath(__file__))
NS = os.path.join(H, '..')
AZ, PE, W, TINTA, MUTED = '#052A76', '#C2D225', '#FFFFFF', '#141B33', '#535B70'
_n = [0]
def sv(ruta, h=None, color=None, extra=''):
    """SVG en línea con ids únicos por copia."""
    _n[0] += 1; u = f'-{_n[0]}'
    s = open(os.path.join(NS, ruta)).read().strip()
    s = re.sub(r'id="([^"]+)"', lambda m: f'id="{m.group(1)}{u}"', s)
    s = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1)}{u})', s)
    st = (f'height:{h}px;width:auto;' if h else '') + 'display:block;flex:none;max-width:100%' + (f';color:{color}' if color else '') + extra
    return s.replace('<svg ', f'<svg style="{st}" ', 1)
F = lambda n, h=None, **k: sv(f'nisalab-final/svg/{n}.svg', h, **k)
AR = lambda a, n, h=None, **k: sv(f'nisalab-areas-final/svg/{a}/{n}.svg', h, **k)
TEMA = json.load(open(os.path.join(NS, 'nisalab-areas-final', 'tema.json')))['paleta']['areas']

def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]; c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
cr = lambda a, b: round((max(lum(a), lum(b)) + .05) / (min(lum(a), lum(b)) + .05), 1)

areas_tabla = ''.join(
    f'<tr><td><div class="ar">{AR(k, "marca", 44)}<b>{v["nombre"]}</b></div></td><td>{AR(k, "icono", 32)}</td>'
    f'<td><span class="dot" style="background:{v["hex"]}"></span>{v["hex"]}</td><td><code>{v["token"]}</code></td><td>{v["blanco_encima"]}:1</td></tr>'
    for k, v in TEMA.items())
areas_logos = ''.join(f'<div class="c">{AR(k, "logotipo", 40)}</div>' for k in ('aguas', 'agave', 'farmacia'))
iconos = ''.join(f'<figure class="ico">{AR(k, "icono", 64)}<figcaption>{v["nombre"]}</figcaption></figure>' for k, v in TEMA.items())
chips = ''.join(f'<span class="tag">{AR(k, "icono", 20)}{v["nombre"]}</span>' for k, v in TEMA.items())

# usos incorrectos, sobre el símbolo real
_s = open(os.path.join(NS, 'nisalab-final', 'svg', 'simbolo.svg')).read()
def var_s(trans='', swap=None, extra=''):
    s = _s
    if swap: s = swap(s)
    return s.replace('<svg ', f'<svg style="height:80px;width:auto;display:block;{trans}" ', 1).replace('</svg>', extra + '</svg>')
mal = [
    ('Rotar el racimo', var_s('transform:rotate(-35deg)')),
    ('Dos células pera', var_s(swap=lambda s: s.replace('fill="#052A76"/><circle cx="39.82"', f'fill="{PE}"/><circle cx="39.82"'))),
    ('Reacomodar las células', var_s(swap=lambda s: s.replace('cx="80.47" cy="69.88"', 'cx="18" cy="18"'))),
    ('Cambiar el azul', var_s(swap=lambda s: s.replace('#052A76', '#1F8A70'))),
    ('Sombras o degradados', var_s('filter:drop-shadow(6px 8px 4px rgba(0,0,0,.45))')),
    ('Pera como texto', f'<span style="font:700 30px Poppins,sans-serif;color:{PE}">NisaLab</span>'),
]
malh = ''.join(f'<figure class="mal"><div>{s}</div><figcaption>{t}</figcaption></figure>' for t, s in mal)

html = f'''<title>NisaLab · manual de marca</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Manual de un sistema de laboratorio: blanco, tinta, azul real y una sola célula pera. Poppins como en el manual de Nisa Nabani. Tema claro deliberado. */
:root{{--bg:#FFFFFF;--fg:{TINTA};--az:{AZ};--pe:{PE};--muted:{MUTED};--line:#DFE3EC;--sunk:#F2F4F8;color-scheme:light}}
body{{background:var(--bg);color:var(--fg);font:16px/1.65 Poppins,system-ui,sans-serif;margin:0;padding-block:0 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:1080px;margin:0 auto}} h1,h2,h3{{margin:0;text-wrap:balance}} h2{{font:700 28px/1.2 Poppins,sans-serif;letter-spacing:-.01em;margin-bottom:8px}} h3{{font:600 17px/1.3 Poppins,sans-serif;margin:24px 0 8px}}
p{{max-width:68ch;margin:0 0 12px}} .muted{{color:var(--muted)}} .num{{font:700 14px Poppins,sans-serif;color:var(--az);display:block;margin-bottom:4px}}
.hero{{padding:52px clamp(20px,4vw,48px) 44px;margin-top:16px;border-radius:28px;background:var(--sunk);display:grid;gap:18px}} .hero p{{font-size:18px;color:var(--muted);margin:0}}
section{{padding:44px 0;border-bottom:1px solid var(--line)}}
.arq{{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin-top:12px}} .arq div{{border:1px solid var(--line);border-radius:14px;padding:14px 16px}} .arq b{{display:block}}
.g{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}} .c{{border:1px solid var(--line);border-radius:18px;padding:22px;display:grid;place-items:center;gap:10px;min-width:0;min-height:120px}} .c.az{{background:var(--az);border-color:var(--az)}} .cap{{font-size:13px;color:var(--muted);text-align:center}} .c.az .cap{{color:#C9D3EA}}
.anat{{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:28px;align-items:center}} .fig{{background:var(--sunk);border-radius:18px;padding:24px;display:grid;place-items:center}} .fig svg{{width:100%;height:auto;max-width:260px}}
ol,ul{{margin:0;padding-left:22px;display:grid;gap:8px}}
.sw{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}} .sw div{{border-radius:16px;padding:16px;min-height:130px;display:grid;align-content:end;gap:2px;font-size:14px;line-height:1.4;border:1px solid var(--line)}} .sw b{{font:700 16px Poppins,sans-serif}}
.bar{{display:flex;height:22px;border-radius:999px;overflow:hidden;margin:14px 0 6px;border:1px solid var(--line)}} .bar i{{display:block}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:15px}} th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:middle}} th{{font-weight:600;background:var(--sunk);font-size:14px}}
.ar{{display:flex;align-items:center;gap:12px}} .dot{{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:8px;vertical-align:-2px}} code{{font:13px "IBM Plex Mono",monospace;background:var(--sunk);padding:2px 6px;border-radius:6px}}
.type{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}} .spec{{border:1px solid var(--line);border-radius:16px;padding:20px}} .spec .big{{font-size:40px;line-height:1.15;margin:6px 0}}
.ov{{font:600 12px/1.4 Poppins,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.two{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}} .si,.nosi{{border-radius:14px;padding:16px 18px;font-size:15px}} .si{{background:#EEF4D6}} .nosi{{background:#FBEDEE}} .si b,.nosi b{{display:block;margin-bottom:6px}}
.icos{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(110px,1fr))}} figure{{margin:0}} .ico{{display:grid;justify-items:center;gap:6px;font-size:13px;color:var(--muted);text-align:center}}
.tags{{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}} .tag{{display:inline-flex;align-items:center;gap:6px;background:var(--sunk);border-radius:999px;padding:4px 12px 4px 4px;font-size:14px;font-weight:500}}
.ui{{display:flex;align-items:center;gap:12px;height:60px;padding:0 16px;border:1px solid var(--line);border-radius:14px;background:#fff}} .ui .nm{{font-size:17px;color:var(--muted)}} .ui .nm b{{color:var(--fg);font-weight:600}} .sp{{flex:1}} .srch{{border:1px solid #858DA3;border-radius:10px;padding:6px 12px;font-size:13px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:45%}}
.login{{border:1px solid var(--line);border-radius:22px;padding:24px;display:grid;gap:12px;max-width:320px;background:#fff;box-shadow:0 10px 30px rgba(20,27,51,.08)}} .login .f{{height:42px;border:1px solid #858DA3;border-radius:10px;padding:0 12px;display:flex;align-items:center;color:var(--muted);font-size:14px}} .login .b{{height:44px;border-radius:10px;background:var(--az);color:#fff;display:grid;place-items:center;font-weight:600}}
.mal{{border:1px solid var(--line);border-radius:14px;padding:16px;display:grid;gap:10px;justify-items:center;overflow:hidden}} .mal div{{height:90px;display:grid;place-items:center}} .mal figcaption{{font-size:14px;font-weight:600}} .mal figcaption::before{{content:"✕ ";color:#B42318}}
.files li{{margin:2px 0}} .pend li{{margin:4px 0}}
@media (max-width:700px){{.anat{{grid-template-columns:1fr}} .ui .srch{{display:none}}}}
</style>
<main>
<header class="hero"><span class="ov">Manual de marca · v1 · sistema de laboratorio de Nisa Nabani</span>{F('logotipo-respaldo', 96, extra=';max-width:100%')}
<p>NisaLab es donde el laboratorio recibe muestras, captura resultados, los revisa y emite certificados. Su símbolo, Colonia, es lo vivo que el laboratorio detecta, cuenta y certifica.</p></header>

<section><span class="num">01</span><h2>Arquitectura y nombre</h2>
<div class="arq"><div><b>Nisa Nabani</b><span class="muted">La empresa. Conserva su logo y su manual.</span></div><div><b>NisaLab</b><span class="muted">El sistema de laboratorio. Este manual.</span></div><div><b>«Área NisaLab»</b><span class="muted">Cada división dentro del sistema: Aguas NisaLab, Farmacia NisaLab…</span></div></div>
<h3>Cómo se escribe</h3>
<p>«NisaLab», junto y con dos mayúsculas. Nunca «Nisa Lab», «NISALAB» ni «Nisalab». Las áreas, con el nombre del área delante: «Aguas NisaLab». La empresa se escribe «Nisa Nabani» y, cuando acompaña, va como respaldo: «de Nisa Nabani».</p></section>

<section><span class="num">02</span><h2>Símbolo: Colonia</h2>
<div class="anat"><div class="fig">{sv('nisalab-colonia/svg/construccion.svg')}</div><div><ol>
<li><b>Cuatro células</b> que casi se tocan, siempre con la misma separación entre ellas.</li>
<li><b>Proporción fija.</b> Los números son el tamaño de cada célula frente a la más chica: 1.0, 1.7, 2.9 y 3.7.</li>
<li><b>Una sola célula pera</b>, arriba a la derecha: la que creció. En las áreas, esa célula toma el color y el ícono del área.</li>
<li><b>El racimo es fijo:</b> no se rota, no se reacomoda, no se le quitan ni agregan células.</li></ol></div></div>
<h3>Versiones</h3>
<div class="g"><div class="c">{F('simbolo', 96)}<span class="cap">Color. La versión principal.</span></div><div class="c az">{F('simbolo-blanco', 96)}<span class="cap">Blanco y pera, sobre azul real.</span></div><div class="c">{F('simbolo-1tinta', 96, color=TINTA)}<span class="cap">Una tinta: sellos, grabados, documentos en blanco y negro.</span></div></div>
<h3>Tamaño mínimo y área de respeto</h3>
<p>Alrededor del símbolo y del logotipo se deja libre, como mínimo, el ancho de la célula grande. Tamaño mínimo: <b>16 px</b> en pantalla y <b>6 mm</b> impreso.</p></section>

<section><span class="num">03</span><h2>Logotipo</h2>
<div class="g"><div class="c">{F('logotipo', 52)}<span class="cap">Horizontal. Para casi todo.</span></div><div class="c">{F('logotipo-respaldo', 64)}<span class="cap">Con respaldo. Documentos para clientes, certificados, presentaciones.</span></div>
<div class="c">{F('logotipo-vertical', 120)}<span class="cap">Vertical. Pantalla de acceso, espacios cuadrados.</span></div>
<div class="c az">{F('logotipo-blanco', 52)}<span class="cap">Blanco, sobre azul real.</span></div><div class="c">{F('logotipo-1tinta', 52, color=TINTA)}<span class="cap">Una tinta.</span></div></div>
<p class="muted" style="margin-top:14px">«Nisa» en Poppins 700 y «Lab» en Poppins 400: la empresa y lo que hace. Los archivos traen el texto convertido a trazos; nunca se reescribe con la fuente.</p></section>

<section><span class="num">04</span><h2>Color</h2>
<div class="sw"><div style="background:var(--az);color:#fff;border-color:var(--az)"><b>Azul real</b>{AZ}<br>Símbolo, logotipo, acción principal. Blanco encima {cr(W, AZ)}:1.</div>
<div style="background:var(--pe);border-color:var(--pe)"><b>Pera</b>{PE}<br>Una sola célula del símbolo. Nunca texto ({cr(PE, W)}:1 sobre blanco).</div>
<div style="background:var(--fg);color:#fff;border-color:var(--fg)"><b>Tinta</b>{TINTA}<br>Texto y versión a una tinta.</div>
<div style="background:#fff"><b>Blanco</b>#FFFFFF<br>Superficies y texto sobre azul.</div></div>
<div class="bar" aria-hidden="true"><i style="width:62%;background:#fff"></i><i style="width:18%;background:var(--fg)"></i><i style="width:14%;background:var(--az)"></i><i style="width:4%;background:#007CA3"></i><i style="width:2%;background:var(--pe)"></i></div>
<p class="muted" style="font-size:14px">Proporción en una pantalla típica: blanco domina; tinta para leer; azul para lo que se toca; el color del área y el pera son detalles.</p>
<p>Azul real y pera son los colores de Nisa Nabani: son el lazo con la empresa. Los colores de las áreas viven aparte (sección 06) y nunca indican estado.</p></section>

<section><span class="num">05</span><h2>Tipografía</h2>
<div class="type"><div class="spec"><span class="ov">Primaria · Poppins</span><div class="big" style="font-weight:700">Resultados del lote</div><p class="muted">La letra del manual de Nisa Nabani: títulos (700 y 600) y todo el texto de interfaz (400 y 500).</p></div>
<div class="spec"><span class="ov">Datos · IBM Plex Mono</span><div class="big" style="font-family:'IBM Plex Mono',monospace;font-weight:500;font-feature-settings:'zero'">0.0124 mg/L</div><p class="muted">Valores, límites, folios y fechas: cifras de ancho fijo y cero con barra para no confundir 0 con O.</p></div></div></section>

<section><span class="num">06</span><h2>Áreas</h2>
<p>Cada división de Nisa Nabani tiene su identidad dentro de NisaLab. La célula que creció toma el color y el ícono del área; el resto del racimo sigue azul. Los ocho colores comparten luminosidad e intensidad (OKLCH 0.54 · 0.12): solo cambia el tono, para que ninguno pese más que otro y ninguno se acerque al pera.</p>
<div class="tw"><table><thead><tr><th>Área</th><th>Ícono</th><th>Color</th><th>Token</th><th>Blanco encima</th></tr></thead><tbody>{areas_tabla}</tbody></table></div>
<h3>Logotipo de área</h3><div class="g">{areas_logos}</div>
<p class="muted" style="margin-top:12px">El área en Poppins 600 y «NisaLab» en 400, en gris. Así se lee primero dónde estás.</p>
<h3>Reglas</h3><ul><li>El color del área solo dice de qué área es; nunca indica estado (conforme, alerta, fuera de especificación).</li><li>El nombre del área acompaña siempre a la marca o al ícono: a 24 px lo que se lee es el color.</li><li>El ícono va en blanco sobre el color del área, o calado en la versión a una tinta.</li></ul></section>

<section><span class="num">07</span><h2>Íconos de área</h2>
<p>Dibujados en una retícula de 40, con las formas redondas de Colonia, en blanco y con el mismo grosor.</p>
<div class="icos">{iconos}</div><h3>En la interfaz</h3><div class="tags">{chips}</div></section>

<section><span class="num">08</span><h2>Voz</h2>
<p>Precisa, breve, sin adornos. Los botones dicen la acción y el objeto; los errores dicen qué pasó y cómo corregirlo. Los términos del laboratorio no se traducen: LD, LC, lote, alícuota, especificación, método.</p>
<div class="two"><div class="si"><b>Así sí</b><ul><li>«Registrar muestra»</li><li>«Liberar lote»</li><li>«El resultado está fuera del intervalo del método (0.005–10 mg/L). Revisa la dilución.»</li></ul></div>
<div class="nosi"><b>Así no</b><ul><li>«Procesar»</li><li>«Ocurrió un error»</li><li>«¡Listo! Tu muestra fue registrada exitosamente en el sistema»</li></ul></div></div></section>

<section><span class="num">09</span><h2>Aplicaciones</h2>
<div class="g"><div class="c">{F('app-icon', 120, extra=';border-radius:26px')}<span class="cap">Ícono de app: símbolo blanco y pera sobre azul real.</span></div>
<div class="c"><div style="display:flex;gap:14px;align-items:flex-end">{F('favicon', 32)}{F('favicon', 24)}{F('favicon', 16)}</div><span class="cap">Favicon a 32, 24 y 16 px.</span></div>
<div class="c"><div class="login">{F('logotipo-respaldo', 46, extra=';max-width:100%')}<div class="f">Correo</div><div class="f">Contraseña</div><div class="b">Entrar</div></div><span class="cap">Inicio de sesión.</span></div></div>
<h3>Barra superior de un área</h3><div class="ui">{AR('aguas', 'marca', 34)}<span class="nm"><b>Aguas</b> NisaLab</span><span class="sp"></span><span class="srch">Buscar muestra, lote o cliente</span></div></section>

<section><span class="num">10</span><h2>Usos incorrectos</h2><div class="g">{malh}</div>
<p class="muted" style="margin-top:12px">Tampoco: usar el color de un área como estado, poner el símbolo sobre fotografías sin contraste, o unir el logo de Nisa Nabani y el de NisaLab en una sola pieza.</p></section>

<section><span class="num">11</span><h2>Archivos y pendientes</h2>
<ul class="files"><li><code>nisalab-final/</code>: símbolo, logotipos, ícono de app, favicon, PNG, <code>tema.json</code> y LEEME.</li>
<li><code>nisalab-areas-final/</code>: marca, ícono y logotipo de las ocho áreas, PNG, <code>tema.json</code> con la paleta y LEEME.</li>
<li><code>nisalab-colonia/</code>: construcción del símbolo.</li></ul>
<h3>Pendiente</h3><ul class="pend"><li>Registro de marca de «NisaLab» en el IMPI y disponibilidad del dominio.</li><li>Confirmar si «Bebidas alcohólicas» sustituye a «Bebidas de agave», es un área nueva o queda como en el manual.</li><li>Actualizar el design system de Nabi a NisaLab: nombre, símbolo, portada y colores de área.</li></ul></section>
</main>'''
open(os.path.join(H, 'guia.html'), 'w').write(html)
print('ok')
