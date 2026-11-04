# Aprobación · Detalle de su cita · r01 · F2

- **Aprobado por el usuario:** 2026-11-04 («apruebo detalle de cita, pásala al prototipo»).
- **Congelado:**
  - Entrada por el enlace del mensaje, sin sesión; vence al terminar el día siguiente a la cita.
  - Fecha límite escrita («puedes cambiarla o cancelarla hasta el … a las …, 24 horas antes»).
  - Acciones: Cómo llegar (principal) · Agregar a mi calendario · «¿Cambió tu plan?»: Cambiar fecha u hora (contorno) y Cancelar cita (texto, separado).
  - Cancelar: diálogo con fecha, hora y médico; foco en «No, conservarla»; Esc cierra sin cancelar.
  - Cambiar: elegir otra hora del mismo consultorio; resumen «Antes → Ahora»; la hora anterior se libera solo al confirmar; si la nueva se ocupa, aviso y la cita actual sigue igual.
  - A menos de 24 h: sin «Cambiar»/«Cancelar»; explicación + llamar al consultorio.
  - Estados: cancelada (fecha tachada + agendar otra vez) · el consultorio canceló · ya pasó (opinar) · enlace vencido (mensaje neutro, pide celular) · carga.
- **Implementado en:** `directorio-prototipo/` (v11), rutas `#cita` y `#cita-cambiar`.

## Decisiones de implementación
- Al confirmar una cita, su hora se quita de la agenda del médico; al cambiar o cancelar, se libera.
- «Ver otros estados (solo prototipo)» al pie de `#cita` para revisar menos de 24 h, ya pasó, enlace vencido y el consultorio canceló.
- El médico se nombra con título y apellido («Dr. Díaz»).

## Sin resolver
- Enlace propio para opinar después de que vence el de la cita; zona horaria del límite (propuesta: la del consultorio); seguridad del código del enlace (con desarrollo).
