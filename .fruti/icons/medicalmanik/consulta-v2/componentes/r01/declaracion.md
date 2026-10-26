# Declaración de cumplimiento · consulta-expediente · componentes · r01

| Campo | Valor |
|---|---|
| Ruta | R1 (dirección ya elegida, separada en componentes) |
| Fidelidad | F2 (estructura, contenido realista, estados y espacio por componente) |
| Pregunta de diseño | ¿Cada pieza tiene una sola responsabilidad, estados completos y comportamiento por espacio, para aprobarse y construirse por separado? |
| Artefactos | brief.md · flujo.md · index.html · hallazgos.md · declaracion.md |
| Modifica producción | No |

## Estándares leídos
- Protocolo `gobernanza-interfaz` (SKILL.md) y sus referencias desde `agentes/kiwi/` (la copia sincronizada de la skill no traía `references/`, `assets/` ni `scripts/`): brief-funcional, user-flow, fidelidad, wireframing, validacion, hig-web-pwa; plantillas brief, flujo, hallazgos, declaración; kit `wireframe-kit.css` y base `wireframe-base.html`.
- `../../../referencias/WCAG-Design-Reference.md` (WCAG 2.2) y `../../auditoria-wcag.md`.
- Fuente de contenido: capturas `../../referencia/1-5`, prototipo `../../p1-marco.html`, shell `../../../shell/gen.py`.

## Desviaciones del protocolo
- El hi-fi existía antes de esta ronda (orden invertido). Esta ronda no lo reemplaza: separa la estructura para aprobarla.
- Un solo `index.html` con selector de componente (C00–C13) en lugar de un archivo por componente, para compartir el kit, el marco de espacio y el panel de estados.
- Iconos representados como cuadros neutros; su nombre accesible se declara en la ficha de cada componente.

## Comprobaciones ejecutadas
- check_artifact.py (F2): ✔ 0 errores · 0 avisos.
- Navegador (Chromium, Playwright): 14 componentes (C00–C13) × todos sus estados (64) × 1440, 834 y 393 px: 0 errores JS, 0 desbordes dentro del marco, 0 controles bajo 24 px, nunca más de una acción primaria visible.
- Página a 375 px: sin desplazamiento horizontal del cuerpo.
- Revisión visual de capturas: composición presencial y teleconsulta, diagnóstico, medicamento, contraindicación, video en compact.

## Matriz de adaptación
| Elemento | compact | medium | expanded | Motivo | Técnica | Foco/estado |
|---|---|---|---|---|---|---|
| C01 Menú | Oculto; «Menú» abre hoja | Riel de íconos | Riel; expandido encima | La consulta necesita el ancho | Container query | Esc/Tab fuera cierran; foco vuelve al botón |
| C02 Paciente | 2–3 renglones, no fija | Fija, avisos en 2.º renglón | Fija, un renglón | No tapar el foco en pantallas bajas (2.4.11) | Sticky condicional | Margen de desplazamiento = altura real |
| C03 Pasos | Fila de 4 | Columna 180 px | Columna 200–230 px fija | Orientación constante | Grid areas | Paso actual con aria-current |
| C04 Panel | Continuar a ancho completo | Pie normal | Pie normal | Pulgar y una sola primaria | Container query | Foco al título al cambiar de paso |
| C05 Signos | 2 columnas | 3 columnas | 4 columnas | Etiquetas sin cortar | auto-fill + minmax | Se conserva lo escrito |
| C07–C11 Paso 2 | Una columna, botones apilados | Igual que expanded | Tarjetas a ancho del panel | Leer diagnóstico y tratamiento juntos | Flujo normal | Foco tras agregar/quitar; deshacer sin tiempo |
| C12 Herramientas | Lista con nombres al final | Riel; herramienta en ventana modal | Lista o riel; herramienta en la columna | Apoyo, no navegación | Container query + modal | Modal: foco contenido, Esc; columna: no tapa |
| C13 Video | Primero, ancho completo | Arriba de la consulta | Arriba de la columna (360 px); Ampliar | Ver al paciente mientras se escribe | Grid areas | Controles con aria-pressed |

## Comprobaciones NO ejecutadas
- Lector de pantalla real (NVDA, VoiceOver) y zoom real del navegador al 200 y 400 %.
- Texto ampliado con la configuración del sistema operativo.
- Prueba con médicos (5 segundos y una consulta completa).
- Validación de las páginas Understanding de la W3C (sin acceso desde el entorno).
- Pasos 3 y 4, Antecedentes: no forman parte de r01.

## Hallazgos
Ver `hallazgos.md`.

## Traspaso
- **→ coco:** al aprobar, construir cada componente con el sistema Ecosistema Manik respetando anatomía, estados y matriz de esta ronda; el hi-fi `../../p1-marco.html` es la referencia visual.
- **→ lima:** registrar C01–C13 en el registro de componentes; C07 (buscador combobox) y C11 (aviso con deshacer) son candidatos a componente del sistema, no locales.
- **→ mora:** documentar contratos cuando estén aprobados.

## Siguiente paso del usuario
Aprobar la estructura de C00–C13 (o señalar qué componente cambia) y responder las incógnitas de `hallazgos.md`.
