# GEMA · ronda 6: R1 (Pantalla + Resultado) elegido por el usuario el 2026-11-17. Versión chica, silueta y prueba en contexto.
AC = 'var(--g-color-brand,#38bdf8)'
r1 = open('../ronda-5/r1-pantalla.svg').read()
# Chica (16–24 px): marco más grueso y solo el pico del resultado, más grande.
chica = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA" class="gema-chica">\n'
 '  <!-- GEMA · versión chica: marco grueso y solo el pico del resultado -->\n'
 f'  <path d="M14 34C19 34 20.5 13 24 13C27.5 13 29 34 34 34Z" fill="{AC}"/>\n'
 '  <rect x="5" y="7" width="38" height="34" rx="8" fill="none" stroke="currentColor" stroke-width="3.6"/>\n'
 '  <path d="M10 34H14C19 34 20.5 13 24 13C27.5 13 29 34 34 34H38" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>\n</svg>\n')
open('gema-chica.svg', 'w').write(chica)
# Silueta de una tinta (notificación Android): marco y pico del resultado rellenos.
sil = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="GEMA">\n'
 '  <rect x="5" y="7" width="38" height="34" rx="8" fill="none" stroke="currentColor" stroke-width="4"/>\n'
 '  <path d="M11 35H14C19 35 20.5 13 24 13C27.5 13 29 35 34 35H37Z" fill="currentColor"/>\n</svg>\n')
open('gema-notificacion.svg', 'w').write(sil)
OSC, CLA, BL, AV, SEC = '#0a0a0b', '#f2f2ee', '#ffffff', '#38bdf8', '#a3a3a8'
def at(s, z): return s.replace('<svg ', f'<svg width="{z}" height="{z}" ', 1)
def tabs(fondo, act, tinta, sec):
    otro = '<span class="fav" style="background:#6b7280"></span>'
    t = lambda ic, txt, a: f'<div class="t" style="{"background:"+act if a else ""};color:{tinta if a else sec}">{ic}<span>{txt}</span></div>'
    return f'<div class="br" style="background:{fondo}">{t(otro,"Bandeja de entrada",False)}{t(at(chica,16),"Recepción · GEMA",True)}{t(otro,"Documentación",False)}</div>'
def home(fondo, forma):
    rad = '50%' if forma == 'c' else '22%'
    ic = ''.join(f'<div class="hi"><div class="ti" style="background:{c};border-radius:{rad}"></div><span>{n}</span></div>' for c, n in [('#2f6fdf','Correo'),('#e0663a','Calendario'),('#2e9b5f','Mapas')])
    return f'<div class="home" style="background:{fondo}"><div class="g">{ic}<div class="hi"><div class="ti" style="background:{OSC};color:{CLA};border-radius:{rad}">{at(r1,38)}</div><span>GEMA</span></div></div><p>{"Android (máscara circular)" if forma=="c" else "iOS"}</p></div>'
def barra(fondo, tinta, linea, sec):
    return (f'<div class="tel" style="background:{fondo};color:{tinta};border-color:{linea}"><div class="top" style="border-color:{linea}">{at(r1,28)}<b class="wm">GEMA</b><span class="sp"></span>'
            f'<span style="color:{sec};font-size:13px">Recepción · Oaxaca</span></div><h3>Muestras recibidas</h3><p style="color:{sec};margin:0">12 hoy · 3 por asignar</p></div>')
def notif(fondo, tinta, sec):
    return (f'<div class="nt" style="background:{fondo};color:{tinta}"><div class="nh" style="color:{sec}">{at(sil,16)}<span>GEMA · ahora</span></div>'
            f'<b>Resultados listos: M-2026-1184</b><span style="color:{sec}">Agua residual · el informe está listo para revisión.</span></div>')
tam = ''.join(f'<figure><div class="z">{at(chica if z <= 24 else r1, z)}</div><figcaption>{z} px{" · chica" if z <= 24 else ""}</figcaption></figure>' for z in (16, 24, 32, 48, 128))
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>GEMA · ronda 6</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{OSC};color:{CLA};font:15px/1.5 'Onest',system-ui,sans-serif;--g-color-brand:{AV}}}
main{{max-width:1180px;margin:0 auto;padding:34px 21px 55px}}
h1{{font-size:34px;line-height:1.05;letter-spacing:-.02em;margin:0 0 8px}} .sub{{margin:0 0 34px;color:{SEC};max-width:78ch}}
section{{border:1px solid #26262b;border-radius:2px;padding:21px;margin-bottom:21px;background:#111114}}
h2{{margin:0;font-size:22px}} section>p{{margin:4px 0 0;max-width:86ch;color:#cfcfca}}
.row{{display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start;margin-top:16px}} .tams{{align-items:flex-end}}
figure{{margin:0;text-align:center}} .z{{display:flex;align-items:flex-end;justify-content:center;min-width:56px;height:128px}} figcaption{{font-size:12px;color:{SEC}}}
.br{{display:flex;gap:2px;padding:8px 8px 0;border-radius:8px 8px 0 0;width:560px;max-width:100%}}
.t{{display:flex;gap:8px;align-items:center;font-size:12px;padding:8px 12px;border-radius:8px 8px 0 0;flex:1;min-width:0;white-space:nowrap;overflow:hidden}} .fav{{width:16px;height:16px;border-radius:4px;flex:none}}
.home{{width:280px;padding:21px;border-radius:21px;text-align:center}} .home p{{margin:13px 0 0;font-size:12px;color:#d0d0cc}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:13px}} .hi{{display:grid;justify-items:center;gap:4px;font-size:11px;color:#fff}} .ti{{width:56px;height:56px;display:grid;place-items:center}}
.tel{{width:340px;border:1px solid;border-radius:16px;overflow:hidden}} .top{{display:flex;gap:8px;align-items:center;padding:10px 13px;border-bottom:1px solid}}
.wm{{font-size:20px;font-weight:700}} .sp{{flex:1}} .tel h3{{margin:16px 13px 0;font-size:22px}} .tel p{{padding:0 13px 16px}}
.nt{{width:340px;border-radius:16px;padding:13px;display:grid;gap:2px;font-size:14px}} .nh{{display:flex;gap:6px;align-items:center;font-size:12px}}
</style></head><body><main><h1>GEMA · identidad, ronda 6 · prueba en contexto</h1>
<p class="sub">R1 (Pantalla + Resultado) en tamaño real. Por debajo de 32 px va la versión chica: marco más grueso y solo el pico del resultado. Cian y Onest siguen provisionales. Datos de ejemplo ficticios.</p>
<section><h2>0 · Tamaños</h2><div class="row tams">{tam}</div></section>
<section><h2>1 · Pestaña del navegador (versión chica a 16 px)</h2><div class="row">{tabs("#dcdcd6", BL, OSC, "#55555c")}{tabs("#1c1c20", "#2a2a30", CLA, SEC)}</div></section>
<section><h2>2 · Icono de la PWA en el celular</h2><p>El símbolo dentro de la zona segura, para que la máscara circular de Android no lo recorte.</p><div class="row">{home("linear-gradient(160deg,#3b4a6b,#1f2a40,#141a28)","c")}{home("linear-gradient(160deg,#c9b6a3,#8a7766,#544437)","s")}</div></section>
<section><h2>3 · Barra superior de la app (28 px)</h2><div class="row">{barra(OSC, CLA, "#2a2a30", SEC)}{barra(CLA, OSC, "#d6d6d0", "#55555c")}</div></section>
<section><h2>4 · Notificación push (silueta de una tinta a 16 px)</h2><p>Android dibuja este icono en un solo color: marco y pico del resultado rellenos.</p><div class="row">{notif("#2a2a30", CLA, SEC)}{notif(BL, OSC, "#55555c")}</div></section>
</main></body></html>'''
open('banco.html', 'w').write(html); print('ok')
