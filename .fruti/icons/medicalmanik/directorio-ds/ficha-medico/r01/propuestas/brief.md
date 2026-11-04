# Brief funcional · FichaMedico (directorio Manik) · r01

**Ruta:** R2 (Actual + A/B/C) · **Fidelidad:** F2 · **Fecha:** 2026-11-04
**Fuentes leídas:** conversación (decisiones del usuario 2026-11-04), sistema «Directorio Manik» v5 (`../../project/components/FichaMedico/`, `../../project/README.md`), manual del directorio v2 (`../../../manik-guia/guia.html`, sección Voz), panel de usuario r1 (estados del perfil), protocolo Kiwi (`agentes/kiwi/references/brief-funcional.md`, `fidelidad.md`, `wireframing.md`, `geometry-contract.md`, `validacion.md`, `.fruti/contracts/adaptativo.md`).

## Enunciado
Un paciente que busca especialista desde su celular (70 % del uso) necesita comparar médicos de la lista y elegir con quién agendar, porque decide por cercanía, precio, disponibilidad y confianza, y cada médico puede atender en varios consultorios con precio y forma de agendar propios.

## Pregunta de diseño
¿Puede el paciente saber, de un vistazo por ficha en un celular, **dónde** atiende (el consultorio que le conviene), **cuánto** cuesta ahí, **cuándo** hay lugar y **cómo** agendar, sin confundir datos de dos consultorios, y decidir entre agendar/llamar o abrir el perfil?

- **Verbo principal:** elegir (comparar fichas y elegir médico y consultorio).
- **Resultado verificable:** el paciente toca un horario y «Agendar» (pasa a confirmar la cita con ese consultorio), toca «Llamar» (se abre el marcador con el número de ese consultorio) o abre el perfil con ese consultorio preseleccionado.
- **Dato/acción dominante:** en disputa; es la pregunta de esta ronda. Actual y A: identidad del médico; B: el próximo lugar disponible; C: el consultorio.

## Usuarios y permisos
| Usuario | Necesita | Permiso |
|---|---|---|
| Paciente sin cuenta | Comparar y llegar a agendar o llamar | Ver directorio público |
| Paciente con cuenta | Lo mismo; agendar sin volver a capturar datos | Ver + agendar [supuesto] |
| Médico | No usa esta ficha; la ve en «Ver mi perfil público» del panel | — |

## Estados
Default · carga (skeleton) · vacío por filtros · error al cargar horarios (solo esa ficha) · sin conexión · horario recién ocupado · sin lugar en las próximas 2 semanas · contenido largo · sin foto (silueta mujer / hombre / neutra) · sin opiniones («Nuevo en Manik») · varios consultorios con formas mixtas (uno en línea, otro por teléfono).

## Flujo anterior / posterior
Anterior: búsqueda (qué + dónde) → lista de resultados con filtros. Posterior: confirmación de cita (consultorio y horario elegidos) · marcador del teléfono · perfil del médico con el consultorio preseleccionado.

## Riesgo por acción
| Acción | Tipo | Confirmación |
|---|---|---|
| Elegir horario | Reversible | Ninguna; el horario queda marcado |
| Agendar | Reversible (lleva a un paso de confirmación, no reserva aún) | En la pantalla siguiente |
| Llamar | Sale de Manik (marcador del teléfono) | Ninguna; el número va escrito antes |
| Copiar número | Reversible | Aviso breve «Número copiado» |
| Ver otro consultorio / perfil | Reversible | Ninguna |

## Continuidad
| Situación | Comportamiento |
|---|---|
| Conexión lenta | Skeleton con la misma huella; los horarios cargan después y la ficha ya es usable (perfil, llamar) |
| Sin conexión | Aviso arriba; fichas ya cargadas visibles; horarios ocultos («pueden haber cambiado»); «Agendar» deshabilitado con motivo; «Llamar» sigue disponible |
| Error | Solo falla el bloque de horarios: «No pudimos cargar los horarios · Reintentar»; el resto de la ficha funciona |
| Sesión reanudada | Vuelve a la lista con los mismos filtros, orden y posición |
| Cambio de tamaño | La ficha se recompone por el ancho de su contenedor; conserva el horario elegido y el foco |

## Alcance MoSCoW
- **Must:** nombre y especialidad; consultorio mostrado con distancia; precio de ESE consultorio; forma de agendar de ESE consultorio; próximo lugar; una acción principal; cédula verificada; avatar cuando no hay foto; aviso de que hay más consultorios.
- **Should:** calificación y número de opiniones; hasta 3 horarios en la ficha; «Nuevo en Manik».
- **Could:** enfoque o subespecialidad; ver otro consultorio sin salir de la lista.
- **Won't (esta ronda):** mapa dentro de la ficha, opiniones escritas, todos los horarios, favoritos, comparar médicos, anuncios.

## Hechos · Supuestos · Incógnitas
**Hechos:** 70 % celular y tableta / 30 % escritorio (usuario). Precio y forma de agendar son de cada consultorio (usuario). Sin foto, silueta de médica u médico (usuario). Voz del manual: «primero quién, dónde, cuándo, cuánto cuesta». Ficha actual del sistema v5. WCAG 2.2 AA obligatorio.
**Supuestos (declarados):** la lista muestra por médico el consultorio más cercano que cumpla los filtros; un solo precio de consulta por consultorio; la distancia se calcula desde el «dónde» de la búsqueda; agendar en línea lleva a una pantalla de confirmación; silueta neutra cuando el perfil no dice «Dr.»/«Dra.».
**Incógnitas (cambian la estructura):**
1. ¿Un precio por consultorio o varios por tipo de consulta (primera vez, subsecuente, en línea)? Cambia el bloque de precio.
2. ¿Qué pasa cuando un consultorio en línea no tiene lugar en 2 semanas: se muestra otro consultorio con lugar, o se muestra igual con «Sin lugar»?
3. ¿Existe la consulta por video? Sería otra «forma de agendar» y otro tipo de lugar.
4. ¿Hace falta cuenta para agendar? Cambia lo que pasa después de «Agendar».
