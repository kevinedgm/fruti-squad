# Brief funcional · Inicio del directorio Manik · r01

**Ruta:** R1 (una dirección; el inicio del prototipo no estaba aprobado) · **Fidelidad:** F0 (flujo) + F2 (estructura) · **Fecha:** 2026-11-04
**Fuentes leídas:** pedido del usuario; sistema «Directorio Manik» (README: voz, celular primero, consultorios); manual del directorio v2 (voz, fotografía); prototipo actual (`../../../directorio-prototipo/`); FichaMedico aprobada (`../../ficha-medico/r03/aprobacion.md`); protocolo Kiwi (`brief-funcional.md`, `user-flow.md`, `fidelidad.md`, `wireframing.md`, `geometry-contract.md`, `validacion.md`, `.fruti/contracts/adaptativo.md`).

## Enunciado
Una persona que llega a Manik por primera vez (prospecto) o que regresa (paciente) necesita saber en segundos qué es Manik y empezar a buscar médico, porque llega con una necesidad de salud concreta y poca paciencia, casi siempre desde el celular (70 %).

## Pregunta de diseño
¿Entiende el prospecto en un vistazo qué puede hacer aquí (encontrar médico verificado, ver precio y agendar en el consultorio) y llega a resultados con una búsqueda útil en uno o dos toques, aunque no sepa qué especialista necesita?

- **Verbo principal:** buscar (encontrar médico).
- **Resultado verificable:** la persona llega a resultados de una especialidad cerca de ella, o al perfil de un médico que buscó por nombre, o al detalle de su próxima cita.
- **Acción dominante:** el buscador («¿Qué necesitas?»).

## Usuarios
| Usuario | Llega para | En el inicio necesita |
|---|---|---|
| Prospecto que sabe qué especialista quiere | Buscar | El buscador, nada más |
| Prospecto que no sabe a quién ir | Orientarse | Entrar por lo que siente (síntomas y categorías) |
| Prospecto que duda de Manik | Confiar | Qué es, cómo funciona, por qué confiar, que es gratis |
| Paciente que regresa con cita | Revisar su cita | Su próxima cita arriba [supuesto: existe cuenta] |
| Médico | Aparecer en Manik | Una entrada discreta «Soy médico» |

## Estados
Primera visita · regresa con cita próxima [supuesto] · ubicación aproximada (sin permiso) · ubicación denegada · carga · sin conexión · búsqueda sin resultados cerca.

## Flujo anterior / posterior
Ver `flujo.md`. Dato clave: muchos prospectos **no entran por el inicio**: llegan a resultados o al perfil desde un buscador o un enlace compartido. El inicio sirve sobre todo a quien escribe la dirección, abre la app o vuelve.

## Riesgo por acción
| Acción | Tipo | Confirmación |
|---|---|---|
| Buscar, elegir categoría, abrir perfil | Reversible | Ninguna |
| Usar mi ubicación | Pide permiso del navegador | Solo cuando la persona toca «Usar mi ubicación», nunca al entrar |
| Cancelar la próxima cita (desde su detalle) | Destructiva | Diálogo con la consecuencia («El consultorio liberará el horario») [fuera de esta pantalla] |

## Continuidad
| Situación | Comportamiento |
|---|---|
| Conexión lenta | El buscador y las categorías se ven al instante (sin datos remotos); lo que depende de la ubicación carga después |
| Sin conexión | Aviso; buscar queda disponible como intención y avisa que se necesita conexión |
| Error | Si falla «Con lugar hoy cerca de ti», se oculta esa sección; el resto funciona |
| Sesión reanudada | Recuerda el último «Dónde» usado |
| Cambio de tamaño | Misma tarea en compact/medium/expanded; el buscador siempre arriba |

## Alcance MoSCoW
- **Must:** qué es Manik en una frase; buscador (qué + dónde); entrada por lo que sientes; confianza (cédula verificada, opiniones reales, gratis); «Soy médico».
- **Should:** cómo funciona en 3 pasos; especialidades frecuentes cerca; «Con lugar hoy cerca de ti» (muestra de médicos reales).
- **Could:** próxima cita del paciente que regresa (depende de cuentas); artículos y preguntas.
- **Won't (esta ronda):** mapa, promociones en el inicio, registro obligatorio, notificaciones.

## Hechos · Supuestos · Incógnitas
**Hechos:** 70 % celular. La cita es presencial; se agenda en Manik o por teléfono. Lema «Tu médico, a la mano». Voz de tú, sin tecnicismos.
**Supuestos:** el «Dónde» inicial es la ciudad aproximada (por IP) y la ubicación precisa solo se pide al tocar «Usar mi ubicación»; existe cuenta de paciente para mostrar la próxima cita; hay datos para «Con lugar hoy cerca de ti».
**Incógnitas (cambian la estructura):**
1. ¿El paciente tiene cuenta (iniciar sesión) o agenda sin cuenta? Decide si existe «Tu próxima cita» y «Entrar».
2. ¿Existen secciones de artículos y preguntas? Hoy aparecen en la navegación del prototipo sin contenido definido.
3. ¿En qué ciudades opera Manik al lanzar? Decide el «Dónde» por defecto y el mensaje fuera de cobertura.
