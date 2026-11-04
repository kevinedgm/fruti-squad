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
