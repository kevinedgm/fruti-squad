# Sello «Hecho en Oaxaca / Made in Oaxaca» · paquete final. Uso: python gen.py <BricolageGrotesque[opsz,wdth,wght].ttf>
import sys, math
exec(open('../ronda-4/gen.py').read().split('\nOUT={}\n')[0])
MANTA_N='#fff8ee'
TXT='var(--oaxaca-texto,#db0077)'   # rosa algo más oscuro: 4.52:1 sobre fondo claro (texto pequeño)
def lab(f): return {'es':'Hecho en Oaxaca','en':'Made in Oaxaca'}.get(f,'Hecho en Oaxaca / Made in Oaxaca')
def doc(w,h,body,label,oscuro=False,style=''):
    col='#fff8ee;--oaxaca-texto:#f30084' if oscuro else '#1a1210'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" role="img" aria-label="{label}" style="color:{col}">{style}{body}</svg>\n'
def centrado(s,size,cx,y,w=800,wd=78,op=48,tr=1.4):
    _,W=texto(s,size,0,0,w,wd,op,tr); return texto(s,size,cx-W/2,y,w,wd,op,tr)
OUT={}
X=122
# --- horizontal bilingüe (L2) y su versión animada (L3 que termina en L2)
da,wa=texto('HECHO EN',19,X,44,800,78,48,1.4); db,wb=texto('MADE IN',19,X,66,800,78,48,1.4)
llave=f'<path class="ll" d="M{X+max(wa,wb)+6:.1f} 30q6 0 6 6v8q0 4 4 6q-4 2-4 6v8q0 6-6 6" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" opacity=".5"/>'
do,wo=texto('OAXACA',48,X-2,114,850,75,48,0.5)
Wh=X+max(wo,max(wa,wb)+24)+6
H=lambda dk: doc(Wh,140,k2(55,70,44,'h')+f'<path fill="{INK}" d="{da}"/><path fill="{TXT}" d="{db}"/>'+llave+f'<path fill="{INK}" d="{do}"/>',lab('bi'),dk)
OUT['sello-horizontal']=H(False); OUT['sello-horizontal-oscuro']=H(True)
# animado: los dos letreros alternan girando sobre su eje horizontal y se asientan apilados (4.8 s, una vez)
dA,_=texto('HECHO EN',26,X,62,800,78,48,1.4*26/19); dB,_=texto('MADE IN',26,X,62,800,78,48,1.4*26/19)
s=19/26

def caja_texto(t,size,x0,y0,w=800,wd=78,op=48,track=0):
    from fontTools.pens.boundsPen import BoundsPen
    f,p=fnt(w,wd,op); hf=hb.Font(hb.Face(hb.Blob.from_file_path(p))); b=hb.Buffer(); b.add_str(t); b.guess_segment_properties(); hb.shape(hf,b,{'kern':True})
    gs=f.getGlyphSet(); order=f.getGlyphOrder(); k=size/f['head'].unitsPerEm; x=x0; bp=BoundsPen(gs)
    for gi,ps in zip(b.glyph_infos,b.glyph_positions):
        gs[order[gi.codepoint]].draw(TransformPen(bp,(k,0,0,-k,x,y0))); x+=ps.x_advance*k+track
    return bp.bounds
def ajuste(g,c,s):
    x0,y0,x1,y1=caja_texto(*g); X0,Y0,X1,Y1=caja_texto(*c); cy=(y0+y1)/2
    return X0-x0, Y0-(cy+(y0-cy)*s)
tx1,ty1=ajuste(('HECHO EN',26,X,62,800,78,48,1.4*26/19),('HECHO EN',19,X,44,800,78,48,1.4),s); tx2,ty2=ajuste(('MADE IN',26,X,62,800,78,48,1.4*26/19),('MADE IN',19,X,66,800,78,48,1.4),s)
anim=('<style>.g1,.g2{transform-box:fill-box;transform-origin:left center;animation:4.8s cubic-bezier(.4,0,.2,1) 1 both}.g1{animation-name:ha}.g2{animation-name:hb}'
      '.ll{animation:hl 4.8s 1 both}'
      '@keyframes ha{0%,18%{transform:scaleY(1);opacity:1}23%,43%{transform:scaleY(0);opacity:0}48%,68%{transform:scaleY(1);opacity:1}'
      f'82%,100%{{transform:translate({tx1:.2f}px,{ty1:.2f}px) scale({s:.4f});opacity:1}}}}'
      '@keyframes hb{0%,18%{transform:scaleY(0);opacity:0}23%,43%{transform:scaleY(1);opacity:1}48%,68%{transform:scaleY(0);opacity:0}'
      f'82%,100%{{transform:translate({tx2:.2f}px,{ty2:.2f}px) scale({s:.4f});opacity:1}}}}'
      '@keyframes hl{0%,76%{opacity:0}100%{opacity:.5}}'
      f'@media (prefers-reduced-motion:reduce){{.g1,.g2,.ll{{animation:none}}.g1{{transform:translate({tx1:.2f}px,{ty1:.2f}px) scale({s:.4f})}}.g2{{transform:translate({tx2:.2f}px,{ty2:.2f}px) scale({s:.4f})}}}}</style>')
A=lambda dk: doc(Wh,140,k2(55,70,44,'a')+f'<path class="g1" fill="{INK}" d="{dA}"/><path class="g2" fill="{TXT}" d="{dB}"/>'+llave+f'<path fill="{INK}" d="{do}"/>',lab('bi'),dk,anim)
OUT['sello-horizontal-animado']=A(False); OUT['sello-horizontal-animado-oscuro']=A(True)
# --- vertical bilingüe: icono arriba, texto centrado
cx=90
v1,_=centrado('HECHO EN',17,cx,166); v2,_=centrado('MADE IN',17,cx,188); v3,w3=centrado('OAXACA',44,cx,234,850,75,48,0.5)
V=lambda dk: doc(180,246,k2(cx,72,44,'v')+f'<path fill="{INK}" d="{v1}"/><path fill="{TXT}" d="{v2}"/><path fill="{INK}" d="{v3}"/>',lab('bi'),dk)
OUT['sello-vertical']=V(False); OUT['sello-vertical-oscuro']=V(True)
# --- un idioma
for lang,frase in (('es','HECHO EN'),('en','MADE IN')):
    d1,w1=texto(frase,22,X,58,800,78,48,1.4); d2,w2=texto('OAXACA',48,X-2,108,850,75,48,0.5)
    for dk in (False,True):
        OUT[f'sello-{lang}'+('-oscuro' if dk else '')]=doc(X+max(w1,w2)+6,140,k2(55,70,44,lang)+f'<path fill="{TXT}" d="{d1}"/><path fill="{INK}" d="{d2}"/>',lab(lang),dk)
# --- icono suelto
OUT['icono']=doc(110,140,k2(55,70,44,'i'),lab('bi')); OUT['icono-oscuro']=doc(110,140,k2(55,70,44,'i'),lab('bi'),True)
for k,v in OUT.items(): open(f'svg/{k}.svg','w').write(v)
print(len(OUT),'svg')
