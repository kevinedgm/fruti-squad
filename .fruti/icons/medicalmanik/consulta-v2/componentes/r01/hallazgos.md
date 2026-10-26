# Hallazgos · consulta-expediente · componentes · r01

| Sev. | Hallazgo | Decisión | Responsable | Siguiente acción |
|---|---|---|---|---|
| Alta | El prototipo hi-fi (`../../p1-marco.html`) se construyó antes de aprobar la estructura por componentes: el protocolo pide lo contrario. | Congelar el hi-fi como referencia visual y aprobar la estructura aquí, componente por componente. | kiwi / usuario | Aprobar o corregir C00–C13. |
| Alta | Se desconoce si es obligatorio al menos un diagnóstico para continuar. | Se mantiene como supuesto (C03, C08). | producto | Confirmar con el usuario. |
| Alta | Se desconoce la expiración de sesión durante una consulta (WCAG 2.2.1). | Pendiente: aviso previo y extensión si expira. | producto | Confirmar política de sesión. |
| Media | Contadores «4 / 5» bajo cada signo vital sin significado conocido. | Quitados en C05 hasta saber qué son. | producto | Preguntar al usuario. |
| Media | Ayuda de dosis por peso sin fuente clínica validada. | Rotulada «propuesta» en C09. | producto / clínica | Definir fuente o quitarla. |
| Media | «Dato de la consulta anterior» (3.3.7) depende de que exista la consulta previa en el sistema. | Rotulado «supuesto» en C05. | coco | Confirmar datos disponibles. |
| Media | Subtítulos en vivo (1.2.4) dependen del proveedor de video. | Mantener control «Subtítulos» marcado como automático. | coco | Verificar proveedor y español. |
| Baja | Quién captura signos vitales (¿asistente?). | Sin cambios de permisos en esta ronda. | producto | Confirmar roles. |
| Baja | Pasos 3, 4 y Antecedentes sin wireframe. | Fuera de alcance de r01. | kiwi | Siguiente ronda. |
