import sys,hashlib,math,unicodedata
S=sys.argv[1]
INK='#052A76'; PERA='#C2D225'; W='#FFFFFF'
FONDOS=[('Azul real',INK),('Azul medio','#3D67AE'),('Cian','#00B4D8'),('Verde','#006D53'),('Verde claro','#38B000'),('Pera',PERA),('Naranja','#F48C06'),('Café','#553739'),('Morado','#3D0066'),('Niebla','#E8EDF7')]
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4 for v in c]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
cr=lambda a,b:(max(lum(a),lum(b))+0.05)/(min(lum(a),lum(b))+0.05)
def tinta(bg): return W if cr(W,bg)>=cr(INK,bg) else INK          # figura: blanco o azul, el de más contraste
def muestra(bg,fig): return PERA if cr(PERA,bg)>=2.2 else fig      # el pocillo pera solo donde se distingue
GL={'A':'010101111101101','B':'110101110101110','C':'011100100100011','D':'110101101101110','E':'111100110100111','F':'111100110100100','G':'011100101101011','H':'101101111101101','I':'111010010010111','J':'001001001101010','K':'101101110101101','L':'100100100100111','M':'111111101101101','N':'101111111111101','O':'010101101101010','P':'110101110100100','Q':'010101101111011','R':'110101110101101','S':'011100010001110','T':'111010010010010','U':'101101101101111','V':'101101101101010','W':'101101101111101','X':'101101010101101','Y':'101101010010010','Z':'111001010100111'}
def iniciales(nombre):
    p=[unicodedata.normalize('NFD',w)[0].upper() for w in nombre.split() if w[0].isalpha()]
    return (p[0]+(p[-1] if len(p)>1 else p[0]))
def fig_A(nombre,bg):   # iniciales en pocillos: dos letras de 3×5
    f=tinta(bg); m=muestra(bg,f); a,b=iniciales(nombre); cells=[]
    for li,ch in enumerate((a,b)):
        g=GL.get(ch,GL['N'])
        for r in range(5):
            for c in range(3): cells.append((li*4+c,r,g[r*3+c]=='1'))
    last=max([(r,c) for c,r,on in cells if on and c>=4])
    s=''; step=12.5; ox=64-3*step; oy=64-2*step
    for c,r,on in cells:
        x=ox+c*step; y=oy+r*step
        if on: s+=f'<circle cx="{x}" cy="{y}" r="5.4" fill="{m if (r,c)==last else f}"/>'
    return s
def fig_B(nombre,bg):   # placa única: patrón 4×4 simétrico derivado del nombre
    f=tinta(bg); m=muestra(bg,f); h=hashlib.sha1(nombre.encode()).digest()
    bits=[(h[i]>>j)&1 for i in range(4) for j in range(2)]  # 8 bits: 2 columnas × 4 filas
    on=set()
    for r in range(4):
        for c in range(2):
            if bits[r*2+c]: on|={(c,r),(3-c,r)}
    if len(on)<6: on|={(1,1),(2,1),(1,2),(2,2)}
    lst=sorted(on); pk=lst[h[9]%len(lst)]
    s=''; step=20; o=64-1.5*step
    for c in range(4):
        for r in range(4):
            x=o+c*step; y=o+r*step
            s+=f'<circle cx="{x}" cy="{y}" r="7.6" fill="{m if (c,r)==pk else f}"/>' if (c,r) in on else f'<circle cx="{x}" cy="{y}" r="2.2" fill="{f}" opacity=".45"/>'
    return s
def fig_C(nombre,bg):   # figura fija para todos: cabeza y hombros hechos de pocillos
    f=tinta(bg); m=muestra(bg,f); s=f'<circle cx="64" cy="50" r="17" fill="{f}"/>'
    for i in range(5):
        a=math.radians(200+i*35); x=64+34*math.cos(a); y=112+34*math.sin(a)
        s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8.5 if i!=2 else 9.5}" fill="{m if i==2 else f}"/>'
    return s
def av(fig,nombre,bg,size):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}" role="img" aria-label="{nombre}"><defs><clipPath id="c"><circle cx="64" cy="64" r="64"/></clipPath></defs><g clip-path="url(#c)"><rect width="128" height="128" fill="{bg}"/>{fig(nombre,bg)}</g></svg>'
U=[('Mariana Ruiz',0),('Jorge Hernández',3),('Lucía Méndez',5),('Óscar Zárate',8),('Ana Sofía Vega',6),('Tomás Ibarra',2)]
C=[('A','Iniciales en pocillos','Las iniciales de cada persona escritas con pocillos, como el símbolo. Se leen: en una lista de capturas se sabe quién fue sin abrir nada. La figura sale del nombre y no se puede cambiar.',fig_A),
   ('B','Placa única','Un patrón de pocillos derivado del nombre, simétrico, con una muestra pera. Es como una huella: único y fijo, pero no se lee; hay que memorizarlo.',fig_B),
   ('C','Figura fija','La misma figura para todos: cabeza y hombros hechos de pocillos. Solo cambia el fondo; el nombre siempre va al lado.',fig_C)]
rows=''
for k,n,t,fn in C:
    users=''.join(f'<div class="u">{av(fn,nm,FONDOS[i][1],72)}<span>{nm}</span></div>' for nm,i in U)
    sizes=''.join(f'<span class="sz">{av(fn,"Mariana Ruiz",INK,z)}{z}</span>' for z in (40,32,24))
    picker=''.join(f'<span class="sw{" on" if j==0 else ""}" title="{nm}">{av(fn,"Mariana Ruiz",bg,40)}</span>' for j,(nm,bg) in enumerate(FONDOS))
    rows+=f'<section><h2>{k} · {n}</h2><p>{t}</p><div class="users">{users}</div><div class="row"><div class="sizes">{sizes}</div><div class="pick"><span class="ov">Elige el fondo</span><div class="sws">{picker}</div></div></div></section>'
for k,n,t,fn in C:
    for nm,i in U: open(f'{k}-{iniciales(nm)}.svg','w').write(av(fn,nm,FONDOS[i][1],128))
contr=' · '.join(f'{nm}: figura {"blanca" if tinta(bg)==W else "azul"} {cr(tinta(bg),bg):.1f}:1' for nm,bg in FONDOS)
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1100px}}h1{{font-size:24px;font-stretch:125%;color:{INK};margin:0 0 4px}}p.i{{margin:0 0 6px;color:#535B70;max-width:960px}}
section{{border-top:1px solid #E2E5EC;padding:20px 0;display:grid;gap:12px}}h2{{margin:0;font-size:17px;font-stretch:125%;color:{INK}}}section p{{margin:0;color:#535B70;max-width:880px}}
.users{{display:flex;gap:26px}}.u{{display:grid;justify-items:center;gap:6px;font-size:12px;color:#535B70}}.row{{display:flex;gap:40px;align-items:end}}
.sizes{{display:flex;gap:14px;align-items:end}}.sz{{display:grid;justify-items:center;gap:4px;font-size:11px;color:#535B70}}
.ov{{font:600 11px Archivo;letter-spacing:.08em;text-transform:uppercase;color:#535B70}}.pick{{display:grid;gap:8px}}.sws{{display:flex;gap:8px}}.sw{{border-radius:50%;padding:2px;border:2px solid transparent;display:block}}.sw svg{{display:block}}.sw.on{{border-color:{INK}}}
small{{color:#535B70}}
</style></head><body><h1>Nabi · avatares · ronda 1</h1><p class="i">Sin foto: cada persona tiene una figura de pocillos asignada por el sistema y solo elige el fondo entre diez colores de Nisa Nabani. La figura cambia sola a blanco o azul según el fondo, y la muestra pera solo aparece donde se distingue.</p>{rows}<small>{contr}</small></body></html>""")
print('ok')
