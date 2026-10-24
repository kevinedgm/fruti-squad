# Vista de los avatares: el icono a 80 % del círculo, línea blanca o tinta según el fondo
import sys, re
S = sys.argv[1]
INK='#052A76'; W='#FFFFFF'; INKL='#121826'
FONDOS=[('Gris','#D9DCE3'),('Azul real',INK),('Azul medio','#3D67AE'),('Cian','#00B4D8'),('Verde','#006D53'),('Verde claro','#38B000'),('Pera','#C2D225'),('Naranja','#F48C06'),('Café','#553739'),('Morado','#3D0066'),('Niebla','#E8EDF7')]
def lum(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)]; c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+.05)/(lb+.05)
def col(bg): return W if cr(W,bg)>=cr(INKL,bg) else INKL
M=['masculine','feminine','masculine-glasses','feminine-glasses']; NOM={'masculine':'Hombre','feminine':'Mujer','masculine-glasses':'Hombre · lentes','feminine-glasses':'Mujer · lentes'}
def av(m,v,bg,z):
    s=open(f'user-avatar-{m}-{v}.svg').read()
    s=s.replace('<svg ',f'<svg width="{z*.8:.1f}" height="{z*.8:.1f}" ',1)
    return f'<span class="av" style="width:{z}px;height:{z}px;background:{bg};color:{col(bg)}">{s}</span>'
V=[('A','Línea','El pelo es un trazo más: corto termina en la sien, largo baja a los hombros.'),
   ('B','Masa','El pelo es una forma llena, como en Notion. La silueta cambia más entre hombre y mujer.'),
   ('C','Moño','Mismo arco para todos; solo el moño lateral marca a la mujer.')]
rows=''
for k,n,t in V:
    v=k.lower()
    big=''.join(f'<figure>{av(m,v,"#D9DCE3",96)}<figcaption>{NOM[m]}</figcaption></figure>' for m in M)
    small=''.join(f'<div class="col">{"".join(av(m,v,"#D9DCE3",z) for z in (40,32,24))}</div>' for m in M)
    sw=''.join(av(M[i%4],v,bg,40) for i,(nm,bg) in enumerate(FONDOS))
    rows+=f'<section><h2>{k} · {n}</h2><p>{t}</p><div class="row"><div class="big">{big}</div><div class="small">{small}</div></div><div class="sw">{sw}</div></section>'
open('vista.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1180px}}
h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}.i{{margin:0 0 8px;color:#535B70}}
section{{border-top:1px solid #E2E5EC;padding:18px 0}}h2{{margin:0;font-size:17px;font-stretch:125%;color:{INK}}}section p{{margin:2px 0 12px;color:#535B70}}
.row{{display:flex;gap:40px;align-items:center}}.big{{display:flex;gap:18px}}figure{{margin:0;display:grid;justify-items:center;gap:6px;font-size:12px;color:#535B70}}
.small{{display:flex;gap:14px}}.col{{display:grid;gap:8px;justify-items:center}}
.av{{border-radius:50%;display:inline-flex;align-items:center;justify-content:center;overflow:hidden}}.av svg{{display:block}}
.sw{{display:flex;gap:8px;margin-top:14px}}
</style></head><body><h1>Nabi · avatares · cara mínima con Uva</h1><p class="i">La cara de la ronda 4 redibujada en la retícula de Uva (24, trazo 1.5). Tres maneras de distinguir hombre y mujer; el usuario solo elige el fondo y la línea cambia sola a blanco o tinta.</p>{rows}</body></html>""")
