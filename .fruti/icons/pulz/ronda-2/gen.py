# PULZ · ronda 2: abstractos (lote, recurso, movimiento; cortes de destilación). Lienzo 64.
MAGUEY='#2f5d58'; COBRE='#b4582f'; CAL='#f4efe6'; TIERRA='#2a211c'
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="PULZ">{body}</svg>\n'
V={}
# Z · movimiento: dos recursos (barras) y el movimiento (diagonal en cobre) que los une
V['z-movimiento']=svg(f'<rect x="10" y="10" width="44" height="11" rx="2.5" fill="{TIERRA}"/><rect x="10" y="43" width="44" height="11" rx="2.5" fill="{TIERRA}"/>'
                      f'<path d="M48.5 21 15.5 43" stroke="{COBRE}" stroke-width="11" stroke-linecap="butt"/>')
# Cortes: puntas, corazón, colas. El corazón (lo que se guarda) es la banda gruesa de cobre
V['cortes']=svg(f'<rect x="10" y="10" width="44" height="7" rx="3.5" fill="{TIERRA}"/><rect x="10" y="22" width="44" height="20" rx="6" fill="{COBRE}"/><rect x="10" y="47" width="44" height="7" rx="3.5" fill="{TIERRA}"/>')
# Primitivas: recurso (cuadrado), lote (círculo de cobre) y movimiento (diagonal) en una sola composición
V['primitivas']=svg(f'<rect x="8" y="8" width="30" height="30" rx="4" fill="{MAGUEY}"/><circle cx="43" cy="43" r="13" fill="{COBRE}"/>'
                    f'<path d="M32 32 52 12" stroke="{TIERRA}" stroke-width="7" stroke-linecap="round"/><path d="M44 12h8v8" fill="none" stroke="{TIERRA}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
for k,s in V.items(): open(f'{k}.svg','w').write(s)
def img(f,h): return f'<img src="{f}" style="height:{h}px">'
def tile(f,h,bg): return f'<span style="display:inline-flex;width:{h}px;height:{h}px;border-radius:{h*.22}px;background:{bg};align-items:center;justify-content:center">{img(f,h*.7)}</span>'
rows=''.join(f'<section style="display:flex;gap:18px;align-items:center;padding:14px 18px;border-bottom:1px solid #e3dccf"><b style="width:100px;font:600 12px sans-serif;color:#6b5d50">{k}</b>{img(k+".svg",112)}{img(k+".svg",48)}{img(k+".svg",24)}{img(k+".svg",16)}{tile(k+".svg",64,"#fff")}{tile(k+".svg",64,TIERRA)}<span style="display:inline-flex;gap:6px;align-items:center;font:600 13px sans-serif;color:{TIERRA};border:1px solid #e3dccf;border-radius:999px;padding:4px 10px 4px 6px;background:#fff">{img(k+".svg",18)}hecho con PULZ</span></section>' for k in V)
open('banco.html','w').write(f'<html><body style="margin:0;background:{CAL}">{rows}</body></html>')
