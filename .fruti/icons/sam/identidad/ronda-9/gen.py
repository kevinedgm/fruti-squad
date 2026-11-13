# SAM · identidad, ronda 9: validación en contexto de C2 (grande) + C4 (16–24 px), elegidos por el usuario el 2026-11-13.
# Criterio acordado: si se lee bien en pestaña, icono de PWA y barra superior, se congela.
OSC, SUP, CLA, BL, VO, SEC = '#0a0a0b', '#16161a', '#f2f2ee', '#ffffff', '#c6f432', '#a3a3a8'
c2 = open('../ronda-8/c2-contorno.svg').read(); c4 = open('../ronda-8/c4-16px.svg').read()
def at(s, z, st=''): return s.replace('<svg ', f'<svg width="{z}" height="{z}" style="{st}" ', 1)
# Silueta de una tinta para la notificación (Android pide icono monocromo): tarjeta delantera rellena, palomita calada.
sil = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="{z}" height="{z}" role="img" aria-label="SAM">'
       '<defs><mask id="sam-sil"><rect width="48" height="48" fill="#fff"/><rect x="13" y="15" width="35" height="29" rx="7" fill="#000"/>'
       '<path d="M23.1 29.9L27.5 34.1L36.1 25.1" stroke="#000" stroke-width="4.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></mask>'
       '<mask id="sam-sil2"><rect width="48" height="48" fill="#fff"/><path d="M23.1 29.9L27.5 34.1L36.1 25.1" stroke="#000" stroke-width="4.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></mask></defs>'
       '<rect x="4" y="8" width="28" height="22" rx="5.5" fill="currentColor" mask="url(#sam-sil)"/>'
       '<rect x="15" y="18" width="29" height="23" rx="5.5" fill="currentColor" mask="url(#sam-sil2)"/></svg>')
open('notificacion.svg', 'w').write(sil.replace('{z}', '48'))
def tabs(fondo, act, tinta, sec):
    t = lambda ic, txt, a: (f'<div class="t{" a" if a else ""}" style="{"background:"+act if a else ""};color:{tinta if a else sec}">{ic}<span>{txt}</span></div>')
    otro = '<span class="fav" style="background:#6b7280"></span>'
    return (f'<div class="br" style="background:{fondo}">{t(otro, "Bandeja de entrada", False)}{t(at(c4, 16), "Mis actividades · SAM", True)}{t(otro, "Documentación", False)}</div>')
def home(fondo, forma):
    rad = '50%' if forma == 'circulo' else '22%'
    otros = [('#2f6fdf', 'Correo'), ('#e0663a', 'Calendario'), ('#2e9b5f', 'Mapas')]
    ic = ''.join(f'<div class="hi"><div class="ti" style="background:{c};border-radius:{rad}"></div><span>{n}</span></div>' for c, n in otros)
    sam = f'<div class="hi"><div class="ti" style="background:{OSC};color:{CLA};border-radius:{rad}">{at(c2, 40)}</div><span>SAM</span></div>'
    return f'<div class="home" style="background:{fondo}"><div class="g">{ic}{sam}</div><p>{"Android (máscara circular)" if forma=="circulo" else "iOS"}</p></div>'
def barra(fondo, tinta, linea, sec):
    return (f'<div class="tel" style="background:{fondo};color:{tinta};border-color:{linea}"><div class="top" style="border-color:{linea}">'
            f'{at(c2, 28)}<b class="wm">SAM</b><span class="sp"></span><span style="color:{sec};font-size:13px">Laura M.</span></div>'
            f'<h3>Mis actividades</h3><p style="color:{sec};margin:0">3 abiertas · 1 vence hoy</p></div>')
def notif(fondo, tinta, sec):
    return (f'<div class="nt" style="background:{fondo};color:{tinta}"><div class="nh" style="color:{sec}">{sil.replace("{z}", "16")}<span>SAM · ahora</span></div>'
            f'<b>INC-2041 avanzó a Revisión</b><span style="color:{sec}">Te toca revisar la evidencia adjunta.</span></div>')
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SAM · ronda 9</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.5 'Instrument Sans',system-ui,sans-serif;--g-color-brand:{VO}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:76ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} section>p{{margin:4px 0 0;max-width:86ch;color:#cfcfca}}
.row{{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;margin-top:16px}}
.br{{display:flex;gap:2px;padding:8px 8px 0;border-radius:8px 8px 0 0;width:560px}}
.t{{display:flex;gap:8px;align-items:center;font-size:12px;padding:8px 12px;border-radius:8px 8px 0 0;flex:1;min-width:0;white-space:nowrap;overflow:hidden}}
.fav{{width:16px;height:16px;border-radius:4px;flex:none}}
.home{{width:280px;padding:21px;border-radius:21px;text-align:center}} .home p{{margin:13px 0 0;font-size:12px;color:#d0d0cc}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}} .hi{{display:grid;justify-items:center;gap:4px;font-size:11px;color:#fff}}
.ti{{width:56px;height:56px;display:grid;place-items:center}}
.tel{{width:340px;border:1px solid;border-radius:16px;overflow:hidden}} .top{{display:flex;gap:8px;align-items:center;padding:10px 13px;border-bottom:1px solid}}
.wm{{font-size:20px;font-weight:700;letter-spacing:-.01em}} .sp{{flex:1}} .tel h3{{margin:16px 13px 0;font-size:22px}} .tel p{{padding:0 13px 16px}}
.nt{{width:340px;border-radius:16px;padding:13px;display:grid;gap:2px;font-size:14px}} .nh{{display:flex;gap:6px;align-items:center;font-size:12px}}
.zoom{{display:flex;gap:16px;align-items:flex-end}} .zoom figure{{margin:0;text-align:center;font-size:12px;color:{SEC}}}
.zoom .px{{image-rendering:pixelated}}
</style></head><body><main><h1>SAM · identidad, ronda 9 · prueba en contexto</h1>
<p class="sub">C2 en tamaños grandes y C4 en 16–24 px, en tamaño real. Criterio acordado: si se lee bien en pestaña, icono de PWA y barra superior, se congela. Nombre en Instrument Sans 700 (provisional).</p>
<section><h2>1 · Pestaña del navegador (C4 a 16 px)</h2><p>Entre otras pestañas, en claro y en oscuro.</p>
<div class="row">{tabs("#dcdcd6", BL, OSC, "#55555c")}{tabs("#1c1c20", "#2a2a30", CLA, SEC)}</div></section>
<section><h2>2 · Icono de la PWA en el celular (C2 a 40 px dentro de un icono de 56)</h2><p>Fondo negro con el símbolo dentro de la zona segura (80 % del icono), para que la máscara circular de Android no lo recorte.</p>
<div class="row">{home("linear-gradient(160deg,#3b4a6b,#1f2a40,#141a28)", "circulo")}{home("linear-gradient(160deg,#c9b6a3,#8a7766,#544437)", "squircle")}</div></section>
<section><h2>3 · Barra superior de la app (C2 a 28 px)</h2><p>Logotipo compacto.</p>
<div class="row">{barra(OSC, CLA, "#2a2a30", SEC)}{barra(CLA, OSC, "#d6d6d0", "#55555c")}</div></section>
<section><h2>4 · Notificación push (silueta de una tinta a 16 px)</h2><p>Android dibuja el icono pequeño de la notificación en un solo color: se usa una silueta, sin lima.</p>
<div class="row">{notif("#2a2a30", CLA, SEC)}{notif(BL, OSC, "#55555c")}</div></section>
</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
