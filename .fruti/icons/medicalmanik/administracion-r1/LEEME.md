# Administración Manik · ronda 1

Pedido del usuario (2026-10-31): identidad de un producto nuevo del Ecosistema Manik, **Administración**, de uso interno: solo las cuentas de la empresa lo ven en el inicio; ahí se configura todo (usuarios activos, configuración del sistema). Los médicos no lo ven. (El mensaje se cortó en «a nivel…».)

Publicado: https://claude.ai/artifact/SUKp1wxWLiJb2K5FhEaqnu · `python3 gen.py <dir>` (lee los sellos de `../final/svg`).

## Brief
- Para: equipo MedicalManik (cuentas de la empresa). Hace: usuarios activos, configuración del sistema y de cada app.
- Nombre según el patrón: **Administración Manik**.

## Conflictos con reglas existentes (resueltos como propuesta)
1. El inicio muestra las apps sin acceso **apagadas con candado**; Administración **no se muestra** a quien no es interno (excepción: es herramienta interna; mostrarla revelaría superficie y generaría solicitudes imposibles).
2. Por eso el sello **no puede ser un candado**: el candado ya significa «sin acceso».
3. El mosaico del ecosistema sigue de **seis cuadros** (emblema fijo); Administración va en una fila aparte, «Herramientas internas», con chip «Solo equipo MedicalManik».

## Sellos (misma línea de pulso; el rasgo en el borde)
- A · Corchetes de control: cuatro esquinas separadas alrededor del cuadro. Riesgo: a 24 px.
- B · Engrane: pieza separada en la esquina superior derecha. Riesgo: se lee como «Ajustes».
- C · Escudo: silueta que termina en punta. Riesgo: suena a «seguridad».

## Color (app-administracion)
- Grafito #3A4558 (9.67:1 con blanco) [recomendado]: neutro, interno, no choca con productos ni estados.
- Ciruela #7A3B6B (7.88:1): cae entre Impulsa y Grupos.
- Tinta #14213D (15.97:1): casi el azul noche de Manik IA.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; en la cuenta de médica no aparece Administración.

**Elegido por el usuario (2026-10-31): B · Engrane, color grafito #3A4558.** Integrado en `../final/svg/administracion*.svg`, `../final/png/`, `../final/tema.json`, tokens y README del sistema.

[pendiente: qué más administra («a nivel…», mensaje cortado)]
