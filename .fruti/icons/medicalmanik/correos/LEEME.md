# Correos MedicalManik

11 plantillas de correo del ecosistema (médicos) y de Manik (pacientes).

- `plantillas/<id>.html`: HTML listo para el servicio de envío, con variables `{{nombre_variable}}` (sintaxis tipo Handlebars).
- `plantillas/<id>.txt`: versión de texto plano del mismo correo.
- `manifiesto.json`: asunto, texto previo, cuándo se envía y lista de variables de cada correo.
- `img/`: imágenes de cabecera. Súbalas a un servidor público y ponga esa dirección en `{{assets_url}}`.
- `vista.html`: todos los correos con datos de ejemplo, para revisar.
- `gen.py`: genera todo lo anterior. Edite ahí y vuelva a correr `python3 gen.py`.

## Reglas usadas
- Tablas de maquetación, estilos en línea y ancho máximo de 600 px.
- Letra Sora y Atkinson Hyperlegible Next con respaldo Arial (Gmail y Outlook usan el respaldo).
- Botones hechos con tablas, texto alternativo en las imágenes y texto previo oculto.
- Médicos: trato de usted. Pacientes (Manik): trato de tú.
- Color de cada producto solo en la franja superior y en el botón principal.
- El resumen semanal lleva enlace para darse de baja; los correos de cuenta y pagos no, porque son transaccionales.

## Pendiente
- Probar en Gmail, Outlook (Windows) y Apple Mail con una herramienta como Litmus o Email on Acid.
- Confirmar nombres de planes, precios, beneficios y paquetes de créditos reales.
- Barras del resumen semanal: el sistema calcula `barra_<día>` como porcentaje del día con más consultas (0 a 100).
