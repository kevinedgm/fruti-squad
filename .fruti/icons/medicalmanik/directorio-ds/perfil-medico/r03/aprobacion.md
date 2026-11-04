# Aprobación · Perfil del médico · r03 · F2

- **Aprobado por el usuario:** 2026-11-04 («apruebo el perfil r03, pásalo al prototipo»), junto con la regla de formación.
- **Congelado:**
  - Cabecera = FichaMedico r03 C en grande (foto o avatar, nombre, especialidad, cédulas, calificación si hay opiniones).
  - Barra de secciones fija, solo con 4 o más secciones.
  - «Agenda tu cita»: consultorio (selector si hay más de uno), días deslizables (sin lugar = deshabilitado con texto), máximo 6 horas + «Ver más horarios», «o llama al…», «Cómo llegar». Tocar una hora lleva directo a «Confirma tu cita».
  - Celular: barra fija con precio + próximo lugar + «Agendar» (o «Llamar»). Escritorio: columna derecha fija con «Próximo lugar · Agendar hh:mm».
  - Orden: Padecimientos → Opiniones → Sobre mí → Formación → Dudas frecuentes → Galería.
  - Sección sin datos = no aparece; sin opiniones = sin calificación ni etiqueta; el aviso de completar va en el panel del médico.
  - Formación generada con los datos de las cédulas verificadas (título, institución y año; confirmado por el usuario). Regla: los títulos con cédula se muestran con los datos verificados; lo capturado a mano se suma como diplomados o cursos.
  - Confirmación: nombre + celular → «Confirmar cita».
- **Implementado en:** `directorio-prototipo/` (v6).

## Decisiones de implementación
- Aviso de privacidad como texto con enlace («Al confirmar aceptas…»), sin casilla: no añade un toque. Se quita «Motivo» (r03 aprobó solo nombre + celular).
- El Dr. Mario Díaz Soto (contenido del usuario) se agrega en la categoría «Niñas y niños»; teléfono, cédulas y precio ($800) de ejemplo; 190 km desde Puebla porque su consultorio está en Xalapa.
- Estados en el prototipo: Dr. Hernández = perfil mínimo; Dra. Quiroz = a medias.
- La «Agendar» de la ficha en resultados sigue abriendo «Elige día y hora» (pantalla por aprobar).

## Sin resolver
- Precio real del Dr. Díaz; fotos de la galería (de ejemplo); páginas «todas las opiniones» y «más fechas».
