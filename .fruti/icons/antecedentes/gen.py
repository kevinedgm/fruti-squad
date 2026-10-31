# Uva · antecedentes clínicos (Expediente Manik), ronda 1: 8 conceptos × 3 variantes.
# Pedido del usuario (2026-10-31): iconos para alergias, personales no patológicos, personales patológicos, cirugías, vacunas,
# heredofamiliares, ginecoobstétricos y perinatales. Estilo: retícula 24, trazo 2 (el de Lucide en las apps Manik), puntas redondas.
# Uso: python3 gen.py → variantes/<id>-<v>.svg y banco.html
import os, math, json
D = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(D, 'variantes')
def puntadas():
    out = []
    for t in (0.2, 0.4, 0.6, 0.8):  # puntos sobre la curva M3 17 Q12 13 21 7 (aprox. cuadrática)
        x = (1-t)**2*3 + 2*(1-t)*t*12 + t*t*21; y = (1-t)**2*17 + 2*(1-t)*t*13 + t*t*7
        dx = 2*(1-t)*(12-3) + 2*t*(21-12); dy = 2*(1-t)*(13-17) + 2*t*(7-13); L = math.hypot(dx, dy); nx, ny = -dy/L, dx/L
        out.append(f'M{x-1.6*nx:.2f} {y-1.6*ny:.2f} L{x+1.6*nx:.2f} {y+1.6*ny:.2f}')
    return ' '.join(out)
# id: (nombre, [(variante, metáfora, hipótesis, cuerpo SVG)])
I = {
 'allergies': ('Alergias', [
  ('a', 'Flor con polen', 'El alérgeno clásico; se distingue por las motas que se desprenden.',
   '<circle cx="10" cy="8.5" r="4"/><path d="M10 8.5h.01"/><path d="M10 12.5V22"/><path d="M10 18c2.5 0 4-1.2 4.5-3.5"/><path d="M17.5 4h.01M20 8h.01M17 10.5h.01"/>'),
  ('b', 'Pastilla con admiración', 'Lo más crítico en el expediente: alergia a un medicamento. El signo de admiración dice «cuidado».',
   '<g transform="rotate(-45 9 15)"><rect x="3" y="12" width="12" height="6" rx="3"/><path d="M9 12v6"/></g><path d="M19.5 3v6"/><path d="M19.5 13h.01"/>'),
  ('c', 'Mano con ronchas', 'La reacción en la piel; mano de Lucide con puntos en la palma.',
   '<path d="M18 11V6a2 2 0 0 0-4 0"/><path d="M14 10V4a2 2 0 0 0-4 0v2"/><path d="M10 10.5V6a2 2 0 0 0-4 0v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-6-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/><path d="M12 14.5h.01M15.5 16.5h.01M12.5 18.5h.01"/>')]),
 'non-pathological-history': ('Personales no patológicos', [
  ('a', 'Persona con hoja', 'Hábitos y estilo de vida: la persona sana; la hoja dice «no es enfermedad».',
   '<circle cx="8.5" cy="7" r="3.5"/><path d="M2.5 21a6 6 0 0 1 12 0"/><path d="M21.5 9.5c-4 0-6.5 2-6.5 6 4 0 6.5-2 6.5-6z"/><path d="M15 15.5l3-3"/>'),
  ('b', 'Casa con corazón', 'Vivienda, entorno y hábitos del hogar; coincide en parte con house-heart de Lucide.',
   '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M12 18s-3.5-2-3.5-4.3a1.75 1.75 0 0 1 3.5-.7 1.75 1.75 0 0 1 3.5.7C15.5 16 12 18 12 18z"/>'),
  ('c', 'Manzana', 'Alimentación y hábitos saludables; muy reconocible, pero cubre solo una parte del concepto.',
   '<path d="M12 7.5c-1.6-1.2-5.2-1.6-6.6 1.4-1.3 2.8-.4 7 2 9.6 1.4 1.6 2.9 1.4 4.6.8 1.7.6 3.2.8 4.6-.8 2.4-2.6 3.3-6.8 2-9.6-1.4-3-5-2.6-6.6-1.4z"/><path d="M12 7.5c0-2 1-3.6 2.8-4.5"/>')]),
 'pathological-history': ('Personales patológicos', [
  ('a', 'Persona con cruz', 'Enfermedades de la persona: la misma persona de los no patológicos, con la cruz médica en lugar de la hoja.',
   '<circle cx="8.5" cy="7" r="3.5"/><path d="M2.5 21a6 6 0 0 1 12 0"/><path d="M18.5 9v7M15 12.5h7"/>'),
  ('b', 'Carpeta con cruz', 'El registro de enfermedades previas.',
   '<rect x="4.5" y="4" width="15" height="18" rx="2"/><path d="M9 2.5h6v3H9z"/><path d="M12 10v7M8.5 13.5h7"/>'),
  ('c', 'Termómetro', 'Enfermedad en general; riesgo: se lee como «fiebre» o «temperatura».',
   '<path d="M14 4v10.5a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0z"/><path d="M12 14v3"/><path d="M17 6h2M17 10h2"/>')]),
 'surgeries': ('Cirugías', [
  ('a', 'Bisturí', 'El instrumento de la cirugía; se distingue del cuchillo por la hoja curva y corta.',
   '<path d="M11 13 16.5 7.5C18 6 20 5 21.5 4.5 21 6 20 8 18.5 9.5L13 15z"/><path d="M12 14 4.5 21.5"/>'),
  ('b', 'Tijeras (Lucide)', 'Referencia de Lucide: dice «cortar» en cualquier software; choca con el dominio.',
   '<circle cx="6" cy="6" r="3"/><path d="M8.12 8.12 12 12M20 4 8.12 15.88"/><circle cx="6" cy="18" r="3"/><path d="M14.8 14.8 20 20"/>'),
  ('c', 'Cicatriz con puntadas', 'Lo que deja una cirugía: la incisión con sus puntadas. Propio de la consulta y difícil de confundir.',
   f'<path d="M3 17Q12 13 21 7"/><path d="{puntadas()}"/>')]),
 'vaccines': ('Vacunas', [
  ('a', 'Jeringa (Lucide)', 'Referencia de Lucide: inmediata, pero también significa «inyección» o «medicamento».',
   '<path d="m18 2 4 4"/><path d="m17 7 3-3"/><path d="M19 9 8.7 19.3c-1 1-2.5 1-3.4 0l-.6-.6c-1-1-1-2.5 0-3.4L15 5"/><path d="m9 11 4 4"/><path d="m5 19-3 3"/><path d="m14 4 6 6"/>'),
  ('b', 'Frasco ámpula', 'El frasco de la vacuna con su tapón; menos ambiguo que la jeringa.',
   '<rect x="9" y="2" width="6" height="3" rx="1"/><path d="M10 5v1.5a2 2 0 0 1-2 2V20a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2V8.5a2 2 0 0 1-2-2V5"/><path d="M8 14h8"/>'),
  ('c', 'Jeringa vertical con gota', 'La aplicación de la vacuna: jeringa de pie, aguja abajo y una gota; se separa de la jeringa diagonal de «medicamento».',
   '<path d="M9 2h6M12 2v4"/><rect x="9" y="6" width="6" height="10" rx="1"/><path d="M9 10h3M9 13h3"/><path d="M12 16v3.5"/><path d="M18.5 17.5c0 1-.7 1.8-1.5 1.8s-1.5-.8-1.5-1.8c0-.9 1.5-2.5 1.5-2.5s1.5 1.6 1.5 2.5z"/>')]),
 'family-history': ('Heredofamiliares', [
  ('a', 'Genograma', 'La convención médica: cuadrado padre, círculo madre, línea de unión y descendencia.',
   '<rect x="2.5" y="3" width="5.5" height="5.5" rx="1"/><circle cx="18.75" cy="5.75" r="2.75"/><path d="M8 5.75h8"/><path d="M12 5.75V14"/><circle cx="12" cy="17.5" r="3.5"/>'),
  ('b', 'ADN (Lucide)', 'Referencia de Lucide: herencia genética; para un médico puede sonar a «estudio genético».',
   '<path d="m10 16 1.5 1.5"/><path d="m14 8-1.5-1.5"/><path d="M15 2c-1.8 2-2.52 4-2.8 6"/><path d="m16.5 10.5 1 1"/><path d="m17 6-2.9-2.9"/><path d="M2 15c6.67-6 13.33 0 20-6"/><path d="m20 9 .9.9"/><path d="M3.1 14.1 4 15"/><path d="m6.5 12.5 1 1"/><path d="m7 18 2.9 2.9"/><path d="M9 22c1.8-2 2.52-4 2.8-6"/>'),
  ('c', 'Adulto y niño', 'Padre o madre con su hijo: «lo que viene de la familia». Se confunde con «usuarios».',
   '<circle cx="8" cy="6" r="3"/><path d="M2 21v-1a6 6 0 0 1 12 0v1"/><circle cx="17.5" cy="10.5" r="2.2"/><path d="M14 21v-.5a3.5 3.5 0 0 1 7 0v.5"/>')]),
 'gyneco-obstetric-history': ('Ginecoobstétricos', [
  ('a', 'Útero', 'El órgano que reúne gineco y obstetricia; esquemático para que sea clínico y no explícito.',
   '<path d="M7 7.5h10c0 5-2 8-4 9V21h-2v-4.5c-2-1-4-4-4-9z"/><path d="M7 7.5C6.3 5 5 4.3 3.5 5"/><path d="M17 7.5c.7-2.5 2-3.2 3.5-2.5"/><circle cx="3.75" cy="8.25" r="1.5"/><circle cx="20.25" cy="8.25" r="1.5"/>'),
  ('b', 'Embarazo de perfil', 'Lo obstétrico: silueta de perfil con el vientre.',
   '<circle cx="10.5" cy="4" r="2"/><path d="M10.5 7.5c-1.5 0-2.5 1-2.5 2.5v4l1.5 1.5V22"/><path d="M10.5 9c2.5 0 4 1.5 4.2 3.5 2.2.6 3.3 2 3.3 3.5 0 1.8-1.5 2.5-3.5 2.5H12V22"/>'),
  ('c', 'Símbolo femenino', 'Muy reconocible, pero dice «sexo: femenino», no «antecedentes ginecoobstétricos».',
   '<circle cx="12" cy="9" r="5.5"/><path d="M12 14.5V22M8.5 18.5h7"/>')]),
 'perinatal-history': ('Perinatales', [
  ('a', 'Bebé (Lucide)', 'Referencia de Lucide: claro, pero puede leerse como «pediatría».',
   '<path d="M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M15 12h.01"/><path d="M19.38 6.81A9 9 0 0 1 20.8 10.2a2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1"/><path d="M9 12h.01"/>'),
  ('b', 'Recién nacido envuelto', 'Perinatal es el nacimiento: el bebé envuelto en su manta.',
   '<circle cx="12" cy="6" r="3.5"/><path d="M7.5 13.5c0-2 2-3.5 4.5-3.5s4.5 1.5 4.5 3.5v4.5c0 2.5-2 4-4.5 4s-4.5-1.5-4.5-4z"/><path d="M7.5 15c3 0 6 1.3 9 3.5"/>'),
  ('c', 'Huella de pie', 'La huella del recién nacido que se toma al nacer.',
   '<path d="M9.5 22c-2.2 0-3.8-2.2-3.8-5.5 0-3.6 1.6-6.5 4.1-6.5s3.7 2.4 3.7 5.1c0 4-1.8 6.9-4 6.9z"/><path d="M7 6.8h.01M9.6 5.6h.01M12.3 6h.01M14.4 7.6h.01"/>')]),
}
os.makedirs(V, exist_ok=True)
def svg(id, v, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'class="uva-icon uva-{id}" aria-hidden="true" focusable="false"><style>.uva-{id}{{stroke-width:var(--uva-stroke,2)}}</style>{body}</svg>')
datos = []
for id, (nom, vs) in I.items():
    for v, met, hip, body in vs:
        s = svg(id, v, body); open(os.path.join(V, f'{id}-{v}.svg'), 'w').write(s)
        datos.append(dict(id=id, nom=nom, v=v, met=met, hip=hip, svg=s))
json.dump(datos, open(os.path.join(D, 'variantes.json'), 'w'), ensure_ascii=False, indent=1)
print(len(datos), 'variantes')
