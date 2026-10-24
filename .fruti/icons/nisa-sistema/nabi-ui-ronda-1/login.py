DIV=['Aguas','Agrícolas','Ambiental','Bebidas','Alimentos','Farmacia','Bebidas de agave','Consultoría']
def plate(cols=8,rows=6,cell=46,r=17,ink='#fff',dot='rgba(255,255,255,.35)'):
    on=set((1,y) for y in range(rows))|set((6,y) for y in range(rows))|{(2,1),(3,2),(4,3),(5,4)}
    s=''
    for c in range(cols):
        for y in range(rows):
            cx=cell/2+c*cell; cy=cell/2+y*cell
            if (c,y)==(6,0): s+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#C2D225"/>'
            elif (c,y) in on: s+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ink}"/>'
            else: s+=f'<circle cx="{cx}" cy="{cy}" r="4" fill="{dot}"/>'
    return f'<svg width="{cols*cell}" height="{rows*cell}" viewBox="0 0 {cols*cell} {rows*cell}" style="display:block">{s}</svg>'
def fld_line(l,v,t='text'):
    return f'<label style="display:grid;gap:6px"><span class="ov">{l}</span><input value="{v}" type="{t}" style="border:0;border-bottom:1.5px solid var(--tx);padding:8px 0;font:17px Archivo;color:var(--tx);outline:0;background:transparent"></label>'
def fld_box(l,v,t='text'):
    return f'<label style="display:grid;gap:6px"><span style="font:500 13px Archivo">{l}</span><input value="{v}" type="{t}" style="height:44px;border:1px solid #858DA3;border-radius:8px;padding:0 12px;font:15px Archivo;color:var(--tx)"></label>'
def form(style='line'):
    f=fld_line if style=='line' else fld_box
    return ('<form style="display:grid;gap:22px;width:360px">'+f('Correo','m.ruiz@nisanabani.mx')+f('Contraseña','••••••••••','password')+
     '<button type="button" style="height:46px;border:0;border-radius:6px;background:var(--az);color:#fff;font:600 15px Archivo;display:flex;align-items:center;justify-content:space-between;padding:0 18px">Entrar <span aria-hidden="true">→</span></button>'
     '<a style="font-size:14px;color:var(--az);text-decoration:underline;text-underline-offset:3px">¿Olvidaste tu contraseña?</a></form>')
def LA():
    divs=''.join(f'<span style="display:flex;gap:8px;align-items:center;font-size:14px"><span class="pz" style="width:8px;height:8px;background:var(--az)"></span>{d}</span>' for i,d in enumerate(DIV))
    left=(f'<section style="padding:44px 56px;display:grid;grid-template-rows:auto 1fr auto;border-right:1px solid var(--ln)">{logo("lockup-familia",44)}'
      f'<div style="align-self:center;display:grid;gap:28px"><h1 class="x" style="margin:0;font-size:68px;line-height:70px;color:var(--az)">Calidad para el desarrollo empresarial<span style="color:var(--pe)">.</span></h1>'
      f'<div style="display:grid;grid-template-columns:repeat(4,auto);gap:10px 28px;justify-content:start">{divs}</div></div>'
      '<span class="m mu" style="font-size:12px">Nisa Nabani · sistema de laboratorio · v1.0</span></section>')
    right=f'<section style="display:grid;place-items:center;padding:40px"><div style="display:grid;gap:30px"><div><span class="ov">Acceso</span><h2 class="x" style="margin:6px 0 0;font-size:30px;line-height:34px">Inicia sesión</h2></div>{form("line")}</div></section>'
    return f'<div style="display:grid;grid-template-columns:7fr 5fr;min-height:820px">{left}{right}</div>'
def LB():
    left=(f'<section style="background:var(--az);color:#fff;padding:44px 52px;display:grid;grid-template-rows:auto 1fr auto;overflow:hidden;position:relative">{logo("lockup-h-blanco",34)}'
      f'<div style="position:absolute;right:44px;top:150px">{plate()}</div>'
      '<div style="align-self:end;display:grid;gap:10px;position:relative"><h1 class="x" style="margin:0;font-size:46px;line-height:50px;max-width:520px">Cada muestra, en su lugar.</h1><p style="margin:0;color:#C9D3EC;max-width:460px">Recepción, análisis, revisión y certificado en un solo sistema.</p></div>'
      '<span class="m" style="font-size:12px;color:#AFC0E3;margin-top:28px">Un sistema de Nisa Nabani</span></section>')
    right=f'<section style="display:grid;place-items:center;padding:40px"><div style="display:grid;gap:26px"><h2 class="x" style="margin:0;font-size:28px;line-height:32px;color:var(--az)">Inicia sesión</h2>{form("box")}</div></section>'
    return f'<div style="display:grid;grid-template-columns:7fr 5fr;min-height:820px">{left}{right}</div>'
def LC():
    return (f'<div style="min-height:820px;background:var(--sk);display:grid;grid-template-rows:56px 1fr 48px"><header style="background:var(--az);display:flex;align-items:center;padding:0 32px">{logo("lockup-h-blanco",24)}</header>'
      f'<main style="display:grid;place-items:center"><div style="background:#fff;border:1px solid var(--ln);border-radius:12px;padding:36px 40px;display:grid;gap:24px;justify-items:start">{logo("carga",56)}<div><h2 class="x" style="margin:0;font-size:26px;line-height:30px;color:var(--az)">Inicia sesión</h2><p class="mu" style="margin:6px 0 0;font-size:14px">Usa tu cuenta del laboratorio.</p></div>{form("box")}</div></main>'
      '<footer class="m mu" style="display:flex;justify-content:space-between;align-items:center;padding:0 32px;font-size:12px"><span>Nisa Nabani</span><span>Calidad para el desarrollo empresarial</span></footer></div>')
