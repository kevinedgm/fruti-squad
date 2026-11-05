# Lleva el diálogo aprobado (r02) al design system: components/Dialogo/{preview.html,README.md}. Uso: python3 componente.py <carpeta project>
import os, sys, re, json, importlib.util
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(sys.argv[1], 'components', 'Dialogo'); os.makedirs(OUT, exist_ok=True)
spec = importlib.util.spec_from_file_location('r02', os.path.join(D, 'gen.py')); G = importlib.util.module_from_spec(spec); spec.loader.exec_module(G)
# estilos de texto como variables locales, a partir de los tokens de tipografía (mismos valores que tokens.json)
TV = ';'.join(f"--t-{n}:{s['fontWeight']} {s['fontSize']}/{s['lineHeight']} var(--font-{fam})" for n, (fam, s) in G.TY.items())
css = G.CSS.split('/* ===== diálogo */')[1].split('/* anatomía')[0]
css = re.sub(r'@media\(max-width:640px\)\{.*', '', css, flags=re.S)
TRAB_HEAD = G.header('neutro', 'flask-conical', 'Bitácora · BIT-02-01 · Rev. 01', '% Alcohol por volumen', 'Vigente desde el 1 de octubre de 2021 · NOM-070-SCFI-2016', hid='p1')
html = f'''<!-- @dsCard group="Overlays" height=760 width=1000 -->
<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Google+Sans+Code:wght@400;500;600&display=swap"><style>
*{{box-sizing:border-box}}html,body{{margin:0}}body{{{TV};background:rgba(20,27,51,.55);color:var(--text);font:var(--t-body);padding:24px;display:grid;gap:24px}}
.i{{flex:none}}.mono{{font-family:var(--font-datos);font-variant-numeric:tabular-nums}}.vh{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
{css}
.fila{{display:grid;grid-template-columns:repeat(2,minmax(0,440px));gap:24px}}
@media (max-width:960px){{.fila{{grid-template-columns:minmax(0,1fr)}}}}
</style></head><body>
<div class="dlg big" role="dialog" aria-labelledby="p1">{TRAB_HEAD}<div class="bd"><p class="txt">Cuerpo del diálogo de trabajo: secciones con título, campos y el resultado sobre el lienzo.</p></div><footer class="ft"><small>Al registrar, la bitácora pasa a visto bueno.</small><button class="btn s">Cerrar</button><button class="btn p">Registrar lecturas</button></footer></div>
<div class="fila">{G.AVISO}{G.RECHAZO}</div></body></html>'''
open(os.path.join(OUT, 'preview.html'), 'w').write(html)
roles = ''.join(f"| {r} | `{s}` ({G.TY[s][1]['fontSize']}/{G.TY[s][1]['lineHeight']} · {G.TY[s][1]['fontWeight']}) | `{col}` | {G.c(col, 'surface')} | {u} |\n" for r, s, col, u, m in G.ROLES)
md = f'''# Dialogo

Ventana sobre la página para trabajar un registro o tomar una decisión. Dos tamaños, una sola estructura: encabezado, cuerpo y pie. La identidad está en el encabezado: avatar con el color del tono, contexto en azul, título y subtítulo.

## Anatomía del encabezado
1. **Avatar**: 48 × 48, radio `radius-lg`, fondo suave del tono e ícono de 24 en el color del tono.
2. **Contexto**: `overline` en `primary`, mayúsculas, +0.06 em. Tipo de diálogo y código (BITÁCORA · BIT-02-01).
3. **Título**: `title-1` en `text`. Lo que se hace o se decide.
4. **Subtítulo**: `body` en `text-muted`. Una frase: vigencia, norma, folio.
5. **Cerrar**: 40 × 40, sin fondo, `text-muted`. Esc también cierra.

Encabezado, cuerpo y pie sobre `surface`, con márgenes de 24 y filete `border` entre ellos. El borde izquierdo del contenido coincide con el del avatar. Los datos agrupados (promedio, resumen) van sobre `bg`, radio `radius-md`.

## Tonos
| Tono | Avatar | Botón principal | Cuándo |
|---|---|---|---|
| Neutro | `primary-soft` / `primary` | `primary` | Trabajar un registro, confirmar, enviar |
| Aviso | `alerta-soft` / `alerta` | `primary` | Fuera de plazo, cerca del límite, requiere justificación |
| Destructivo | `fuera-soft` / `fuera` | `fuera` | Rechazar, cancelar, eliminar: no se deshace |
| Éxito | `conforme-soft` / `conforme` | `primary` («Listo») | Confirmación después de registrar |

El tono solo cambia el avatar y, si es destructivo, el botón. La estructura no cambia.

## Tipografía
| Papel | Estilo | Color | Sobre blanco | Uso |
|---|---|---|---|---|
{roles}
El peso separa niveles (600 títulos, 500 etiquetas y datos, 400 texto); el color separa importancia (tinta para leer, gris para acompañar, azul para contexto y acción).

## Medidas y capas
- Ancho: trabajo 720 px, decisión 440 px. En celular, hoja inferior a todo el ancho; avatar de 40.
- Separaciones: avatar ↔ texto 16 · secciones 24 · campos 16 · etiqueta ↔ campo 6.
- Sombras: `shadow-overlay` en el diálogo, `shadow-inset` en campos, `shadow-primary` en el botón principal.
- Velo detrás del diálogo: tinta al 55 %.

## Pie
Ayuda opcional a la izquierda (`caption`, `text-muted`); a la derecha la secundaria y una sola principal. Verbo + objeto: «Registrar lecturas», «Rechazar bitácora».

## Accesibilidad
- `role="dialog"` (trabajo) o `role="alertdialog"` (decisión) con `aria-modal="true"` y `aria-labelledby` al título.
- Al abrir, el foco va al primer campo o, si no hay, al título; el foco queda atrapado dentro y vuelve al botón que lo abrió al cerrar.
- Esc y «Cerrar»/«Cancelar» cierran sin cambios. En destructivos el botón principal nunca es el foco inicial.
- El tono nunca es la única señal: el título y el texto dicen la consecuencia.

Aprobado el 2026-11-05 (ronda `dialogos-r02`).
'''
open(os.path.join(OUT, 'README.md'), 'w').write(md)
print('ok', OUT)
