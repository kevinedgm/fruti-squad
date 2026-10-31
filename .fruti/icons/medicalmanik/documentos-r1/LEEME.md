# Expediente Manik · documentos para el paciente r1

Pedido del usuario (2026-10-31): identidad visual (tipo hoja membretada) de los documentos que genera Expediente Manik: el **estado de salud** que recibe el paciente al terminar la consulta (rango de peso, etc.) y el **historial clínico** cuando alguien lo pide. Expediente Manik muy sutil en logo y color, para no quitarle protagonismo al médico ni incomodarlo.

Publicado: https://claude.ai/artifact/3aM3B9Fv1g7B43USyzA4Kp · `python3 gen.py <dir>` (usa los iconos recomendados de `../../antecedentes/` y el sello de Expediente a una tinta).

## Decisiones [propuesta]
- **Hoja carta** (816 × 1056 px a 96 ppp); CSS de impresión `@page letter` para el producto real.
- **El médico al frente:** membrete con su logo (o sus iniciales si no tiene), nombre, especialidad, cédulas, institución, consultorio y contacto; título del documento, fecha y folio a la derecha.
- **Acento elegido por el médico** entre 5 tonos sobrios (tinta por defecto, azul, verde, vino, grafito). Ningún color de Manik en la hoja.
- **Manik solo al pie:** «Generado con Expediente Manik · folio · página», 9.5 px gris, sello de Expediente a una tinta de 11 px al 55 %.
- **Estado de salud:** medidas con rango de referencia dibujado y lectura en palabras (IMC con peso adecuado calculado, presión, glucosa en ayuno, cintura), signos breves, «Lo que encontramos» en lenguaje claro, indicaciones, próxima cita, firma. Rangos en el acento, no semáforo rojo/verde: informan sin alarmar.
- **Historial → «Resumen clínico»:** es lo que el paciente puede pedir por escrito según la NOM-004-SSA3-2012 (el expediente pertenece al prestador) [confianza media-alta; validar con legal]. Ficha, alergias en recuadro, antecedentes con los iconos nuevos en gris, consultas con CIE-10, medicamentos actuales.

## Rangos usados [validar con el área médica]
IMC (OMS / NOM-008): <18.5 bajo, 18.5–24.9 adecuado, 25–29.9 sobrepeso, ≥30 obesidad · Presión (NOM-030): <120/80 óptima, 120–129/80–84 normal, 130–139/85–89 normal alta, ≥140/90 alta · Glucosa en ayuno (NOM-015): <100 normal, 100–125 alterada, ≥126 diabetes · Cintura mujer: ≥80 cm con riesgo.

## Pendiente
Campos obligatorios del membrete y del resumen (NOM-004) con legal · segunda página del resumen · versión digital (PDF con texto seleccionable y firma electrónica) · logo real del médico (subido en su perfil).

Datos ficticios: médico, paciente, cédulas (0000000) y folios.
