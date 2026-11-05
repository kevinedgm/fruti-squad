# Bitácora % Alcohol por volumen (BIT-02-01) · brief · r01

Ruta R1 (una dirección) · Fidelidad F3 con el sistema real: design system NisaLab v3 (25 colores, Poppins + Google Sans Code).
Fuente: HTML del modal de producción que pegó el usuario (no se guarda; solo se usa su contenido y estructura).

**Enunciado.** El analista necesita registrar tres lecturas de alcohol y temperatura de una muestra porque la bitácora es el registro controlado del ensayo (NOM-070-SCFI-2016).
**Pregunta de diseño.** ¿Se puede ver de un vistazo si la captura cumple el criterio (repetibilidad) antes de registrar, sin perder el orden actual del formulario?
**Verbo principal.** Registrar lecturas. **Resultado verificable.** Promedio calculado + repetibilidad dentro de ±0.1 % alc. vol. + bitácora registrada.

Datos: código BIT-02-01, revisión 01, vigencia 01-oct-2021; equipo (Densímetro digital Anton Paar, DD-01); fecha de análisis (obligatoria); 3 corridas × (alc. vol., temperatura °C); U exp (0.02); promedio y repetibilidad automáticos; referencia de evaluación (35–55 % alc. vol.); observaciones; adjuntos (máx. 10 × 10 MB); criterio de aceptación (repetibilidad ±0.1, reproducibilidad ±0.2); firmas (analista, visto bueno).
Estados: nueva · capturada conforme · repetibilidad fuera de criterio · reabierta por supervisión · firmada (solo lectura) · cierre fuera de plazo (aviso).
Riesgo: Registrar es reversible solo por reapertura de supervisión (no destructivo, pero deja registro).

Hechos / supuestos / incógnitas
- Hecho: el modal actual muestra «Selecciona una fecha válida» en rojo antes de que el analista toque el campo.
- Hecho: «Pendiente» de firma usa ámbar; el sistema dice que pendiente es gris (no urgente).
- Supuesto: repetibilidad = máximo − mínimo de las tres lecturas.
- Incógnita 1: si la repetibilidad está fuera de criterio, ¿se puede registrar igual (con observación) o se bloquea?
- Incógnita 2: ¿la reproducibilidad (±0.2) se evalúa en esta pantalla o contra otra bitácora?

Se conserva: orden de secciones, campos, textos normativos, acciones (Cerrar, Registrar).
Cambios declarados: ver declaracion.md.
