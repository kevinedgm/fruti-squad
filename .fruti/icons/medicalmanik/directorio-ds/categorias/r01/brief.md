# Brief · «Busca por lo que sientes» como sellos · r01

- **Pedido (usuario, 2026-11-04):** rediseñar las categorías del inicio («Piel», «Salud mental»…) con algo moderno, como una especie de sello, que tengan identidad.
- **Ruta:** R2 (Actual + A/B/C, esperar elección) · **Fidelidad:** F3 con tokens del DS directorio Manik.
- **Alcance:** solo el componente TarjetaCategoria (inicio aprobado r03: estructura y orden congelados; solo cambia la apariencia de las tarjetas).
- **Función (sin cambios):** quien no sabe a qué especialista ir elige por lo que siente; nombre en palabras del paciente + especialidad debajo.
- **Restricciones:** colores solo de tokens existentes (fondos de categoría + cian-ui / cálido / azul); pictogramas Lucide reutilizados (pictogramas propios = trabajo de Uva tras elegir dirección); nombre y especialidad como texto real; lo escrito dentro del sello es decorativo (aria-hidden).
- **Direcciones:** A sello circular con leyenda en arco · B estampilla con borde perforado · C emblema con silueta propia por categoría.
- **Comprobado:** contrastes de la tinta del sello sobre su fondo 4.61 / 5.44 / 7.6:1 (≥ 3:1 para gráficos; ≥ 4.5:1 para el texto de la leyenda); sin desbordes ni controles menores de 24 px a 390 y 1300 px; sin errores JS.
- **No ejecutado:** lector de pantalla, texto ampliado.
- **Incógnita:** si se quiere un color propio por categoría (hoy rotan 3), es una decisión de tokens para Lima.
