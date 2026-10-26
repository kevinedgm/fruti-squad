# Consulta v2 · prototipo 1 (marco) · auditoría WCAG 2.2

Fuente normativa: `../referencias/WCAG-Design-Reference.md` (guía que entregó el usuario).
Evidencia faltante: las páginas «Understanding» de la W3C enlazadas en la guía no se pudieron abrir desde este entorno (`www.w3.org` no resuelve). La auditoría se basa en los resúmenes de la guía y en el texto conocido de WCAG 2.2; hay que confirmarla contra la W3C y con prueba humana.

Archivo auditado: `p1-marco.html` (generado desde `plantilla-1.html`).
Prueba automática en Chromium (Playwright), 26/10/2026: anchos 1500, 1100, 900, 640 (equivale a 200 % de zoom sobre 1280) y 320 px; espaciado de texto forzado; teclado.

Estado: **C** cumple · **C\*** cumple con una corrección hecha en esta revisión · **N/A** no aplica a esta pantalla · **P** pendiente de verificar.

## 1. Color y apariencia
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 1.4.1 Uso del color | A | C | Fiebre: borde, fondo, ícono y texto «Fiebre (normal 36.5–37.5)». Pasos hechos: círculo verde **con palomita** y «Completo». Dato nuevo en Gráficas: insignia con texto. Pausa: el botón cambia a «Reanudar». |
| 1.4.3 Contraste de texto | AA | C | Texto secundario 8.8:1 (blanco), 7.5:1 (lienzo); aviso 7.7:1; éxito 7.6:1; ayudas y placeholder 7.5:1; botón azul 8.5:1. |
| 1.4.11 Contraste de componentes | AA | C | Bordes de campos y casillas 5.4:1 (blanco), 4.6:1 (lienzo); borde de campo con aviso 4.3:1; foco 7.2:1; íconos de herramientas 7.3:1. |
| 1.4.6 Contraste mejorado | AAA | C\* | Se oscurecieron el texto de aviso (6.4 → 7.7:1), el de éxito (6.5 → 7.6:1) y el placeholder (5.4 → 7.5:1). |

## 2. Tipografía y lectura
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 1.3.3 Características sensoriales | A | C | Ninguna instrucción depende de forma, tamaño o posición. |
| 1.4.4 Cambio de tamaño | AA | C | A 640 px (200 % de 1280) el diseño pasa a una columna sin desplazamiento horizontal. P: zoom real del navegador. |
| 1.4.5 Imágenes de texto | AA | C | Todo es texto real; el logotipo es la única imagen con letras (excepción de logotipos). |
| 1.4.12 Espaciado de texto | AA | C\* | La barra superior tenía alto fijo (52 px) → alto mínimo. Con interlineado 1.5, letras 0.12 em, palabras 0.16 em y párrafos 2 em: 0 elementos recortados. |

## 3. Foco
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 2.1.1 Teclado | A | C | Pasos, herramientas, panel, cronómetro, dictado y campos son botones o campos nativos. |
| 2.1.2 Sin trampa de teclado | A | C | Panel en modo ventana: el foco se queda dentro, pero «Cerrar» y Esc siempre lo sacan y regresan el foco a la herramienta que lo abrió. |
| 2.4.3 Orden del foco | A | C | Orden del código: barra, paciente, pasos, consulta, herramientas. Al cambiar de paso el foco va al título del paso. |
| 2.4.7 Foco visible | AA | C | Contorno azul de 3 px con separación de 2 px en todos los controles. |
| 1.4.13 Contenido al pasar o enfocar | AA | C\* | Con herramientas plegadas, el nombre aparece al pasar o enfocar, se puede recorrer con el ratón, no se va solo y Esc lo oculta. |
| 2.4.11 Foco no oculto | AA | C\* | La barra fija del paciente podía tapar el campo enfocado → margen de desplazamiento igual a la altura real de la barra. El panel de herramienta tapaba la consulta → ahora ocupa la columna derecha (sin traslape medido); en angosto es ventana modal. |
| 2.4.13 Apariencia del foco | AAA | C\* | Contorno subido de 2 a 3 px, 7.2:1 sobre el lienzo. |

## 4. Objetivos táctiles
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 2.5.8 Tamaño mínimo | AA | C | Todos los controles miden 44 px o más de alto. |
| 2.5.5 Tamaño mejorado | AAA | C\* | Avisos del paciente, botones del cronómetro, «Dictar» y plegar herramientas subieron de 36–40 a 44 px. Los campos de signos vitales medían 24 px de zona de toque dentro de un recuadro de 46 px → ahora todo el recuadro es zona de toque (medido: ningún control bajo 44 px a 1500 y 390 px). |

## 5. Estructura
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 1.3.2 Secuencia con significado | A | C | El orden visual coincide con el del código; el panel de herramienta va después de las herramientas. |
| 1.4.10 Reajuste | AA | C\* | A 320 px no hay desplazamiento horizontal; los grupos de herramientas ahora se acomodan en varias líneas en lugar de deslizarse. |
| 1.3.4 Orientación | AA | C | No se bloquea la orientación. |

## 6. Formularios
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 3.3.1 Identificación de errores | A | C\* | Padecimiento vacío al continuar: borde de 2 px, fondo, ícono y texto; `aria-invalid` y el foco va al campo. |
| 3.3.2 Etiquetas o instrucciones | A | C\* | Anotación privada sin etiqueta visible → etiqueta «Anotación privada». Tensión arterial con ejemplo de formato «90/60». |
| 3.3.7 Entrada redundante | A | N/A | No se pide repetir datos en este paso. P: en el prototipo de signos vitales, ofrecer talla y peso de la consulta anterior. |
| 3.3.3 Sugerencia de error | AA | C\* | «Escriba al menos el motivo de la consulta para continuar; puede dictarlo con el botón Dictar». |
| 3.3.4 Prevención de errores | AA | P | «Terminar consulta» guarda datos legales: el prototipo 4 debe pedir revisión antes de confirmar. |
| 3.3.8 Autenticación accesible | AA | N/A | No hay inicio de sesión en esta pantalla. |

## 7. Gestos
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 2.5.1 Gestos de puntero | A | N/A | No hay gestos de varios dedos. |
| 2.5.7 Arrastre | AA | C\* | El padecimiento crecía arrastrando la esquina → ahora crece solo con el texto. |
| 2.5.4 Movimiento del dispositivo | A | N/A | — |

## 8. Animación y tiempo
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 2.2.1 Tiempo ajustable | A | P | Falta saber si la sesión expira durante una consulta larga; si expira, avisar antes y permitir extenderla. |
| 2.2.2 Pausar, detener, ocultar | A | C\* | El cronómetro cambia cada segundo: ahora se puede pausar el conteo o solo «Ocultar» la cifra sin detenerlo. |
| 2.3.1 Tres destellos | A | C | No hay destellos. |
| 2.3.3 Animación por interacción | AAA | C | No hay animaciones decorativas. |

## 9. Navegación y predicción
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 2.4.4 Propósito de los enlaces | A | C | «Agenda de hoy», «Registrar» (alergias), «Continuar: Diagnóstico y tratamiento». |
| 3.2.1 Al recibir el foco | A | C | Enfocar no abre nada; los paneles se abren con clic o Enter. |
| 3.2.2 Al introducir datos | A | C | Escribir no cambia de paso ni envía nada. |
| 3.2.6 Ayuda consistente | A | C\* | Se agregó «Ayuda» en la barra superior; debe ir en el mismo lugar en todas las pantallas del ecosistema. |
| 2.4.6 Encabezados y etiquetas | AA | C | Títulos descriptivos: «Herramientas de apoyo», «Signos vitales», «Padecimiento actual». |
| 3.2.3 Navegación consistente | AA | P | Verificar contra las demás pantallas de Expediente. |
| 3.2.4 Identificación consistente | AA | C | Mismo ícono y palabra «Cerrar» para cerrar; mismo patrón de botón en todas las herramientas. |
| 2.4.5 Múltiples vías | AA | N/A | Es una pantalla de tarea dentro de la consulta, no una página del sitio. |
| 2.4.8 Ubicación | AAA | C | Ruta «Agenda de hoy › Consulta» y «Paso 2 de 4» con el paso actual marcado. |

## 10. Imágenes y medios
| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 1.1.1 Contenido no textual | A | C | Íconos decorativos ocultos al lector; la gráfica de peso tiene descripción («Peso de 6.1 a 8.9 kg en seis meses»); las iniciales del paciente se ocultan porque el nombre está escrito al lado. |
| 1.2.2 Subtítulos | A | N/A | Sin video. |
| 1.4.2 Control de audio | A | N/A | Sin audio automático. |

## Más allá de la guía
- **Transparencia de IA:** al activar «Dictar» aparece «El dictado se convierte en texto de forma automática y puede equivocarse. Revíselo antes de continuar».
- **3.1.1 Idioma de la página (A):** la página declara `lang="es"`.
- **2.5.3 Etiqueta en el nombre (A):** los nombres accesibles de las herramientas contienen el texto visible («Anotaciones privadas» antes se anunciaba como «Anotaciones del médico»).

## Pendientes (requieren persona o información)
1. Confirmar cada criterio contra las páginas Understanding de la W3C.
2. Prueba con lector de pantalla (NVDA o VoiceOver) y con zoom real del navegador al 200 % y 400 %.
3. Prueba con médicos mayores de 50 años.
4. 2.2.1: política de expiración de sesión.
5. 3.3.4: revisión antes de «Terminar consulta» (prototipo 4).

## Revisión 2: menú de la app y videoconsulta
Prueba automática en Chromium, 1500, 1100 y 390 px: sin desplazamiento horizontal, sin errores de consola; ningún control bajo 44 px.

| Criterio | Nivel | Estado | Evidencia |
|---|---|---|---|
| 3.2.3 Navegación consistente | AA | C | El menú es el del shell de Expediente (mismos grupos, mismo orden; Ayuda al pie del menú en todas las pantallas). |
| 3.2.6 Ayuda consistente | A | C\* | «Ayuda» se movió de la barra superior al pie del menú, donde está en el shell, para que esté siempre en el mismo lugar. |
| 1.4.13 Contenido al pasar o enfocar | AA | C | En el riel cada ícono muestra su nombre al pasar o enfocar; Esc lo oculta; se puede recorrer con el ratón. En celular las herramientas muestran siempre su nombre (no hay «pasar»). |
| 2.4.11 Foco no oculto | AA | C\* | El menú expandido cubre parte de la consulta: se cierra al salir de él con Tab, con Esc o con clic fuera, así que nunca tapa el elemento enfocado. |
| 2.1.1 / 2.1.2 Teclado, sin trampa | A | C | Menú, sala de espera y controles de la llamada son botones nativos; Esc cierra el menú y devuelve el foco al botón que lo abrió (medido). |
| 4.1.2 Nombre, función, valor | A | C | Micrófono, cámara, compartir, subtítulos y ampliar usan `aria-pressed` y cambian su texto («Mic. apagado», «Reducir»). |
| 1.4.1 Uso del color | A | C | El estado de cada control se indica con fondo, texto y `aria-pressed`, no solo con color; «Colgar» además tiene ícono y texto. |
| 1.2.4 Subtítulos en directo | AA | C\* | No está en la guía, pero WCAG 2.2 lo pide para audio en vivo: botón «Subtítulos» con la marca «Subtítulos automáticos» (transparencia de IA). P: confirmar que el proveedor de video los ofrece en español. |
| 1.1.1 Contenido no textual | A | P | El video real de la llamada no necesita alternativa (es comunicación en vivo); el sello del ecosistema y los íconos del riel tienen nombre accesible. |
| 3.3.4 Prevención de errores | AA | C | «Colgar» no cierra la consulta; aviso visible: «Colgar termina la llamada, no la consulta». |
