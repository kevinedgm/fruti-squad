# EstadoPerfil

Estado del perfil público del médico, tal como lo ve él en su panel (no el paciente). **Propuesta** del panel de usuario r1, pendiente de confirmar.

- **Visible:** aparece en búsquedas; acciones «Ver mi perfil público» y «Editar perfil».
- **Oculto:** no aparece; «Mostrar en Manik». Ocultar pide confirmación; mostrar no.
- **Incompleto:** no se publica hasta completar lo obligatorio de cada consultorio: dirección, precio de consulta y una forma de agendar (en Manik o por teléfono). La foto se pide pero no bloquea: sin ella sale el avatar.
- **En revisión:** se está verificando la cédula; el interruptor de visibilidad queda bloqueado.
- Siempre texto + color; aviso e información toman los tonos del ecosistema oscurecidos para llegar a 4.5:1 sobre su fondo (#A15D02, #3C7190); aún no son tokens del directorio.
- El consumidor provee: estado, fecha y datos faltantes. Supuestos: solo médicos tienen perfil público; la verificación de cédula existe.
