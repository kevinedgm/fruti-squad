# Uva E5 · propuesta conjunta de los iconos de dominio de PULZ (una página para elegir los cinco)
import os,subprocess,html
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
U='/home/user/fruti-squad/agentes/uva/scripts/buscar-lucide.mjs'
def var(id,v): return open(f'{R}/{id}/variantes/{id}-{v}.svg').read().strip()
def luc(n):
    r=subprocess.run(['node',U,'--svg',n,'--stroke','2'],capture_output=True,text=True).stdout; return r[r.index('<svg'):].strip()
I=[ # id, etiqueta en la app, recomendada, alternativas {v: motivo}, actual en la app, confusiones
 ('agave','Maguey','b',{'a':'un solo contorno en zigzag: se lee corona o fuego','c':'pencas bajas arqueadas: también corona'},'sprout',['tree-palm','flame','crown'],
  'Tres pencas rectas muy abiertas: la roseta ancha y baja del espadín. Lo rígido y puntiagudo la separa del brote, que hoy usa la app.'),
 ('earth-oven','Horno cónico','c',{'a':'montículo alto sobre cono: es un cono de helado','b':'cono hondo: helado o copa'},'flame',['ice-cream-cone','martini','cooking-pot'],
  'El montículo de piñas cociendo sobre el hoyo, con humo. La línea de suelo que sobresale por los dos lados dice «está enterrado».'),
 ('masonry-oven','Mampostería','c',{'a':'bóveda sola: se lee iglú o túnel','b':'juntas y chimenea: fábrica, y a 16 px es ruido'},'flame',['house','warehouse','brick-wall-fire'],
  'Horno de obra sobre el suelo con boca en arco y vapor. El vapor lo separa de una casa.'),
 ('stone-mill','Tahona','b',{'a':'el centro de la rueda se lee como ojo','c':'rueda sola en el suelo: disco o rodillo'},'cog',['ferris-wheel','disc','tractor'],
  'La rueda de piedra unida por la vara al poste del centro: la estructura de la tahona. El engrane de hoy dice «maquinaria».'),
 ('fermenting','Fermentación','b',{'a':'con el aro del medio, a trazo 2 se lee pastel de capas'},'barrel',['database','trash','cylinder'],
  'La tina de Uva que ya teníamos, a trazo 2 y sin el aro del medio. Las burbujas la separan de la base de datos; el barril de hoy dice «vino».'),
]
nav=lambda pick:''.join(f'<li>{var(id,v) if pick else luc(cur)}<span>{lab}</span></li>' for id,lab,v,_,cur,_,_ in I)
cards=''
for id,lab,v,alts,cur,conf,why in I:
    rec=var(id,v)
    sizes=''.join(f'<span class="sz" style="width:{s}px;height:{s}px">{rec}</span>' for s in (16,20,24,32))
    alt=''.join(f'<figure>{var(id,a)}<figcaption><b>{a.upper()}</b> · {html.escape(m)}</figcaption></figure>' for a,m in alts.items())
    cf=''.join(f'<figure class="cf">{luc(n)}<figcaption>{n}</figcaption></figure>' for n in [cur]+conf)
    cards+=f'''<article class="icono" aria-labelledby="t-{id}">
 <div class="cab"><div class="grande">{rec}</div><div class="txt"><span class="eyebrow">{lab} · <code>{id}</code></span><h3 id="t-{id}">Recomendada: {v.upper()}</h3><p>{html.escape(why)}</p><div class="tamanos">{sizes}<small>16 · 20 · 24 · 32 px</small></div></div></div>
 <div class="fila"><h4>Junto a sus confusiones, a 24 px</h4><div class="conf"><figure class="cf rec">{rec}<figcaption>{id}</figcaption></figure>{cf}</div></div>
 <div class="fila"><h4>Descartadas</h4><div class="alts">{alt}</div></div>
</article>'''
T=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'plantilla.html')).read()
out=T.replace('{{NAV_ANTES}}',nav(False)).replace('{{NAV_DESPUES}}',nav(True)).replace('{{CARDS}}',cards)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'iconos-pulz.html'),'w').write(out); print(len(out))
