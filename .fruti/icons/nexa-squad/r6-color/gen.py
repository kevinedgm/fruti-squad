# Nexa Squad · ronda 6 · dos opciones de color sobre la familia Huecos. python3 gen.py -> color.html
import os, math, itertools, importlib.util
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D,'../r5-huecos/gen.py')).read().split('for i, n, r in AG:\n    open(')[0]
ns = {'__file__': os.path.join(D,'../r5-huecos/gen.py')}; exec(src, ns)
AG, CUT = ns['AG'], ns['CUT']
TINTA, BLANCO, CLARO, OSCURO = '#16161B', '#F3F3EE', '#FFFFFF', '#101014'
# A · un color por agente: tono que avanza con la cadena (Orka → Vera); luminancia 0.15–0.24 para pasar 3:1 en blanco y en oscuro con el mismo valor
A = {'squad':None,'orka':'#DD5C00','inqa':'#977700','arko':'#428300','fluxa':'#008E8E','kompa':'#008CCE','kura':'#4761E4','forja':'#874CD4','vera':'#BF308F'}
# B · tinta + un acento que llena el hueco (claro: bloque tinta; oscuro: bloque claro)
ACC = [('cian','Cian','#22C3E6','#00728A'),('senal','Señal','#FFC21A','#8A6100'),('violeta','Violeta','#9D8CFF','#5B45DB')]

def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): a,b=lum(a),lum(b); return (max(a,b)+.05)/(min(a,b)+.05)
def lin(h): return [ (x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for x in [int(h[i:i+2],16)/255 for i in (1,3,5)]]
def oklab(c):
    r,g,b=c; l=(0.4122214708*r+0.5363325363*g+0.0514459929*b)**(1/3); m=(0.2119034982*r+0.6806995451*g+0.1073969566*b)**(1/3); s=(0.0883024619*r+0.2817188376*g+0.6299787005*b)**(1/3)
    return (0.2104542553*l+0.7936177850*m-0.0040720468*s, 1.9779984951*l-2.4285922050*m+0.4505937099*s, 0.0259040371*l+0.7827717662*m-0.8086757660*s)
def deutan(c):
    M=[[0.367322,0.860646,-0.227968],[0.280085,0.672501,0.047413],[-0.011820,0.042940,0.968881]]
    return [max(0,sum(M[i][j]*c[j] for j in range(3))) for i in range(3)]
def dE(a,b,f=lambda c:c): A_,B_=oklab(f(lin(a))),oklab(f(lin(b))); return 100*math.dist(A_,B_)
cols=[(k,v) for k,v in A.items() if v]
pares=[(a[0],b[0],dE(a[1],b[1]),dE(a[1],b[1],deutan)) for a,b in itertools.combinations(cols,2)]
peor=min(pares,key=lambda p:p[2]); peorD=min(pares,key=lambda p:p[3])

def sym(id_, size, uid, label, fill='currentColor', acc=None):
    under = f'<rect x="4" y="4" width="40" height="40" rx="7" fill="{acc}"/>' if acc else ''
    return (f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" role="img" aria-label="{label}">'
            f'<defs><mask id="{uid}" maskUnits="userSpaceOnUse" x="0" y="0" width="48" height="48"><rect width="48" height="48" fill="#fff"/>{CUT[id_]}</mask></defs>'
            f'{under}<rect x="4" y="4" width="40" height="40" rx="7" fill="{fill}" mask="url(#{uid})"/></svg>')
n=[0]
def u(): n[0]+=1; return f'q{n[0]}'
def colA(i, oscuro): return A[i] or (BLANCO if oscuro else TINTA)
def famA(oscuro, sz=56): return ''.join(f'<figure>{sym(i,sz,u(),nm,colA(i,oscuro))}<figcaption>{nm}</figcaption></figure>' for i,nm,_ in AG)
def famB(oscuro, sz=56): return ''.join(f'<figure>{sym(i,sz,u(),nm,"var(--b-bloque)" if not oscuro else "var(--b-bloque-o)", "var(--acc)" if not oscuro else "var(--acc-o)")}<figcaption>{nm}</figcaption></figure>' for i,nm,_ in AG)
def tira(f, oscuro): return ''.join(f(i,oscuro) for i,_,_ in AG)
appA = ''.join(f'<span class="app" style="background:{A[i] or TINTA}">{sym(i,46,u(),nm,"#fff")}</span>' for i,nm,_ in AG)
appB = ''.join(f'<span class="app" style="background:{TINTA}">{sym(i,46,u(),nm,"#F3F3EE","var(--acc-o)")}</span>' for i,nm,_ in AG)
def ficha(opt, i, nm, r):
    if opt=='A': s = sym(i,40,u(),nm,colA(i,False)); bar = f'style="--c:{A[i] or TINTA}"'
    else: s = sym(i,40,u(),nm,TINTA,'var(--acc)'); bar = 'style="--c:var(--acc-o)"'
    return f'<div class="mk" {bar}>{s}<div><b>{nm}</b><span>{r}</span></div><i>Instalar</i></div>'
mkA = ''.join(ficha('A',i,nm,r) for i,nm,r in AG[1:5]); mkB = ''.join(ficha('B',i,nm,r) for i,nm,r in AG[1:5])
filasA = ''.join(f'<tr><th>{nm}</th><td><span class="sw" style="background:{A[i]}"></span>{A[i]}</td><td>{cr(A[i],CLARO):.2f}</td><td>{cr(A[i],OSCURO):.2f}</td></tr>' for i,nm,_ in AG if A[i])
filasB = ''.join(f'<tr><th>{nom}</th><td><span class="sw" style="background:{l}"></span>{l}</td><td>{cr(l,TINTA):.2f}</td><td><span class="sw" style="background:{d}"></span>{d}</td><td>{cr(d,BLANCO):.2f}</td></tr>' for k,nom,l,d in ACC)
btns = ''.join(f'<button type="button" data-l="{l}" data-d="{d}" aria-pressed="{"true" if j==0 else "false"}">{nom}</button>' for j,(k,nom,l,d) in enumerate(ACC))
NOM = dict((i,nm) for i,nm,_ in AG)
HTML = f'''<title>Nexa Squad · Color r6</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..700&display=swap">
<style>
/* Dos columnas que se comparan fila por fila: familia en claro, en oscuro, iconos de app, fichas de marketplace y contraste */
:root{{--bg:#f5f5f2;--fg:#16161b;--muted:#5a5a65;--line:#dbdbd4;--card:#fff;--paper:#fff;--night:#101014;--nightfg:#f3f3ee;
--acc:{ACC[0][2]};--acc-o:{ACC[0][3]};--b-bloque:{TINTA};--b-bloque-o:{BLANCO};--f:'Bricolage Grotesque',ui-sans-serif,system-ui,sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#131317;--fg:#ededea;--muted:#a2a2ac;--line:#2b2b32;--card:#1a1a1f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#131317;--fg:#ededea;--muted:#a2a2ac;--line:#2b2b32;--card:#1a1a1f;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 var(--f);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}}
.w{{max-width:1240px;margin:0 auto;display:grid;gap:36px}}
h1{{font-size:clamp(30px,5vw,52px);line-height:1.03;margin:0;text-wrap:balance}} h2{{margin:0;font-size:28px;line-height:1.1}} h3{{margin:0;font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.intro{{display:grid;gap:12px;max-width:72ch}} .intro p{{margin:0;color:var(--muted)}}
.ojo{{margin:0;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}}
.dos{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}}
.op{{display:grid;gap:16px;align-content:start;padding:20px;background:var(--card);border:1px solid var(--line);border-radius:16px;min-width:0}}
.op>header{{display:grid;gap:6px}} .op>header p{{margin:0;font-size:15px}}
.lien{{display:flex;flex-wrap:wrap;gap:14px 16px;padding:18px;border-radius:12px}} .lien.cl{{background:var(--paper);border:1px solid var(--line);color:#16161b}} .lien.os{{background:var(--night);color:var(--nightfg)}}
figure{{margin:0;display:grid;justify-items:center;gap:4px}} figcaption{{font-size:12px;opacity:.7}}
.apps{{display:flex;flex-wrap:wrap;gap:10px}} .app{{display:grid;place-items:center;width:64px;height:64px;border-radius:15px}}
.mks{{display:grid;gap:8px}} .mk{{display:flex;gap:12px;align-items:center;padding:12px 14px;border-radius:12px;background:var(--paper);border:1px solid var(--line);border-left:5px solid var(--c);color:#16161b}}
.mk b{{display:block;font-size:17px;line-height:1.1}} .mk span{{font-size:13px;color:#5a5a65}} .mk i{{margin-left:auto;font-style:normal;font-weight:600;font-size:14px;padding:6px 14px;border-radius:999px;background:#16161b;color:#fff}}
.tw{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:14px;font-variant-numeric:tabular-nums}} th,td{{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}} thead th{{font-size:12px;color:var(--muted);font-weight:600}}
.sw{{display:inline-block;width:14px;height:14px;border-radius:4px;vertical-align:-2px;margin-right:6px;border:1px solid var(--line)}}
.sel{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}} .sel button{{font:600 14px var(--f);padding:7px 14px;border-radius:999px;border:1.5px solid var(--line);background:var(--paper);color:#16161b;cursor:pointer}}
.sel button[aria-pressed="true"]{{border-color:#16161b;background:#16161b;color:#fff}} .sel button:focus-visible{{outline:3px solid var(--fg);outline-offset:2px}}
.nota{{margin:0;font-size:14px;color:var(--muted)}}
.cierre ul{{margin:0;padding-left:20px;display:grid;gap:6px;max-width:76ch}}
@media (max-width:900px){{.dos{{grid-template-columns:1fr}}}}
</style>
<div class="w">
<div class="intro"><p class="ojo">Ronda 6 · color sobre la familia Huecos</p><h1>Nexa Squad: dos formas de dar color</h1>
<p>A le da un color a cada agente, como Fruti Squad. B deja el bloque en tinta y pone un solo acento dentro del hueco: el color cae justo en lo que el agente hace. Mismos símbolos, mismas aplicaciones, lado a lado.</p></div>
<div class="dos">
<section class="op" aria-labelledby="ta"><header><p class="ojo">Opción A</p><h2 id="ta">Un color por agente</h2>
<p>El tono avanza con la cadena, de Orka (naranja) a Vera (rosa); el squad va en tinta. Cada color tiene la misma luminancia, así que pasa 3:1 en blanco y en oscuro sin una versión aparte.</p></header>
<h3>Claro</h3><div class="lien cl">{famA(False)}</div><h3>Oscuro</h3><div class="lien os">{famA(True)}</div>
<h3>Icono de app</h3><div class="apps">{appA}</div>
<h3>Ficha de marketplace</h3><div class="mks">{mkA}</div>
<h3>Contraste del bloque</h3><div class="tw"><table><thead><tr><th>Agente</th><th>Color</th><th>Sobre blanco</th><th>Sobre #101014</th></tr></thead><tbody>{filasA}</tbody></table></div>
<p class="nota">Par más parecido: {NOM[peor[0]]} y {NOM[peor[1]]} (ΔE {peor[2]:.1f}). Con deuteranopia simulada, varios pares casi se igualan: {NOM[peorD[0]]} y {NOM[peorD[1]]} (ΔE {peorD[3]:.1f}), Kura y Forja (2.8), Inqa y Arko (4.5). Es el costo de darles la misma luminancia: para quien no distingue rojo y verde solo queda el eje azul-amarillo. El símbolo los separa igual; el color nunca es lo único que distingue a un agente.</p>
</section>
<section class="op" aria-labelledby="tb"><header><p class="ojo">Opción B</p><h2 id="tb">Tinta y un acento en el hueco</h2>
<p>Un solo color para toda la marca. En claro el bloque es tinta y el hueco se llena con el acento; en oscuro el bloque es claro y el acento baja de tono. Prueba tres acentos:</p>
<div class="sel" role="group" aria-label="Acento">{btns}</div></header>
<h3>Claro</h3><div class="lien cl">{famB(False)}</div><h3>Oscuro</h3><div class="lien os">{famB(True)}</div>
<h3>Icono de app</h3><div class="apps">{appB}</div>
<h3>Ficha de marketplace</h3><div class="mks">{mkB}</div>
<h3>Contraste del acento contra su bloque</h3><div class="tw"><table><thead><tr><th>Acento</th><th>En claro</th><th>Contra tinta</th><th>En oscuro</th><th>Contra bloque claro</th></tr></thead><tbody>{filasB}</tbody></table></div>
<p class="nota">El acento solo vive dentro del bloque, así que su contraste se mide contra el bloque, no contra la página. Distinguir agentes depende del hueco, igual que en tinta.</p>
</section></div>
<section class="cierre"><h2>Cómo decidir</h2><ul>
<li><b>A</b> sirve si cada agente se va a vender o instalar por separado: el color lo identifica en el marketplace aunque el símbolo sea chico.</li>
<li><b>B</b> sirve si Nexa se vende como un solo paquete: la marca se ve más unida y más sobria, y el color refuerza la idea de la familia (lo que hace el agente es lo que brilla).</li>
<li><b>Con Fruti Squad:</b> A se parece a su sistema (un color por integrante); B separa a Nexa con claridad.</li></ul></section>
</div>
<script>
document.querySelectorAll('.sel button').forEach(b=>b.addEventListener('click',()=>{{
  document.querySelectorAll('.sel button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));
  document.documentElement.style.setProperty('--acc',b.dataset.l);document.documentElement.style.setProperty('--acc-o',b.dataset.d);
}}));
</script>'''
open(os.path.join(D,'color.html'),'w').write(HTML)
print('peor', peor, 'deutan', peorD); print([ (nm,round(cr(l,TINTA),2),round(cr(d,BLANCO),2)) for k,nm,l,d in ACC])
