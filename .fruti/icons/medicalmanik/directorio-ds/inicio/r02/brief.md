# Brief funcional · Inicio del directorio Manik · r02 (delta sobre r01)

**Ruta:** R1 · **Fidelidad:** F0 + F2 · **Fecha:** 2026-11-04 · Brief base: `../r01/brief.md`.

## Respuestas del usuario (hechos nuevos)
1. **El paciente no tendrá cuenta.** → Se quitan «Entrar» y «Tu próxima cita». Quien agenda recibe confirmación y recordatorio por mensaje (SMS / WhatsApp [supuesto: canal]) con un enlace al detalle de su cita, donde puede cambiarla o cancelarla.
2. **Habrá artículos y preguntas.** → Nueva sección «Resuelve tus dudas» y entradas en la navegación.
3. **Opera en todo México y Centroamérica.** → No existe «fuera de cobertura»; existe **baja densidad** (pocos médicos cerca) y **variación por país**.

## Variación por país (hechos e inferencias)
| Qué cambia | Ejemplo | Consecuencia |
|---|---|---|
| Registro profesional | México: cédula profesional · Guatemala: colegiado activo [verificar el término de cada país] | La insignia no puede decir siempre «Cédula verificada» |
| Moneda | MXN $ · GTQ Q · HNL L · CRC ₡ · USD $ (El Salvador; Panamá usa balboa y dólar) | El precio lleva el símbolo del país; «$» es ambiguo entre MXN y USD |
| Teléfono | +52 · +502 · +503 · +504 · +505 · +506 · +507 · +501 | Formato y código por país |
| «Dónde» por defecto | Ciudad aproximada por la conexión | Ejemplo: «Cerca de Ciudad de Guatemala» |

## Cambios a la estructura
- Navegación: Especialidades · Preguntas · Artículos · Soy médico (sin «Entrar»).
- Nueva sección **Resuelve tus dudas**: 2 preguntas respondidas por médicos + 2 artículos, con «Ver más preguntas» y «Ver artículos» [qué es una «pregunta» se supone: un paciente pregunta y un médico verificado responde].
- «Con lugar hoy cerca de ti» con baja densidad: muestra lo que hay y amplía la distancia en el texto («a menos de 30 km»).

## Incógnitas nuevas
1. ¿Cómo se llama la verificación en cada país y qué etiqueta común usamos? Propuesta: «Registro verificado» como etiqueta común, con el nombre local en el perfil («Cédula profesional 1234567», «Colegiado activo 12345»).
2. ¿Canal del mensaje de confirmación: SMS, WhatsApp o ambos?
3. ¿Quién puede hacer una pregunta sin cuenta (pide celular o correo para avisar la respuesta)?
