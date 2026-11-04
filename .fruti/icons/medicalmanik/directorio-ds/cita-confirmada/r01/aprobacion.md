# Aprobación · Cita confirmada · r01 · F2

- **Aprobado por el usuario:** 2026-11-04 («apruebo cita confirmada, pásala al prototipo»), junto con el aviso de «horario ocupado».
- **Congelado:**
  - «Tu cita está confirmada» + saludo con el nombre de pila; el foco llega al título.
  - Resumen: día de la semana + fecha en palabras + hora · médico · lugar y dirección · precio (pagas en el consultorio) · paciente y celular.
  - Acción principal: «Agregar a mi calendario» (archivo .ics); secundaria: «Cómo llegar».
  - «Te enviamos la confirmación» al celular, con vista del mensaje (corto, con enlace para cambiar o cancelar) y «¿No te llegó? Reenviar».
  - «¿Necesitas algo más?»: cambiar o cancelar · llamar al consultorio · volver al inicio.
  - Celular: resumen → mensaje → más. Escritorio: resumen y «más» a la izquierda; mensaje a la derecha.
  - Confirmación inmediata (sin aceptación del médico).
- **Horario ocupado (en «Confirma tu cita»):** aviso «Ese horario se acaba de ocupar» con el foco, 3 horas cercanas, datos conservados; «Cuándo» y la barra dicen «Elige otro horario» y «Confirmar» queda deshabilitado (también con Enter) hasta elegir.
- **Implementado en:** `directorio-prototipo/` (v8). Para ver el aviso: Dra. Soto, hoy 17:00, o Dr. Díaz, hoy 17:30 (simulación).

## Decisión de implementación (prototipo)
- El visor de artifacts no permite ofrecer archivos .ics (no están en la lista de formatos de descarga). En el prototipo, «Agregar a mi calendario» abre Google Calendar con la cita llena; «Apple u Outlook (.ics)» explica que en el producto se descarga el archivo. En el producto real: .ics + Google Calendar.

## Sin resolver
- Canal del mensaje (SMS o WhatsApp); plazo para cambiar o cancelar; pantalla «Detalle de su cita» (enlace del mensaje).
- El estado «no pudimos enviar el mensaje» está en el wireframe, no simulado en el prototipo.
