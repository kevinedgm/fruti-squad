# Laranda · sistema de reseñas, calificación y guardados, con la dirección A del design system.
import sys,math
S=sys.argv[1]
INK='#111013'; MUTED='#5C5A61'; LINE='#E4E3E0'; SUNK='#F3F3F1'; VIO='#5B3BB5'; VSOFT='#EFEBFA'; NAR='#E0611A'; NART='#F2C9B2'; ORO='#D9A400'; VERDE='#0E8F5E'; VSOFT2='#DCF3E8'; ONV='#0B5E3E'
def svg(b,vb='0 0 128 128',w=None): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" fill="none"{f" width={chr(34)}{w}{chr(34)}" if w else ""}>{b}</svg>'
# la flor de cinco lóbulos como calificación: n lóbulos llenos (violeta), el resto solo contorno; el quinto, el separado, va en naranja
def florcal(n,size=20,k=VIO):
    b=''
    for i in range(5):
        a=math.radians(-126+i*72); cx,cy=64+20*math.cos(a),66+20*math.sin(a)
        if i==1: cx+=5; cy-=5
        lleno=i<n
        if i==1 and n==5: b+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="15" fill="{NAR}"/>'
        elif lleno: b+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="15" fill="{k}"/>'
        else: b+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="13.5" stroke="{k}" stroke-width="3"/>'
    b+=f'<circle cx="64" cy="66" r="7" fill="#fff" stroke="{k}" stroke-width="3"/>'
    return svg(b,w=size).replace('width=',f'height="{size}" width=')
# el lóbulo suelto como «guardar»: contorno (no guardado) → relleno naranja (guardado)
def lobulo(on,size=22):
    attr=f'fill="{NAR}"' if on else f'stroke="{INK}" stroke-width="5"'
    return svg(f'<path d="M70 20 C78 14 92 18 96 30 C98 40 90 48 80 46 C72 44 66 32 70 20Z" transform="translate(-133 -10) scale(2.4)" {attr}/>',w=size).replace('width=',f'height="{size}" width=')
sil=open('/home/user/fruti-squad/.fruti/icons/laranda/final/svg/silueta.svg').read().replace('viewBox','width="22" height="22" viewBox')
css=f'''@font-face{{font-family:BR;src:url("file://{S}/fuentes/BricolageGrotesque[opsz,wdth,wght].ttf");font-weight:200 800}} @font-face{{font-family:ON;src:url("file://{S}/fuentes/Onest.ttf");font-weight:100 900}} @font-face{{font-family:PM;src:url("file://{S}/fuentes/IBMPlexMono.ttf");font-weight:500}}
body{{margin:0;padding:28px;background:#E9E9E7;color:{INK};font:14px/1.45 ON,system-ui;width:1200px;box-sizing:border-box}} .sub{{margin:0 0 14px;color:#333}}
.g{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}} .c{{background:#fff;border:1px solid {LINE};border-radius:8px;padding:16px;display:grid;gap:12px;align-content:start}} h2{{font:700 15px ON;margin:0}} .ov{{font:500 11px/16px ON;letter-spacing:.08em;text-transform:uppercase;color:{MUTED}}} .nota{{font:400 12px ON;color:{MUTED}}}
svg{{display:block}} .row{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.big{{font:700 40px/1 BR;letter-spacing:-.01em}} .mid{{font:700 22px/1.1 BR}}
.card{{border:1px solid {LINE};border-radius:8px;padding:12px;display:grid;gap:8px}} .meta{{font:400 12px ON;color:{MUTED}}} .tag{{display:inline-flex;align-items:center;gap:4px;font:600 12px ON;padding:3px 8px;border:1px solid {LINE};border-radius:6px}} .tag.on{{border-color:{VIO};color:{VIO};background:{VSOFT}}}
.sello{{display:inline-flex;align-items:center;gap:6px;font:500 12px ON;color:{ONV};background:{VSOFT2};padding:3px 8px;border-radius:6px}} .sello svg{{width:14px;height:14px}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 16px;border-radius:6px;font:700 15px ON;border:1px solid transparent}} .prim{{background:{INK};color:#fff}} .sec{{border-color:{INK}}} .ghost{{color:{VIO}}} .si{{background:{INK};color:#fff}} .no{{border-color:{INK}}}
.guardar{{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 12px;border:1px solid {INK};border-radius:6px;font:600 14px ON}} .guardar.on{{border-color:{NAR};background:{NART};color:{INK}}}
.paso{{display:grid;gap:8px;border-top:1px solid {LINE};padding-top:10px}} .paso b{{font:700 16px BR}}
.barra{{height:8px;background:{SUNK};border-radius:4px;overflow:hidden}} .barra i{{display:block;height:100%;background:{VIO}}}
.lista{{display:grid;gap:0}} .lista .it{{display:flex;gap:10px;align-items:center;padding:10px 0;border-top:1px solid {LINE}}} .av{{width:40px;height:40px;border-radius:50%;background:#D9D6CF;flex:none}}
.mono{{font:500 12px PM;color:{MUTED}}}
'''
def resena(nombre,fecha,n,tags,txt,vuelve=True):
    t=''.join(f'<span class="tag">{x}</span>' for x in tags)
    return f'<div class="card"><div class="row" style="justify-content:space-between"><div class="row">{florcal(n,18)}<b>{n} de 5</b></div><span class="sello">{sil.replace(VIO,ONV)}con folio</span></div><p style="margin:0">{txt}</p><div class="row">{t}</div><div class="meta">{nombre} · {fecha} · {"volvió a reservar" if vuelve else "primera cita"}</div></div>'
html=f'''<!doctype html><meta charset="utf-8"><style>{css}</style><p class="sub">Laranda · reseñas, calificación y guardados · propuesta con el design system (dirección A). La calificación es la flor: cinco lóbulos, y el quinto, el que se abre, solo con 5. La métrica principal es «vuelven». Guardar es el lóbulo suelto.</p>
<div class="g">
<div class="c"><h2>1 · La flor como calificación</h2><span class="nota">Cinco lóbulos en vez de cinco estrellas. Se llenan de uno en uno; el quinto es el lóbulo que se abre y solo se enciende con 5. El número siempre va escrito al lado: nunca solo la forma.</span>
<div class="row">{florcal(1,36)}{florcal(2,36)}{florcal(3,36)}{florcal(4,36)}{florcal(5,36)}</div>
<div class="row"><span class="mono">1 de 5</span><span class="mono">2 de 5</span><span class="mono">3 de 5</span><span class="mono">4 de 5</span><span class="mono">5 de 5 · florece</span></div>
<div class="row" style="margin-top:6px">{florcal(4,16)}<span><b>4.8</b> <span class="meta">· 128 reseñas</span></span></div>
<div class="row">{florcal(5,16)}<b>5 de 5</b> <span class="meta">en línea, 16 px</span></div>
<span class="ov">Para calificar (al tocar)</span><div class="row">{florcal(0,40)}{florcal(0,40)}{florcal(0,40)}{florcal(0,40)}{florcal(0,40)}</div><span class="nota">Cinco flores vacías, 44 px de objetivo cada una; al tocar la cuarta se llenan las cuatro. Con teclado: flechas y número.</span></div>

<div class="c"><h2>2 · «Vuelven»: la métrica propia</h2><span class="nota">Lo que un oficio quiere demostrar es que la gente regresa. Se calcula sola con las citas: clientes con dos o más folios entre todos los clientes de los últimos 12 meses. No depende de que nadie escriba nada.</span>
<div><span class="ov">De cada 10 clientes</span><div class="big">9 vuelven</div><div class="meta">87 % con dos o más citas · últimos 12 meses · 128 citas</div></div>
<div class="barra"><i style="width:87%"></i></div>
<div class="card"><span class="ov">Cómo se ve en la tarjeta</span><div class="row"><b class="mid">Andrés Cortés</b></div><div class="row">{florcal(5,16)}<b>4.9</b><span class="meta">· 128</span><span class="meta">·</span><b>9 de 10 vuelven</b></div></div>
<div class="card" style="background:{SUNK};border-color:{SUNK}"><span class="ov">Antes de tener datos</span><div class="row">{sil.replace(VIO,MUTED)}<span class="meta">Nuevo en Laranda · 3 citas</span></div><span class="nota">Sin «vuelven» hasta 10 clientes distintos; sin promedio hasta 3 reseñas. Nunca un 0 ni un 5.0 con una sola reseña.</span></div></div>

<div class="c"><h2>3 · Guardar: el lóbulo suelto</h2><span class="nota">Sin corazón ni estrella. Guardar es el lóbulo que se abre: contorno cuando no, relleno naranja cuando sí. Los guardados viven en «Mis oficios», una lista de personas a las que vuelves.</span>
<div class="row"><span class="guardar">{lobulo(False)}Guardar</span><span class="guardar on">{lobulo(True)}Guardado</span></div>
<span class="nota">Al guardar, el lóbulo se despega 150 ms y se rellena. Con «reducir movimiento», cambia sin moverse.</span>
<span class="ov">Mis oficios</span>
<div class="lista"><div class="it"><span class="av"></span><div style="flex:1"><b>Andrés Cortés</b><div class="meta">Barbería · Centro · 9 de 10 vuelven</div></div>{lobulo(True,18)}</div><div class="it"><span class="av"></span><div style="flex:1"><b>Mariana Ruiz</b><div class="meta">Colorista · Reforma · última cita 3 oct</div></div>{lobulo(True,18)}</div><div class="it"><span class="av"></span><div style="flex:1"><b>Laura Méndez</b><div class="meta">Podología · Reforma</div></div>{lobulo(True,18)}</div></div>
<div class="row"><span class="btn prim">Reservar de nuevo</span></div><span class="nota">En la lista, la acción es volver a reservar: para eso se guarda.</span></div>
</div>

<div class="g" style="margin-top:18px">
<div class="c"><h2>4 · Reseñar: 20 segundos después de la cita</h2><span class="nota">Solo quien tuvo folio puede reseñar; la reseña lleva el sello «con folio». Tres pasos, los dos primeros con un toque.</span>
<div class="paso"><span class="ov">Paso 1</span><b>¿Volverías con Andrés?</b><div class="row"><span class="btn si">Sí, vuelvo</span><span class="btn no">No</span></div></div>
<div class="paso"><span class="ov">Paso 2 · ¿Qué salió bien?</span><div class="row"><span class="tag on">Puntual</span><span class="tag on">Como lo pedí</span><span class="tag">Limpio</span><span class="tag">Buen trato</span><span class="tag">Buen precio</span><span class="tag">Explica</span></div></div>
<div class="paso"><span class="ov">Paso 3 · opcional</span><div class="card" style="background:{SUNK};border-color:{SUNK}"><span class="meta">Cuéntale a otros clientes, si quieres.</span></div><div class="row"><span class="btn prim">Publicar reseña</span><span class="btn ghost">Ahora no</span></div></div>
<span class="nota">La calificación de 1 a 5 se deriva: «Sí» con tres o más etiquetas = 5; «Sí» = 4; «No» con etiquetas = 2; «No» = 1. Quien quiera afinar, toca las flores. Así la mayoría califica sin pensar en números.</span></div>

<div class="c"><h2>5 · La reseña publicada</h2>
{resena('Luis G.','18 oct',5,['Puntual','Como lo pedí','Explica'],'Me atendió a la hora y el degradado quedó justo como lo pedí. Ya tengo la siguiente cita.')}
{resena('Ana P.','9 oct',4,['Buen trato','Limpio'],'Buen corte. El local estaba lleno y esperé 10 minutos.',False)}
<div class="card" style="border-color:{VIO}"><span class="ov" style="color:{VIO}">Respuesta de Andrés</span><p style="margin:0">Gracias, Ana. Ya abrí espacios de 15 minutos entre citas para que no pase.</p></div>
<span class="nota">El profesional responde una vez, en público. Las reseñas no se borran; se pueden reportar y se marcan «en revisión».</span></div>

<div class="c"><h2>6 · La primera reseña: florece</h2><span class="nota">Hito del negocio: la flor se abre con «bloom» y el perfil pasa a mostrar calificación.</span>
<div class="card" style="background:{VSOFT};border-color:{VSOFT}"><div class="row">{sil}<b style="color:{VIO}">Tu primera reseña</b></div><p style="margin:0">Luis G. te dio 5 de 5 y dice que vuelve. Tu perfil ya muestra tu calificación.</p><div class="row"><span class="btn prim">Ver reseña</span><span class="btn ghost">Compartir</span></div></div>
<span class="ov">Resumen en el perfil</span>
<div class="card"><div class="row" style="justify-content:space-between"><div><div class="big" style="font-size:32px">4.9</div><div class="row">{florcal(5,16)}<span class="meta">128 reseñas</span></div></div><div style="text-align:right"><div class="big" style="font-size:32px">9<span style="font-size:18px;color:{MUTED}">/10</span></div><div class="meta">vuelven</div></div></div>
<div class="row"><span class="tag">Puntual · 96</span><span class="tag">Como lo pedí · 88</span><span class="tag">Buen trato · 71</span></div></div>
<span class="nota">Las etiquetas agregadas dicen más que el promedio: cuántas veces se dijo cada cosa.</span></div>
</div>'''
open('propuesta.html','w').write(html); print('ok')
