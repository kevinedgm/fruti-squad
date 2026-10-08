# Genera Coco, Bruno (builder), Mora y Fruti Squad 24 px con el contrato común de la squad:
#   svg/<id>.small.svg · svg/<id>.svg · svg/<id>.large.svg · svg/<id>-{claro,oscuro,auto}.svg
#   svg/<id>-tile.svg · svg/<id>-tile-animado.svg · svg/<id>-animado-ejemplo.svg · manifest.json
# Uso (desde .fruti/icons): python3 squad-build.py
import json, math, os, re

TILE = '#161616'


def wrap(id_, body, sw, color, a11y, cls, css):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" class="uva-icon uva-{id_}{cls}" {a11y}>\n'
            f'  <!-- {id_} · {AG[id_]["desc"]} -->\n  <style>{css}</style>\n{body}</svg>\n')


def wrap_tile(id_, body, sw, color, a11y, cls, css, escala):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="uva-icon uva-{id_}{cls}" {a11y}>\n'
            f'  <!-- {id_} · {AG[id_]["desc"]} -->\n  <style>{css}</style>\n'
            f'  <rect width="24" height="24" rx="5.25" fill="{TILE}"/>\n'
            f'  <g transform="translate(12 12) scale({escala}) translate(-12 -12)" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">\n{body}  </g>\n</svg>\n')


def small(svg):
    s = re.sub(r'\s*<style>.*?</style>', '', svg, flags=re.S)
    s = re.sub(r'\s*<!--.*?-->', '', s, flags=re.S)
    s = re.sub(r' class="uva-[\w-]+__[\w-]+"', '', s)
    return s.replace(' pathLength="1"', '')


def css_anim(id_, mod, piezas, sw):
    """piezas: [(clase, tipo 'trazar'|'aparecer', duración ms, retraso ms, curva)]"""
    var = lambda c: f'--uva-{id_}-{c}'
    s = f'.uva-{id_}{{stroke-width:var(--uva-stroke,{sw})}}'
    s += f'.uva-{id_}--{mod}{{' + ';'.join(f'{var(c)}:uva-{id_}-{t}' for c, t, *_ in piezas) + '}'
    for c, t, d, r, ease in piezas:
        extra = 'stroke-dasharray:1 1.1;' if t == 'trazar' else 'transform-box:fill-box;transform-origin:center;'
        s += f'.uva-{id_}__{c}{{{extra}animation:var({var(c)},none) {d}ms {ease} {r}ms 1 both}}'
    s += f'@keyframes uva-{id_}-trazar{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}'
    s += f'@keyframes uva-{id_}-aparecer{{from{{opacity:0;transform:scale(0)}}to{{opacity:1;transform:none}}}}'
    s += f'@media (prefers-reduced-motion:reduce){{.uva-{id_}--{mod}{{' + ';'.join(f'{var(c)}:none' for c, *_ in piezas) + '}}'
    return s


EASE_T = 'cubic-bezier(.2,.6,.3,1)'
EASE_P = 'cubic-bezier(.3,1.5,.5,1)'

# ---------------------------------------------------------------- piezas por agente


def coco(sw):
    i = 'coco'
    return (f'  <circle class="uva-{i}__circulo" pathLength="1" cx="12" cy="12" r="9"/>\n'
            f'  <path class="uva-{i}__nodo1" d="M8 15h0"/>\n'
            f'  <path class="uva-{i}__nodo2" d="M11 12h0"/>\n'
            f'  <circle class="uva-{i}__foco" cx="14.5" cy="8.5" r=".6" fill="currentColor"/>\n')


def bruno(sw):
    i = 'bruno-builder'
    y0, fin = 2 + sw / 2 + .0, 22 - sw / 2
    return (f'  <rect class="uva-{i}__modulo" pathLength="1" x="4" y="{y0:g}" width="16" height="{15 - y0:g}" rx="4.5"/>\n'
            f'  <path class="uva-{i}__entrada" pathLength="1" d="M9 {fin:g}V15"/>\n'
            f'  <path class="uva-{i}__salida" pathLength="1" d="M15 15V{fin:g}"/>\n')


def mora(sw):
    i = 'mora'
    return (f'  <path class="uva-{i}__base" pathLength="1" d="M4.5 20.5H19.5"/>\n'
            f'  <circle class="uva-{i}__documento" pathLength="1" cx="7.5" cy="13.75" r="2.5"/>\n'
            f'  <circle class="uva-{i}__evidencia" pathLength="1" cx="16.5" cy="13.75" r="2.5"/>\n'
            f'  <circle class="uva-{i}__registro" pathLength="1" cx="12" cy="5.95" r="2.5"/>\n')


# Fruti Squad 24: la Espiral aprobada (r 116→212 en 46°, trazo 64, núcleo 44 sobre 512) escalada para caber con margen 2
K = 10 / (212 + 32)
FS_W, FS_CORE = 64 * K, 44 * K


def fruti(sw):
    i = 'fruti-squad'
    out = ''
    for k, n in enumerate(['kiwi', 'lima', 'coco', 'bruno', 'mora']):
        pts = [(12 + (116 + 96 * t / 12) * K * math.cos(math.radians(-90 + k * 72 + 46 * t / 12)),
                12 + (116 + 96 * t / 12) * K * math.sin(math.radians(-90 + k * 72 + 46 * t / 12))) for t in range(13)]
        out += f'  <path class="uva-{i}__{n}" d="M' + ' '.join('%.2f %.2f' % p for p in pts) + '"/>\n'
    out += f'  <circle class="uva-{i}__nucleo" cx="12" cy="12" r="{FS_CORE - FS_W / 2:.2f}" fill="currentColor"/>\n'
    return out


def fruti_css(sw, mod='orquestar'):
    i = 'fruti-squad'
    s = f'.uva-{i}{{stroke-width:var(--uva-stroke,{sw:.2f})}}'
    s += f'.uva-{i}--{mod}{{--uva-{i}-brazo:uva-{i}-abrir;--uva-{i}-nucleo:uva-{i}-aparecer}}'
    for k, n in enumerate(['kiwi', 'lima', 'coco', 'bruno', 'mora']):
        s += (f'.uva-{i}__{n}{{transform-box:view-box;transform-origin:12px 12px;'
              f'animation:var(--uva-{i}-brazo,none) 600ms cubic-bezier(.25,1.3,.5,1) {k * 70}ms 1 both}}')
    s += (f'.uva-{i}__nucleo{{transform-box:fill-box;transform-origin:center;'
          f'animation:var(--uva-{i}-nucleo,none) 400ms {EASE_P} 640ms 1 both}}')
    s += f'@keyframes uva-{i}-abrir{{from{{opacity:0;transform:rotate(-150deg) scale(.35)}}to{{opacity:1;transform:none}}}}'
    s += f'@keyframes uva-{i}-aparecer{{from{{opacity:0;transform:scale(0)}}to{{opacity:1;transform:none}}}}'
    s += f'@media (prefers-reduced-motion:reduce){{.uva-{i}--{mod}{{--uva-{i}-brazo:none;--uva-{i}-nucleo:none}}}}'
    return s


AG = {
    'coco': dict(name='Coco', role='visual-construction', verb='inspeccionar', symbol='🥥', accent='#C89A68', light='#9C6D39',
                 desc='avatar del agente Coco (construcción visual y auditoría): círculo + tres puntos que crecen hacia el foco',
                 piezas=coco, sw=2, sw_av=2, sw_tile=2, esc=.96, dur=700, rtl='fixed',
                 anim=[('circulo', 'trazar', 360, 0, EASE_T), ('nodo1', 'aparecer', 160, 300, EASE_P),
                       ('nodo2', 'aparecer', 160, 400, EASE_P), ('foco', 'aparecer', 200, 500, EASE_P)]),
    'bruno-builder': dict(name='Bruno', role='functional-builder', verb='conectar', symbol='🥐', accent='#E5A447', light='#A46A17',
                          desc='avatar del agente Bruno (construcción funcional): módulo + dos puertos, props entra y events sale',
                          piezas=bruno, sw=2, sw_av=2.5, sw_tile=2.75, esc=.84, dur=660, rtl='fixed',
                          anim=[('modulo', 'trazar', 340, 0, EASE_T), ('entrada', 'trazar', 180, 300, 'cubic-bezier(.3,0,.2,1)'),
                                ('salida', 'trazar', 180, 480, 'cubic-bezier(.3,0,.2,1)')]),
    'mora': dict(name='Mora', role='documentation', verb='catalogar', symbol='🫐', accent='#8468E8', light='#7D5FE7',
                 desc='avatar del agente Mora (documentación): tres módulos, documento, evidencia y registro, sobre una base',
                 piezas=mora, sw=2, sw_av=2, sw_tile=2, esc=.96, dur=660, rtl='fixed',
                 anim=[('base', 'trazar', 200, 0, EASE_T), ('documento', 'trazar', 220, 160, EASE_T),
                       ('evidencia', 'trazar', 220, 300, EASE_T), ('registro', 'trazar', 220, 440, EASE_T)]),
    'fruti-squad': dict(name='Fruti Squad', role='orchestrator', verb='orquestar', symbol='🍓', accent='#F8F8F5', light='#161616',
                        core='#B7F34D', desc='icono del orquestador: cinco módulos en espiral alrededor del núcleo',
                        piezas=fruti, sw=FS_W, sw_av=FS_W, sw_tile=FS_W, esc=.86, dur=1040, rtl='fixed', anim=None),
}


def build(id_):
    a = AG[id_]
    d = id_ if id_ != 'fruti-squad' else 'fruti-squad'
    os.makedirs(f'{d}/svg', exist_ok=True)
    mod = a['verb']
    css = (lambda sw: fruti_css(sw)) if id_ == 'fruti-squad' else (lambda sw: css_anim(id_, mod, a['anim'], sw))
    w = lambda p, s: open(f'{d}/svg/{p}', 'w').write(s)
    lbl = f'role="img" aria-label="{a["name"]}"'
    std = wrap(id_, a['piezas'](a['sw']), f'{a["sw"]:g}' if isinstance(a['sw'], int) else f'{a["sw"]:.2f}', 'currentColor', 'aria-hidden="true"', '', css(a['sw']))
    w(f'{id_}.svg', std)
    w(f'{id_}.large.svg', std)
    w(f'{id_}.small.svg', small(std))
    w(f'{id_}-animado-ejemplo.svg', std.replace(f'class="uva-icon uva-{id_}"', f'class="uva-icon uva-{id_} uva-{id_}--{mod}"'))
    swa = a['sw_av']
    body = a['piezas'](swa)
    if id_ == 'fruti-squad':
        def col(c_arm, c_core, extra=''):
            b = body.replace('fill="currentColor"', f'fill="{c_core}" stroke="{c_core}"')
            return wrap(id_, b, f'{swa:.2f}', c_arm, lbl, extra, css(swa))
        w(f'{id_}-oscuro.svg', col(a['accent'], a['core']))
        w(f'{id_}-claro.svg', col(a['light'], a['light']))
        auto = col(a['light'], a['light']).replace('</style>', f'.uva-{id_}{{stroke:{a["light"]}}}.uva-{id_}__nucleo{{fill:{a["light"]};stroke:{a["light"]}}}'
                                                     f'@media (prefers-color-scheme:dark){{.uva-{id_}{{stroke:{a["accent"]}}}.uva-{id_}__nucleo{{fill:{a["core"]};stroke:{a["core"]}}}}}</style>')
        w(f'{id_}-auto.svg', auto)
        multi = col(a['accent'], a['core'])
        for n, c in zip(['kiwi', 'lima', 'coco', 'bruno', 'mora'], ['#7FCF5B', '#C9F36B', '#C89A68', '#E5A447', '#8468E8']):
            multi = multi.replace(f'class="uva-{id_}__{n}"', f'class="uva-{id_}__{n}" stroke="{c}"')
        w(f'{id_}-multicolor.svg', multi)
        tb = body.replace('fill="currentColor"', f'fill="{a["core"]}" stroke="{a["core"]}"')
        w(f'{id_}-tile.svg', wrap_tile(id_, tb, f'{swa:.2f}', a['accent'], lbl, '', css(swa), a['esc']))
        w(f'{id_}-tile-animado.svg', wrap_tile(id_, tb, f'{swa:.2f}', a['accent'], lbl, f' uva-{id_}--{mod}', css(swa), a['esc']))
    else:
        def col(c):
            return wrap(id_, body.replace('fill="currentColor"', f'fill="{c}"'), f'{swa:g}', c, lbl, '', css(swa))
        w(f'{id_}-oscuro.svg', col(a['accent']))
        w(f'{id_}-claro.svg', col(a['light']))
        auto = col(a['light']).replace('</style>', f'.uva-{id_}{{stroke:{a["light"]}}}@media (prefers-color-scheme:dark){{.uva-{id_}{{stroke:{a["accent"]}}}}}</style>')
        # el relleno del foco (Coco) sigue al trazo con currentColor + color
        auto = auto.replace(f'fill="{a["light"]}"', 'fill="currentColor"').replace('</style>', f'.uva-{id_}{{color:{a["light"]}}}@media (prefers-color-scheme:dark){{.uva-{id_}{{color:{a["accent"]}}}}}</style>')
        w(f'{id_}-auto.svg', auto)
        swt = a['sw_tile']
        tb = a['piezas'](swt).replace('fill="currentColor"', f'fill="{a["accent"]}"')
        w(f'{id_}-tile.svg', wrap_tile(id_, tb, f'{swt:g}', a['accent'], lbl, '', css(swt), a['esc']))
        w(f'{id_}-tile-animado.svg', wrap_tile(id_, tb, f'{swt:g}', a['accent'], lbl, f' uva-{id_}--{mod}', css(swt), a['esc']))


if __name__ == '__main__':
    for k in AG:
        build(k)
        print('ok', k)
