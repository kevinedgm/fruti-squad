# Grana · paleta de marca. Calcula OKLCH, contraste WCAG y busca los tonos que cumplen los mínimos de Grana (texto 4.5:1, controles 3:1).
import math, json
def srgb_to_lin(c): return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
def lin_to_srgb(c): return 12.92*c if c<=.0031308 else 1.055*c**(1/2.4)-.055
def hex2rgb(h): return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def rgb2hex(r): return '#%02x%02x%02x'%tuple(max(0,min(255,round(v*255))) for v in r)
def to_oklch(h):
    r,g,b=[srgb_to_lin(v) for v in hex2rgb(h)]
    l=.4122214708*r+.5363325363*g+.0514459929*b; m=.2119034982*r+.6806995451*g+.1073969566*b; s=.0883024619*r+.2817188376*g+.6299787005*b
    l,m,s=[v**(1/3) for v in (l,m,s)]
    L=.2104542553*l+.7936177850*m-.0040720468*s; a=1.9779984951*l-2.4285922050*m+.4505937099*s; bb=.0259040371*l+.7827717662*m-.8086757660*s
    return L, math.hypot(a,bb), math.degrees(math.atan2(bb,a))%360
def from_oklch(L,C,H):
    a=C*math.cos(math.radians(H)); b=C*math.sin(math.radians(H))
    l=(L+.3963377774*a+.2158037573*b)**3; m=(L-.1055613458*a-.0638541728*b)**3; s=(L-.0894841775*a-1.2914855480*b)**3
    r=4.0767416621*l-3.3077115913*m+.2309699292*s; g=-1.2684380046*l+2.6097574011*m-.3413193965*s; bl=-.0041960863*l-.7034186147*m+1.7076147010*s
    return rgb2hex([lin_to_srgb(max(0,min(1,v))) for v in (r,g,bl)])
def lum(h): r,g,b=[srgb_to_lin(v) for v in hex2rgb(h)]; return .2126*r+.7152*g+.0722*b
def cr(a,b): x,y=sorted([lum(a),lum(b)]); return (y+.05)/(x+.05)
def ok(h): L,C,H=to_oklch(h); return f'oklch({L*100:.1f}% {C:.3f} {H:.1f})'
CERA='#f7f2ea'; TINTA='#1d1517'; NOCHE='#151012'; CERA_N='#efe7dd'
CARMIN='#a3123a'
# carmín para fondo oscuro: mismo tono, más luz hasta 4.5:1 sobre la noche
L,C,H=to_oklch(CARMIN)
for k in range(200):
    c=from_oklch(L+k*.004,C,H)
    if cr(c,NOCHE)>=4.5: CARMIN_N=c; break
NOPAL='#2f6a3d'
L2,C2,H2=to_oklch(NOPAL)
for k in range(200):
    c=from_oklch(L2+k*.004,C2,H2)
    if cr(c,NOCHE)>=4.5: NOPAL_N=c; break
P={'claro':{'carmin':CARMIN,'nopal':NOPAL,'cera':CERA,'tinta':TINTA},'oscuro':{'carmin':CARMIN_N,'nopal':NOPAL_N,'cera':NOCHE,'tinta':CERA_N}}
rep={}
for modo,p in P.items():
    rep[modo]={k:{'hex':v,'oklch':ok(v)} for k,v in p.items()}
    fondo=p['cera']
    rep[modo]['contraste']={f'{k} sobre fondo':round(cr(v,fondo),2) for k,v in p.items() if k!='cera'}
    rep[modo]['contraste']['cera sobre carmín (texto en botón)']=round(cr(CERA if modo=='claro' else NOCHE,p['carmin']),2)
json.dump(rep,open('paleta.json','w'),ensure_ascii=False,indent=2)
print(json.dumps(rep,ensure_ascii=False,indent=1))
