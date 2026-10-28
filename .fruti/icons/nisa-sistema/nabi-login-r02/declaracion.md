# Declaración de cumplimiento · Nabi · inicio de sesión · r02

| Campo | Valor |
|---|---|
| Ruta | R1 |
| Fidelidad | F3 |
| Pregunta de diseño | ¿La identidad v2 da personalidad sin quitar claridad, y las microinteracciones informan el estado del acceso en lugar de decorar? |
| Artefactos | brief.md · flujo.md · identidad-v2.md · nabi-identidad-v2.css · nabi-tokens.css · plantilla.html · gen.py · login.html · hallazgos.md · declaracion.md |
| Modifica producción | No |

## Estándares leídos
- Protocolo `gobernanza-interfaz` (SKILL.md) y sus referencias en `agentes/kiwi/references/` (brief-funcional, user-flow, fidelidad, validacion, hig-web-pwa) y plantillas.
- Sistema real: `../nabi-design-system/tokens.json`, README y componentes Boton, Campo y Carga; marca `../nabi-final/` (lockup, carga, tema).
- Skill `nisa` (dirección visual, fuente de diseño, QA visual): se tomaron sus criterios de jerarquía y QA; su acabado Verdant no aplica porque el usuario pidió el sistema de Nabi.
- WCAG 2.2: `../../medicalmanik/referencias/WCAG-Design-Reference.md`.

## Desviaciones del protocolo
- `references/sistema-real.md` no existe ni en la skill sincronizada ni en `agentes/kiwi/`: se localizó el sistema por el repositorio (Nabi DS).
- La regla «sin `:root` paralelo» se cumple generando `nabi-tokens.css` desde `tokens.json`; la capa v2 redefine tokens del mismo sistema a petición del usuario y está marcada como propuesta.
- Tres familias tipográficas (Archivo, IBM Plex Mono y Newsreader, nueva): declarado en `identidad-v2.md`.

## Comprobaciones ejecutadas
- Navegador (Chromium, Playwright) a 1440, 1024, 768, 390 y 320 px: 0 errores JS, sin desplazamiento horizontal, fuentes cargadas, ningún control bajo 24 px.
- Flujo completo: escribir (la placa se llena), Entrar → «Verificando…» con la carga de Nabi y lectura de placa, error con foco y contraseña seleccionada, intentos restantes, bloqueo con hora, correo inválido al salir del campo, éxito con saludo, sin conexión con Entrar deshabilitado y motivo escrito.
- Doble envío bloqueado mientras verifica (`aria-busy`).
- `check_artifact.py`: no aplica a F3 (verifica grises y una familia de F1/F2); no se ejecutó.

## Matriz de adaptación
| Elemento | compact (<600) | medium (600–1023) | expanded (≥1024) | Motivo | Técnica | Foco/estado |
|---|---|---|---|---|---|---|
| Columna editorial | Lockup, título y entradilla arriba | Igual que compact | 7/12 con placa y divisiones | El formulario es lo primero que se usa | Media query | Sin foco; decorativa salvo el texto |
| Placa | Oculta | Oculta | Visible, responde a la escritura | No compite en pantallas chicas | Media query | aria-hidden |
| Tarjeta de acceso | Ancho completo, sombra 1 | Ancho máx. 560 | 5/12, sombra 2 | Protagonista | Grid | Se conserva lo escrito al cambiar de tamaño |
| Panel del prototipo | Plegado abajo a la derecha | Igual | Igual | No es producto | Fixed + details | — |

## Comprobaciones NO ejecutadas
- Lector de pantalla real y zoom real al 200 %.
- Contraste de la capa v2 medido en navegador (se calcularon los tokens: texto ≥ 4.5:1; bordes de control 3.3:1).
- Gestor de contraseñas real (autocompletado): solo se verificaron los atributos `autocomplete`.
- Prueba con usuarios del laboratorio.

## Hallazgos
Ver `hallazgos.md`.

## Traspaso
- **→ coco:** implementar con los tokens aprobados; el login no requiere componentes nuevos salvo la placa (componente de marca local).
- **→ lima:** decidir la capa v2 y pasarla a `tokens.json`; registrar Newsreader como voz editorial.
- **→ mora:** documentar la identidad v2 en la guía de Nabi si se aprueba.

## Siguiente paso del usuario
Aprobar o ajustar la identidad v2 (fondo, sombras, voz editorial) y el login.
