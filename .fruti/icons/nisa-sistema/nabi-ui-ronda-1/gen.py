import sys
S=sys.argv[1]; F='/home/user/fruti-squad/.fruti/icons/nisa-sistema/nabi-final/svg/'
sv=lambda n:open(F+n+'.svg').read()
def logo(n,h): return sv(n).replace('<svg ','<svg height="%s" '%h)
FONTS=f"@font-face{{font-family:'Archivo';src:url('file://{S}/fuentes/ArchivoVar.ttf');font-weight:100 900;font-stretch:62% 125%}}@font-face{{font-family:'Plex';src:url('file://{S}/fuentes/IBMPlexMono.ttf')}}"
BASE=FONTS+''':root{--az:#052A76;--pe:#C2D225;--pes:#F2F6CF;--tx:#141B33;--mu:#535B70;--ln:#E2E5EC;--sk:#F4F6FA;--ok:#006D53;--bad:#B42318;--pend:#3D67AE}
*{box-sizing:border-box}body{margin:0;background:#fff;color:var(--tx);font:15px/22px Archivo,sans-serif;width:1280px}
.m{font-family:Plex,monospace;font-feature-settings:"zero"}.mu{color:var(--mu)}.ov{font:600 11px/16px Archivo;letter-spacing:.09em;text-transform:uppercase;color:var(--mu)}
.x{font-stretch:125%;font-weight:700;letter-spacing:-.01em}.pz{display:inline-block;width:10px;height:10px;border-radius:50%;flex:none}
table{border-collapse:collapse;width:100%}td,th{text-align:left}
'''
R=[('pH','NMX-AA-008','7.42','—','6.5 – 8.5',(6.5,8.5,0,14,7.42),'ok','Conforme'),
   ('Conductividad','NMX-AA-093','412.0','µS/cm','≤ 1500.0',(0,1500,0,2000,412),'ok','Conforme'),
   ('Plomo (Pb)','NMX-AA-051','0.0124','mg/L','≤ 0.0100',(0,0.01,0,0.015,0.0124),'bad','Fuera'),
   ('Arsénico (As)','NMX-AA-051','< 0.0020','mg/L','≤ 0.0250',(0,0.025,0,0.035,0.002),'ok','Conforme'),
   ('Coliformes totales','NMX-AA-042','1.2 × 10³','NMP/100 mL','< 1.1',(0,1.1,0,1.6,99),'bad','Fuera'),
   ('Dureza total','NMX-AA-072','—','mg/L CaCO₃','≤ 500.0',None,'cur','En análisis')]
COL={'ok':'var(--ok)','bad':'var(--bad)','cur':'var(--pe)'}
def ruler(r,w=150,dark=False):
    if not r: return f'<span class="mu" style="font-size:12px">pendiente</span>'
    lo,hi,a,b,v=r; X=lambda q:max(0,min(w,(q-a)/(b-a)*w)); out=v>b
    band=f'<rect x="{X(lo):.1f}" y="5" width="{X(hi)-X(lo):.1f}" height="6" rx="3" fill="{"rgba(255,255,255,.22)" if dark else "#E3E8F2"}"/>'
    base=f'<rect x="0" y="7" width="{w}" height="2" rx="1" fill="{"rgba(255,255,255,.25)" if dark else "#E2E5EC"}"/>'
    vx=w-5 if out else X(v); ok=lo<=v<=hi
    mk=f'<circle cx="{vx:.1f}" cy="8" r="5" fill="{"#C2D225" if ok else "#B42318"}" stroke="#fff" stroke-width="1.5"/>'
    arr=f'<path d="M{w+2} 4 l5 4 -5 4z" fill="#B42318"/>' if out else ''
    return f'<svg width="{w+10}" height="16" viewBox="0 0 {w+10} 16" style="display:block">{base}{band}{mk}{arr}</svg>'
STEPS=['Recepción','Análisis','Revisión','Certificado']
def steps(cur=1,dark=False,vertical=False):
    c_done='#fff' if dark else 'var(--az)'; c_todo='rgba(255,255,255,.35)' if dark else '#C9CFDC'
    items=''
    for i,s in enumerate(STEPS):
        col='var(--pe)' if i==cur else (c_done if i<cur else c_todo)
        txt=('#fff' if dark else 'var(--tx)') if i<=cur else ('rgba(255,255,255,.6)' if dark else 'var(--mu)')
        items+=f'<div style="display:flex;align-items:center;gap:10px;color:{txt};font-size:14px"><span class="pz" style="width:14px;height:14px;background:{col}"></span>{s}</div>'
    d='grid;gap:14px' if vertical else 'flex;gap:28px'
    return f'<div style="display:{d}">{items}</div>'
meta=[('Cliente','Agua Purificada del Valle'),('Recepción','2026-10-24 09:12'),('Lote','L-2026-10-147'),('Matriz','Agua potable')]
def val_color(st): return 'color:var(--bad);font-weight:600' if st=='bad' else ''
# ---------- A · Hoja de placa
def A():
    top=f'<header style="display:flex;align-items:center;justify-content:space-between;padding:18px 40px;border-bottom:1px solid var(--ln)"><div style="height:30px">{logo("lockup-h",30)}</div><span class="m mu" style="font-size:13px">Muestras / Agua / <b style="color:var(--tx)">NN-26-00417</b></span></header>'
    hd=f'<section style="padding:34px 40px 26px;display:grid;gap:18px"><span class="ov">Muestra · agua potable</span><div style="display:flex;align-items:baseline;gap:22px"><h1 class="x" style="margin:0;font-size:46px;line-height:50px;color:var(--az)">Agua de pozo, toma 1</h1><span class="m" style="font-size:20px">NN-26-00417</span></div>{steps(1)}</section>'
    mt='<section style="display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--tx);border-bottom:1px solid var(--ln);margin:0 40px">'+''.join(f'<div style="padding:12px 0;{"border-left:1px solid var(--ln);padding-left:16px" if i else ""}"><div class="ov">{k}</div><div class="{"m" if k in ("Recepción","Lote") else ""}" style="font-size:15px">{v}</div></div>' for i,(k,v) in enumerate(meta))+'</section>'
    big='<section style="display:grid;grid-template-columns:repeat(3,1fr);margin:28px 40px 0">'+''.join(f'<div style="padding:4px 24px 8px;{"border-left:1px solid var(--ln)" if i else "padding-left:0"}"><div class="ov">{p}</div><div class="m" style="font-size:58px;line-height:66px;{val_color(st)}">{v}<span style="font-size:16px;color:var(--mu)"> {u if u!="—" else ""}</span></div><div style="display:flex;gap:14px;align-items:center;font-size:13px"><span class="m mu">ESP {e}</span><span style="display:inline-flex;gap:6px;align-items:center"><span class="pz" style="background:{COL[st]}"></span>{s}</span></div></div>' for i,(p,m,v,u,e,r,st,s) in enumerate([R[0],R[2],R[4]]))+'</section>'
    rows=''.join(f'<tr style="border-bottom:1px solid var(--ln);{"background:var(--pes)" if st=="cur" else ""}"><td style="padding:12px 0">{p}</td><td class="mu" style="font-size:13px">{m}</td><td class="m" style="text-align:right;{val_color(st)}">{v}</td><td class="m mu" style="font-size:13px;padding-left:14px">{u}</td><td class="m mu" style="text-align:right;font-size:13px">{e}</td><td style="padding-left:28px"><span style="display:inline-flex;gap:8px;align-items:center"><span class="pz" style="background:{COL[st]}"></span>{s}</span></td></tr>' for p,m,v,u,e,r,st,s in R)
    tb=f'<section style="margin:30px 40px 40px"><div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--tx);padding-bottom:8px"><h2 class="x" style="margin:0;font-size:22px;color:var(--az)">Resultados</h2><span class="m mu" style="font-size:13px">6 parámetros · 2 fuera</span></div><table><thead><tr class="ov"><th style="padding:10px 0">Parámetro</th><th>Método</th><th style="text-align:right">Resultado</th><th style="padding-left:14px">Unidad</th><th style="text-align:right">Especificación</th><th style="padding-left:28px">Estado</th></tr></thead><tbody>{rows}</tbody></table></section>'
    return top+hd+mt+big+tb
# ---------- B · Bloque azul
def B():
    side=f'''<aside style="background:var(--az);color:#fff;padding:28px 30px;display:grid;align-content:start;gap:26px;min-height:820px">
<div style="height:28px">{logo("lockup-h-blanco",28)}</div>
<div style="display:grid;gap:8px;margin-top:20px"><span class="ov" style="color:#AFC0E3">Muestra</span><span class="m" style="font-size:30px;line-height:34px;color:var(--pe)">NN-26-00417</span><h1 class="x" style="margin:0;font-size:30px;line-height:34px">Agua de pozo, toma 1</h1></div>
<div style="display:grid;gap:12px;border-top:1px solid rgba(255,255,255,.2);padding-top:18px">'''+''.join(f'<div><div class="ov" style="color:#AFC0E3">{k}</div><div class="{"m" if k in ("Recepción","Lote") else ""}">{v}</div></div>' for k,v in meta)+f'''</div>
<div style="border-top:1px solid rgba(255,255,255,.2);padding-top:18px">{steps(1,True,True)}</div></aside>'''
    rows=''.join(f'<tr style="border-bottom:1px solid var(--ln);{"background:var(--pes)" if st=="cur" else ""}"><td style="padding:14px 0 14px 4px;font-weight:500">{p}<div class="mu" style="font-size:12px;font-weight:400">{m}</div></td><td class="m" style="text-align:right;font-size:20px;{val_color(st)}">{v}</td><td class="m mu" style="font-size:13px;padding-left:12px">{u}</td><td style="padding-left:24px">{ruler(r)}</td><td class="m mu" style="font-size:13px">{e}</td><td><span style="display:inline-flex;gap:8px;align-items:center"><span class="pz" style="background:{COL[st]}"></span>{s}</span></td></tr>' for p,m,v,u,e,r,st,s in R)
    main=f'''<main style="padding:34px 40px;display:grid;gap:22px;align-content:start"><div style="display:flex;justify-content:space-between;align-items:end"><div><span class="ov">Resultados</span><h2 class="x" style="margin:4px 0 0;font-size:34px;line-height:38px;color:var(--az)">2 de 6 fuera de especificación</h2></div><button style="height:40px;padding:0 18px;border:0;border-radius:6px;background:var(--az);color:#fff;font:600 14px Archivo">Enviar a revisión</button></div>
<table><thead><tr class="ov" style="border-bottom:1px solid var(--tx)"><th style="padding:8px 4px">Parámetro</th><th style="text-align:right">Resultado</th><th style="padding-left:12px">Unidad</th><th style="padding-left:24px">Dentro de especificación</th><th>Esp.</th><th>Estado</th></tr></thead><tbody>{rows}</tbody></table></main>'''
    return f'<div style="display:grid;grid-template-columns:330px 1fr">{side}{main}</div>'
# ---------- C · Instrumento
def C():
    top=f'<header style="display:flex;align-items:center;gap:28px;padding:0 32px;height:56px;background:var(--az);color:#fff"><div style="height:24px">{logo("lockup-h-blanco",24)}</div><nav style="display:flex;gap:22px;font-size:14px;color:#C9D3EC;align-items:center;height:56px"><span>Recepción</span><span style="color:#fff;box-shadow:inset 0 -3px 0 var(--pe);padding:17px 0">Análisis</span><span>Revisión</span><span>Certificados</span></nav><span class="m" style="margin-left:auto;font-size:13px;color:#C9D3EC">L-2026-10-147 · 12/18</span></header>'
    hd=f'<section style="padding:22px 32px;display:flex;align-items:end;justify-content:space-between;border-bottom:1px solid var(--ln)"><div><span class="ov">Agua potable · Agua Purificada del Valle</span><div style="display:flex;gap:16px;align-items:baseline"><h1 class="x" style="margin:2px 0 0;font-size:32px;line-height:38px;color:var(--az)">Agua de pozo, toma 1</h1><span class="m" style="font-size:16px">NN-26-00417</span></div></div>{steps(1)}</section>'
    tiles=''
    for p,m,v,u,e,r,st,s in R:
        bd='var(--bad)' if st=='bad' else ('var(--pe)' if st=='cur' else 'var(--ln)')
        tiles+=f'<div style="border:1px solid var(--ln);{"border-top:3px solid "+bd if st!="ok" else "border-top:3px solid var(--ln)"};border-radius:8px;padding:16px 18px;display:grid;gap:10px;{"background:var(--pes)" if st=="cur" else ""}"><div style="display:flex;justify-content:space-between"><span style="font-weight:600">{p}</span><span style="display:inline-flex;gap:6px;align-items:center;font-size:13px"><span class="pz" style="background:{COL[st]}"></span>{s}</span></div><div class="m" style="font-size:40px;line-height:44px;{val_color(st)}">{v}<span style="font-size:14px;color:var(--mu)"> {u if u!="—" else ""}</span></div>{ruler(r,300)}<div style="display:flex;justify-content:space-between" class="m mu"><span style="font-size:12px">ESP {e}</span><span style="font-size:12px">{m}</span></div></div>'
    grid=f'<section style="padding:22px 32px 32px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;background:var(--sk)">{tiles}</section>'
    return top+hd+grid
for k,fn,name,desc in [('A',A,'Hoja de placa','Editorial y tipográfica: sin tarjetas, solo filetes; títulos anchos grandes, resultados protagonistas a 58 px y el proceso como fila de pocillos.'),('B',B,'Bloque azul','La identidad de la muestra vive en un panel azul a la izquierda, con folio en pera; a la derecha, la tabla con una regla de especificación por resultado.'),('C',C,'Instrumento','Cada parámetro es una lectura de instrumento: valor grande y una regla que muestra dónde cae frente a la especificación. Barra superior azul.')]:
    open(f'{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}</style></head><body>{fn()}</body></html>')
exec(open('login.py').read())
for k,fn in [('A',LA),('B',LB),('C',LC)]:
    open(f'login-{k}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}</style></head><body>{fn()}</body></html>')
print('ok')
