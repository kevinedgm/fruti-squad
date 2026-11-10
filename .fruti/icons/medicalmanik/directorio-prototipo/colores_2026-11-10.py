# Directorio Manik · cambio de paleta a «Mi Médico Manik» (2026-11-10).
# Fuente: design system «Mi Médico Manik» (https://claude.ai/artifact/GeGQEx9qFjmmKyDSemA34R, tokens.json + README «Color»).
# Solo color: tipografía, radios y sombras siguen como estaban (pendiente de decidir).
# Uso: python3 colores_2026-11-10.py && python3 gen.py   (idempotente: si ya se aplicó, no cambia nada)
import os, re
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'plantilla.html')
s = open(P).read()
if '--teal:' in s:
    print('ya aplicado'); raise SystemExit

ROOT_NEW = """:root{
  /* Paleta «Mi Médico Manik» (2026-11-10). Nombres y valores del design system de origen. */
  --bruma:#F5FAFB;--blanco:#FFFFFF;--tinta:#14213D;--muted:#4A5674;--linea:#DCE4EA;--linea-control:#6B7590;
  --teal:#0A7F8F;--teal-hover:#08707F;--teal-presionado:#054E59;--pleca:#009499;--turquesa:#3ECEDD;--resaltador:#95E4EC;
  --menta-hielo:#D8F0F4;--turquesa-suave:#BFEBF1;--hero-inicio:#E3F5F8;--avatar-inicio:#9FE3EC;--luz-calida:#F5C9A6;
  --exito-suave:#E7F5EE;--exito:#157B4A;--exito-oscuro:#0E6338;--error-suave:#FDECEA;--error:#B42318;
  --no-disponible:#D9E3E7;--no-disponible-texto:#3F565E;--estrella:#F5B301;
  --lila-impulsa:#B9A8FF;--lila-suave:#EFEAFF;--violeta-impulsa:#504CA1;
  /* Locales sin equivalente en el sistema de origen (pendientes): texto claro sobre tinta y rojo presionado. */
  --confianza-texto:#C7D2E4;--error-presionado:#8A1C12;--velo:rgba(20,33,61,.38);"""
i = s.index(':root{'); j = s.index('--display:', i)
s = s[:i] + ROOT_NEW + '\n  ' + s[j:]

SUST = [
    # Acción: relleno y bordes en teal; texto en teal-hover (teal sobre bruma o menta-hielo no llega a 4.5:1)
    ('background:var(--cian-ui-hover)', 'background:var(--teal-hover)'),
    ('color:var(--cian-ui)', 'color:var(--teal-hover)'),
    ('--sc:var(--cian-ui)', '--sc:var(--teal-hover)'),
    ('var(--cian-ui)', 'var(--teal)'),
    ('.primario:hover{background:var(--teal-hover)}', '.primario:hover{background:var(--teal-hover)}.primario:active{background:var(--teal-presionado)}'),
    ('.secundario{background:var(--blanco);color:var(--teal-hover)', '.secundario{background:var(--blanco);color:var(--teal)'),
    ('.secundario:hover{background:var(--luz-cian)}', '.secundario:hover{background:var(--menta-hielo)}'),
    ('.horas button{font:600 15px var(--sans);font-variant-numeric:tabular-nums;color:var(--teal-hover)', '.horas button{font:600 15px var(--sans);font-variant-numeric:tabular-nums;color:var(--teal)'),
    # Fondos claros
    ('rgba(211,240,244,0)', 'rgba(216,240,244,0)'), ('rgba(255,239,210,0)', 'rgba(245,201,166,0)'),
    ('var(--luz-cian)', 'var(--menta-hielo)'),
    ('linear-gradient(180deg,var(--bruma) 0%,var(--blanco) 100%)', 'linear-gradient(180deg,var(--hero-inicio) 0%,var(--bruma) 100%)'),
    # Categorías: menta-hielo, luz-calida, turquesa-suave; trazo teal-hover salvo la cálida (tinta); leyenda siempre en tinta
    ('.cat:nth-child(3n+1){background:var(--cat-cian)}.cat:nth-child(3n+2){background:var(--cat-calida)}.cat:nth-child(3n){background:var(--cat-azul)}',
     '.cat:nth-child(3n+1){background:var(--menta-hielo)}.cat:nth-child(3n+2){background:var(--luz-calida)}.cat:nth-child(3n){background:var(--turquesa-suave)}'),
    ('.scat:nth-child(3n+1){--sf:var(--cat-cian);--sc:var(--teal-hover)}.scat:nth-child(3n+2){--sf:var(--cat-calida);--sc:var(--icono-calido)}.scat:nth-child(3n){--sf:var(--cat-azul);--sc:var(--tinta)}',
     '.scat:nth-child(3n+1){--sf:var(--menta-hielo);--sc:var(--teal-hover)}.scat:nth-child(3n+2){--sf:var(--luz-calida);--sc:var(--tinta)}.scat:nth-child(3n){--sf:var(--turquesa-suave);--sc:var(--teal-hover)}'),
    ('.sello .ley{fill:var(--sc);', '.sello .ley{fill:var(--tinta);'),
    # Miniaturas de artículos: sin luz-calida junto a otro pastel
    ('background:var(--cat-cian);color:var(--teal-hover)}', 'background:var(--menta-hielo);color:var(--teal-hover)}'),
    ('.q.art:nth-of-type(even) .th{background:var(--cat-calida)', '.q.art:nth-of-type(even) .th{background:var(--turquesa-suave)'),
    # Avatar sin foto y marcadores de foto
    ('.face{border-radius:16px;aspect-ratio:3/4;overflow:hidden;background:linear-gradient(160deg,var(--foto-inicio),var(--foto-fin))',
     '.face{border-radius:16px;aspect-ratio:3/4;overflow:hidden;background:linear-gradient(160deg,var(--avatar-inicio),var(--luz-calida))'),
    ('linear-gradient(160deg,var(--foto-inicio),var(--foto-fin))', 'linear-gradient(160deg,var(--hero-inicio),var(--menta-hielo))'),
    # Bloque oscuro de confianza
    ('color:var(--confianza-icono)', 'color:var(--turquesa)'),
    # Desactivado y fondos neutros (antes «lavado»)
    ('.primario[aria-disabled="true"]{background:var(--lavado);color:var(--muted)', '.primario[aria-disabled="true"]{background:var(--no-disponible);color:var(--no-disponible-texto)'),
    ('.estado.gris{background:var(--lavado);color:var(--muted)}', '.estado.gris{background:var(--no-disponible);color:var(--no-disponible-texto)}'),
    ('style="background:var(--lavado);color:var(--muted)"', 'style="background:var(--no-disponible);color:var(--no-disponible-texto)"'),
    ('.ib:hover{background:var(--lavado)}', '.ib:hover{background:var(--menta-hielo)}'),
    ('.cmsg{background:var(--lavado)', '.cmsg{background:var(--menta-hielo)'),
    ('display:block;background:var(--lavado)}', 'display:block;background:var(--lila-suave)}'),
    # Impulsa: lila solo en promociones
    ('.etq{justify-self:start;font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--texto-calido);background:var(--luz-calida)',
     '.etq{justify-self:start;font-size:12px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--tinta);background:var(--lila-impulsa)'),
    ('.aplicada{display:flex;gap:8px;align-items:center;flex-wrap:wrap;background:var(--luz-calida)', '.aplicada{display:flex;gap:8px;align-items:center;flex-wrap:wrap;background:var(--lila-suave)'),
    ('<span class="nw">con Impulsa Manik</span>', '<span class="nw imp">con Impulsa Manik</span>'),
    ('.impulsa b{color:var(--tinta);font-weight:600}', '.impulsa b{color:var(--violeta-impulsa);font-weight:600}.imp{color:var(--violeta-impulsa);font-weight:600}'),
    ('.ad{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;background:var(--luz-calida)', '.ad{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;background:var(--lila-suave)'),
    ('.ad .lbl{font-weight:700;font-size:13px;line-height:18px;color:var(--texto-calido);background:var(--blanco)', '.ad .lbl{font-weight:700;font-size:13px;line-height:18px;color:var(--tinta);background:var(--lila-impulsa)'),
    # Etiqueta de propuesta: énfasis en tinta con texto blanco
    ('.prop{display:inline-flex;gap:6px;align-items:center;justify-self:start;font-size:13px;font-weight:600;color:var(--texto-calido);background:var(--luz-calida)',
     '.prop{display:inline-flex;gap:6px;align-items:center;justify-self:start;font-size:13px;font-weight:600;color:var(--blanco);background:var(--tinta)'),
    # Cédula y opinión verificadas: escudo en teal-hover sobre menta-hielo, no etiqueta verde
    ('.meta .v{color:var(--on-exito-suave);font-weight:600;background:var(--exito-suave)}', '.meta .v{color:var(--teal-hover);font-weight:600;background:var(--menta-hielo)}'),
    ('.ced .ico{flex:none;width:16px;height:16px;margin-top:1px;color:var(--on-exito-suave)}', '.ced .ico{flex:none;width:16px;height:16px;margin-top:1px;color:var(--teal-hover)}'),
    ('.op .ver{display:inline-flex;align-items:center;gap:5px;font-size:13px;font-weight:600;color:var(--on-exito-suave)}', '.op .ver{display:inline-flex;align-items:center;gap:5px;font-size:13px;font-weight:600;color:var(--teal-hover)}'),
    # Éxito y error con tokens
    ('var(--on-exito-suave)', 'var(--exito)'),
    ('.ocupado b{color:#8A1C12}', '.ocupado b{color:var(--error)}'),
    ('background:#FDECEA', 'background:var(--error-suave)'),
    ('.btn.rojo:hover{background:#8A1C12}', '.btn.rojo:hover{background:var(--error-presionado)}'),
    ('#B42318', 'var(--error)'),
]
for a, b in SUST:
    if a not in s:
        raise SystemExit('no encontrado: ' + a[:90])
    s = s.replace(a, b)

# Ilustraciones de ejemplo (portadas, banners, foto simulada): mismos tonos, valores nuevos
for a, b in [('#D3F0F4', '#D8F0F4'), ('#FFEFD2', '#F5C9A6'), ('#9FDCE5', '#9FE3EC'), ('#00788A', '#0A7F8F')]:
    s = s.replace(a, b)

rest = re.findall(r'var\(--(cian|cian-ui|cian-ui-hover|luz-cian|lavado|cat-cian|cat-calida|cat-azul|texto-calido|icono-calido|foto-inicio|foto-fin|confianza-icono|on-exito-suave)\)', s)
if rest:
    raise SystemExit('quedan tokens viejos: ' + ', '.join(sorted(set(rest))))
open(P, 'w').write(s); print('ok')
