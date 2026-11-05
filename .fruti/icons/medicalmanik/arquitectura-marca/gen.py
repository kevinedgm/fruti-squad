# MedicalManik · arquitectura de marca explicada (por qué se renombraron los productos).
# Pedido (2026-11-05): «un artifact aparte, documentado, explicando toda la lógica y concepto detrás de MedicalManik:
# por qué renombramos los productos para diferenciar la marca de sus productos».
# Fuentes: ../ronda-1-nombres … ../ronda-5-seis, ../final/ (tema.json, LEEME), ../manik-final/, ../manual-marca/,
# ../design-system/project/README.md, ../manik-ia/LEEME.md, ../directorio-nombre-r02/. Uso: python3 gen.py → arquitectura.html
import os, base64, json
D = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(D, '..')
uri = lambda p: 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.join(M, p), 'rb').read()).decode()
T = json.load(open(os.path.join(M, 'final/tema.json')))
P = T['productos']
S = {k: uri(f'final/svg/{k}.svg') for k in ['medicalmanik', 'expediente', 'agenda', 'compras', 'farmacia', 'impulsa', 'grupos', 'administracion', 'ecosistema']}
PIN = uri('manik-final/svg/simbolo.svg'); LOGO = uri('final/svg/medicalmanik-logotipo.svg')
IA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 3.5c.45 4.2 3.8 7.55 8 8-4.2.45-7.55 3.8-8 8-.45-4.2-3.8-7.55-8-8 4.2-.45 7.55-3.8 8-8z" fill="#5FD3E2"/><path d="M19 2c.2 1.6 1.4 2.8 3 3-1.6.2-2.8 1.4-3 3-.2-1.6-1.4-2.8-3-3 1.6-.2 2.8-1.4 3-3z" fill="#5FD3E2"/></svg>'

PROD = [('expediente', 'Expediente'), ('agenda', 'Agenda'), ('compras', 'Compras'), ('farmacia', 'Farmacia'), ('impulsa', 'Impulsa'), ('grupos', 'Grupos')]
RASGO = {'expediente': 'pestaña de carpeta', 'agenda': 'argollas de calendario', 'compras': 'borde de ticket', 'farmacia': 'cruz', 'impulsa': 'flecha que sale', 'grupos': 'segunda tarjeta detrás'}
sellos = ''.join(f'<figure><img src="{S[k]}" alt="" width="64" height="64"><figcaption><b>{n}</b> Manik<span>{P[n]["para"]}</span><span class="r">{RASGO[k]}</span></figcaption></figure>' for k, n in PROD)

ANTES = [
 ('La empresa', 'MedicalManik', 'MedicalManik', 'Sin cambio: es quien respalda. Su sello es el cuadro limpio con la línea de pulso.', 'hecho'),
 ('El expediente clínico', 'MedicalManik (el producto y la empresa se llamaban igual)', 'Expediente Manik', 'La ronda 1 de nombres partió de aquí: «la empresa sigue siendo MedicalManik; el producto lleva nombre propio».', 'hecho'),
 ('Campañas de prevención', 'Manik Impulsa (en producción)', 'Impulsa Manik', 'Se invierte el orden para seguir el patrón; su sistema en producción conserva su violeta como color de identidad.', 'hecho'),
 ('Agenda, Compras, Farmacia, Grupos', 'Sin nombre de producto', 'Agenda Manik · Compras Manik · Farmacia Manik · Grupos Manik', 'Nacen con el patrón desde el principio.', 'hecho'),
 ('Herramienta interna', 'No existía como producto', 'Administración Manik', 'Solo la ve el equipo de MedicalManik; para una clínica no existe.', 'hecho'),
 ('El directorio para pacientes', 'Mi Médico Manik', 'Manik → nombre nuevo en revisión', '«Manik» solo no se puede registrar; se exploran nombres como MediManik o DocManik.', 'en curso'),
 ('La inteligencia artificial', '«Recomendar tratamientos»', 'Manik IA (una función de Expediente)', 'No es un producto ni un personaje: en pantalla se llama «IA» y siempre sugiere.', 'hecho'),
]
filas = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td><b>{c}</b></td><td>{d}</td><td><span class="est {e.replace(" ", "-")}">{e}</span></td></tr>' for a, b, c, d, e in ANTES)

HTML = f'''<title>Arquitectura de MedicalManik</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap" rel="stylesheet">
<style>
/* Una sola luz, como la marca (tema claro único por decisión de marca): fondo papel, columna de lectura y láminas.
   Estructura de explicación: tesis → problema → tres niveles → regla del nombre → cómo se ve → casos → antes/ahora → abierto. */
:root{{--azul:#234899;--azul-osc:#1E3C7D;--cian:#009BB0;--cian-ui:#00788A;--papel:#F7F8FB;--blanco:#FFFFFF;--tinta:#14213D;--muted:#4A5674;--linea:#E1E6F0;--suave:#EEF1F7;
 --noche:#0F1C3F;--luz-cian:#D3F0F4;--luz-calida:#FFEFD2;--ok:#157B4A;--ok-s:#E7F5EE;--curso:#6B4A00;--curso-s:#FFF4E0;
 --display:"Urbanist","Segoe UI",system-ui,sans-serif;--sans:"Atkinson Hyperlegible Next","Atkinson Hyperlegible",system-ui,sans-serif;color-scheme:light}}
*{{box-sizing:border-box}}
body{{background:var(--papel);color:var(--tinta);font:400 17px/1.6 var(--sans);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
h1,h2,h3,h4{{font-family:var(--display);margin:0;text-wrap:balance;color:var(--tinta)}}p{{margin:0}}a{{color:var(--cian-ui)}}:focus-visible{{outline:3px solid var(--azul);outline-offset:2px}}
.hoja{{max-width:1060px;margin:0 auto;padding-block:32px 96px;display:grid;gap:72px;grid-template-columns:minmax(0,1fr)}}
.eti{{font:700 12px/16px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--cian-ui)}}
.texto{{max-width:64ch;display:grid;gap:14px}}.nota{{font-size:15px;line-height:22px;color:var(--muted)}}
section{{display:grid;gap:24px}}section>header{{display:grid;gap:6px}}h2{{font-size:clamp(26px,3.6vw,36px);line-height:1.15;font-weight:600}}h3{{font-size:21px;line-height:1.3;font-weight:600}}
/* portada */
.portada{{border-radius:32px;padding:clamp(28px,6vw,64px);display:grid;gap:22px;background:radial-gradient(ellipse 55% 80% at 0 0,var(--luz-cian),transparent 70%),radial-gradient(ellipse 45% 70% at 100% 10%,var(--luz-calida),transparent 70%),var(--blanco);border:1px solid var(--linea)}}
.portada img.logo{{width:min(300px,70%);height:auto}}
.portada h1{{font-size:clamp(34px,5.6vw,58px);line-height:1.05;font-weight:300;letter-spacing:-.02em;max-width:18ch}}.portada h1 b{{font-weight:600}}
.portada .lead{{font-size:19px;line-height:1.55;max-width:58ch}}
.claves{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}.claves div{{background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:4px}}.claves b{{font:600 17px/1.3 var(--display)}}.claves span{{font-size:15px;line-height:22px;color:var(--muted)}}
/* problema */
.antes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));gap:12px}}
.ficha{{background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:18px;display:grid;gap:8px;align-content:start}}.ficha b{{font:600 18px/1.3 var(--display)}}
.ficha .q{{font:600 22px/1.2 var(--display);color:var(--muted)}}
/* niveles */
.niveles{{display:grid;gap:0;border:1px solid var(--linea);border-radius:24px;overflow:hidden;background:var(--blanco)}}
.niv{{display:grid;grid-template-columns:120px minmax(0,1fr) minmax(0,1.2fr);gap:20px;align-items:center;padding:22px 24px;border-top:1px solid var(--linea)}}.niv:first-child{{border-top:0}}
.niv .k{{font:700 12px/16px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}.niv .k b{{display:block;font:600 34px/1 var(--display);letter-spacing:0;color:var(--azul);text-transform:none}}
.niv .ej{{display:flex;align-items:center;gap:12px;flex-wrap:wrap}}.niv .ej img{{width:44px;height:44px}}.niv .nm{{font:400 24px/1.2 var(--display);color:var(--muted)}}.niv .nm b{{font-weight:600;color:var(--tinta)}}
.niv p{{font-size:16px;line-height:24px}}
.analogia{{background:var(--noche);color:#fff;border-radius:24px;padding:24px 28px;display:grid;gap:10px}}.analogia h3{{color:#fff}}.analogia p{{color:#DCE3F2}}.analogia b{{color:#fff}}
.familia{{display:flex;flex-wrap:wrap;gap:8px 18px;font:400 22px/1.3 var(--display);color:#C9D3EA}}.familia b{{color:#fff;font-weight:600}}.familia span.ap{{color:#7FDCE6}}
/* regla del nombre */
.regla{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}}
.si,.no{{background:var(--blanco);border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:12px;align-content:start}}.si h4{{color:var(--ok)}}.no h4{{color:#B23A48}}
.si ul,.no ul{{margin:0;padding:0;list-style:none;display:grid;gap:10px}}.si li,.no li{{font:400 22px/1.2 var(--display)}}.si li b{{font-weight:600}}.no li{{color:var(--muted);text-decoration:line-through;text-decoration-color:#B23A48}}.no li small,.si li small{{display:block;font:400 14px/20px var(--sans);text-decoration:none;color:var(--muted)}}
.porque{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:12px}}.porque div{{border-left:3px solid var(--cian);padding:4px 0 4px 16px;display:grid;gap:4px}}.porque b{{font:600 17px/1.35 var(--display)}}
.tag{{display:inline-block;font:700 11px/16px var(--sans);letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:2px 8px;margin-left:6px;vertical-align:2px}}.tag.h{{background:var(--ok-s);color:var(--ok)}}.tag.i{{background:var(--suave);color:var(--muted)}}
/* sellos */
.sellos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:12px}}
.sellos figure{{margin:0;background:var(--blanco);border:1px solid var(--linea);border-radius:18px;padding:16px;display:grid;gap:10px;justify-items:start}}
.sellos figcaption{{display:grid;gap:2px;font:400 17px/1.3 var(--display);color:var(--muted)}}.sellos figcaption b{{font-weight:600;color:var(--tinta)}}.sellos figcaption span{{font:400 14px/20px var(--sans)}}.sellos .r{{color:var(--cian-ui)}}
.madre{{display:flex;flex-wrap:wrap;gap:24px;align-items:center;background:var(--blanco);border:1px solid var(--linea);border-radius:24px;padding:24px}}.madre img{{width:88px;height:88px}}.madre .texto{{flex:1;min-width:min(100%,280px)}}
.dos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:16px}}
.lam{{background:var(--blanco);border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:12px;align-content:start}}
.chip{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:6px 14px 6px 8px;font:600 15px/20px var(--sans)}}
.btn{{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border-radius:14px;background:var(--azul);color:#fff;font:600 15px/20px var(--sans)}}
.fila{{display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
/* tres familias */
.fams{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}.fam{{background:var(--blanco);border:1px solid var(--linea);border-radius:20px;padding:20px;display:grid;gap:10px;align-content:start}}
.fam .ic{{width:48px;height:48px;display:grid;place-items:center;border-radius:14px}}.fam .ic img{{width:44px;height:44px}}.fam .ic svg{{width:26px;height:26px}}
.fam dl{{margin:0;display:grid;gap:6px;font-size:15px;line-height:22px}}.fam dt{{font-weight:700;color:var(--muted);font-size:12px;letter-spacing:.06em;text-transform:uppercase}}.fam dd{{margin:0 0 6px}}
/* tabla */
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:20px;background:var(--blanco)}}
table{{border-collapse:collapse;width:100%;min-width:760px}}th,td{{text-align:left;vertical-align:top;padding:14px 16px;border-bottom:1px solid var(--linea);font-size:15px;line-height:22px}}thead th{{font:700 12px/16px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--suave)}}tbody tr:last-child>*{{border-bottom:0}}tbody th{{font-weight:700;min-width:150px}}
.est{{display:inline-block;border-radius:999px;padding:2px 10px;font:700 12px/18px var(--sans);white-space:nowrap}}.est.hecho{{background:var(--ok-s);color:var(--ok)}}.est.en-curso{{background:var(--curso-s);color:var(--curso)}}
.abiertos{{margin:0;padding-left:24px;display:grid;gap:10px;max-width:72ch}}
.glos{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:12px 28px;margin:0}}.glos div{{display:grid;gap:2px}}.glos dt{{font:600 17px/1.3 var(--display)}}.glos dd{{margin:0;font-size:15px;line-height:22px;color:var(--muted)}}
.pie{{border-top:1px solid var(--linea);padding-top:18px;display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between;font-size:14px;color:var(--muted)}}
@media (max-width:760px){{.claves,.fams,.regla{{grid-template-columns:1fr}}.niv{{grid-template-columns:1fr;gap:10px}}}}
</style>

<main class="hoja">
<header class="portada">
 <img class="logo" src="{LOGO}" alt="MedicalManik">
 <span class="eti">Arquitectura de marca · cómo se nombra todo</span>
 <h1>Una empresa que <b>respalda</b>, una familia que <b>se reconoce</b> y productos que <b>dicen qué hacen</b></h1>
 <p class="lead">MedicalManik dejó de usar un solo nombre para todo. La empresa es quien está detrás; cada producto tiene un nombre que dice para qué sirve, y «Manik» los une como un apellido. Este documento explica esa lógica, por qué se tomó y cómo se aplica.</p>
 <div class="claves"><div><b>MedicalManik</b><span>La empresa y el sello madre. Firma, respalda, no compite con sus productos.</span></div><div><b>Manik</b><span>El apellido de la familia. Une a todo lo que hace la empresa.</span></div><div><b>Expediente, Agenda…</b><span>El nombre de pila: dice qué hace cada producto y para quién.</span></div></div>
</header>

<section aria-labelledby="h-prob"><header><span class="eti">El punto de partida</span><h2 id="h-prob">Un nombre hacía tres trabajos a la vez</h2></header>
 <div class="texto"><p>Antes, «MedicalManik» nombraba a la empresa y también a su producto principal, el expediente clínico. Otros productos tenían nombres armados cada uno a su manera: «Manik Impulsa» ponía la familia primero; «Mi Médico Manik», para pacientes, agregaba un posesivo. Cuando una empresa crece de un producto a varios, ese arreglo deja de funcionar.</p></div>
 <div class="antes">
  <div class="ficha"><span class="q">«¿Uso MedicalManik?»</span><b>No dice cuál</b><p class="nota">Si la empresa y el producto se llaman igual, una clínica que contrata Farmacia no sabe si «ya tiene MedicalManik» o le falta.</p></div>
  <div class="ficha"><span class="q">Manik Impulsa · Mi Médico Manik</span><b>Cada uno con su regla</b><p class="nota">Sin un patrón, cada producto nuevo inventa su forma de nombrarse y la familia deja de verse como familia.</p></div>
  <div class="ficha"><span class="q">Seis productos, un sello</span><b>No se distinguen</b><p class="nota">En un selector de apps, seis cosas llamadas igual con el mismo símbolo obligan a leer cada etiqueta.</p></div>
 </div>
</section>

<section aria-labelledby="h-niv"><header><span class="eti">La lógica</span><h2 id="h-niv">Tres niveles, cada uno con un trabajo</h2></header>
 <div class="niveles">
  <div class="niv"><span class="k">Nivel<b>1</b></span><div class="ej"><img src="{S["medicalmanik"]}" alt=""><span class="nm"><b>MedicalManik</b></span></div><p><b>La empresa.</b> Da confianza: seguridad de la información, cumplimiento normativo, respaldo. Aparece en contratos, facturas, firma institucional y como «de MedicalManik» junto a los productos.</p></div>
  <div class="niv"><span class="k">Nivel<b>2</b></span><div class="ej"><img src="{S["ecosistema"]}" alt=""><span class="nm"><b>Ecosistema</b> Manik</span></div><p><b>La familia.</b> «Manik» es el apellido que comparten todos los productos. Su identificador es el mosaico de seis cuadros, el botón que lleva de una app a otra.</p></div>
  <div class="niv"><span class="k">Nivel<b>3</b></span><div class="ej"><img src="{S["farmacia"]}" alt=""><span class="nm"><b>Farmacia</b> Manik</span></div><p><b>El producto.</b> El nombre dice qué hace y para quién: Farmacia surte recetas y lleva inventario. Su sello cambia solo el borde; su color lo identifica.</p></div>
 </div>
 <div class="analogia"><h3>Funciona como un nombre y un apellido</h3><p>Nadie confunde a dos hermanos porque compartan apellido: el nombre de pila dice quién es cada uno y el apellido dice de qué familia viene. Así se leen los productos:</p>
  <p class="familia">{"".join(f'<span><b>{n}</b> <span class="ap">Manik</span></span>' for _, n in PROD)}</p>
  <p>Y la empresa es como los padres: no tiene que aparecer en cada presentación, pero respalda a todos («de MedicalManik»).</p></div>
 <div class="texto"><p class="nota">En los manuales de marca a este modelo se le llama <b>casa con marcas respaldadas</b>: está entre una marca única para todo (como un banco que llama a todo con su nombre) y una casa de marcas independientes (como una empresa de consumo cuyos productos no se parecen entre sí). Toma lo mejor de ambos: cada producto es claro y la familia se reconoce.</p></div>
</section>

<section aria-labelledby="h-reg"><header><span class="eti">La regla del nombre</span><h2 id="h-reg">Siempre «Producto Manik»</h2></header>
 <div class="regla">
  <div class="si"><h4>Así</h4><ul><li><b>Expediente</b> Manik<small>El producto en negritas, «Manik» en regular.</small></li><li><b>Impulsa</b> Manik</li><li><b>Grupos</b> Manik</li></ul></div>
  <div class="no"><h4>Así no</h4><ul><li>Manik Farmacia<small>El orden invertido rompe la familia.</small></li><li>Farmacia<small>Solo, se pierde de qué familia viene.</small></li><li>MedicalManik Agenda<small>La empresa no se usa como apellido del producto.</small></li></ul></div>
 </div>
 <div class="porque">
  <div><b>El producto va primero <span class="tag i">razón inferida</span></b><p class="nota">En un menú o un selector la vista lee la primera palabra. Si todas empezaran con «Manik», habría que leer hasta la segunda para distinguirlas.</p></div>
  <div><b>«Manik» y no «MedicalManik» <span class="tag i">razón inferida</span></b><p class="nota">Es corto y se puede repetir en seis nombres sin cansar. «MedicalManik» queda reservado para la empresa y su respaldo.</p></div>
  <div><b>Pesos distintos <span class="tag h">regla vigente</span></b><p class="nota">El producto en 600 y «Manik» en 400. La vista se queda en lo que distingue y el apellido acompaña.</p></div>
 </div>
</section>

<section aria-labelledby="h-ver"><header><span class="eti">Cómo se ve</span><h2 id="h-ver">La misma línea de pulso, un borde distinto</h2></header>
 <div class="madre"><img src="{S["medicalmanik"]}" alt="Sello de MedicalManik"><div class="texto"><p>El <b>sello madre</b> es el cuadro limpio con la M dibujada como línea de pulso. Esa línea es idéntica en todos los sellos de la familia y nunca se redibuja. Cada producto cambia solo el <b>borde del cuadro</b> con un rasgo que cuenta qué es, y la línea nunca se corta.</p></div></div>
 <div class="sellos">{sellos}</div>
 <div class="dos">
  <div class="lam"><h3>El color tiene dos trabajos que no se mezclan</h3><p><b>Identidad:</b> cada producto tiene su color, que vive en su sello y en su tarjeta. Dice en qué app estás.</p><p><b>Interfaz:</b> el botón principal es azul MedicalManik en las siete apps, y los estados (éxito, aviso, error) son iguales en todas.</p>
   <div class="fila"><span class="btn">Guardar receta</span><span class="chip" style="background:var(--ok-s);color:var(--ok)">Surtida</span></div>
   <p class="nota">Por qué: Farmacia es verde como «éxito», Compras ámbar como «aviso» y Grupos rojizo como «error». Si fueran color de botón, un «Guardar» rojo en Grupos se leería como peligro.</p></div>
  <div class="lam"><h3>Y en pantalla, solo cambia el sello</h3><p>Barra superior, botones, campos, diálogos y navegación son los mismos en las siete apps. Quien pasa de Agenda a Farmacia no reaprende nada: lo único que cambia es el sello y el nombre arriba a la izquierda.</p>
   <div class="fila">{"".join(f'<img src="{S[k]}" alt="{n} Manik" width="36" height="36">' for k, n in PROD)}</div><p class="nota">Detalle en el sistema de diseño del Ecosistema: <a href="https://claude.ai/artifact/28z6yfie6L8btocL8QBZi9" target="_blank" rel="noopener">AppShell, EncabezadoApp y controles ↗</a>.</p></div>
 </div>
</section>

<section aria-labelledby="h-fam"><header><span class="eti">Para quién es cada cosa</span><h2 id="h-fam">Tres familias bajo el mismo respaldo</h2></header>
 <div class="fams">
  <div class="fam"><span class="ic"><img src="{S["ecosistema"]}" alt=""></span><h3>Ecosistema Manik</h3><dl><dt>Para</dt><dd>Clínicas, hospitales, médicos y su equipo.</dd><dt>Qué es</dt><dd>Seis apps de trabajo y Administración, que es interna.</dd><dt>Cómo se nombra</dt><dd>«Producto Manik».</dd></dl></div>
  <div class="fam"><span class="ic"><img src="{PIN}" alt=""></span><h3>El directorio para pacientes</h3><dl><dt>Para</dt><dd>Pacientes que buscan médico.</dd><dt>Qué es</dt><dd>La cara pública: buscar, ver precio y agendar.</dd><dt>Cómo se nombra</dt><dd>Nombre propio con Manik y respaldo «de MedicalManik». En revisión: «Manik» solo no se puede registrar.</dd></dl></div>
  <div class="fam"><span class="ic" style="background:var(--noche)">{IA}</span><h3>Manik IA</h3><dl><dt>Para</dt><dd>Médicos, dentro de Expediente.</dd><dt>Qué es</dt><dd>Una función, no un producto ni un personaje.</dd><dt>Cómo se nombra</dt><dd>En pantalla, solo «IA»: «Resumir con IA». Siempre sugiere; el médico decide.</dd></dl></div>
 </div>
 <div class="texto"><p class="nota">El directorio tiene otra voz (de tú, cercana) y otra paleta (luz cian y cálida) porque habla con pacientes, no con médicos. Conserva la línea de pulso dentro de un pin: se reconoce como parte de la familia.</p></div>
</section>

<section aria-labelledby="h-casos"><header><span class="eti">Casos especiales</span><h2 id="h-casos">Las excepciones también tienen regla</h2></header>
 <div class="dos">
  <div class="lam"><img src="{S["administracion"]}" alt="" width="48" height="48"><h3>Administración Manik es invisible para las clínicas</h3><p>Es la herramienta del equipo de MedicalManik. A diferencia de una app que la clínica no contrató (que se ve apagada, con candado), Administración no aparece en absoluto: mostrarla revelaría una superficie interna y generaría solicitudes imposibles. Por eso queda fuera del mosaico de seis.</p></div>
  <div class="lam"><img src="{S["impulsa"]}" alt="" width="48" height="48"><h3>Impulsa ya existía</h3><p>Se llamaba «Manik Impulsa» y tiene sistema propio en producción. Pasa a «Impulsa Manik» por el patrón, y su violeta se conserva como color de identidad. Quedan abiertas tres diferencias con el sistema común: su tipografía, el color de sus botones y sus grises.</p></div>
 </div>
</section>

<section aria-labelledby="h-tabla"><header><span class="eti">Antes y ahora</span><h2 id="h-tabla">Qué cambió, producto por producto</h2></header>
 <div class="tw" tabindex="0" role="region" aria-label="Antes y ahora, producto por producto"><table><thead><tr><th scope="col">Qué es</th><th scope="col">Antes</th><th scope="col">Ahora</th><th scope="col">Por qué</th><th scope="col">Estado</th></tr></thead><tbody>{filas}</tbody></table></div>
</section>

<section aria-labelledby="h-abi"><header><span class="eti">Lo que sigue abierto</span><h2 id="h-abi">Decisiones pendientes</h2></header>
 <ol class="abiertos"><li><b>Nombre del directorio para pacientes.</b> «Manik» solo no se puede registrar. Hay propuestas con el molde de Doctoralia (MediManik, DocManik, DoctorManik) y la tipografía del logotipo será Sora. Falta saber por qué se rechazó «Manik» y hacer la búsqueda en el registro de marcas.</li>
 <li><b>Impulsa y el sistema común:</b> tipografía, color de acción y grises.</li>
 <li><b>Registro y dominios</b> de los nombres de producto en México y Centroamérica: no se han verificado.</li></ol>
</section>

<section aria-labelledby="h-glos"><header><span class="eti">Glosario</span><h2 id="h-glos">Palabras que usa este documento</h2></header>
 <dl class="glos">
  <div><dt>Arquitectura de marca</dt><dd>Cómo se relacionan y se nombran la empresa y sus productos.</dd></div>
  <div><dt>Marca madre</dt><dd>La marca de la empresa que respalda a las demás: MedicalManik.</dd></div>
  <div><dt>Respaldo</dt><dd>La firma pequeña que dice quién está detrás de un producto: «de MedicalManik».</dd></div>
  <div><dt>Sello</dt><dd>El símbolo de cada producto: la línea de pulso dentro de un cuadro con un rasgo propio en el borde.</dd></div>
  <div><dt>Color de identidad</dt><dd>El color que dice qué producto es. Vive en el sello y la tarjeta; nunca en botones ni estados.</dd></div>
  <div><dt>Mosaico del ecosistema</dt><dd>Los seis cuadros de color que abren el selector de apps. Siempre seis, aunque se sumen productos.</dd></div></dl>
</section>

<footer class="pie"><span>MedicalManik · Arquitectura de marca · noviembre 2026</span><span>Fuente: rondas de nombre y sello (24 de octubre), manual de identidad 2026 y sistema de diseño del Ecosistema</span></footer>
</main>'''
open(os.path.join(D, 'arquitectura.html'), 'w').write(HTML); print('ok', len(HTML) // 1024, 'KB')
