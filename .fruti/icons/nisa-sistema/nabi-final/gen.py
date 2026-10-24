import sys,json
S=sys.argv[1]
src=open('../nabi-ronda-4/gen.py').read().split("V={'R'")[0]
g={}; sys.argv=['x',S]; exec(src,g)
INK,PERA,W='#052A76','#C2D225','#FFFFFF'
sym=lambda ink=INK,anim=False:g['sym']('R',ink,anim=anim)
fav=lambda ink=INK:g['fav']('R',ink)
def wm(ink=INK,x0=0,y0=100,size=92):
    s,x=g['wordmark'](x0,y0,size); return s.replace(INK,ink),x
def palabra(t,size,x0,y0,track=0): return g['palabra'](t,size,x0,y0,track)
def out(name,body,vb,w=None,h=None):
    wh=(' width="%s" height="%s"'%(w,h)) if w else ''
    open(f'svg/{name}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{wh}>{body}</svg>')
P={}
for nm,ink in [('simbolo',INK),('simbolo-tinta',INK),('simbolo-blanco',W),('simbolo-blanco-una',W)]:
    b=sym(ink)
    if nm=='simbolo-tinta': b=b.replace(PERA,INK)
    if nm=='simbolo-blanco-una': b=b.replace(PERA,W)
    out(nm,b,'10 10 108 108')
for nm,ink in [('wordmark',INK),('wordmark-blanco',W)]:
    s,x=wm(ink); out(nm,s,f'-4 22 {x+8:.0f} 90')
s,x=wm(INK); out('wordmark-tinta',s.replace(PERA,INK),f'-4 22 {x+8:.0f} 90')
for nm,ink in [('lockup-h',INK),('lockup-h-blanco',W),('lockup-h-tinta',INK)]:
    s,x=wm(ink,150); b=sym(ink)+s
    if nm.endswith('tinta'): b=b.replace(PERA,INK)
    out(nm,b,f'8 8 {x:.0f} 112')
# familia: lockup + «NISA NABANI» en versal ancha
d,xx=palabra('NISA NABANI',20,152,138,track=3.2)
for nm,ink in [('lockup-familia',INK),('lockup-familia-blanco',W)]:
    s,x=wm(ink,150); out(nm,sym(ink)+s+f'<path d="{d}" fill="{ink}"/>',f'8 8 {max(x,xx):.0f} 140')
# vertical
s,x=wm(INK,0,236,92)
out('lockup-v',f'<g transform="translate({(x-128)/2:.1f} 0)">{sym()}</g>'+s,f'-6 6 {x+12:.0f} 246')
# favicon con esquema
fv=fav('currentColor')
out('favicon',f'<style>svg{{color:{INK}}}@media (prefers-color-scheme:dark){{svg{{color:{W}}}}}</style>'+fv,'0 0 128 128')
out('favicon-tinta',fav(INK),'0 0 128 128')
# app icons
def app(bg,ink,pad=22,r=38):
    return f'<rect x="{-pad}" y="{-pad}" width="{128+2*pad}" height="{128+2*pad}" rx="{r}" fill="{bg}"/>'+sym(ink)
out('app-icon',app(INK,W),'-22 -22 172 172')
out('app-icon-claro',app(W,INK),'-22 -22 172 172')
out('app-icon-maskable',app(INK,W,52,0),'-52 -52 232 232')
out('avatar',f'<circle cx="64" cy="64" r="88" fill="{INK}"/>'+sym(W),'-24 -24 176 176')
# carga
out('carga',sym(INK,True),'10 10 108 108'); out('carga-blanco',sym(W,True),'10 10 108 108')
# tarjeta de redes
s,x=wm(INK,150); sc=600/x
out('tarjeta-redes',f'<rect width="1200" height="630" fill="{W}"/><g transform="translate({600-x*sc/2:.1f} {315-64*sc:.1f}) scale({sc:.3f})">{sym()}{s}</g><text x="600" y="560" text-anchor="middle" font-family="Onest, sans-serif" font-size="34" fill="{INK}">Sistema de laboratorio de Nisa Nabani</text>','0 0 1200 630')
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4 for v in c]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
cr=lambda a,b:round((max(lum(a),lum(b))+0.05)/(min(lum(a),lum(b))+0.05),1)
pairs=[('Azul sobre blanco',INK,W,4.5),('Blanco sobre azul',W,INK,4.5),('Pera sobre azul (acento)',PERA,INK,3),('Pera sobre blanco',PERA,W,3),('Azul sobre pera',INK,PERA,4.5)]
md='# Pruebas de contraste · Nabi\n\n| Par | Ratio | Mínimo | Resultado |\n|---|---|---|---|\n'+''.join(f'| {n} | {cr(a,b)}:1 | {m}:1 | {"PASA" if cr(a,b)>=m else "NO PASA"} |\n' for n,a,b,m in pairs)
md+='\nEl pera sobre blanco no alcanza 3:1: en el símbolo es un pocillo más (la N se lee por los pocillos azules) y nunca es texto ni el único portador de información. Sobre azul el pera sí cumple como acento.\n'
open('pruebas.md','w').write(md)
json.dump({'nombre':'Nabi','arquitectura':'marca de familia de Nisa Nabani','simbolo':'placa de 4×4 pocillos redondos; los llenos dibujan la N, los vacíos son puntos y la muestra pera ocupa el pocillo superior derecho',
 'color':{'azul':INK,'pera':PERA,'blanco':W,'nota':'Colores primarios del laboratorio Nisa Nabani.'},
 'tipografia':{'wordmark':'Archivo 700, ancho 125 %, minúsculas; i sin punto con pocillo pera; en trazados','interfaz':'pendiente: la UI usa Verdant WebKit v3'},
 'movimiento':{'carga':'la muestra pera recorre la N en orden de trazo, 10 pasos de 200 ms; con prefers-reduced-motion queda fija en el último pocillo'},
 'reglas':['El pera nunca es texto.','No reordenar ni quitar pocillos; la N tiene 10 llenos y 6 vacíos.','A 16–32 px se usa el favicon: solo la N, sin vacíos.','La muestra pera siempre es una sola.'],
 'pendiente':['Conciliar azul/pera de marca con el acento esmeralda de Verdant en la interfaz.','Búsqueda de marca «Nabi» (IMPI, USPTO, dominios).']},open('tema.json','w'),indent=1,ensure_ascii=False)
print('ok')
