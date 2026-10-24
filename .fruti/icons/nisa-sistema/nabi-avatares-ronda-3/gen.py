import sys,math,random
S=sys.argv[1]
INK='#121826'; PERA='#C2D225'; W='#FFFFFF'; AZ='#052A76'
TINTES=[('Azul real','#DCE3F3'),('Azul medio','#D3E0F4'),('Cian','#CCEEF5'),('Verde','#CFE7DE'),('Verde claro','#DBF1CC'),('Pera','#EEF4C2'),('Naranja','#FDE2C2'),('Café','#E9DDDB'),('Morado','#E4D7EF'),('Niebla','#EEF1F6')]
def wob(pts,seed,amp=0.7):
    r=random.Random(seed); return [(x+r.uniform(-amp,amp),y+r.uniform(-amp,amp)) for x,y in pts]
def smooth(pts,closed=True):
    n=len(pts); d=f'M{pts[0][0]:.1f} {pts[0][1]:.1f}'
    rng=range(n) if closed else range(n-1)
    for i in rng:
        p0=pts[(i-1)%n]; p1=pts[i]; p2=pts[(i+1)%n]; p3=pts[(i+2)%n]
        if not closed: p0=pts[max(i-1,0)]; p3=pts[min(i+2,n-1)]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6); c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f' C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d+('Z' if closed else '')
L=lambda d,w=3.4,f='none':f'<path d="{d}" fill="{f}" stroke="{INK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def head(seed,rx=21,ry=25,cx=64,cy=60):
    pts=[(cx+rx*math.cos(math.radians(a))*(0.92 if 40<a<140 else 1),cy+ry*math.sin(math.radians(a))) for a in range(0,360,30)]
    return L(smooth(wob(pts,seed)),f=W)
def cuerpo(seed):
    s=L('M57 82 C57 88 56 92 55 96 M71 82 C71 88 72 92 73 96')
    s+=L(smooth(wob([(14,132),(20,108),(40,95),(64,93),(88,95),(108,108),(114,132)],seed,0.6),False)+' L114 140 L14 140Z',f=W)
    s+=L('M51 96 L64 113 L77 96',3)+f'<circle cx="81" cy="103" r="4.6" fill="{PERA}" stroke="{INK}" stroke-width="1.6"/>'
    return s
oreja=lambda: L('M84 57 C90 54 92 64 85 67',3)
nariz=lambda v=0: L(['M65 58 L60 69 L66 70','M64 59 L61 69 C63 70 65 70 67 69','M66 58 L62 68 L67 68'][v],2.8)
def ojos(v):
    if v=='punto': return f'<circle cx="55.5" cy="58" r="2.6" fill="{INK}"/><circle cx="72.5" cy="58" r="2.6" fill="{INK}"/>'
    if v=='feliz': return L('M52 59 Q55.5 55 59 59',2.8)+L('M69 59 Q72.5 55 76 59',2.8)
    if v=='ovalo': return f'<ellipse cx="55.5" cy="58" rx="2.2" ry="3.2" fill="{INK}"/><ellipse cx="72.5" cy="58" rx="2.2" ry="3.2" fill="{INK}"/>'
cejas=lambda: L('M51 51 L59 49.5',2.6)+L('M69 49.5 L77 51',2.6)
lentes=lambda: L('M48 53 h14 v9 a3 3 0 0 1 -3 3 h-8 a3 3 0 0 1 -3 -3Z M66 53 h14 v9 a3 3 0 0 1 -3 3 h-8 a3 3 0 0 1 -3 -3Z M62 56 h4',2.6)
boca=lambda v: L(['M59 77 Q64 80.5 69 77','M59 77.5 H68','M58 76 Q64 82 70 76'][v],2.8)
H={ # (detrás de la cabeza, encima)
 'crop':   ('', 'M42 54 C38 30 88 28 86 52 C82 42 72 37 61 39 C52 41 46 46 42 54Z'),
 'raya':   ('', 'M41 57 C36 27 90 25 87 55 C84 43 76 37 66 38 C62 44 52 48 41 57Z'),
 'chongo': ('', 'M42 53 C40 32 88 32 86 53 C80 43 72 40 64 40 C56 40 48 43 42 53Z'),
 'largo':  ('M38 60 C33 26 95 26 90 60 L94 98 C80 103 48 103 34 98Z', 'M42 56 C40 30 88 30 86 56 C80 44 70 39 58 42 C51 44 46 49 42 56Z'),
 'rizos':  ('', ''),
 'bob':    ('M39 58 C36 28 92 28 89 58 L90 82 C86 86 81 84 80 79 L48 79 C47 84 42 86 38 82Z', 'M42 52 C42 32 86 32 86 52 L42 52Z'),
 'calvo':  ('', 'M43 58 C42 52 44 46 47 43 M85 58 C86 52 84 46 81 43'),
 'coleta': ('M84 44 C102 44 104 72 95 86 C93 68 89 57 82 51Z', 'M42 53 C40 31 88 31 86 53 C80 43 72 40 64 40 C56 40 48 43 42 53Z'),
}
P=[('Mariana','chongo',dict(ojos='punto',nariz=0,boca=0,cejas=False,lentes=False,barba=False)),
   ('Jorge','raya',dict(ojos='punto',nariz=1,boca=1,cejas=True,lentes=True,barba=False)),
   ('Lucía','largo',dict(ojos='feliz',nariz=0,boca=2,cejas=False,lentes=False,barba=False)),
   ('Óscar','calvo',dict(ojos='punto',nariz=2,boca=0,cejas=True,lentes=False,barba=True)),
   ('Ana','rizos',dict(ojos='ovalo',nariz=1,boca=0,cejas=False,lentes=False,barba=False)),
   ('Tomás','crop',dict(ojos='punto',nariz=0,boca=1,cejas=True,lentes=False,barba=False)),
   ('Sofía','bob',dict(ojos='punto',nariz=2,boca=0,cejas=False,lentes=True,barba=False)),
   ('Diego','coleta',dict(ojos='feliz',nariz=1,boca=2,cejas=False,lentes=False,barba=False))]
def figura(hair,f,seed):
    back,top=H[hair]; s=''
    if back: s+=L(back,2.6,INK)
    s+=cuerpo(seed)+head(seed)+oreja()
    if hair=='rizos': s+=''.join(f'<circle cx="{64+24*math.cos(math.radians(a)):.1f}" cy="{54+24*math.sin(math.radians(a)):.1f}" r="9" fill="{INK}"/>' for a in range(165,376,26))
    elif hair=='calvo': s+=L(top,3)
    elif top: s+=L(top,2.6,INK)
    if hair=='chongo': s+=f'<circle cx="64" cy="29" r="9.5" fill="{INK}"/>'
    if f['barba']: s+=L('M44 64 C44 92 84 92 84 64 C80 74 73 79 64 79 C55 79 48 74 44 64Z',2.6,INK)
    s+=ojos(f['ojos'])
    if f['cejas']: s+=cejas()
    if f['lentes']: s+=lentes()
    s+=nariz(f['nariz'])
    s+=boca(f['boca']).replace(INK,W) if f['barba'] else boca(f['boca'])
    return s
def av(i,bg,size):
    n,h,f=P[i]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="{size}" height="{size}" role="img" aria-label="{n}"><defs><clipPath id="c{i}{size}{bg[1:]}"><circle cx="64" cy="64" r="64"/></clipPath></defs><g clip-path="url(#c{i}{size}{bg[1:]})"><rect width="128" height="128" fill="{bg}"/><g transform="translate(64 68) scale(1.32) translate(-64 -64)">{figura(h,f,i+3)}</g></g></svg>'
people=''.join(f'<div class="u">{av(i,TINTES[(i*3)%10][1],88)}<span>{P[i][0]}</span></div>' for i in range(len(P)))
sizes=''.join(f'<span class="sz">{av(0,TINTES[0][1],z)}{z}</span>' for z in (48,40,32,24))
picker=''.join(f'<span class="sw{" on" if j==5 else ""}" title="{nm}">{av(0,bg,44)}</span>' for j,(nm,bg) in enumerate(TINTES))
ctx=f'<div class="ctx"><div class="li">{av(1,TINTES[1][1],32)}<span><b>Jorge Hernández</b> capturó <span class="m">0.0124 mg/L</span> · Plomo</span></div><div class="li">{av(3,TINTES[7][1],32)}<span><b>Óscar Zárate</b> envió el lote <span class="m">L-2026-10-147</span> a revisión</span></div><div class="li">{av(0,TINTES[5][1],32)}<span><b>Mariana Ruiz</b> liberó <span class="m">NN-26-00417</span></span></div></div>'
for i in range(len(P)): open(f'{P[i][0]}.svg','w').write(av(i,TINTES[0][1],128))
open('banco.html','w').write(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}@font-face{{font-family:'Plex';src:url('file://{S}/fuentes/IBMPlexMono.ttf')}}
body{{margin:0;background:#fff;color:#141B33;font:14px/1.45 Archivo,sans-serif;padding:32px;width:1100px}}h1{{font-size:24px;font-stretch:125%;color:{AZ};margin:0 0 4px}}p.i{{margin:0 0 18px;color:#535B70;max-width:960px}}
.users{{display:flex;gap:22px;margin-bottom:22px}}.u{{display:grid;justify-items:center;gap:6px;font-size:12px;color:#535B70}}
.row{{display:flex;gap:40px;align-items:end;border-top:1px solid #E2E5EC;padding-top:18px}}.sizes{{display:flex;gap:14px;align-items:end}}.sz{{display:grid;justify-items:center;gap:4px;font-size:11px;color:#535B70}}
.ov{{font:600 11px Archivo;letter-spacing:.08em;text-transform:uppercase;color:#535B70}}.pick{{display:grid;gap:8px}}.sws{{display:flex;gap:8px}}.sw{{border-radius:50%;padding:2px;border:2px solid transparent;display:block}}.sw svg{{display:block}}.sw.on{{border-color:{AZ}}}
.ctx{{margin-top:22px;border-top:1px solid #E2E5EC;padding-top:14px;display:grid;gap:10px;max-width:640px}}.li{{display:flex;gap:12px;align-items:center}}.li svg{{flex:none}}.m{{font-family:Plex,monospace;font-feature-settings:"zero"}}
</style></head><body><h1>Nabi · avatares · ronda 3 · caras</h1><p class="i">Caras dibujadas a mano con la gramática de Mango: ojos simples, nariz lineal angular, oreja simplificada, cabello sólido y bata con gafete pera. La figura es fija; el usuario solo elige el fondo entre diez tintes claros de los colores de Nisa Nabani, para que la figura se lea siempre.</p>
<div class="users">{people}</div><div class="row"><div class="sizes">{sizes}</div><div class="pick"><span class="ov">Elige el fondo</span><div class="sws">{picker}</div></div></div>{ctx}</body></html>""")
print('ok')
