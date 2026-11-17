# GEMA · plantillas de correo a clientes y proveedores

Decisión del usuario (2026-11-17): los correos externos los firma el laboratorio **Nisa Nabani** con el estilo de GEMA (navy, Onest); GEMA no aparece ante el cliente.
Sin portal de clientes (ADR-011): cada documento va como PDF adjunto. HTML de tablas con estilos en línea, ancho máximo 600 px. Generadas con `gen.py`.

| Plantilla | Para | Variables |
|---|---|---|
| `informe-resultados.html` | Cliente | orden, contacto, fecha_recepcion, filas, archivo, peso |
| `estado-cuenta.html` | Cliente | cliente, contacto, fecha_corte, saldo, vencido, filas, total, archivo, peso, datos_pago |
| `cotizacion.html` | Cliente | folio, servicio, contacto, vigencia, tiempo_entrega, filas, total, archivo, peso |
| `orden-compra.html` | Proveedor | folio, laboratorio, contacto, fecha_entrega, sucursal, condiciones, filas, total, archivo, peso |

Todas: `encabezado` (logotipo oficial del laboratorio vía `logo_url`), `firma` y `pie_contacto`. No se inventan datos del laboratorio: en las muestras van entre corchetes.
`filas`, `total` y `encabezado` son fragmentos HTML que arma el código (`fila()`, `total()`, `folio()` en `gen.py`); el resto es texto y se escapa.
Montos de las muestras ficticios; IVA 16 %; sumas verificadas.

**Pendiente:** logotipo oficial de Nisa Nabani en PNG (no se dibuja ni se copia aquí), datos de contacto por sucursal, datos para pago.
No verificado: render en clientes de correo reales.
