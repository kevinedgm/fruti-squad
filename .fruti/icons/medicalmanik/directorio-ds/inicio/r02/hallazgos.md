# Hallazgos · Inicio Manik · r02

| # | Hallazgo | Severidad | Decisión | Responsable | Siguiente acción |
|---|---|---|---|---|---|
| 1 | «Cédula verificada» solo existe en México; Centroamérica usa otros registros (Guatemala: colegiado activo) | Alta | Etiqueta común propuesta «Registro verificado» + número local en cada médico | Lima | Confirmar el término por país |
| 2 | «$» es ambiguo entre MXN y USD (El Salvador, Panamá) | Alta | Wireframe usa «MXN 900» y «Q350» | Lima (token/formato de moneda) | Decidir formato de precio |
| 3 | El usuario pide cédulas con número: «Céd. Prof. 10234567 · Céd. Esp. 11876543» | Media | Aplicado en tarjetas del inicio; «Céd. Esp.» solo para especialistas | Kiwi → Lima | Cambia la anatomía aprobada de FichaMedico r03 C: requiere aprobación para llevarlo al DS y al prototipo |
| 4 | Números de cédula y precio se partían entre líneas a 393 px | Media | Cada pieza separada por «·» no se corta por dentro | Kiwi | Resuelto |
| 5 | Miniaturas de artículos ocupaban media pantalla en celular | Baja | Miniatura lateral 88 px | Kiwi | Resuelto |
| 6 | Sin cuenta de paciente: la cita solo se recupera por el enlace del mensaje | Media | Entrada E4 en flujo | Producto | Elegir SMS, WhatsApp o ambos |
| 7 | Preguntar sin cuenta: falta definir cómo se avisa la respuesta | Media | Incógnita 3 | Producto | Decidir |
