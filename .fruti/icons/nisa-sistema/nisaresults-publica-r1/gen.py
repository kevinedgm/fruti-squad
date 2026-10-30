# NisaResults · página pública del cliente (QR), prototipo r1. Datos y límites de ejemplo, no verificados contra la norma.
# Estructura: negocio → resumen → tipo de agua/muestra (con descripción) → parámetros por tipo (Mb, Fq, Me…) → historial bajo demanda.
# Uso: python3 gen.py → publica.html (para publicar como Artifact)
import json, os, re
H = os.path.dirname(os.path.abspath(__file__)); NS = os.path.join(H, '..')
sello = re.sub(r'<title>.*?</title>|\s(role|aria-label)="[^"]*"', '', open(os.path.join(NS, 'nisaresults-final', 'svg', 'sello.svg')).read().strip())
sello = sello.replace('<svg ', '<svg width="36" height="36" aria-hidden="true" focusable="false" ', 1)
TIPO = {'Mb': ('Microbiológicos', 'Buscan bacterias que indicarían contaminación.'), 'Fq': ('Fisicoquímicos', 'Miden cómo es el agua: acidez, claridad, desinfección.'),
        'Me': ('Metales', 'Miden metales que no deben pasar de cierta cantidad.')}
TIPO_A = {'Mb': ('Microbiológicos', 'Buscan bacterias que indicarían falta de higiene o contaminación.')}
def P(id, nombre, desc, val, unidad, lim, ok, hist, lo=None, hi=None, fecha='28 oct 2026'):
    return dict(id=id, nombre=nombre, desc=desc, val=val, unidad=unidad, lim=lim, ok=ok, hist=hist, lo=lo, hi=hi, fecha=fecha)
AREAS = {
 'agua': dict(nombre='Agua', resumen='Calidad del agua', tipos=[
   dict(nombre='Agua para uso y consumo humano', desc='Agua que se bebe o se usa para preparar alimentos y para el aseo personal. Debe cumplir límites estrictos porque entra al cuerpo.',
        donde='Habitaciones · Cocina · Bebederos', norma='NOM-127-SSA1-2021 (por confirmar)', fecha='28 oct 2026', grupos=[
     ('Mb', [P('ct', 'Coliformes totales', 'Bacterias que indican si el agua tuvo contacto con suciedad. Lo ideal es que no se detecten.', '<1.1', 'NMP/100 mL', 'No detectable', True, [0, 0, 0, 0, 0, 0]),
             P('ec', 'E. coli', 'Bacteria de origen fecal. Su presencia indicaría contaminación; no debe detectarse.', 'No detectable', '', 'No detectable', True, [0, 0, 0, 0, 0, 0])]),
     ('Fq', [P('ph', 'pH', 'Qué tan ácida o alcalina es el agua. Un pH equilibrado es agradable y no daña la piel ni las tuberías.', '7.3', '', '6.5 a 8.5', True, [6.9, 7.1, 7.4, 7.2, 7.0, 7.3], 6.5, 8.5),
             P('tu', 'Turbiedad', 'Qué tan clara es el agua. Mientras más baja, más transparente.', '0.6', 'UTN', 'Hasta 4', True, [0.8, 0.5, 0.7, 0.6, 0.9, 0.6], 0, 4),
             P('cl', 'Cloro residual libre', 'El desinfectante que queda en el agua para protegerla en el camino hasta la llave.', '0.8', 'mg/L', '0.2 a 1.5', True, [0.6, 0.9, 1.1, 0.7, 0.8, 0.8], 0.2, 1.5)]),
     ('Me', [P('pb', 'Plomo', 'Metal que puede venir de tuberías antiguas. Debe estar por debajo del límite.', '0.004', 'mg/L', 'Hasta 0.01', True, [0.003, 0.005, 0.004, 0.004, 0.003, 0.004], 0, 0.01),
             P('as', 'Arsénico', 'Metal de origen natural en algunos pozos. Debe estar por debajo del límite.', '0.006', 'mg/L', 'Hasta 0.025', True, [0.005, 0.006, 0.007, 0.006, 0.005, 0.006], 0, 0.025)])]),
   dict(nombre='Agua para uso recreativo', desc='Agua de albercas y chapoteaderos. No se bebe, pero está en contacto con la piel, los ojos y la boca, por eso se vigila su desinfección.',
        donde='Alberca principal · Chapoteadero', norma='Norma sanitaria de albercas (por confirmar)', fecha='27 oct 2026', grupos=[
     ('Mb', [P('ctr', 'Coliformes totales', 'Bacterias que indican si el agua tuvo contacto con suciedad.', '<1.1', 'NMP/100 mL', 'No detectable', True, [0, 0, 0, 0, 0, 0])]),
     ('Fq', [P('phr', 'pH', 'Qué tan ácida o alcalina es el agua. Fuera de rango puede irritar ojos y piel.', '7.4', '', '7.2 a 7.8', True, [7.3, 7.5, 7.6, 7.4, 7.3, 7.4], 7.2, 7.8),
             P('clr', 'Cloro residual libre', 'El desinfectante del agua de la alberca. Muy poco no protege; demasiado irrita.', '3.4', 'mg/L', '1.0 a 3.0', False, [2.1, 2.4, 2.2, 2.8, 2.6, 3.4], 1.0, 3.0, '27 oct 2026')])])]),
 'alimentos': dict(nombre='Alimentos', resumen='Higiene en alimentos', tipos=[
   dict(nombre='Superficies en contacto con alimentos', desc='Mesas, tablas de corte y utensilios de la cocina. Se toma una muestra frotando la superficie (frotis) para ver si quedó bien limpia.',
        donde='Cocina principal · Barra de desayunos', norma='Norma de prácticas de higiene (por confirmar)', fecha='25 oct 2026', grupos=[
     ('Mb', [P('mes', 'Mesófilos aerobios', 'Cuenta general de bacterias en la superficie: dice qué tan bien se limpió.', '120', 'UFC/cm²', 'Hasta 400', True, [180, 150, 210, 130, 160, 120], 0, 400),
             P('cts', 'Coliformes totales', 'Bacterias que indican falta de higiene en la superficie.', '<10', 'UFC/cm²', 'Hasta 200', True, [10, 10, 10, 10, 10, 10], 0, 200)])]),
   dict(nombre='Alimentos preparados', desc='Platillos listos para servir. Se analizan para confirmar que se prepararon y conservaron con higiene.',
        donde='Restaurante · Buffet', norma='NOM-251-SSA1-2009 y criterios aplicables (por confirmar)', fecha='25 oct 2026', grupos=[
     ('Mb', [P('sal', 'Salmonella', 'Bacteria que causa infecciones intestinales. No debe estar presente.', 'Ausente', 'en 25 g', 'Ausente', True, [0, 0, 0, 0, 0, 0]),
             P('eca', 'E. coli', 'Bacteria que indica contaminación fecal en el alimento.', '<10', 'UFC/g', 'Hasta 10', True, [10, 10, 10, 10, 10, 10])])])]),
}
FECHAS = ['may', 'jun', 'jul', 'ago', 'sep', 'oct']
HIST = {}
def chip(ok): return (f'<span class="st ok"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M4.8 8.2 7 10.4 11.2 5.9" fill="none" stroke="#fff" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>Óptimo</span>' if ok else
                      '<span class="st no"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M8 4.2v5M8 11.6v.2" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>No óptimo</span>')
def area_html(k, a):
    total = sum(len(ps) for t in a['tipos'] for _, ps in t['grupos']); oks = sum(p['ok'] for t in a['tipos'] for _, ps in t['grupos'] for p in ps)
    tipos = ''
    for i, t in enumerate(a['tipos']):
        tt = sum(len(ps) for _, ps in t['grupos']); to = sum(p['ok'] for _, ps in t['grupos'] for p in ps)
        grupos = ''
        for g, ps in t['grupos']:
            nom, gd = (TIPO_A if k == 'alimentos' else TIPO)[g]
            filas = ''
            for p in ps:
                HIST[p['id']] = dict(nombre=p['nombre'], unidad=p['unidad'], lim=p['lim'], lo=p['lo'], hi=p['hi'], hist=p['hist'], val=p['val'], ok=p['ok'], numerico=p['lo'] is not None)
                vu = f'{p["val"]} <small>{p["unidad"]}</small>' if p['unidad'] else p['val']
                filas += (f'<li class="pr{"" if p["ok"] else " bad"}"><div class="ph"><h5>{p["nombre"]}</h5>{chip(p["ok"])}</div><p class="pd">{p["desc"]}</p>'
                          f'<dl><div><dt>Resultado</dt><dd class="v">{vu}</dd></div><div><dt>Límite</dt><dd>{p["lim"]}</dd></div><div><dt>Último análisis</dt><dd>{t["fecha"]}</dd></div></dl>'
                          f'<button class="hb" data-p="{p["id"]}">Ver historial</button></li>')
            grupos += f'<div class="gr"><div class="gh"><span class="fi" aria-hidden="true">{g}</span><div><h4>{nom}</h4><p>{gd}</p></div></div><ul class="pl">{filas}</ul></div>'
        tipos += (f'<section class="tp" aria-labelledby="t-{k}-{i}"><header class="th"><h3 id="t-{k}-{i}">{t["nombre"]}</h3><p>{t["desc"]}</p>'
                  f'<ul class="meta"><li><b>Dónde</b>{t["donde"]}</li><li><b>Última muestra</b>{t["fecha"]}</li><li><b>Se compara con</b>{t["norma"]}</li></ul>'
                  f'<p class="cnt">{chip(to == tt)}<span>{to} de {tt} parámetros dentro del límite</span></p></header>{grupos}</section>')
    return (f'<div class="area" id="area-{k}" role="tabpanel" aria-labelledby="tab-{k}"{"" if k == "agua" else " hidden"}>'
            f'<div class="sum"><div><span class="ov">{a["resumen"]}</span><p class="big"><b>{oks} de {total}</b> parámetros dentro del límite</p><p class="mut">Último análisis: {a["tipos"][0]["fecha"]}</p></div>'
            f'<div class="bar" role="img" aria-label="{oks} de {total} óptimos">{"".join(f"<i class=" + chr(34) + ("bo" if j < oks else "bx") + chr(34) + "></i>" for j in range(total))}</div></div>{tipos}</div>')
areas = ''.join(area_html(k, a) for k, a in AREAS.items())
tabs = ''.join(f'<button role="tab" id="tab-{k}" aria-controls="area-{k}" aria-selected="{"true" if k == "agua" else "false"}" tabindex="{0 if k == "agua" else -1}">{a["nombre"]}</button>' for k, a in AREAS.items())
logo = ('<svg viewBox="0 0 64 64" width="64" height="64" aria-hidden="true"><rect width="64" height="64" rx="16" fill="#0F5E4E"/>'
        '<path d="M32 48V26" stroke="#F4E3B5" stroke-width="3.5" stroke-linecap="round"/><path d="M32 27c-6-7-14-7-18-3 6-1 11 1 18 3zm0 0c6-7 14-7 18-3-6-1-11 1-18 3zm0 0c-3-8-1-14 4-17-2 5-3 10-4 17z" fill="#F4E3B5"/>'
        '<path d="M14 50c6-3 12-3 18 0s12 3 18 0" fill="none" stroke="#7FD1C3" stroke-width="3" stroke-linecap="round"/></svg>')
html = f'''<title>Hotel Las Palmas · Calidad</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Página pública de NisaResults (QR): una columna pensada para teléfono; el negocio arriba, el laboratorio firma abajo. Tema claro deliberado. */
:root{{--bg:#F3F5F9;--sf:#FFFFFF;--tx:#141B33;--mu:#535B70;--ln:#DFE3EC;--az:#052A76;--ci:#00B4D8;--ok:#1E6B34;--ok-s:#E3F1E4;--no:#A11D1D;--no-s:#FCE4E4;
--sans:Poppins,system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:light}}
[hidden]{{display:none!important}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font:15px/1.55 var(--sans);padding-block:0 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
main{{max-width:760px;margin:0 auto;display:grid;gap:16px}}h1,h2,h3,h4,h5{{margin:0;text-wrap:balance}}p{{margin:0}}
.neg{{display:grid;grid-template-columns:auto 1fr;gap:16px;align-items:center;padding:24px 0 4px}}.neg h1{{font:700 26px/1.2 var(--sans)}}.neg p{{color:var(--mu);font-size:14px}}.neg .ub{{font-size:13px;margin-top:2px}}
.tabs{{display:flex;gap:6px;background:var(--sf);border:1px solid var(--ln);border-radius:12px;padding:4px;position:sticky;top:env(safe-area-inset-top,0px);z-index:5}}
.tabs button{{flex:1;font:600 15px var(--sans);color:var(--mu);background:none;border:0;border-radius:9px;padding:10px;min-height:44px;cursor:pointer}}.tabs button[aria-selected="true"]{{background:var(--az);color:#fff}}
button:focus-visible{{outline:3px solid var(--ci);outline-offset:2px}}
.area{{display:grid;gap:16px}}.sum{{background:var(--sf);border:1px solid var(--ln);border-radius:16px;padding:20px;display:grid;gap:14px}}
.ov{{font:600 12px/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--mu)}}.big{{font-size:20px;margin-top:6px}}.big b{{font-size:28px}}.mut{{color:var(--mu);font-size:13px}}
.bar{{display:flex;gap:3px}}.bar i{{flex:1;height:10px;border-radius:3px}}.bar i.bo{{background:#3E9B57}}.bar i.bx{{background:#C2412D}}
.tp{{background:var(--sf);border:1px solid var(--ln);border-radius:16px;overflow:hidden}}.th{{padding:20px;display:grid;gap:10px;border-bottom:1px solid var(--ln)}}.th h3{{font:600 20px/1.3 var(--sans)}}.th>p{{color:var(--mu);font-size:14px}}
.meta{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px 16px;font-size:13px}}.meta b{{display:block;font-weight:500;color:var(--mu);font-size:12px}}
.cnt{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font-size:14px}}
.gr{{padding:16px 20px 4px}}.gh{{display:flex;gap:12px;align-items:flex-start}}.gh h4{{font:600 16px var(--sans)}}.gh p{{color:var(--mu);font-size:13px}}
.fi{{width:30px;height:30px;border-radius:7px;background:var(--az);color:#fff;font:600 14px/30px var(--sans);text-align:center;flex:none;letter-spacing:-.02em}}
.pl{{list-style:none;margin:12px 0 0;padding:0;display:grid}}.pr{{border-top:1px solid var(--ln);padding:14px 0 16px;display:grid;gap:8px}}
.ph{{display:flex;justify-content:space-between;gap:12px;align-items:flex-start}}.ph h5{{font:600 15px var(--sans)}}.pd{{font-size:14px;color:var(--mu)}}
dl{{margin:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}}dl div{{min-width:0}}dt{{font-size:12px;color:var(--mu)}}dd{{margin:0;font:500 14px var(--mono);overflow-wrap:anywhere}}dd small{{font-size:12px;color:var(--mu)}}.pr.bad .v{{color:var(--no);font-weight:600}}
.st{{display:inline-flex;align-items:center;gap:6px;font:600 13px/18px var(--sans);border-radius:999px;padding:3px 10px 3px 6px;white-space:nowrap}}.st svg{{width:15px;height:15px}}.st.ok{{background:var(--ok-s);color:var(--ok)}}.st.no{{background:var(--no-s);color:var(--no)}}
.hb{{justify-self:start;font:600 14px var(--sans);color:var(--az);background:none;border:1px solid var(--ln);border-radius:9px;padding:8px 14px;min-height:40px;cursor:pointer}}.hb:hover{{background:#EEF1F6}}
.nota{{font-size:13px;color:var(--mu);background:var(--sf);border:1px solid var(--ln);border-radius:16px;padding:16px 20px;display:grid;gap:6px}}
.firma{{display:flex;align-items:center;gap:12px;padding:8px 4px;font-size:14px;color:var(--mu)}}.firma b{{color:var(--az)}}
dialog{{border:0;border-radius:18px;padding:0;width:min(640px,calc(100% - 24px));max-height:calc(100% - 48px);color:var(--tx);background:var(--sf)}}dialog::backdrop{{background:rgba(20,27,51,.45)}}
.dh{{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;padding:18px 20px;border-bottom:1px solid var(--ln)}}.dh h2{{font:600 18px var(--sans)}}.dh p{{font-size:13px;color:var(--mu)}}
.x{{font:600 14px var(--sans);background:#EEF1F6;border:0;border-radius:9px;min-height:40px;padding:0 14px;cursor:pointer}}.db{{padding:16px 20px 20px;display:grid;gap:14px}}
.ley{{display:flex;gap:12px;flex-wrap:wrap;font-size:12px;color:var(--mu)}}.ley span{{display:inline-flex;align-items:center;gap:6px}}.ley i{{width:12px;height:12px;border-radius:3px;display:inline-block}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th{{text-align:left;font-weight:500;color:var(--mu);font-size:12px;padding:6px 8px;border-bottom:1px solid var(--ln)}}td{{padding:8px;border-bottom:1px solid var(--ln);font-family:var(--mono)}}
@media (max-width:520px){{.neg{{grid-template-columns:1fr}}dl{{grid-template-columns:1fr 1fr}}dl div:last-child{{grid-column:1/-1}}}}
@media (prefers-reduced-motion:no-preference){{dialog[open]{{animation:up .18s ease-out}}@keyframes up{{from{{transform:translateY(12px);opacity:.6}}}}}}
</style>
<main>
<header class="neg">{logo}<div><h1>Hotel Las Palmas</h1><p>Hotel frente al mar con 120 habitaciones, alberca y restaurante. Publicamos los análisis de laboratorio de nuestra agua y nuestra cocina.</p><p class="mut ub">Mazatlán, Sinaloa · logo y datos de ejemplo</p></div></header>
<div class="tabs" role="tablist" aria-label="Qué se analiza">{tabs}</div>
{areas}
<aside class="nota"><b>Qué significa «Óptimo»</b><p>El resultado está dentro de los límites permisibles de la norma con la que se compara. «No óptimo» quiere decir que ese análisis quedó fuera del límite. Este resumen no sustituye al informe de laboratorio, que el negocio puede mostrarte si lo pides.</p></aside>
<footer class="firma">{sello}<span>Analizada por <b>Nisa Nabani</b> · laboratorio de análisis</span></footer>
</main>
<dialog id="hist" aria-labelledby="h-t"><div class="dh"><div><h2 id="h-t"></h2><p id="h-s"></p></div><button class="x" id="h-x">Cerrar</button></div><div class="db"><div id="h-g"></div><div class="ley" id="h-l"></div><table><thead><tr><th>Mes</th><th>Resultado</th><th>Estado</th></tr></thead><tbody id="h-b"></tbody></table></div></dialog>
<script>
const H={json.dumps(HIST, ensure_ascii=False)}, M={json.dumps(FECHAS)};
const tabs=[...document.querySelectorAll('[role=tab]')];
function sel(t){{tabs.forEach(b=>{{const on=b===t;b.setAttribute('aria-selected',on);b.tabIndex=on?0:-1;document.getElementById(b.getAttribute('aria-controls')).hidden=!on;}});}}
tabs.forEach((t,i)=>{{t.addEventListener('click',()=>sel(t));t.addEventListener('keydown',e=>{{if(e.key==='ArrowRight'||e.key==='ArrowLeft'){{const n=tabs[(i+(e.key==='ArrowRight'?1:tabs.length-1))%tabs.length];sel(n);n.focus();}}}});}});
const dlg=document.getElementById('hist');let origen=null;
function graf(p){{const W=420,Hh=210,L=44,R=14,T=14,B=30,vals=p.hist;const pad=(p.hi-p.lo)*.35||1;const lo=Math.max(0,p.lo-pad),hi=p.hi+pad;
 const y=v=>T+(hi-v)*(Hh-T-B)/(hi-lo),x=i=>L+i*(W-L-R)/(vals.length-1);
 let s=`<rect x="${{L}}" y="${{T}}" width="${{W-L-R}}" height="${{Hh-T-B}}" fill="#FCE4E4"/><rect x="${{L}}" y="${{y(p.hi)}}" width="${{W-L-R}}" height="${{y(p.lo)-y(p.hi)}}" fill="#E3F1E4"/>`;
 [p.lo,p.hi].forEach(v=>s+=`<text x="${{L-6}}" y="${{y(v)+4}}" text-anchor="end" font-size="14" fill="#535B70" font-family="IBM Plex Mono,monospace">${{v}}</text>`);
 M.forEach((m,i)=>s+=`<text x="${{x(i)}}" y="${{Hh-8}}" text-anchor="middle" font-size="14" fill="#535B70">${{m}}</text>`);
 s+=`<path d="M${{vals.map((v,i)=>x(i)+' '+y(v)).join(' L')}}" fill="none" stroke="#052A76" stroke-width="2.5"/>`;
 vals.forEach((v,i)=>{{const fuera=v<p.lo||v>p.hi;s+=`<circle cx="${{x(i)}}" cy="${{y(v)}}" r="6" fill="${{fuera?'#A11D1D':(i===vals.length-1?'#00B4D8':'#052A76')}}" stroke="#fff" stroke-width="1.5"/>`;}});
 return `<svg viewBox="0 0 ${{W}} ${{Hh}}" style="width:100%;height:auto;display:block" role="img" aria-label="${{p.nombre}} en los últimos seis meses">${{s}}</svg>`;}}
document.querySelectorAll('.hb').forEach(b=>b.addEventListener('click',()=>{{const p=H[b.dataset.p];origen=b;
 document.getElementById('h-t').textContent=p.nombre;document.getElementById('h-s').textContent='Últimos seis meses · límite: '+p.lim;
 document.getElementById('h-g').innerHTML=p.numerico?graf(p):'<p class="mut">En todos los análisis el resultado fue el mismo: '+p.lim.toLowerCase()+'.</p>';
 document.getElementById('h-l').innerHTML=p.numerico?'<span><i style="background:#E3F1E4"></i>Dentro del límite</span><span><i style="background:#FCE4E4"></i>Fuera del límite</span><span><i style="background:#00B4D8;border-radius:50%"></i>Último análisis</span>':'';
 document.getElementById('h-b').innerHTML=p.hist.map((v,i)=>{{const fuera=p.numerico&&(v<p.lo||v>p.hi);const val=p.numerico?v+(p.unidad?' '+p.unidad:''):(i===p.hist.length-1?p.val:p.lim);return `<tr><td>${{M[i]}} 2026</td><td>${{val}}</td><td>${{fuera?'No óptimo':'Óptimo'}}</td></tr>`;}}).reverse().join('');
 dlg.showModal();}}));
document.getElementById('h-x').addEventListener('click',()=>dlg.close());dlg.addEventListener('close',()=>origen&&origen.focus());
dlg.addEventListener('click',e=>{{if(e.target===dlg)dlg.close();}});
</script>'''
open(os.path.join(H, 'publica.html'), 'w').write(html); print('ok', len(HIST))
