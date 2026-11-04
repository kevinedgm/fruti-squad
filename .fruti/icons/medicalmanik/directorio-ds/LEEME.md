# Directorio Manik · sistema de diseño (2026-11-04)

Artifact (tipo Design System): https://claude.ai/artifact/MTg2EAZVsJKZJRFCWGvAuj
Regenerar: `python3 build.py <carpeta>` → `<carpeta>/project/` y publicar con `root` = esa carpeta. `project/` aquí es la copia publicada.

Fuentes: manual del directorio v2 (`../manik-guia/guia.html`, dirección bienestar), paquete de marca (`../manik-final/`), prototipo bienestar v1 (`../directorio-c/`) y panel de usuario r1 (estado del perfil, propuesta).
- 68 tokens de color, tipo (Urbanist + Onest), espacio, radio, sombra y layout, con contraste en cada nota.
- 12 componentes con preview: Boton, Buscador, Chip, TarjetaCategoria, FichaMedico, Horarios, Insignias, FotoMedico, Anuncio, FranjaConfianza, Encabezado, EstadoPerfil (propuesta) + Cover.
- Assets subidos: Marca (5), Logotipos (5), Iconos Lucide (14).

Decisiones / correcciones:
- «Cédula verificada»: #15814B sobre #E7F5EE daba 4.4:1 → `on-exito-suave` #157B4A (4.7:1).
- Estado del perfil: aviso #A15D02 e info #3C7190 (oscurecidos para 4.5:1).
- Estrella #E3A21C (manual v2) sobre #F2B33D (paquete anterior).
- Escala de espacio tomada del prototipo (por confirmar).

## Cambio 2026-11-04 · consultorios y avatar
- Decisión del usuario: precio y forma de agendar son de cada consultorio. La ficha muestra el consultorio más cercano que cumpla los filtros y «Atiende en N consultorios · ver todos».
- Decisión del usuario: sin foto, avatar de silueta de médica u hombre (reemplaza la regla de iniciales del manual v2); neutro si el perfil no indica «Dr./Dra.». `avatares.py` → `avatares/`, subidos al grupo «Avatares».
- Propuesta: un consultorio se publica solo con dirección, precio y una forma de agendar; si falta, el perfil queda «Incompleto».

## Cambio 2026-11-04 · celular primero
- Dato del usuario: 70 % del uso en celular y tableta, 30 % en escritorio.
- Ficha con container query (compacta < 560 px, avatar 72 px; amplia ≥ 560 px); máximo 3 horarios + «Más horarios»; acciones a todo el ancho.
- «Llamar» (`tel:`) es la acción principal de consultorios por teléfono (corrige «Copiar número» como única acción).
- Buscador: campo único que abre búsqueda a pantalla completa; píldora doble solo ≥ 1024 px.
- Nuevos: BarraFiltros (hoja inferior) y BarraAccion (barra fija del perfil). Iconos extra (phone, sliders-horizontal, x, arrow-left) en `iconos-extra/`.
- Tokens: foto-ficha-movil, ficha-amplia, bp-tableta, bp-escritorio, barra-inferior. Fotos en WebP 176 × 234 en ficha de celular.

## Cambio 2026-11-04 · lenguaje
- Pedido del usuario: «En línea» confunde (se lee como consulta por internet). La cita es presencial; solo se reserva desde el directorio.
- Ahora: «Agenda en Manik», «Por teléfono» o «Agenda en Manik o por teléfono». Filtro «Agenda en Manik». Regla de voz en el README.

## Cambio 2026-11-04 · FichaMedico aprobada
- El usuario aprobó el wireframe FichaMedico r03, opción C (`ficha-medico/r03/aprobacion.md`); r04 (C + horarios) descartada.
- Componente FichaMedico reescrito en F3 con esa anatomía: médico arriba; consultorios en filas (máx. 2 + «Ver n más») con lugar · distancia · precio, forma de agendar + próximo lugar o teléfono, y su acción; «o llama al …» si agenda de las dos formas; un solo sólido por ficha. Sin tokens nuevos.

## Cambio 2026-11-04 · sin «Nuevo en Manik»
- Pedido del usuario: se retira la etiqueta. Sin opiniones, la ficha muestra solo «Cédula verificada». Aplicado en el sistema, el prototipo y la aprobación de r03.

- 2026-11-04: FichaMedico y prototipo muestran cédulas con número («Céd. Prof. · Céd. Esp.») en lugar de «Cédula verificada». DS versión 9.
