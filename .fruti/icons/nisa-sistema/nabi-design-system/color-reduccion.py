import re,sys,glob,os,json
root=sys.argv[1]; extra=sys.argv[2:]
M={'surface-sunken':'bg','surface-hover':'bg','text-subtle':'text-muted','border-strong':'border','on-primary':'surface','pera-soft':'primary-soft','on-pera':'primary','focus':'primary',
 'on-fuera-soft':'fuera','on-alerta-soft':'alerta','alerta-fill':'alerta','pendiente':'text-muted','pendiente-soft':'bg','on-pendiente-soft':'text-muted',
 'muestra-no-ingresada':'alerta-soft','on-muestra-no-ingresada':'alerta','muestra-en-proceso':'primary-soft','on-muestra-en-proceso':'primary',
 'muestra-generando-informe':'primary-soft','on-muestra-generando-informe':'primary','muestra-terminada':'conforme-soft','on-muestra-terminada':'on-conforme-soft',
 'muestra-cancelada':'fuera-soft','on-muestra-cancelada':'fuera','pago-no-pagada':'fuera','pago-parcial':'alerta','pago-pagada':'conforme','pago-cortesia':'primary'}
HEX={'bg':'#F2F4F8','surface':'#FFFFFF','text-muted':'#535B70','border':'#DFE3EC','primary':'#052A76','primary-soft':'#E8EDF7','fuera':'#B42318','fuera-soft':'#FDE7E5',
 'alerta':'#8A6100','alerta-soft':'#FBF0CC','conforme':'#2E7D32','conforme-soft':'#E3F1E4','on-conforme-soft':'#1E5A22'}
pat=re.compile(r'var\(--('+'|'.join(sorted(map(re.escape,M),key=len,reverse=True))+r')(\s*,[^()]*)?\)')
def rep(m):
    n=M[m.group(1)]; return f'var(--{n},{HEX[n]})' if m.group(2) else f'var(--{n})'
fs=glob.glob(os.path.join(root,'components/*/preview.html'))+[os.path.join(root,x) for x in extra]
tot=0
for f in fs:
    s=open(f).read(); s2,k=pat.subn(rep,s)
    if k: open(f,'w').write(s2); tot+=k; print(k,os.path.relpath(f,root))
print('total',tot)

# ---- tokens.json: quita los colores unidos y actualiza el uso de los que quedan (2026-11-05, revisión ds-color-r01 aprobada)
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
cr=lambda a,b:f'{(max(lum(a),lum(b))+.05)/(min(lum(a),lum(b))+.05):.1f}:1'
tp=os.path.join(root,'tokens.json'); d=json.load(open(tp)); T=d['color']['tokens']
if any(t['name'] in M for t in T):
    T[:]=[t for t in T if t['name'] not in M]
    U={
     'bg':f"Lienzo de la página. También: encabezado de tabla, hover de fila, campos de solo lectura y deshabilitados (borde de campo encima {cr('#858DA3','#F2F4F8')}), avatar inactivo y fondo de «Pendiente». Texto encima: «text» {cr('#141B33','#F2F4F8')}, «text-muted» {cr('#535B70','#F2F4F8')}. Nunca blanco sobre blanco: las superficies se separan de él con borde y sombra.",
     'surface':"Tarjetas, tablas, paneles y campos. También el texto y los íconos sobre «primary» (blanco, 13.1:1).",
     'text-muted':f"Metadatos, ayudas, encabezados de columna, placeholders y el estado «Pendiente» (con reloj y texto). {cr('#535B70','#FFFFFF')} sobre blanco, {cr('#535B70','#F2F4F8')} sobre «bg».",
     'border':"Filete de 1 px entre filas, alrededor de tarjetas, chips y pozos vacíos. Decorativo.",
     'primary':"Azul real de Nisa Nabani: acción primaria, enlaces, encabezado, «Cortesía» y texto sobre «pera» (7.8:1). Anillo de foco de 2 px desplazado 2 px; sobre «primary», el anillo va en «pera». 13.1:1 sobre blanco.",
     'primary-soft':"Selección, filtro activo, registro en curso (con filete «pera») y las etapas «En proceso» y «Generando informe» (las distingue el ícono de avance). Texto encima en «primary» (11.2:1).",
     'pera':"La célula que creció del símbolo Colonia, lo que está en curso (filete o punto) y la marca «Urgente» (texto en «primary», 7.8:1). Nunca texto sobre blanco (1.7:1). Una sola cosa pera por pantalla.",
     'conforme':"Resultado dentro de especificación, «Completo», «Firmado» y la etiqueta de pago «Pagada». 5.1:1 sobre blanco. Siempre con ícono y texto.",
     'conforme-soft':"Fondo de conforme y de la etapa «Terminada».",
     'on-conforme-soft':"Texto sobre «conforme-soft»: 7.1:1. Necesario porque «conforme» encima mide 4.4:1.",
     'fuera':"Fuera de especificación, rechazo, etapa «Cancelada», pago «No pagada» y botón destructivo. 6.6:1 sobre blanco; 5.5:1 sobre «fuera-soft». Siempre con ícono y texto.",
     'fuera-soft':"Fondo de fuera, rechazo y «Cancelada».",
     'alerta':"Cerca del límite, en revisión, destiempo, etapa «No ingresada» y pago «Pago parcial». 5.5:1 sobre blanco; 4.9:1 sobre «alerta-soft». También marcadores e indicadores.",
     'alerta-soft':"Fondo de alerta y de «No ingresada».",
    }
    for t in T:
        if t['name'] in U: t['usage']=U[t['name']]
    open(tp,'w').write(json.dumps(d,indent=1,ensure_ascii=False)+'\n')
print('colores:',len(T))
