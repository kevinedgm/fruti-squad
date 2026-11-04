# FotoMedico

La cara del médico en la ficha y el perfil.

- **Con foto:** 3:4 vertical, `radius-foto`. Reglas de la sección Fotografía: mínimo 900 × 1200 px; servida en WebP a 176 × 234 en la ficha de celular (≤ 20 KB, el 70 % del uso) y a 480 × 640 en perfil y ficha amplia (≤ 120 KB), con `srcset`, luz natural, fondo liso, sin filtros ni retoque que cambie rasgos.
- **Sin foto: avatar de silueta** (decisión 2026-11-04): médica o médico con bata y estetoscopio, en `silueta` sobre el degradado `foto-inicio` → `foto-fin`, mismo formato 3:4. Archivos en el grupo «Avatares».
- Cuál silueta: «Dra.» → mujer; «Dr.» → hombre; si el perfil no dice tratamiento ni sexo, la **neutra**. Nunca se adivina por el nombre.
- La silueta es un respaldo, no un perfil: el panel del médico le sigue pidiendo su foto («Los pacientes eligen con más confianza cuando ven tu cara»).
- Texto alternativo: con foto «Dra. Lucía Herrera, dermatóloga»; sin foto «Sin foto: Dra. Lucía Herrera».
- El consumidor provee: URL de la foto o el tipo de avatar, nombre y especialidad.
