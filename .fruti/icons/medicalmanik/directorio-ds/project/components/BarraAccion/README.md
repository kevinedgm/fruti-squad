# BarraAccion

Barra de acción fija al pie del perfil del médico en celular y tableta: el precio y la acción siempre al alcance del pulgar.

- Izquierda: precio del consultorio elegido en `precio` y «Consulta · <consultorio>»; derecha: la acción de ese consultorio: «Agendar» o «Llamar» (`tel:`).
- Al cambiar de consultorio en el perfil, la barra cambia con él: precio y acción nunca se mezclan entre consultorios.
- 72 px (`barra-inferior`) más el inset inferior del dispositivo; fondo blanco, borde superior `linea` y sombra suave hacia arriba. El contenido de la página deja ese espacio libre al final.
- **Escritorio:** no hay barra; la acción vive en la columna del consultorio elegido.
- El consumidor provee: consultorio elegido, precio, forma de agendar y teléfono.
