# Convia · modelo de datos: perfil + actividad + sede

**Aprobado por el usuario (2026-10-31).** Resuelve dónde viven los eventos y talleres, y a quién se ligan los organizadores que no son ningún giro.

## Tres piezas
| Pieza | Qué es | Campos clave |
|---|---|---|
| **Perfil** (quién) | Quien recibe gente u organiza | `tipo`: `lugar` (café, restaurante, hotel, museo/galería) u `organizador` (estudio, operador de recorridos, maestro/a, colectivo); nombre, rasgos, contacto; `lugar` además: dirección, horario |
| **Actividad** (qué y cuándo) | Algo con fecha | `tipo`: taller · recorrido · evento · exposición; `organizador` → perfil; `sede` → perfil `lugar` o dirección suelta; `fechas` (una o varias) **o** `rango` (exposiciones: del–al); precio (o «incluida con la entrada» / «entrada libre»); cupo |
| **Sede** (dónde) | Dónde pasa | perfil `lugar` o dirección |

## Reglas
- Toda actividad tiene **organizador** y **sede**. Aparece en el perfil del organizador («Organiza») y en el de la sede («Aquí pasa»), aunque sean distintos.
- «Talleres», «Recorridos» y «Eventos» del directorio son **tipos de actividad**, ordenados por fecha; cada tarjeta dice «Organiza: …» y «En: …».
- Actividad **pasada**: queda en el perfil con «N marcaron que fueron» (personas que marcaron «Ya fui» en Convia) y su «X de cada 10 volverían» si llega a 10.
- Perfil `organizador` sin local: se revisa con referencias o asistiendo a una actividad suya. [pendiente: operación]
- Nombre público del tipo `organizador`. [pendiente: «Organizadores», «Maestros y colectivos» o «Anfitriones»]

## Ejemplos
- Cata en un café → organiza el café, sede el café.
- Taller de un museo → organiza el museo, sede el museo.
- Maestra independiente da un taller en un museo → organiza ella, sede el museo: sale en los dos perfiles.
