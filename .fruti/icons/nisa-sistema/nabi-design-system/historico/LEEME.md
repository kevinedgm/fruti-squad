# Scripts históricos del design system NisaLab

Pasos que ya corrieron, en orden. Ninguno se corre sobre el estado actual: cada uno se detiene al inicio salvo que se ejecute con `NISALAB_HISTORICO=1` (solo para reproducir el pasado en una copia).

| Orden | Script | Fecha | Qué hizo | Por qué es histórico |
|---|---|---|---|---|
| 1 | `build.py` | 2026-10-24 | Design system inicial «Nabi» (Archivo + IBM Plex Mono) | Nombre, tipografía y colores ya reemplazados |
| 2 | `modulos.py` | 2026-10-28 | Identidad v2 y manual de módulos (Usuarios) | Usa colores retirados el 2026-11-05 |
| 3 | `marca-nisa.py` | 2026-10-29 | Aplica el manual de Nisa Nabani (Poppins) | Usa colores retirados |
| 4 | `marca-nisalab.py` | 2026-10-30 | Nabi → NisaLab | Usa colores retirados |
| 5 | `encabezado-area.py` | 2026-10-30 | EncabezadoModulo con variante por área | Ya aplicado; reescribiría el componente |
| 6 | `areas-sin-color.py` | 2026-10-30 | Áreas nunca en tablas | Ya aplicado; reescribiría componentes |
| 7 | `estado-muestra.py` | 2026-10-30 | EstadoMuestra con colores propios de proceso y pago | Esos colores se unieron a los de estado |

Paso vigente (sigue en la carpeta principal): `../color-reduccion.py` (2026-11-05), color de 53 a 25. Es idempotente: si ya no hay colores retirados, no cambia nada.

Para cambiar el sistema hoy se editan directamente `tokens.json`, `README.md` y `components/`, y se publica al artefacto https://claude.ai/artifact/FzzBwrjsBqAm4gdgcTduiV.
