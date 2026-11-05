# App Shell NisaLab · brief · r01

Ruta R1 (una dirección) · F3 con el design system NisaLab v3 (tokens.json) y el lenguaje del componente Dialogo aprobado (superficies claras, jerarquía tipográfica, acento azul).
Pedido: «App Shell con sidebar, navbar y footer; el sidebar con módulos y submódulos» + accesos frecuentes (respuesta del usuario).

Usuarios: analistas, supervisión de calidad, recepción, administración. Escritorio casi siempre; tableta en el laboratorio.
Pregunta de diseño: ¿cómo se llega en uno o dos clics a la pantalla de trabajo diaria (una bitácora, registrar una muestra) sin perder de vista en qué módulo se está?

Sidebar: logotipo; accesos frecuentes (máx. 4, fijables); módulos con submódulos desplegables: Inicio · Recepción · Muestras · Bitácoras · Informes · Catálogos · Administración; abajo Ayuda y plegar.
Navbar: abrir/plegar menú, ruta (módulo / submódulo / pantalla), búsqueda global (Ctrl K), avisos, aplicaciones Nisa, usuario (nombre y rol).
Footer: marca con respaldo, versión, estado del sistema, hora del servidor (los registros se fechan con ella), soporte.
Estados: expandido · plegado (solo íconos, 72 px) · celular (cajón con velo) · submódulo abierto · sin permiso (el módulo no aparece).
Hechos: módulos y bitácoras tomados del shell anterior (nisa-shell-r2) y del CSS de bitácoras que pegó el usuario (alcohol, metanol y aldehídos, extracto seco, acidez, azúcares, congenéricos).
Supuestos: submódulos de Recepción, Muestras, Informes, Catálogos y Administración (a confirmar con el flujo real).
Incógnitas: ¿los accesos frecuentes se calculan por uso o solo los fija la persona? ¿Hay selector de área?
