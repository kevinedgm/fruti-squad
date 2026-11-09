# Ecosistema Manik · tipografía aprobada el 2026-11-09: sustitutos libres de la tipografía de marca.
# Outfit (en lugar de Filson Pro) en marca, títulos, subtítulos y botones; Lexend (en lugar de Scandia) en párrafos, interfaz y datos.
# Las dos tienen la «a» de un piso, como Filson Pro en el logotipo; Lexend distingue I, l y 1 (su I lleva remates).
# Rondas: ../tipografia-r01, ../tipografia-r02. Paso idempotente sobre project/; build.py lo llama al final.
import os, re, json, glob, datetime
D = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(D, 'project')
URL_OLD = 'family=Urbanist:wght@300..700&family=Atkinson+Hyperlegible+Next:wght@400;500;600;700'
URL_NEW = 'family=Outfit:wght@300..700&family=Lexend:wght@300..700'
FAM_D = '"Outfit", "Segoe UI", system-ui, sans-serif'
FAM_S = '"Lexend", system-ui, -apple-system, "Segoe UI", sans-serif'
SUST = [(URL_OLD, URL_NEW),
        ('"Urbanist", "Segoe UI", system-ui, sans-serif', FAM_D),
        ('"Atkinson Hyperlegible Next", "Atkinson Hyperlegible", system-ui, -apple-system, "Segoe UI", sans-serif', FAM_S),
        ('"Urbanist",', '"Outfit",'), ('"Atkinson Hyperlegible Next",', '"Lexend",'),
        ('Urbanist para la marca, como el directorio Manik; Atkinson Hyperlegible Next para cada dato.', 'Outfit para la marca y los títulos; Lexend para cada dato.')]
for f in glob.glob(os.path.join(P, 'components', '*', 'preview.html')):
    s = open(f).read(); o = s
    for a, b in SUST: s = s.replace(a, b)
    s = re.sub(r'(\.btn\{[^}]*font:600 15px/20px )var\(--font-sans\)', r'\1var(--font-display)', s)  # botones (CTA) en la letra de marca
    s = s.replace('font:600 15px/20px var(--font-sans,"Lexend",sans-serif);border:1px solid transparent;cursor:pointer', 'font:600 15px/20px var(--font-display,"Outfit",sans-serif);border:1px solid transparent;cursor:pointer')
    if s != o: open(f, 'w').write(s)
README_COMP = [('Urbanist 600', 'Outfit 600'), ('Urbanist 300', 'Outfit 300'), ('Atkinson distingue I, l y 1', 'Lexend distingue I, l y 1'), ('(Atkinson 600', '(Lexend 600'),
               ('Atkinson en todo el texto: distingue 1, l e I, y 0 y O.', 'Lexend en todo el texto: su I con remates la distingue de l y 1.')]
for f in glob.glob(os.path.join(P, 'components', '*', 'README.md')):
    s = open(f).read(); o = s
    for a, b in README_COMP: s = s.replace(a, b)
    if s != o: open(f, 'w').write(s)
tp = os.path.join(P, 'tokens.json'); T = json.load(open(tp)); ty = T['type']
ty['families'] = {'display': FAM_D, 'sans': FAM_S}
g1, g2 = ty['groups'][0], ty['groups'][1]
g1['name'] = 'Primaria · Outfit'
g1['note'] = 'Sustituto libre de Filson Pro (la letra del logotipo, con la misma «a» de un piso): marca, saludos, títulos, subtítulos y botones. 300 grande solo en portada e inicio; 600 en títulos, nombres de app y botones. Nunca en párrafos, tablas ni valores clínicos.'
g2['name'] = 'Secundaria · Lexend'
g2['note'] = 'Sustituto libre de Scandia: párrafos, interfaz y todo dato clínico. Su I lleva remates y se distingue de l y 1 en dosis, folios y claves; la «a» es de un piso, como en los títulos. Cifras tabulares (font-variant-numeric: tabular-nums) en tablas y valores.'
bt = [s for s in g2['styles'] if s['name'] == 'button']
if bt:
    g2['styles'] = [s for s in g2['styles'] if s['name'] != 'button']
    b = bt[0]; b['usage'] = 'Botones y llamados a la acción, en la letra de marca.'; g1['styles'].append(b)
json.dump(T, open(tp, 'w'), indent=1, ensure_ascii=False)
rp = os.path.join(P, 'README.md'); R = open(rp).read()
R = R.replace('Comparte la identidad del directorio Manik (Urbanist, cian del pin y fondos de luz) en la marca, la portada, el inicio de sesión, el inicio del ecosistema y los títulos. Dentro de cada app manda la legibilidad clínica: Atkinson en interfaz y datos, y el botón en azul Manik.',
              'Comparte con el directorio Manik el cian del pin y los fondos de luz en la marca, la portada, el inicio de sesión y el inicio del ecosistema. La letra es Outfit en marca, títulos y botones, y Lexend en interfaz y datos: sustitutos libres de Filson Pro y Scandia. Dentro de cada app manda la legibilidad clínica y el botón va en azul Manik.')
SEC = '''## Tipografía

Aprobada el 2026-11-09: sustitutos libres de la tipografía de marca (Filson Pro y Scandia son de licencia comercial). Las dos tienen la «a» de un piso, como Filson Pro en el logotipo.

- **Primaria · Outfit** (Google Fonts), en lugar de Filson Pro: marca, saludos, títulos, subtítulos y botones. 300 grande en portada e inicio; 600 en títulos, nombres de app y botones. Nunca en párrafos, tablas ni datos clínicos.
- **Secundaria · Lexend** (Google Fonts), en lugar de Scandia: párrafos, interfaz y todo dato. Su I lleva remates y se distingue de l y 1; en un expediente eso evita leer mal una dosis o una clave.
- Cifras tabulares (`font-variant-numeric: tabular-nums`) en tablas, dosis y signos.
- Piso de 13 px: nada clínico por debajo.
- Carga: `family=Outfit:wght@300..700&family=Lexend:wght@300..700`.
- El logotipo sigue siendo el vector original en Filson Pro; no se escribe «MedicalManik» con Outfit.

'''
R = re.sub(r'## Tipografía\n.*?(?=\n## )\n', SEC, R, flags=re.S)
if '**Tipografía (2026-11-09):**' not in R:
    R = R.replace('1. **Tipografía:** de Ubuntu a Urbanist (títulos) + Atkinson Hyperlegible Next (interfaz y datos).',
                  '1. **Tipografía:** de Ubuntu a Urbanist (títulos) + Atkinson Hyperlegible Next (interfaz y datos).\n   **Tipografía (2026-11-09):** Outfit (títulos y botones) + Lexend (interfaz y datos), sustitutos de Filson Pro y Scandia.')
open(rp, 'w').write(R)
jp = os.path.join(P, 'design-system.json'); J = json.load(open(jp))
J['lastChange'] = {'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'by': 'Kevin', 'via': 'Claude Code',
                   'note': 'Tipografía: Outfit (títulos, subtítulos y botones) y Lexend (texto y datos), sustitutos libres de Filson Pro y Scandia con la misma «a» de un piso.'}
json.dump(J, open(jp, 'w'), indent=2, ensure_ascii=False)
print('ok')
