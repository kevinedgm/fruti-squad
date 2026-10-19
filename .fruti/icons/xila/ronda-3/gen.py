# Xila · ronda 3: disruptivo. El brocado no es ornamento: es dato. Tres ideas.
import sys,glob,random,math
S=sys.argv[1]; INK='#15171f'; PAPEL='#f7f5f0'; COB='#1f4bd8'; COB_D='#7a9bff'
sg=glob.glob(S+'/fuentes/SpaceGrotesk*')[0]
def svg(body,vb): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
# E · el hilo que se sale: el rombo tejido; un hilo en cobalto abandona la trama y sigue como línea de 2 px hasta su último valor, con punto y anillo y la cifra al final (la anatomía editorial de Xila: nada de leyenda)
def hilo(w=160,val='12.4',dark=False):
    ink=PAPEL if dark else INK; cob=COB_D if dark else COB; bg=INK if dark else PAPEL
    L=[6,14,22,30,38,30,22,14,6]; b=''
    for i,l in enumerate(L):
        y=12+i*5
        if i==4:
            b+=f'<path d="M{32-l/2} {y} H{32+l/2} C 62 {y} 70 {y-10} 84 {y-12} S 104 {y-24} 118 {y-26}" stroke="{cob}" stroke-width="3"/><circle cx="118" cy="{y-26}" r="4.5" fill="{cob}" stroke="{bg}" stroke-width="2.5"/><text x="127" y="{y-22}" font-family="SG,system-ui" font-size="11" font-weight="700" fill="{ink}">{val}</text>'
        else: b+=f'<path d="M{32-l/2} {y} H{32+l/2}" stroke="{ink}" stroke-width="3"/>'
    return svg(b,f'0 0 {w} 64')
def hilo_icono(dark=False):
    ink=PAPEL if dark else INK; cob=COB_D if dark else COB; bg=INK if dark else PAPEL
    L=[6,14,22,30,22,14,6]; b=''
    for i,l in enumerate(L):
        y=14+i*6
        if i==3: b+=f'<path d="M{24-l/2} {y} H{24+l/2} C 44 {y} 46 {y-8} 54 {y-12}" stroke="{cob}" stroke-width="3.5"/><circle cx="54" cy="{y-12}" r="4" fill="{cob}" stroke="{bg}" stroke-width="2.5"/>'
        else: b+=f'<path d="M{24-l/2} {y} H{24+l/2}" stroke="{ink}" stroke-width="3.5"/>'
    return svg(b,'0 0 64 64')
# F · telar generativo: el rombo es una distribución real. Cada conjunto de datos teje su propio brocado: el logo canónico es una muestra congelada
def telar(seed,dark=False):
    ink=PAPEL if dark else INK; cob=COB_D if dark else COB
    random.seed(seed); b=''; n=11
    vals=[max(.08,math.exp(-((i-5)/2.2)**2)+random.uniform(-.18,.18)) for i in range(n)]
    m=max(vals); modo=vals.index(m)
    for i,v in enumerate(vals):
        l=6+40*v/m; y=8+i*4.8
        b+=f'<path d="M{32-l/2} {y:.1f} H{32+l/2}" stroke="{cob if i==modo else ink}" stroke-width="3"/>'
    return svg(b,'0 0 64 64')
# G · xila tejida: el nombre hecho de hileras de hilo (como el brocado teje las figuras); el punto de la i en cobalto
def tejida(dark=False,h=9):
    ink=PAPEL if dark else INK; cob=COB_D if dark else COB
    # rejilla 5 filas por letra (x-altura) en celdas de 4; cada 1 es un tramo de hilo
    X=['1100011','0110110','0011100','0011100','0110110','1100011']; I=['0001000','0000000','0011000','0011000','0011000','0011000']; L=['1100000','1100000','1100000','1100000','1100000','1111111']; A=['0111110','0000011','0111111','1100011','1100011','0111111']
    letras=[X,I,L,A]; b=''; ox=4
    for li,g in enumerate(letras):
        for r,row in enumerate(g):
            y=5+r*5.6
            c=0
            while c<7:
                if row[c]=='1':
                    s=c
                    while c<7 and row[c]=='1': c+=1
                    x0=ox+s*4; x1=ox+(c-1)*4
                    col=cob if (li==1 and r==0) else ink
                    b+=f'<path d="M{x0} {y} H{x1}" stroke="{col}" stroke-width="3.2"/>'
                else: c+=1
        ox+=32
    return svg(b,'0 0 132 40')
css=f'''@font-face{{font-family:SG;src:url("file://{sg}");font-weight:300 700}}
body{{margin:0;padding:28px;background:#fff;color:{INK};font:14px/1.4 system-ui,sans-serif;width:1200px;box-sizing:border-box}}
h2{{font:700 18px SG;margin:0 0 4px}} .sub{{color:#666;margin:0 0 14px;max-width:1100px}} p.idea{{margin:0 0 10px;color:#444;max-width:520px}}
.fila{{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-bottom:30px}}
.celda{{display:grid;gap:12px;align-content:start}} svg{{display:block}}
.row{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}
.light{{background:{PAPEL};border-radius:12px;padding:14px}} .dark{{background:{INK};border-radius:12px;padding:14px}}
.tag{{font:400 12px system-ui;color:#666}}
.lock{{display:flex;align-items:center;gap:12px}} .lock b{{font:700 30px SG;letter-spacing:-.02em}}'''
E=f'''<div class="celda"><h2>E · el hilo que se sale</h2><p class="idea">El rombo tejido es el ornamento; un hilo en cobalto se escapa de la trama y sigue como línea de 2 px hasta su último valor, con punto y anillo y la cifra al final. Es la tesis de Xila: «formas que salen de la línea y la barra clásicas», dibujada con su propia anatomía.</p>
<div class="row"><div class="light"><span style="width:320px;display:block">{hilo()}</span></div><div class="dark"><span style="width:320px;display:block">{hilo(dark=True)}</span></div></div>
<div class="row"><div class="light" style="display:flex;gap:14px;align-items:center"><span style="width:64px">{hilo_icono()}</span><span style="width:24px">{hilo_icono()}</span><span style="width:16px">{hilo_icono()}</span></div><div class="dark" style="display:flex;gap:14px;align-items:center"><span style="width:64px">{hilo_icono(True)}</span><span style="width:24px">{hilo_icono(True)}</span></div><div class="lock"><span style="width:44px">{hilo_icono()}</span><b>xila</b></div></div>
<span class="tag">símbolo solo (el hilo sale y termina en punto) · el logo completo lleva la cifra, que puede ser real en cada uso</span></div>'''
F=f'''<div class="celda"><h2>F · telar generativo</h2><p class="idea">El rombo es una distribución real: cada hilera es un valor. Xila teje su propio logo a partir de datos (<code>xila.weave(data)</code>): en cada dashboard el brocado es distinto, hecho con los datos del cliente. El logo canónico es una muestra congelada; la moda, en cobalto.</p>
<div class="row"><div class="light" style="display:flex;gap:18px">{''.join(f'<span style="width:96px">{telar(s)}</span>' for s in (7,11,23,42))}</div></div>
<div class="row"><div class="dark" style="display:flex;gap:18px">{''.join(f'<span style="width:96px">{telar(s,True)}</span>' for s in (7,11))}</div><div class="lock"><span style="width:44px">{telar(7)}</span><b>xila</b></div></div>
<span class="tag">cuatro semillas, cuatro brocados · el de la izquierda sería el canónico</span></div>'''
G=f'''<div class="celda"><h2>G · xila tejida</h2><p class="idea">El nombre no se escribe: se teje. Cada letra son hileras de hilo, como el brocado teje sus figuras. El punto de la i, en cobalto, es el dato. El wordmark es el patrón y el patrón es el wordmark.</p>
<div class="row"><div class="light"><span style="width:396px;display:block">{tejida()}</span></div><div class="dark"><span style="width:264px;display:block">{tejida(True)}</span></div></div>
<div class="row"><div class="light"><span style="width:132px;display:block">{tejida()}</span></div><div class="light" style="display:flex;gap:0;flex-wrap:wrap;width:400px">{''.join(f'<span style="width:132px;display:block;opacity:{1 if i==4 else .55}">{tejida()}</span>' for i in range(9))}</div></div>
<span class="tag">a 122 px aún se lee; como banda repetida es textura de marca</span></div>'''
open('banco.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Xila · ronda 3 · disruptivo: el brocado no es ornamento, es dato. Tres ideas que solo Xila puede contar.</p><div class="fila">{E}{F}</div><div class="fila">{G}</div>')
print('ok')
