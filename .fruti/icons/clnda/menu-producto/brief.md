# CLNDA Menú · brief funcional (borrador 1, 2026-10-30)

## Qué es (usuario)
App instalable en cada restaurante (incluidos restaurantes de hotel) para administrar mesas, comandas y órdenes: el mesero elige mesa, comensal y platillos **tocando imágenes**, con **pocos clics**. Reemplazo moderno de una app de restaurante muy usada en hoteles, naranja y de aspecto viejo (probablemente Soft Restaurant; por confirmar).

## Modelo (usuario, 2026-10-30)
**Local primero y gratis**: se instala en la computadora del negocio; los datos viven ahí (servidor local), sin depender de internet. La operación del restaurante es gratis.
**De pago, lo que necesita la nube**: sincronización y consulta remota desde el teléfono, reportes y analítica, y otros adicionales.

| Gratis (local) | De pago (nube) — propuesta |
|---|---|
| mesas, comandas, cocina, cuenta y cobro, menú con fotos | consulta y monitoreo remoto desde el teléfono |
| funciona en la red local del negocio, sin internet | respaldo en la nube |
| | reportes y analítica con historial |
| | facturación CFDI (requiere internet) — inferencia |
| | cargo a la habitación con CLNDA Booking — inferencia |
| | **Mesanda Reservas** (complemento tipo OpenTable, usuario 2026-10-30): reservas en línea que llegan al plano como «Reservada · hora» |

Por qué cierra (inferencia): el usuario gratis no genera costo de servidor; el costo y el valor aparecen juntos cuando el dueño quiere ver su negocio desde fuera.
Riesgos: pérdida de datos si falla la computadora (el respaldo es urgente, no lujo); costo de soporte de instalaciones gratuitas; actualizaciones en equipos sin internet.

## Complemento Mesanda Reservas (usuario, 2026-10-30)
Reservas en línea tipo OpenTable. Vive en la nube (de pago), porque el comensal reserva desde internet; se sincroniza con el plano local y la mesa aparece «Reservada · hora».
Regla propuesta para el modo sin internet: la nube solo confirma sola dentro de un **cupo reservado para internet** (mesas u horarios que el restaurante aparta); fuera del cupo, la reserva queda «por confirmar» hasta que el restaurante la acepte. Así una reserva en línea nunca choca con una mesa asignada en el local mientras la computadora estaba desconectada.
Inferencia de venta: cobro fijo mensual frente al cobro por comensal de OpenTable (verificar tarifas actuales antes de usarlo como argumento).

## Enunciado
El **mesero** necesita **tomar la orden de cada comensal y enviarla a cocina** en segundos, porque hoy lo hace en libreta o en un sistema lento de muchas pantallas.
- Verbo principal: tomar orden. Resultado verificable: la comanda llega a cocina/barra con mesa, comensal y notas.
- Métrica del concepto «pocos clics»: toques desde «mesa» hasta «enviado a cocina» (objetivo por definir; medir contra el sistema actual).

## Flujo central (propuesta)
plano de mesas (libre / ocupada / por cobrar) → tocar mesa → comensales → categoría → platillo (foto) → modificadores (sin cebolla, término) → enviar a cocina → … → cuenta (por comensal o junta) → cobrar o **cargar a la habitación** (si el restaurante es de un hotel con CLNDA Booking).

## Plano y estados de mesa (usuario, 2026-10-30)
- **Modo edición** (dueño/gerente): dibujar el plano del restaurante y colocar mesas (forma, número, sillas, zona).
- **Modo servicio** (mesero): tocar una mesa; vacía → iniciar comanda; ocupada → seguir agregando a la orden; al pedir la cuenta, todo ya está concentrado en la mesa.

Estados de mesa (propuesta):
| Estado | Cómo entra | Qué hace el toque |
|---|---|---|
| Libre | inicio, o tras cobrar | iniciar comanda (comensales) |
| Reservada | reserva para una hora | ver reserva; sentar → ocupada |
| Ocupada | comanda abierta | abrir orden y agregar |
| Cuenta pedida | el mesero la pide | ver cuenta, dividir, cobrar |
| Por limpiar (opcional) | tras cobrar | marcar libre |
Excepciones: cambiar de mesa, juntar mesas, cancelar un platillo ya enviado, cuenta dividida por comensal.

## Superficies probables
App del mesero · pantalla de cocina/barra · caja/cuenta · panel del dueño (menú con fotos, mesas, reportes).

## Hechos / supuestos / incógnitas
- Hecho: selección visual, pocos clics, instalable por negocio.
- Hecho: funciona sin internet por diseño (local); la nube es opcional y de pago.
- Inferencia: el naranja de CLNDA Menú (#ea580c) se parece al color del competidor viejo: revisar.
- Inferencia: el nombre «Menú» sugiere menú digital para el comensal, no comandas: revisar.
- Incógnitas: dónde se toma la orden (en la computadora o en celulares/tablets conectados a ella por wifi local); sistema operativo de las computadoras; impresora de comandas o pantalla de cocina; facturación (CFDI); propinas; cuentas divididas; inventario.
