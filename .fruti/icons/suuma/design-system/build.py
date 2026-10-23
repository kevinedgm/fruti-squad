import json,os,sys,datetime
S=sys.argv[1]; F='/home/user/fruti-squad/.fruti/icons/suuma/final/'
ids={'simbolo.svg':'e7d0edbd77acfa940de3d694ae4b06ce','simbolo-tinta.svg':'6a03144e54c06e9cb63774a27f3dae2f','simbolo-blanco.svg':'09068b62bf49aed5fb83832d45b80f9a','wordmark.svg':'bea87782a5d98a6e072891f7fe55c49c','wordmark-oscuro.svg':'b536e145fefdac9cb844af8035139731','lockup-h.svg':'30d7f9a23e529153954322c52142ecc9','lockup-h-oscuro.svg':'6c042687573c60a9cc077e1f44e6c53f','lockup-v.svg':'8ad3f1f79ec11122d0b80c2f7eb27302','app-icon.svg':'ddc8141a4eab047baf21c71093f29fa7','app-icon-maskable.svg':'c55c45c6cc173e1daf3ee60aceed8b1c','avatar.svg':'db4becb4f59372b6bf17d5cbee21eec7','favicon.svg':'a518d0f1aca3f79f57138ccd35a4be3d','tarjeta-redes.svg':'552f6dc4643ec9f16edeb0399eb3777b','icon-512.png':'6a9c052f738f0ad94f968d0082a6c301','icon-192.png':'2359ae35b90b237cbfabd9f0ef1377e1'}
b=lambda n:f'/_blob/{ids[n]}'
os.chdir('project')
# ---- tokens
def ct(n,l,d,u): return {'name':n,'value':{'light':l,'dark':d},'usage':u}
tokens={'name':'SUUMA','version':1,
'color':{'themes':[{'id':'light','name':'Claro'},{'id':'dark','name':'Oscuro'}],'tokens':[
 ct('bg','#FFFFFF','#121212','Fondo de página: blanco. En oscuro, tinta.'),
 ct('surface','#FFFFFF','#1C1C1C','Tarjetas y hojas; se separan con «border», sin sombra.'),
 ct('surface-sunken','#F5F4F0','#262626','Papel: tablas, campos deshabilitados, zonas dentro de una tarjeta.'),
 ct('text','#121212','#F5F4F0','Texto principal. 18.7:1 sobre «bg».'),
 ct('text-muted','#5F5E5A','#B3B1AC','Metadatos, ayudas, versalitas. 6.5:1 sobre «bg».'),
 ct('text-subtle','#6B6A65','#8E8C87','Placeholders. 4.9:1 sobre «surface-sunken».'),
 ct('border','#E3E2DD','#333333','Línea fina de 1 px entre tarjetas y filas. Decorativa, no de control.'),
 ct('border-control','#8A8984','#777570','Bordes de campos y casillas: 3.5:1 sobre «bg».'),
 ct('primary','#121212','#F5F4F0','Acción primaria: botón en tinta con «on-primary». En oscuro, hueso.'),
 ct('on-primary','#FFFFFF','#121212','Texto sobre «primary».'),
 ct('cadmio','#FFD400','#FFD400','La nota de la marca: la u interior, destacados, chips activos, fondos con texto en tinta. Nunca texto ni borde de control (1.4:1 sobre blanco).'),
 ct('cadmio-soft','#FFF3B0','#3D3300','Fondo marcado: fila activa, aviso de marca, chip seleccionado; texto encima en «text».'),
 ct('on-cadmio','#121212','#121212','Texto sobre «cadmio»: 13.1:1.'),
 ct('focus','{text}','{cadmio}','Anillo de foco de 2 px, desplazado 2 px: tinta en claro, cadmio en oscuro.'),
 ct('success','#0E7C4A','#5FD39A','Éxito: confirmado, publicado. Siempre con icono y texto. 5.2:1 sobre «bg». Provisional.'),
 ct('success-soft','#DDF3E6','#10301F','Fondo de aviso de éxito; texto en «on-success-soft».'),
 ct('on-success-soft','#0A5A36','#B7EBCF','Texto sobre «success-soft».'),
 ct('danger','#C8102E','#FF7B8A','Error y cancelación. Siempre con icono y texto. 5.9:1 sobre «bg». Provisional.'),
 ct('danger-soft','#FBE1E4','#3A1216','Fondo de aviso de error.'),
 ct('on-danger-soft','#8E0B21','#FFC2C9','Texto sobre «danger-soft».')]},
'type':{'fonts':[],'families':{'display':'"Bricolage Grotesque", system-ui, sans-serif','sans':'"Onest", system-ui, -apple-system, "Segoe UI", sans-serif','mono':'"IBM Plex Mono", ui-monospace, Menlo, monospace'},
 'groups':[{'name':'Marca y títulos','family':'display','note':'Bricolage Grotesque 600; 700 solo en display grande. Tamaño óptico según el cuerpo.','styles':[
   {'name':'display','fontSize':'34px','lineHeight':'38px','fontWeight':700,'letterSpacing':'-0.015em','sample':'Tu talento, nuevas posibilidades.','usage':'Una por pantalla: cabecera, bienvenida.'},
   {'name':'title-1','fontSize':'24px','lineHeight':'30px','fontWeight':600,'letterSpacing':'-0.01em','sample':'Mariana Ruiz','usage':'Nombre del profesional, título de sección.'},
   {'name':'title-2','fontSize':'18px','lineHeight':'24px','fontWeight':600,'sample':'Disponible esta semana','usage':'Título de tarjeta y de diálogo.'}]},
  {'name':'Interfaz','family':'sans','note':'Onest 400, 500 y 700. Todo el cuerpo y los controles.','styles':[
   {'name':'body','fontSize':'16px','lineHeight':'24px','fontWeight':400,'sample':'Corte, color y tratamientos. Col. Roma, CDMX.','usage':'Texto corrido. 16 px mínimo en móvil.'},
   {'name':'overline','fontSize':'11px','lineHeight':'16px','fontWeight':500,'letterSpacing':'0.08em','sample':'PRÓXIMO ESPACIO','usage':'Etiquetas en versalitas sobre un dato, en «text-muted».'},
   {'name':'label','fontSize':'14px','lineHeight':'20px','fontWeight':500,'sample':'Fecha de la cita','usage':'Etiquetas de campo, pestañas, chips.'},
   {'name':'button','fontSize':'16px','lineHeight':'20px','fontWeight':700,'sample':'Contactar','usage':'Botones. 44 px de alto mínimo.'},
   {'name':'caption','fontSize':'13px','lineHeight':'18px','fontWeight':400,'sample':'4.9 · 128 reseñas','usage':'Metadatos y ayudas, en «text-muted».'}]},
  {'name':'Datos','family':'mono','note':'IBM Plex Mono 500, tabular. Provisional.','styles':[{'name':'dato','fontSize':'14px','lineHeight':'20px','fontWeight':500,'sample':'$350 · 45 min','usage':'Precios, horas, folios.'}]}]},
'spacing':{'tokens':[{'name':f'space-{n}','value':f'{v}px','usage':u} for n,v,u in [(1,4,'Icono–texto, dentro de chips.'),(2,8,'Entre controles relacionados.'),(3,12,'Padding de chips y celdas.'),(4,16,'Padding de tarjetas; gutter lateral en móvil.'),(5,20,'Entre campos de un formulario.'),(6,24,'Entre secciones.'),(8,32,'Entre bloques de la cabecera.'),(12,48,'Respiro de pantallas vacías.')]]},
'radius':{'tokens':[{'name':'radius-sm','value':'8px','usage':'Chips, casillas, botones.'},{'name':'radius-md','value':'12px','usage':'Campos, tarjetas, avisos.'},{'name':'radius-lg','value':'16px','usage':'Hojas inferiores y diálogos.'},{'name':'radius-pill','value':'999px','usage':'Avatar y puntos.'}]},
'sizing':{'tokens':[{'name':'control-h','value':'44px','usage':'Alto mínimo de botones y campos.'},{'name':'control-h-lg','value':'52px','usage':'Contactar en la cabecera de perfil.'},{'name':'icon','value':'20px','usage':'Iconos en línea.'},{'name':'avatar','value':'56px','usage':'Avatar en cabecera.'},{'name':'mark-min','value':'16px','usage':'Tamaño mínimo del símbolo.'}]},
'shadow':{'tokens':[{'name':'shadow-sheet','value':'0 -8px 32px rgba(18, 18, 18, 0.14)','usage':'Solo la hoja inferior. Las tarjetas no llevan sombra.'}]},
'motion':{'tokens':[{'name':'quick','value':'150ms','usage':'Hover, foco, chips.'},{'name':'ease-out','value':'cubic-bezier(0.2, 0.8, 0.2, 1)','usage':'Entradas y hojas.'}]}}
json.dump(tokens,open('tokens.json','w'),indent=1,ensure_ascii=False)
# ---- README
open('README.md','w').write(f'''# SUUMA

Plataforma móvil que conecta a profesionales independientes de belleza y cuidado personal con quienes los buscan. Habla claro, humano y directo: «tu talento», «tu próximo cliente», «cada talento tiene su lugar». Español e inglés sin juegos de palabras. Móvil primero.

![Lockup de SUUMA]({b('lockup-h.svg')})

## Principios

- **Una u dentro de la otra.** El nombre se escribe «suma» y la segunda u vive dentro de la primera, en cadmio. Cada quien conserva su forma; juntas hacen el nombre. Nunca se escriben las dos u seguidas.
- **Editorial y vivo.** Blanco y tinta como base; el cadmio es la única nota de color. La interfaz es sobria para que el trabajo de cada profesional, sus fotos y su nombre, sea lo que se ve.
- **El cadmio marca, no ordena.** Nunca es texto ni borde de control (1.4:1 sobre blanco). Va en la u interior, en chips activos, en destacados y en fondos con texto en tinta. La acción primaria es tinta.
- **Nada depende solo del color.** Estados y categorías llevan icono y texto.
- **Sin clichés de belleza.** Ni tijeras, ni rostros, ni siluetas, ni flores literales. Sin caritas: la u no lleva ojos.

## Contenido y tono

Claro, humano, directo y optimista sin promesas exageradas. Los botones dicen lo que hacen: Contactar, Publicar perfil, Reservar. Los errores dicen qué pasó y cómo seguir. Nunca «potencia», «sinergia», «revoluciona».

## Color

Dos neutros y una nota. Validado por contraste: todo texto 4.5:1 sobre su fondo en ambos temas.

- `text` sobre `bg`: 18.7:1. `text-muted`: 6.5:1. `text-subtle` sobre `surface-sunken`: 4.9:1.
- `primary` es tinta con `on-primary` blanco: la acción principal de cada pantalla.
- `cadmio` #FFD400 solo como relleno: la u interior, chips seleccionados, destacados y fondos con texto en `on-cadmio` (13.1:1). `cadmio-soft` para filas y avisos marcados.
- `focus` es tinta en claro y cadmio en oscuro, 2 px con separación de 2 px.
- `success` y `danger` siempre con icono y etiqueta; avisos en `*-soft` con `on-*-soft`. Son provisionales hasta probarlos en producto.
- Oscuro: fondo tinta, superficies #1C1C1C, `primary` pasa a hueso; el cadmio no cambia.

## Tipografía

- **Bricolage Grotesque** 600 (`display`) para el wordmark, `display`, `title-1` y `title-2`. 700 solo en display grande. Una `display` por pantalla.
- **Onest** 400, 500 y 700 (`sans`) para todo el cuerpo y los controles. 16 px mínimo en móvil.
- **IBM Plex Mono** 500 (`mono`) para precios, horas y folios. Provisional.
- Las tres se cargan de Google Fonts; el wordmark va en trazados.

## Espacio, forma y elevación

Escala de 4 px. Gutter de 16 px en móvil (`space-4`). Controles de 44 px (`control-h`); Contactar en cabecera, 52 px. Radios 8, 12 y 16; píldora solo en avatar y puntos. Las tarjetas se separan con `border`, sin sombra; solo la hoja inferior lleva `shadow-sheet`. Etiquetas sobre datos en `overline`.

## Movimiento

Todo es `quick` (150 ms, `ease-out`). Sin animación de marca por ahora; con `prefers-reduced-motion`, sin transiciones.

## Iconografía y marca

- Iconos de trazo de 1.75 px a 20 px (`icon`), en el color del texto que acompañan. Sin emoji.
- Símbolo: la doble u anidada desde 16 px (`mark-min`). Área de respeto: la altura de la u interior. Piezas y reglas en la sección «Marca» y en el grupo de assets «Marca».

## Accesibilidad

WCAG 2.2 AA: texto 4.5:1 en ambos temas, componentes y bordes 3:1, objetivos táctiles de 44 px, foco visible de 2 px. El cadmio nunca es el único portador de información.
''')
open('marca.md','w').write(f'''# Marca

Una u dentro de la otra: el nombre viene de «suma» y la segunda u vive dentro de la primera.

![Lockup]({b('lockup-h.svg')})

## Piezas

| Pieza | Uso | Archivo |
|---|---|---|
| Símbolo | Favicon, app icon, avatar, sello; desde 16 px | `simbolo.svg` · `simbolo-tinta.svg` · `simbolo-blanco.svg` |
| Wordmark | Documentos, firmas, cabecera; mínimo 80 px | `wordmark.svg` · `wordmark-oscuro.svg` |
| Lockup horizontal | Web, correo, cabecera de perfil; mínimo 140 px | `lockup-h.svg` · `lockup-h-oscuro.svg` |
| Lockup vertical | Social, stickers, carteles; mínimo 90 px | `lockup-v.svg` |
| App icon | PWA e iOS; maskable con margen del 42 % | `app-icon.svg` · `app-icon-maskable.svg` · `icon-512.png` · `icon-192.png` |
| Avatar | Redes, en círculo | `avatar.svg` |
| Favicon | Cambia con el esquema del sistema | `favicon.svg` |
| Tarjeta de redes | 1200×630 | `tarjeta-redes.svg` |

## Anatomía

- Cuenco exterior con el tallo de Bricolage Grotesque 600, sin espolón.
- Interior al 60 % del grosor del tallo; ancho igual al cuenco menos dos tallos y medio; arranca al 60 % de la altura de x y termina 1.45 tallos sobre la línea base. En cadmio.
- Wordmark: «suma» en Bricolage 600, opsz 96, tracking −1 %, en trazados.

## Reglas

- Área de respeto: la altura de la u interior.
- Fondos permitidos: `bg`, `surface`, `surface-sunken`, `text` y `cadmio` (ahí todo en tinta).
- Una tinta: todo en `text`, o en `bg` sobre oscuro.
- No escribir las dos u seguidas, no poner ojos ni boca, no usar el cadmio como texto, no rotar ni separar las u, no degradados ni sombras.
''')
# ---- components
HEAD='''<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Onest:wght@400;500;700&family=IBM+Plex+Mono:wght@500&display=swap"><style>
html,body{margin:0} body{background:var(--bg,#FFFFFF);color:var(--text,#121212);font-family:var(--font-sans,"Onest",system-ui,sans-serif);font-size:16px;line-height:24px;padding:var(--space-4,16px);display:flex;gap:var(--space-3,12px);flex-wrap:wrap;align-items:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:var(--control-h,44px);padding:0 20px;border-radius:var(--radius-sm,8px);font-weight:700;font-size:16px;border:1px solid transparent;cursor:pointer;font-family:inherit}
.btn:focus-visible{outline:2px solid var(--focus,#121212);outline-offset:2px}
.b-primary{background:var(--primary,#121212);color:var(--on-primary,#fff)} .b-secondary{background:transparent;color:var(--text,#121212);border-color:var(--text,#121212)} .b-ghost{background:transparent;color:var(--text,#121212);text-decoration:underline;text-underline-offset:3px} .b-danger{background:transparent;color:var(--danger,#C8102E);border-color:var(--danger,#C8102E)} .b-marca{background:var(--cadmio,#FFD400);color:var(--on-cadmio,#121212)}
.chip{display:inline-flex;align-items:center;gap:6px;min-height:32px;padding:0 12px;border-radius:var(--radius-sm,8px);font-weight:600;font-size:13px;background:var(--surface,#fff);color:var(--text,#121212);border:1px solid var(--border,#E3E2DD)} .chip svg{width:16px;height:16px;display:block} .chip.sel{border-color:var(--text,#121212);background:var(--cadmio-soft,#FFF3B0)}
.field{display:grid;gap:6px;min-width:240px} .field label{font-size:14px;line-height:20px;font-weight:500} .field input{height:var(--control-h,44px);border:1px solid var(--border-control,#8A8984);border-radius:var(--radius-md,12px);background:var(--surface,#fff);color:var(--text,#121212);padding:0 12px;font:inherit} .field input:focus-visible{outline:2px solid var(--focus,#121212);outline-offset:2px} .field small{font-size:13px;color:var(--text-muted,#5F5E5A)} .field.err input{border-color:var(--danger,#C8102E)} .field.err small{color:var(--danger,#C8102E)}
.card{background:var(--surface,#fff);border:1px solid var(--border,#E3E2DD);border-radius:var(--radius-md,12px);padding:var(--space-4,16px);display:grid;gap:12px;width:min(100%,360px)} .card h3{margin:0;font-family:var(--font-display,"Bricolage Grotesque",sans-serif);font-size:24px;line-height:30px;font-weight:600;letter-spacing:-.01em} .card p{margin:0;color:var(--text-muted,#5F5E5A)} .av{width:56px;height:56px;border-radius:50%;background:var(--surface-sunken,#F5F4F0)} .row{display:flex;gap:12px;align-items:center} .meta{font-size:13px;color:var(--text-muted,#5F5E5A)} .ov{font-size:11px;line-height:16px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted,#5F5E5A)} .dato{font-family:var(--font-mono,"IBM Plex Mono",monospace);font-size:14px;font-weight:500}
.estado{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:var(--radius-md,12px);font-weight:500;font-size:14px} .estado svg{width:16px;height:16px;display:block;flex:none} .e-ok{background:var(--success-soft,#DDF3E6);color:var(--on-success-soft,#0A5A36)} .e-bad{background:var(--danger-soft,#FBE1E4);color:var(--on-danger-soft,#8E0B21)} .e-marca{background:var(--cadmio-soft,#FFF3B0);color:var(--text,#121212)}
.nav{display:flex;width:min(100%,390px);background:var(--surface,#fff);border-top:1px solid var(--border,#E3E2DD);padding:6px 0 10px} .nav a{flex:1;display:grid;justify-items:center;gap:2px;font-size:12px;font-weight:500;color:var(--text-muted,#5F5E5A);text-decoration:none;min-height:44px;align-content:center} .nav a svg{width:22px;height:22px;display:block} .nav a.on{color:var(--text,#121212)} .nav a.on i{display:block;width:18px;height:3px;border-radius:2px;background:var(--cadmio,#FFD400)}
.cal{display:inline-flex;align-items:center;gap:8px} .cal svg{display:block;width:22px;height:22px} .cal b{font-weight:700} .cal .n{font-size:13px;color:var(--text-muted,#5F5E5A)}
</style></head><body>'''
ico=lambda d:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'+d+'</svg>'
OK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>'
X='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
U='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="butt"><path d="M5 3v11a7 7 0 0 0 14 0V3"/></svg>'
def cuenco(lleno): # calificación: cuencos (u) llenos en cadmio o vacíos
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 3v10a8 8 0 0 0 16 0V3" fill="{"var(--cadmio,#FFD400)" if lleno else "none"}" stroke="var(--text,#121212)" stroke-width="2.4"/></svg>'
def calif(n,txt): return f'<span class="cal">{"".join(cuenco(i<n) for i in range(5))}<b>{txt}</b></span>'
I_HOY=ico('<path d="M4 11l8-7 8 7v9H4z"/>'); I_BU=ico('<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'); I_AG=ico('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'); I_PF=ico('<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>')
comps={
'Boton':('Actions',96,'<button class="btn b-primary">Contactar</button><button class="btn b-secondary">Ver perfil</button><button class="btn b-ghost">Cancelar</button><button class="btn b-marca">Destacar perfil</button><button class="btn b-danger">Cancelar cita</button>',
 'Botón de acción. La acción primaria va en tinta; el cadmio queda para una sola acción de marca por pantalla.\n\n- `primary`: `primary` con `on-primary`. La acción principal de la pantalla: Contactar, Publicar perfil, Reservar.\n- `secondary`: borde y texto en `text`. `ghost`: texto subrayado en `text`. `danger`: borde y texto `danger`, siempre con confirmación.\n- `marca`: fondo `cadmio` con texto `on-cadmio` (13.1:1). Una por pantalla y solo para acciones de marca (destacar, compartir); nunca para confirmar ni pagar.\n- 44 px de alto mínimo (`control-h`); 52 px en la cabecera de perfil. Radio `radius-sm`. Foco: anillo 2 px en `focus`.\n- El consumidor provee: etiqueta (verbo concreto), estado de carga y `aria-disabled`.'),
'Campo':('Forms',200,'<div class="field"><label for="a">Nombre del servicio</label><input id="a" value="Corte y barba"><small>Como lo verán tus clientes.</small></div><div class="field err"><label for="b">Precio</label><input id="b" value="$"><small>Escribe un precio, por ejemplo 350.</small></div>',
 'Campo de texto con etiqueta arriba, ayuda abajo y error en `danger`.\n\n- 44 px de alto, borde `border-control` (3.5:1), radio `radius-md`, fondo `surface`.\n- Foco: anillo `focus`. Error: borde `danger` y mensaje que dice cómo corregir.\n- Etiqueta `label` 14/20 a 500; ayuda `caption` en `text-muted`.\n- El consumidor provee: etiqueta, valor, mensaje de ayuda o error y el `id` que une etiqueta y campo.'),
'ChipCategoria':('Data display',72,f'<span class="chip">{U}Barbería</span><span class="chip">{U}Uñas</span><span class="chip sel">{U}Colorista</span><span class="chip">{U}Masaje</span>',
 'Chip de categoría: icono + texto en un borde fino, nunca solo color.\n\n- Fondo `surface`, borde `border`, texto `text`. Seleccionado: borde `text` sobre `cadmio-soft`.\n- Icono de la categoría a 16 px, o la u de la marca mientras no exista.\n- Altura 32 px, radio `radius-sm`, 13 px a 600.\n- El consumidor provee: nombre de la categoría y, si filtra, `aria-pressed`.'),
'TarjetaProfesional':('Data display',320,f'<div class="card"><div class="row"><span class="av"></span><div><h3>Andrés Cortés</h3><div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:4px"><span class="chip">{U}Barbería</span></div></div></div><p>Corte, barba y navaja. Col. Roma, CDMX. Lunes a sábado.</p>{calif(5,"4.9")}<div><span class="ov">Desde</span><br><span class="dato">$350 · 45 min</span></div><button class="btn b-primary">Contactar</button></div>',
 'Tarjeta de profesional: foto, nombre en `title-1`, categoría como chip, descripción, calificación, precio y el botón Contactar.\n\n- Fondo `surface`, borde `border`, radio `radius-md`, padding `space-4`. Sin sombra. Etiquetas sobre datos en `overline`; precio y duración en `dato` (mono).\n- El nombre va en Bricolage; todo lo demás en Onest.\n- Contactar es el único botón primario de la tarjeta.\n- El consumidor provee: foto real, nombre, categorías, descripción corta, calificación, precio desde y la acción de contacto.'),
'Calificacion':('Data display',110,f'<div style="display:grid;gap:10px">{calif(1,"1 de 5")}{calif(3,"3 de 5")}{calif(5,"5 de 5")}{calif(4,"4.8")}<span class="cal" style="font-size:13px;color:var(--text-muted,#5F5E5A)">Nuevo en SUUMA · 3 citas</span></div>',
 'Calificación en cuencos: cinco u abiertas que se llenan de cadmio. El número siempre va escrito.\n\n- Lectura: cinco cuencos a 22 px y el número («4 de 5», «4.8 · 128 reseñas»). Nunca solo la forma.\n- Lleno: `cadmio` con contorno `text`; vacío: solo contorno. Entrada: cinco cuencos de 44 px en un `radiogroup`, flechas y números 1 a 5.\n- Sin promedio hasta 3 reseñas: «Nuevo en SUUMA · n citas».\n- El consumidor provee: valor, conteo y, en entrada, `onChange`.'),
'Estado':('Feedback',120,f'<span class="estado e-ok">{OK}Perfil publicado</span><span class="estado e-bad">{X}Cita cancelada</span><span class="estado e-marca">{U}Perfil destacado</span>',
 'Aviso de estado: icono + texto sobre el fondo suave del estado.\n\n- Éxito: `success-soft` con `on-success-soft` y palomita. Error: `danger-soft` con `on-danger-soft` y cruz.\n- Hitos de marca (perfil destacado, verificado): `cadmio-soft` con `text` y la u del símbolo.\n- Nunca solo color; el texto dice qué pasó. Radio `radius-md`, padding 8 por 12.\n- El consumidor provee: el texto y, si procede, la acción siguiente.'),
'NavInferior':('Navigation',88,f'<nav class="nav"><a href="#" class="on">{I_HOY}Hoy<i></i></a><a href="#">{I_BU}Buscar</a><a href="#">{I_AG}Agenda</a><a href="#">{I_PF}Perfil</a></nav>',
 'Navegación inferior para móvil: cuatro destinos; el activo en `text` con una barra de cadmio debajo.\n\n- Fondo `surface`, borde superior `border`, 44 px mínimo por destino, icono de 22 px y etiqueta de 12 px a 500.\n- Activo: texto en `text` y barra de 18×3 px en `cadmio`; inactivo: `text-muted`. Nunca solo color.\n- Destinos: Hoy, Buscar, Agenda, Perfil.\n- El consumidor provee: rutas y destino activo.')}
for name,(grp,h,body,md) in comps.items():
    os.makedirs(f'components/{name}',exist_ok=True)
    open(f'components/{name}/preview.html','w').write(f'<!-- @dsCard group="{grp}" height={h} -->\n{HEAD}{body}</body></html>')
    open(f'components/{name}/README.md','w').write(f'# {name}\n\n{md}\n')
# ---- cover
sym=open(F+'svg/simbolo.svg').read().replace('#121212','var(--text, #121212)').replace('#FFD400','var(--cadmio, #FFD400)')
wm=open(F+'svg/wordmark.svg').read().replace('#121212','var(--text, #121212)').replace('#FFD400','var(--cadmio, #FFD400)')
os.makedirs('components/Cover',exist_ok=True)
open('components/Cover/preview.html','w').write(f'''<!-- @dsCard height=288 -->
<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500&display=swap"><style>
html,body{{margin:0;height:100%}} body{{background:var(--bg,#FFFFFF);color:var(--text,#121212);font-family:var(--font-sans,"Onest",system-ui,sans-serif);overflow:hidden}}
.cover{{position:relative;height:288px;overflow:hidden}}
.art{{position:absolute;top:28px;right:40px;width:230px;height:230px;opacity:.12}} .art svg{{width:100%;height:100%;display:block}}
.words{{position:absolute;left:var(--space-6,24px);bottom:var(--space-6,24px);max-width:460px;display:grid;gap:10px}} .words .wm{{width:260px}} .words .wm svg{{width:100%;height:auto;display:block}}
.tag{{margin:0;font-size:15px;line-height:22px;color:var(--text-muted,#5F5E5A)}} .tag b{{color:var(--text,#121212);font-weight:500;background:var(--cadmio,#FFD400);padding:0 4px;border-radius:3px}}
</style></head><body><div class="cover"><div class="art" aria-hidden="true">{sym}</div><div class="words"><div class="wm" role="img" aria-label="suma">{wm}</div><p class="tag">Cada talento tiene su lugar. · <b>Tu talento, nuevas posibilidades.</b></p></div></div></body></html>''')
# ---- index
files={}
for n,i in ids.items():
    p=F+('png/' if n.endswith('.png') else 'svg/')+n
    files[n]={'name':n,'blob':i,'size':os.path.getsize(p),'type':'image/png' if n.endswith('.png') else 'image/svg+xml'}
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
idx={'v':3,'layout':'files','createdOnFiles':{'v':1,'at':now},'title':'SUUMA','namespace':'SUUMA','libraries':[],'sections':{},'groups':['Marca'],
 'assetGroups':{'Marca':{'name':'Marca','tile':'m','order':list(ids),'files':files}},'blobs':{},'docs':{'readme':'project/README.md','sections':[]},
 'lastChange':{'at':now,'by':'Kevin','via':'Claude Code','note':'Sistema inicial de SUUMA: tokens cadmio y tinta en claro y oscuro, tipografía Bricolage + Onest, marca y siete componentes.'}}
json.dump(idx,open('design-system.json','w'),indent=2,ensure_ascii=False)
print(sorted(os.listdir('.')),sorted(os.listdir('components')))
