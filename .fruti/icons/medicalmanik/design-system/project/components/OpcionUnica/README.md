# OpcionUnica

Opción única: una sola opción entre 2 y 5 visibles. Con más de 5, Campo de tipo lista.

- Círculo de 20 px, borde 1.5 px «line-control»; elegida con punto «manik».
- Fila de 44 px tocable, `<input type="radio">` nativo con el mismo `name`, dentro de `<fieldset>` y `<legend>`.
- Siempre hay una elegida por defecto cuando existe una respuesta razonable; si no, ninguna y el formulario la pide al enviar.
