import json,os,sys,datetime
S=sys.argv[1]; F='/home/user/fruti-squad/.fruti/icons/nisa-sistema/nabi-final/'
ids={'simbolo.svg':'18a1e1a03e437685b3bf82bda6037aa1','simbolo-tinta.svg':'1eb1f4383665a117487d34a24468c339','simbolo-blanco.svg':'5bc4939f9aa0f943ed74a3cd87e923f7','wordmark.svg':'ebe63b37f78d79fa05e9bac3247e4e2a','wordmark-blanco.svg':'6b1d53d371f0719468c0b6e23e8034f2','lockup-h.svg':'7a1dbf9ca2424cafb0c2164b6b1182cf','lockup-h-blanco.svg':'800f980fbd3cd25994500a3bb7fbc154','lockup-familia.svg':'3534ef111e16fe05c60c372a3d61e030','lockup-v.svg':'0f6d988fd2e293d334cf7415f10cec81','favicon.svg':'89cacadb924feccc38c722f27cd59acb','app-icon.svg':'33764acad863aca77506517a2459fa3f','app-icon-maskable.svg':'276c10cf51876d764f20ef3c8e66cfce','carga.svg':'53e142ecc52182e4225c1419d007b881','icon-512.png':'a2ea7d4a10b50b57e6df7e98cb5071c4','carga.gif':'6358d06d47e59e7d479475ad1ab7587b'}
b=lambda n:f'/_blob/{ids[n]}'
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]; c=[v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4 for v in c]; return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
cr=lambda a,b_:round((max(lum(a),lum(b_))+0.05)/(min(lum(a),lum(b_))+0.05),1)
C=dict(bg='#FFFFFF',surface='#FFFFFF',sunken='#F4F6FA',text='#141B33',muted='#535B70',subtle='#646B80',border='#E2E5EC',control='#858DA3',primary='#052A76',hover='#021C52',psoft='#E8EDF7',pera='#C2D225',perasoft='#F2F6CF',ok='#006D53',oksoft='#DFF2EC',onok='#004A38',bad='#B42318',badsoft='#FDE7E5',onbad='#8A1A12',warn='#8A4B00',warnfill='#F48C06',warnsoft='#FEF0DA',onwarn='#6E3C00',info='#3D67AE',infosoft='#E6EDF8',oninfo='#234A8C')
chk={k:cr(a,c) for k,(a,c) in {'text/bg':(C['text'],C['bg']),'muted/bg':(C['muted'],C['bg']),'subtle/sunken':(C['subtle'],C['sunken']),'control/bg':(C['control'],C['bg']),'primary/bg':(C['primary'],C['bg']),'white/primary':('#FFFFFF',C['primary']),'pera/primary':(C['pera'],C['primary']),'primary/pera':(C['primary'],C['pera']),'ok/bg':(C['ok'],C['bg']),'onok/oksoft':(C['onok'],C['oksoft']),'bad/bg':(C['bad'],C['bg']),'onbad/badsoft':(C['onbad'],C['badsoft']),'warn/bg':(C['warn'],C['bg']),'onwarn/warnsoft':(C['onwarn'],C['warnsoft']),'info/bg':(C['info'],C['bg']),'oninfo/infosoft':(C['oninfo'],C['infosoft']),'primary/psoft':(C['primary'],C['psoft']),'text/perasoft':(C['text'],C['perasoft'])}.items()}
print(chk)
os.chdir('project')
def t(n,v,u): return {'name':n,'value':v,'usage':u}
tokens={'name':'Nabi','version':1,
'color':{'themes':[{'id':'light','name':'Claro'}],'tokens':[
 t('bg',C['bg'],'Fondo de página. El sistema es de tema claro: denso, para escanear y comparar registros.'),
 t('surface',C['surface'],'Tarjetas, tablas y paneles; se separan con «border», sin sombra.'),
 t('surface-sunken',C['sunken'],'Encabezados de tabla, filas alternas, campos de solo lectura.'),
 t('text',C['text'],f"Texto principal. {chk['text/bg']}:1 sobre «bg»."),
 t('text-muted',C['muted'],f"Metadatos, ayudas, encabezados de columna. {chk['muted/bg']}:1."),
 t('text-subtle',C['subtle'],f"Placeholders. {chk['subtle/sunken']}:1 sobre «surface-sunken»."),
 t('border',C['border'],'Línea de 1 px entre filas y tarjetas. Decorativa.'),
 t('border-control',C['control'],f"Bordes de campos y casillas: {chk['control/bg']}:1."),
 t('primary',C['primary'],f"Azul real de Nisa Nabani: acción primaria, enlaces, foco, encabezado. {chk['primary/bg']}:1 sobre blanco."),
 t('primary-hover',C['hover'],'Hover y presionado de «primary».'),
 t('on-primary','#FFFFFF',f"Texto sobre «primary»: {chk['white/primary']}:1."),
 t('primary-soft',C['psoft'],f"Fila seleccionada, filtro activo; texto en «primary» ({chk['primary/psoft']}:1)."),
 t('pera',C['pera'],f"La muestra: el pocillo del símbolo, la muestra activa, el marcador de selección. Nunca texto (1.7:1 sobre blanco). Sobre azul, {chk['pera/primary']}:1."),
 t('pera-soft',C['perasoft'],f"Fondo del registro en curso; texto encima en «text» ({chk['text/perasoft']}:1)."),
 t('on-pera',C['primary'],f"Texto sobre «pera»: {chk['primary/pera']}:1."),
 t('focus','{primary}','Anillo de foco de 2 px, desplazado 2 px. Sobre «primary», el anillo va en «pera».'),
 t('conforme',C['ok'],f"Resultado dentro de especificación, muestra liberada. Verde del laboratorio. {chk['ok/bg']}:1. Siempre con icono y texto."),
 t('conforme-soft',C['oksoft'],'Fondo de estado conforme.'),
 t('on-conforme-soft',C['onok'],f"Texto sobre «conforme-soft»: {chk['onok/oksoft']}:1."),
 t('fuera',C['bad'],f"Resultado fuera de especificación, muestra rechazada. {chk['bad/bg']}:1. Siempre con icono y texto."),
 t('fuera-soft',C['badsoft'],'Fondo de estado fuera de especificación.'),
 t('on-fuera-soft',C['onbad'],f"Texto sobre «fuera-soft»: {chk['onbad/badsoft']}:1."),
 t('alerta',C['warn'],f"Cerca del límite o en revisión. {chk['warn/bg']}:1 como texto."),
 t('alerta-fill',C['warnfill'],'Naranja del laboratorio: solo relleno de marcadores e indicadores. Nunca texto.'),
 t('alerta-soft',C['warnsoft'],'Fondo de alerta.'),
 t('on-alerta-soft',C['onwarn'],f"Texto sobre «alerta-soft»: {chk['onwarn/warnsoft']}:1."),
 t('pendiente',C['info'],f"Pendiente, en análisis, información. Azul secundario del laboratorio. {chk['info/bg']}:1."),
 t('pendiente-soft',C['infosoft'],'Fondo de estado pendiente.'),
 t('on-pendiente-soft',C['oninfo'],f"Texto sobre «pendiente-soft»: {chk['oninfo/infosoft']}:1.")]},
'type':{'fonts':[],'families':{'display':'"Archivo", system-ui, sans-serif','sans':'"Archivo", system-ui, -apple-system, "Segoe UI", sans-serif','datos':'"IBM Plex Mono", ui-monospace, Menlo, monospace'},
 'groups':[
  {'name':'Títulos','family':'display','note':'Archivo 700 al 125 % de ancho (font-stretch: 125%), la misma familia del wordmark. Solo en títulos.','styles':[
   {'name':'display','fontSize':'30px','lineHeight':'36px','fontWeight':700,'letterSpacing':'-0.01em','sample':'Lote 2026-10-147','usage':'Una por pantalla: encabezado de lote o de certificado. font-stretch 125%.'},
   {'name':'title-1','fontSize':'22px','lineHeight':'28px','fontWeight':700,'sample':'Resultados del análisis','usage':'Título de sección. font-stretch 125%.'},
   {'name':'title-2','fontSize':'16px','lineHeight':'22px','fontWeight':600,'sample':'Fisicoquímicos','usage':'Título de tarjeta, panel y diálogo. Ancho normal.'}]},
  {'name':'Interfaz','family':'sans','note':'Archivo 400, 500 y 600 a ancho normal (100 %). Todo el texto de la interfaz.','styles':[
   {'name':'body','fontSize':'15px','lineHeight':'22px','fontWeight':400,'sample':'Muestra de agua potable, toma en garrafón de 20 L.','usage':'Texto corrido y descripciones.'},
   {'name':'label','fontSize':'13px','lineHeight':'18px','fontWeight':500,'sample':'Parámetro','usage':'Etiquetas de campo, encabezados de columna, pestañas.'},
   {'name':'button','fontSize':'14px','lineHeight':'20px','fontWeight':600,'sample':'Liberar resultados','usage':'Botones. 40 px de alto en escritorio, 44 px en táctil.'},
   {'name':'caption','fontSize':'12px','lineHeight':'16px','fontWeight':400,'sample':'Capturado por M. Ruiz','usage':'Metadatos y ayudas, en «text-muted».'},
   {'name':'overline','fontSize':'11px','lineHeight':'16px','fontWeight':600,'letterSpacing':'0.08em','sample':'ESPECIFICACIÓN','usage':'Etiqueta en versalitas sobre un valor.'}]},
  {'name':'Valores y resultados','family':'datos','note':'IBM Plex Mono con cero con barra (font-feature-settings: "zero"). Todo número que se mide, compara o copia: resultados, límites, unidades, folios, lotes, fechas y horas de análisis.','styles':[
   {'name':'valor-xl','fontSize':'32px','lineHeight':'36px','fontWeight':500,'sample':'7.42','usage':'Resultado protagonista en la ficha de un parámetro.'},
   {'name':'valor','fontSize':'14px','lineHeight':'20px','fontWeight':500,'sample':'0.012 mg/L','usage':'Resultados en tablas y tarjetas; alineados a la derecha.'},
   {'name':'valor-sm','fontSize':'12px','lineHeight':'16px','fontWeight':400,'sample':'6.5 – 8.5','usage':'Especificación, límites (LD, LC) e incertidumbre junto al valor.'},
   {'name':'folio','fontSize':'13px','lineHeight':'18px','fontWeight':500,'letterSpacing':'0.02em','sample':'NN-26-00417','usage':'Identificadores de muestra, lote y certificado.'}]}]},
'spacing':{'tokens':[t(f'space-{n}',f'{v}px',u) for n,v,u in [(1,4,'Icono–texto, dentro de chips.'),(2,8,'Entre controles relacionados; padding vertical de celda.'),(3,12,'Padding horizontal de celda y chip.'),(4,16,'Padding de tarjeta; gutter en móvil.'),(5,20,'Entre campos.'),(6,24,'Entre secciones de una pantalla.'),(8,32,'Entre bloques mayores.')]]},
'radius':{'tokens':[t('radius-sm','6px','Chips, casillas, botones.'),t('radius-md','8px','Campos, tarjetas, avisos.'),t('radius-lg','12px','Diálogos y paneles laterales.'),t('radius-pill','999px','Pocillos, puntos de estado, avatar.')]},
'sizing':{'tokens':[t('control-h','40px','Alto de botones y campos en escritorio.'),t('control-h-touch','44px','Alto mínimo en táctil.'),t('row-h','40px','Alto de fila de tabla.'),t('icon','18px','Iconos en línea.'),t('pozo','10px','Diámetro del pocillo de estado en tablas.')]},
'shadow':{'tokens':[t('shadow-overlay','0 12px 32px rgba(5, 42, 118, 0.16)','Solo menús, diálogos y paneles que flotan. Las tarjetas no llevan sombra.')]},
'motion':{'tokens':[t('quick','150ms','Hover, foco.'),t('paso-carga','200ms','Cada paso de la muestra pera en la animación de carga.'),t('ease-out','cubic-bezier(0.2, 0.8, 0.2, 1)','Entradas de paneles.')]}}
json.dump(tokens,open('tokens.json','w'),indent=1,ensure_ascii=False)
open('README.md','w').write(f'''# Nabi

Nabi es el sistema de laboratorio de Nisa Nabani: recepción de muestras, lotes, ensayos, captura y revisión de resultados, y certificados. Lo usan analistas, supervisores de calidad y personal de recepción, casi siempre en escritorio, durante toda la jornada. La interfaz es densa y funcional: se escanea y se compara, no se contempla.

![Lockup de Nabi]({b('lockup-familia.svg')})

## Principios

- **El dato manda.** Cada pantalla tiene un valor o un estado protagonista; todo lo demás se subordina. La marca vive en el encabezado, la carga y los documentos, no en las tablas.
- **Dos voces tipográficas.** Archivo habla (títulos, etiquetas, texto); IBM Plex Mono mide (resultados, límites, unidades, folios). Si un número se mide, se compara o se copia, va en Plex Mono. Ver la sección «Valores y resultados».
- **Una sola muestra pera.** El pera marca lo que está en curso: la muestra activa, la fila seleccionada, el pocillo del símbolo. Si hay dos cosas en pera, una sobra.
- **Nada depende solo del color.** Conforme, fuera de especificación, alerta y pendiente llevan icono y texto, además de color.
- **Tema claro.** El sistema no tiene tema oscuro.

## Contenido y tono

Preciso, breve, sin adornos. Los botones dicen la acción y el objeto: Registrar muestra, Capturar resultado, Liberar lote, Emitir certificado. Los errores dicen qué pasó y cómo corregirlo: «El resultado está fuera del intervalo del método (0.005–10 mg/L). Revisa la dilución.» Términos del laboratorio sin traducir: LD, LC, lote, alícuota, especificación, método.

## Color

Los primarios de Nisa Nabani ordenan la interfaz; los secundarios del laboratorio dan los estados.

- `primary` (azul real #052A76) es la acción primaria, los enlaces y el encabezado. `primary-soft` para la fila seleccionada.
- `pera` (#C2D225) es la muestra: el pocillo del símbolo y la muestra activa. Nunca texto sobre blanco (1.7:1). `pera-soft` para el registro en curso.
- Estados de resultado: `conforme` (verde del laboratorio #006D53), `fuera` (#B42318), `alerta` (texto #8A4B00; el naranja del laboratorio #F48C06 solo como relleno) y `pendiente` (azul secundario #3D67AE). Cada uno con su fondo `*-soft` y su texto `on-*-soft`.
- Contrastes verificados: todo texto ≥ 4.5:1 sobre su fondo; `border-control` {chk['control/bg']}:1.

## Tipografía

- **Archivo** (`display`, `sans`). Una sola familia variable en dos anchos: 125 % y 700 en `display` y `title-1`, la misma voz del wordmark; ancho normal en todo lo demás. 15 px de cuerpo para pantallas densas.
- **IBM Plex Mono** (`datos`). Para valores y resultados de análisis. Cifras de ancho fijo, para que las columnas se alineen solas; cero con barra (`font-feature-settings: "zero"`) para no confundir 0 con O; tiene µ, ±, ×, ≤, ≥, ° y superíndices.
- Las dos se cargan de Google Fonts: `Archivo:wdth,wght@62..125,100..900` y `IBM Plex Mono:wght@400;500;600`.

## Espacio, forma y elevación

Escala de 4 px. Filas de tabla de 40 px (`row-h`), controles de 40 px en escritorio y 44 px en táctil. Radios contenidos: 6, 8 y 12 px; la píldora solo para pocillos y puntos de estado. Sin sombras en tarjetas; solo lo que flota lleva `shadow-overlay`.

## Movimiento

La carga es el símbolo: la muestra pera recorre la N, 200 ms por paso (`paso-carga`). Con `prefers-reduced-motion` se detiene en el pocillo final. Todo lo demás es `quick` (150 ms).

![Carga]({b('carga.gif')})

## Iconografía y marca

- Iconos de trazo de 1.75 px a 18 px (`icon`), en el color del texto que acompañan.
- El pocillo es el átomo gráfico: los estados en tablas se marcan con un pocillo de 10 px (`pozo`) del color del estado, junto al texto.
- Símbolo, wordmark y lockups en la sección «Marca» y en el grupo de assets «Marca».

## Pendiente

- La interfaz actual del producto usa Verdant WebKit con acento esmeralda. Este sistema propone el azul y pera de Nisa Nabani; falta decidir si sustituye el acento de Verdant o si convive con él.
- Los nombres de estado de muestra (Recibida, En análisis, En revisión, Liberada, Rechazada) son una propuesta: confirmar con el flujo real del laboratorio.
''')
open('valores.md','w').write('''# Valores y resultados

La segunda fuente existe para una sola cosa: que un resultado se lea, se compare y se copie sin error. Todo valor analítico va en **IBM Plex Mono** con cero con barra.

## Qué va en Plex Mono

- Resultados y lecturas: `7.42`, `0.012`, `1.2 × 10³`.
- Unidades junto al valor: `mg/L`, `UFC/100 mL`, `°Bx`, `% v/v`, `µS/cm`.
- Especificaciones y límites: `6.5 – 8.5`, `≤ 0.010`, `LD 0.002`, `LC 0.005`.
- Incertidumbre: `7.42 ± 0.05`.
- Identificadores: muestra `NN-26-00417`, lote `L-2026-10-147`, certificado `CER-26-0091`.
- Fechas y horas de análisis en tablas: `2026-10-24 09:42`.

Los nombres de parámetro (pH, Plomo, Coliformes totales), los métodos (NMX-AA-008-SCFI-2016) y el texto corrido van en Archivo.

## Cómo se escriben

- **Decimales:** los que reporta el método, nunca los que da el cálculo. El punto es el separador decimal.
- **Alineación:** en tablas, valores a la derecha; con cifras de ancho fijo los decimales quedan en columna.
- **Debajo del límite:** `< 0.002` (menor que el LD), no `0` ni «ND» a secas; si el informe usa ND, `ND (LD 0.002)`.
- **Unidad:** separada del valor por un espacio, en `text-muted` en tablas; en la ficha, el valor en `valor-xl` y la unidad en `valor`.
- **Notación científica:** `1.2 × 10³`, con signo de multiplicar real y superíndice; nunca `1.2E3` en la interfaz.
- **Rangos:** guion medio con espacios: `6.5 – 8.5`.
- **Estado:** el color nunca va solo. Fuera de especificación lleva icono, texto «Fuera» y el valor en `fuera`; conforme lleva icono y texto «Conforme».

## Estilos

| Estilo | Uso |
|---|---|
| `valor-xl` 32/36 | Resultado protagonista en la ficha de un parámetro |
| `valor` 14/20 | Resultados en tablas y tarjetas |
| `valor-sm` 12/16 | Especificación, LD/LC, incertidumbre |
| `folio` 13/18 | Muestra, lote, certificado |
''')
open('marca.md','w').write(f'''# Marca

Nabi es marca de familia de Nisa Nabani. Su símbolo es una placa de 4 × 4 pocillos: los llenos dibujan la N, los vacíos quedan como puntos y la muestra pera ocupa el pocillo superior derecho.

![Lockup]({b('lockup-h.svg')})

## Piezas

| Pieza | Uso | Archivo |
|---|---|---|
| Símbolo | Encabezado, carga, sellos | `simbolo.svg` · `simbolo-tinta.svg` · `simbolo-blanco.svg` |
| Favicon | 16–32 px: solo la N, sin vacíos | `favicon.svg` |
| Wordmark | «nabi» en Archivo 700 al 125 %, pocillo pera en la i | `wordmark.svg` · `wordmark-blanco.svg` |
| Lockup horizontal | Barra superior del sistema | `lockup-h.svg` · `lockup-h-blanco.svg` |
| De familia | Certificados, documentos para clientes, portada | `lockup-familia.svg` |
| Vertical | Pantalla de acceso | `lockup-v.svg` |
| App icon | PWA | `app-icon.svg` · `app-icon-maskable.svg` · `icon-512.png` |
| Carga | Indicador animado | `carga.svg` · `carga.gif` |

## Reglas

- Área de respeto: un pocillo alrededor de toda pieza.
- No mover, quitar ni añadir pocillos; una sola muestra pera.
- En certificados y documentos para clientes, siempre el lockup de familia.
''')
HEAD='''<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@400;500;600&display=swap"><style>
html,body{margin:0} body{background:var(--bg,#FFFFFF);color:var(--text,#141B33);font-family:var(--font-sans,"Archivo",system-ui,sans-serif);font-size:15px;line-height:22px;padding:var(--space-4,16px);display:flex;gap:var(--space-3,12px);flex-wrap:wrap;align-items:center}
.d{font-family:var(--font-datos,"IBM Plex Mono",monospace);font-feature-settings:"zero"} .mut{color:var(--text-muted,#535B70)}
.btn{display:inline-flex;align-items:center;gap:8px;min-height:var(--control-h,40px);padding:0 16px;border-radius:var(--radius-sm,6px);font:600 14px/20px var(--font-sans,"Archivo",sans-serif);border:1px solid transparent;cursor:pointer}
.btn:focus-visible{outline:2px solid var(--focus,#052A76);outline-offset:2px}
.b-primary{background:var(--primary,#052A76);color:var(--on-primary,#fff)} .b-secondary{background:var(--surface,#fff);color:var(--primary,#052A76);border-color:var(--border-control,#858DA3)} .b-ghost{background:transparent;color:var(--primary,#052A76)} .b-danger{background:var(--surface,#fff);color:var(--fuera,#B42318);border-color:var(--fuera,#B42318)}
.ico{width:16px;height:16px;display:block;flex:none}
.est{display:inline-flex;align-items:center;gap:6px;padding:3px 10px 3px 8px;border-radius:var(--radius-sm,6px);font:500 13px/18px var(--font-sans,"Archivo",sans-serif)}
.e-ok{background:var(--conforme-soft,#DFF2EC);color:var(--on-conforme-soft,#004A38)} .e-bad{background:var(--fuera-soft,#FDE7E5);color:var(--on-fuera-soft,#8A1A12)} .e-warn{background:var(--alerta-soft,#FEF0DA);color:var(--on-alerta-soft,#6E3C00)} .e-pend{background:var(--pendiente-soft,#E6EDF8);color:var(--on-pendiente-soft,#234A8C)} .e-cur{background:var(--pera-soft,#F2F6CF);color:var(--text,#141B33)} .e-neu{background:var(--surface-sunken,#F4F6FA);color:var(--text-muted,#535B70)}
.pz{width:10px;height:10px;border-radius:50%;flex:none;display:inline-block}
</style></head><body>'''
I={'ok':'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>',
   'bad':'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 7v6M12 17h.01"/><circle cx="12" cy="12" r="9"/></svg>',
   'warn':'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
   'pend':'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
   'copy':'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V5a1 1 0 0 1 1-1h9"/></svg>'}
est=lambda cls,ic,txt:f'<span class="est {cls}">{I[ic]}{txt}</span>'
carga=open(F+'svg/carga.svg').read().replace('<svg ','<svg width="56" height="56" ')
comps={
'Boton':('Actions',88,'<button class="btn b-primary">Liberar resultados</button><button class="btn b-secondary">Capturar resultado</button><button class="btn b-ghost">Ver historial</button><button class="btn b-danger">Rechazar muestra</button>',
 'Botón de acción: el primario va en azul real; los destructivos en borde «fuera».\n\n- `primary`: «primary» con «on-primary». Una acción principal por vista: Liberar resultados, Registrar muestra, Emitir certificado.\n- `secondary`: fondo «surface», borde «border-control», texto «primary». `ghost`: solo texto en «primary». `danger`: borde y texto «fuera», siempre con confirmación y motivo.\n- 40 px de alto (`control-h`), 44 px en táctil. Radio `radius-sm`. Texto `button` en Archivo. Foco: anillo de 2 px en «focus».\n- El pera no es color de botón.\n- El consumidor provee: verbo + objeto, estado de carga (con la animación de carga a 16 px) y `aria-disabled`.'),
'Campo':('Forms',190,'<div style="display:grid;gap:6px;min-width:220px"><label for="a" style="font:500 13px/18px Archivo,sans-serif">Descripción de la muestra</label><input id="a" value="Agua de pozo, toma 1" style="height:40px;border:1px solid var(--border-control,#858DA3);border-radius:var(--radius-md,8px);padding:0 12px;font:15px Archivo,sans-serif;color:var(--text,#141B33)"><small class="mut" style="font-size:12px">Como aparecerá en el certificado.</small></div><div style="display:grid;gap:6px;min-width:200px"><label for="b" style="font:500 13px/18px Archivo,sans-serif">Plomo (Pb)</label><div style="display:flex;align-items:center;height:40px;border:1px solid var(--fuera,#B42318);border-radius:var(--radius-md,8px);padding:0 12px;gap:8px"><input id="b" class="d" value="0.0124" style="border:0;outline:0;font-size:15px;width:100%;text-align:right;color:var(--text,#141B33);font-family:inherit"><span class="d mut" style="font-size:13px">mg/L</span></div><small style="font-size:12px;color:var(--fuera,#B42318)">Fuera de especificación: máximo <span class="d">0.010</span>.</small></div>',
 'Campo de captura. El texto va en Archivo; el valor de un resultado se escribe en Plex Mono, alineado a la derecha, con la unidad fija al final.\n\n- 40 px de alto, borde «border-control», radio `radius-md`. Etiqueta `label` arriba; ayuda `caption` abajo.\n- Campo de resultado: `datos` a 15 px, `text-align: right`, unidad como sufijo en «text-muted». Acepta solo el número; la unidad la pone el método.\n- Validación contra la especificación al salir del campo: borde y mensaje en «fuera» con el límite escrito en `datos`. No bloquea la captura: un resultado fuera se registra y se marca.\n- El consumidor provee: etiqueta (parámetro y símbolo), unidad, especificación, decimales del método y el `id`.'),
'ResultadoAnalisis':('Data display',230,f'''<div style="display:grid;grid-template-columns:repeat(3,minmax(170px,1fr));gap:12px;width:100%">
<div style="border:1px solid var(--border,#E2E5EC);border-radius:var(--radius-md,8px);padding:14px;display:grid;gap:6px"><span style="font:600 16px/22px Archivo,sans-serif">pH</span><span><span class="d" style="font-size:32px;line-height:36px;font-weight:500">7.42</span> <span class="d mut" style="font-size:12px">± 0.05</span></span><span class="d mut" style="font-size:12px">ESP 6.5 – 8.5</span>{est('e-ok','ok','Conforme')}</div>
<div style="border:1px solid var(--border,#E2E5EC);border-radius:var(--radius-md,8px);padding:14px;display:grid;gap:6px"><span style="font:600 16px/22px Archivo,sans-serif">Plomo (Pb)</span><span><span class="d" style="font-size:32px;line-height:36px;font-weight:500;color:var(--fuera,#B42318)">0.0124</span> <span class="d mut" style="font-size:14px">mg/L</span></span><span class="d mut" style="font-size:12px">ESP ≤ 0.010</span>{est('e-bad','bad','Fuera de especificación')}</div>
<div style="border:1px solid var(--border,#E2E5EC);border-radius:var(--radius-md,8px);padding:14px;display:grid;gap:6px"><span style="font:600 16px/22px Archivo,sans-serif">Arsénico (As)</span><span><span class="d" style="font-size:32px;line-height:36px;font-weight:500">&lt; 0.002</span> <span class="d mut" style="font-size:14px">mg/L</span></span><span class="d mut" style="font-size:12px">LD 0.002 · ESP ≤ 0.025</span>{est('e-ok','ok','Conforme')}</div></div>''',
 'Ficha de un parámetro: el resultado es el protagonista, en Plex Mono grande, con su especificación y su estado.\n\n- Nombre del parámetro en `title-2` (Archivo). Valor en `valor-xl` (Plex Mono 32/36, cero con barra); unidad e incertidumbre en `valor` o `valor-sm` y «text-muted».\n- Especificación y límites (ESP, LD, LC) en `valor-sm`.\n- Estado con icono y texto: Conforme (`conforme-soft`), Fuera de especificación (`fuera-soft`, y el valor en «fuera»), Alerta (`alerta-soft`), Pendiente (`pendiente-soft`).\n- Debajo del límite de detección: «< LD» con el LD escrito, nunca 0.\n- El consumidor provee: parámetro, valor con los decimales del método, unidad, incertidumbre si aplica, especificación, LD/LC y estado.'),
'TablaResultados':('Data display',300,f'''<div style="width:100%;overflow-x:auto"><table style="border-collapse:collapse;width:100%;min-width:640px;font-size:14px"><thead><tr style="background:var(--surface-sunken,#F4F6FA);color:var(--text-muted,#535B70);font:500 13px/18px Archivo,sans-serif;text-align:left"><th style="padding:8px 12px">Parámetro</th><th style="padding:8px 12px">Método</th><th style="padding:8px 12px;text-align:right">Resultado</th><th style="padding:8px 12px">Unidad</th><th style="padding:8px 12px;text-align:right">Especificación</th><th style="padding:8px 12px">Estado</th></tr></thead><tbody>
'''+''.join(f'<tr style="border-bottom:1px solid var(--border,#E2E5EC);{bg}"><td style="padding:9px 12px">{p}</td><td style="padding:9px 12px;font-size:13px" class="mut">{m}</td><td class="d" style="padding:9px 12px;text-align:right;{vc}">{v}</td><td class="d mut" style="padding:9px 12px;font-size:13px">{u}</td><td class="d mut" style="padding:9px 12px;text-align:right;font-size:13px">{e}</td><td style="padding:9px 12px"><span style="display:inline-flex;align-items:center;gap:6px;font-size:13px"><span class="pz" style="background:{pc}"></span>{s}</span></td></tr>' for p,m,v,u,e,s,pc,vc,bg in [
 ('pH','NMX-AA-008','7.42','—','6.5 – 8.5','Conforme','var(--conforme,#006D53)','',''),
 ('Conductividad','NMX-AA-093','412.0','µS/cm','≤ 1500.0','Conforme','var(--conforme,#006D53)','',''),
 ('Plomo (Pb)','NMX-AA-051','0.0124','mg/L','≤ 0.0100','Fuera','var(--fuera,#B42318)','color:var(--fuera,#B42318);font-weight:600',''),
 ('Arsénico (As)','NMX-AA-051','&lt; 0.0020','mg/L','≤ 0.0250','Conforme','var(--conforme,#006D53)','',''),
 ('Coliformes totales','NMX-AA-042','1.2 × 10³','NMP/100 mL','&lt; 1.1','Fuera','var(--fuera,#B42318)','color:var(--fuera,#B42318);font-weight:600',''),
 ('Dureza total','NMX-AA-072','—','mg/L CaCO₃','≤ 500.0','En análisis','var(--pera,#C2D225)','color:var(--text-muted,#535B70)','background:var(--pera-soft,#F2F6CF)')])+'</tbody></table></div>',
 'Tabla de resultados de una muestra: nombres en Archivo, valores en Plex Mono alineados a la derecha.\n\n- Encabezado en `label` sobre «surface-sunken»; filas de 40 px (`row-h`) separadas por «border».\n- Resultado y especificación en `valor` / `valor-sm` (Plex Mono), a la derecha: con cifras de ancho fijo y los mismos decimales, el punto decimal queda en columna.\n- Unidad en su propia columna, en «text-muted».\n- Estado: pocillo de 10 px (`pozo`) del color del estado + texto. Fuera de especificación también pone el valor en «fuera» y en 600.\n- La fila que se está capturando lleva fondo «pera-soft» y pocillo pera: es la muestra activa.\n- El consumidor provee: filas con parámetro, método, valor, unidad, especificación y estado; los decimales que fija cada método.'),
'EstadoMuestra':('Feedback',96,est('e-neu','pend','Recibida')+est('e-pend','pend','En análisis')+est('e-warn','warn','En revisión')+est('e-ok','ok','Liberada')+est('e-bad','bad','Rechazada')+est('e-cur','pend','En captura'),
 'Estado de una muestra o lote: icono + texto sobre el fondo suave del estado.\n\n- Recibida (neutro), En análisis (`pendiente-soft`), En revisión (`alerta-soft`), Liberada (`conforme-soft`), Rechazada (`fuera-soft`). En captura (`pera-soft`) marca la muestra en la que se trabaja ahora: solo una a la vez.\n- Nunca solo color: icono y palabra siempre.\n- Los nombres son una propuesta; deben coincidir con los estados del flujo real del laboratorio.\n- El consumidor provee: el estado y, si aplica, quién y cuándo lo cambió (en `caption`).'),
'IdMuestra':('Data display',96,f'<span style="display:inline-flex;align-items:center;gap:10px;border:1px solid var(--border,#E2E5EC);border-radius:var(--radius-sm,6px);padding:6px 10px"><span class="mut" style="font:600 11px/16px Archivo,sans-serif;letter-spacing:.08em">MUESTRA</span><span class="d" style="font-size:13px;font-weight:500;letter-spacing:.02em">NN-26-00417</span><button class="btn b-ghost" aria-label="Copiar folio" style="min-height:28px;padding:0 6px">{I["copy"]}</button></span><span style="display:inline-flex;align-items:center;gap:10px;border:1px solid var(--border,#E2E5EC);border-radius:var(--radius-sm,6px);padding:6px 10px"><span class="mut" style="font:600 11px/16px Archivo,sans-serif;letter-spacing:.08em">LOTE</span><span class="d" style="font-size:13px;font-weight:500;letter-spacing:.02em">L-2026-10-147</span></span><span style="display:inline-flex;align-items:center;gap:10px;border:1px solid var(--border,#E2E5EC);border-radius:var(--radius-sm,6px);padding:6px 10px"><span class="mut" style="font:600 11px/16px Archivo,sans-serif;letter-spacing:.08em">CERTIFICADO</span><span class="d" style="font-size:13px;font-weight:500;letter-spacing:.02em">CER-26-0091</span></span>',
 'Identificador de muestra, lote o certificado: etiqueta en versalitas (Archivo) y folio en Plex Mono, copiable.\n\n- Etiqueta en `overline`; folio en `folio` (Plex Mono 13/18, cero con barra, tracking 0.02em) para que 0 y O, 1 e I nunca se confundan.\n- Botón de copiar en las vistas donde el folio se pega en otro sistema.\n- El consumidor provee: tipo, folio y si es copiable. El formato del folio lo define el laboratorio; los de ejemplo son ilustrativos.'),
'Carga':('Feedback',110,f'<span style="display:inline-flex;align-items:center;gap:14px">{carga}<span><b style="font:600 15px/22px Archivo,sans-serif">Procesando lote</b><br><span class="d mut" style="font-size:13px">L-2026-10-147 · 12 de 18 muestras</span></span></span>',
 'Indicador de carga y proceso: el símbolo de Nabi con la muestra pera recorriendo la N.\n\n- 10 pasos de 200 ms (`paso-carga`), en bucle. Con `prefers-reduced-motion` se detiene en el último pocillo.\n- A 56 px en estados de carga de página o de proceso largo, con texto de qué se procesa y el avance en `datos`. A 16–20 px dentro de botones.\n- No usar un spinner genérico en el sistema.\n- El consumidor provee: el texto de la tarea y, si se conoce, el avance.')}
for name,(grp,h,body,md) in comps.items():
    os.makedirs(f'components/{name}',exist_ok=True)
    open(f'components/{name}/preview.html','w').write(f'<!-- @dsCard group="{grp}" height={h} -->\n{HEAD}{body}</body></html>')
    open(f'components/{name}/README.md','w').write(f'# {name}\n\n{md}\n')
sym=open(F+'svg/simbolo.svg').read().replace('#052A76','var(--primary, #052A76)').replace('#C2D225','var(--pera, #C2D225)')
wm=open(F+'svg/lockup-familia.svg').read().replace('#052A76','var(--primary, #052A76)').replace('#C2D225','var(--pera, #C2D225)')
os.makedirs('components/Cover',exist_ok=True)
open('components/Cover/preview.html','w').write(f'''<!-- @dsCard height=288 -->
<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=IBM+Plex+Mono:wght@500&display=swap"><style>
html,body{{margin:0;height:100%}} body{{background:var(--bg,#FFFFFF);color:var(--text,#141B33);font-family:var(--font-sans,"Archivo",system-ui,sans-serif);overflow:hidden}}
.cover{{position:relative;height:288px;overflow:hidden}}
.art{{position:absolute;top:22px;right:32px;width:244px;height:244px}} .art svg{{width:100%;height:100%;display:block}}
.words{{position:absolute;left:var(--space-6,24px);bottom:var(--space-6,24px);display:grid;gap:12px;max-width:440px}} .wm svg{{width:300px;height:auto;display:block}}
.tag{{margin:0;font-size:14px;line-height:20px;color:var(--text-muted,#535B70)}} .tag .d{{font-family:"IBM Plex Mono",monospace;font-feature-settings:"zero";color:var(--text,#141B33)}}
</style></head><body><div class="cover"><div class="art" aria-hidden="true">{sym}</div><div class="words"><div class="wm" role="img" aria-label="nabi, de Nisa Nabani">{wm}</div><p class="tag">Sistema de laboratorio · muestras, lotes, resultados, certificados · <span class="d">pH 7.42 ± 0.05</span></p></div></div></body></html>''')
files={}
for n,i in ids.items():
    p=F+('png/' if n.endswith(('.png','.gif')) else 'svg/')+n
    files[n]={'name':n,'blob':i,'size':os.path.getsize(p),'type':{'svg':'image/svg+xml','png':'image/png','gif':'image/gif'}[n.rsplit('.',1)[1]]}
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump({'v':3,'layout':'files','createdOnFiles':{'v':1,'at':now},'title':'Nabi','namespace':'Nabi','libraries':[],'sections':{},'groups':['Marca'],
 'assetGroups':{'Marca':{'name':'Marca','tile':'m','order':list(ids),'files':files}},'blobs':{},'docs':{'readme':'project/README.md','sections':[]},
 'lastChange':{'at':now,'by':'Kevin','via':'Claude Code','note':'Sistema inicial de Nabi: azul y pera de Nisa Nabani, Archivo para interfaz e IBM Plex Mono para valores y resultados, estados de análisis y siete componentes.'}},open('design-system.json','w'),indent=2,ensure_ascii=False)
print(sorted(os.listdir('components')))
