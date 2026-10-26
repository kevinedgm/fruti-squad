# Brief funcional · consulta-expediente (componentes) · r01

**Ruta:** R1 (una dirección ya elegida, separada en componentes) · **Fidelidad:** F2 · **Fecha:** 2026-10-26
**Fuentes leídas:** capturas actuales de la consulta (`../../referencia/1-5`), prototipo `../../p1-marco.html` (marco, paso 1, paso 2, videoconsulta), `../../auditoria-wcag.md`, shell de Expediente (`../../../shell/gen.py`), guía `../../../referencias/WCAG-Design-Reference.md`, conversación con el usuario.

## Enunciado
El médico (≈40 % mayor de 50 años, viene de Word o libreta) necesita **registrar una consulta completa** (exploración, diagnóstico, tratamiento, estudios y receta) mientras atiende al paciente en persona o por video, porque hoy la pantalla mezcla herramientas, pestañas y datos sin jerarquía y es fácil perderse.

## Pregunta de diseño
¿Cada pieza de la consulta tiene una sola responsabilidad, estados completos y un comportamiento definido por espacio, de modo que pueda aprobarse y construirse por separado sin rediseñar las demás?

- **Verbo principal:** registrar la consulta.
- **Resultado verificable:** la consulta queda con padecimiento, al menos un diagnóstico y su tratamiento, y el paso 4 permite terminarla (prototipo 4, pendiente).
- **Dato/acción dominante:** el paso actual de la consulta; acción primaria «Continuar» (una por vista).

## Usuarios y permisos
| Usuario | Necesita | Permiso |
|---|---|---|
| Médico | Registrar y terminar la consulta | Escritura en el expediente del paciente |
| Asistente | (incógnita) ¿captura signos vitales? | Incógnita |
| Paciente / tutor (teleconsulta) | Entrar a la llamada | Solo videollamada |

## Estados
Carga · vacío (sin diagnósticos, sin medicamentos, sin resultados) · error de validación · error al guardar · sin conexión · contenido largo · fuera de rango · contraindicación · controlado · llamada (espera, en curso, terminada, reconectando, sin permiso de cámara).

## Flujo anterior / posterior
Anterior: «Hoy» (agenda) → abrir cita. Posterior: receta y solicitudes entregadas; regreso a «Hoy».

## Riesgo por acción
| Acción | Tipo | Confirmación |
|---|---|---|
| Continuar / regresar de paso | Reversible | Ninguna (validación de obligatorios) |
| Quitar diagnóstico o medicamento | Con deshacer | Aviso con «Deshacer», sin tiempo límite |
| Agregar medicamento contraindicado | Riesgo clínico | Alerta + justificación obligatoria |
| Colgar videollamada | Reversible | Aviso «no termina la consulta»; «Volver a llamar» |
| Terminar consulta | Destructiva/legal | Revisión previa (prototipo 4) |

## Continuidad
| Situación | Comportamiento |
|---|---|
| Conexión lenta | Esqueleto con la misma huella; lo escrito sigue editable |
| Sin conexión | Aviso persistente; la nota se guarda local y se sincroniza; búsquedas de catálogo bloqueadas con mensaje |
| Error | Mensaje + «Reintentar»; nada de lo capturado se pierde |
| Sesión reanudada | Vuelve al paso en el que estaba (incógnita: expiración de sesión, 2.2.1) |
| Cambio de tamaño | Conserva paso, foco y herramienta abierta; la herramienta pasa de columna a ventana |

## Alcance MoSCoW
- **Must:** shell (riel), barra del paciente, pasos, panel del paso, signos vitales, padecimiento, buscador, diagnóstico, medicamento, contraindicación, deshacer, herramientas, videoconsulta.
- **Should:** ayuda de dosis por peso (requiere fuente validada), datos de la consulta anterior.
- **Could:** subtítulos traducidos.
- **Won't (esta ronda):** paso 3 (estudios), paso 4 (receta y cierre), antecedentes.

## Hechos · Supuestos · Incógnitas
**Hechos:** pasos y campos tomados de las capturas; herramientas de apoyo no son navegación (usuario); menú plegado durante la consulta (usuario); «DX escrito» = diagnóstico sin CIE-10 (usuario); catálogo COFEPRIS con bandera de controlado, contraindicaciones y medicamentos asociados a CIE-10 (usuario).
**Supuestos (declarados):** se requiere al menos un diagnóstico para continuar; rangos normales por edad disponibles; la ayuda de dosis por peso es propuesta.
**Incógnitas:** significado de los contadores «4 / 5» bajo signos vitales; expiración de sesión; si la asistente captura signos; proveedor de video y subtítulos en español.
