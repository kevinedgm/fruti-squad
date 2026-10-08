exec(open('gen.py').read().split('\nV={}')[0])
MAD='#b98e5e'
V={}
def mk(n,**k):
    b,sw=esfera(55,72,44,n); V[n]=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 144" role="img" aria-label="Hecho en Oaxaca">{b}{espiga(55,72,44,sw,**k)}</svg>\n'
mk('d0-actual',color=INK)
mk('e1-madera',color=MAD)
mk('e2-hueco',color=INK,hueco=.07)
mk('e3-madera-hueco',color=MAD,hueco=.07)
for k,s in V.items(): open(f'{k}.svg','w').write(s)
def r(f,h,bg,col): return f'<span style="display:inline-flex;padding:10px;background:{bg};color:{col};border-radius:10px">'+open(f).read().replace('<svg ',f'<svg height="{h}" ',1)+'</span>'
rows=''.join(f'<section style="display:flex;gap:14px;align-items:center;padding:12px 18px;border-bottom:1px solid #33261f"><b style="width:130px;font:600 12px sans-serif;color:#bfae9f">{k}</b>{r(k+".svg",120,"#1a1210","#fff8ee")}{r(k+".svg",48,"#1a1210","#fff8ee")}{r(k+".svg",28,"#1a1210","#fff8ee")}{r(k+".svg",48,"#000","#fff8ee")}</section>' for k in V)
open('banco-oscuro.html','w').write(f'<html><body style="margin:0;background:#120c0a">{rows}</body></html>')
