# Declaración de cumplimiento · Cita confirmada · r01

- **Ruta / fidelidad:** R1 · F2 (kit neutral).
- **Estándares leídos:** brief, kit, decisiones de inicio r02 (sin cuenta, mensaje con enlace), perfil r03 (confirmación nombre + celular), WCAG 2.2 AA.

## Comprobaciones ejecutadas
- `check_artifact.py --fidelidad F2`: 0 errores, 0 avisos.
- Playwright 393 / 834 / 1440 × 4 estados: 0 controles menores de 24 px, 1 primaria visible (0 en «pendiente», a propósito), 0 errores JS. El único «desborde» medido es el título oculto para lector de pantalla (1 px por diseño).
- Revisión visual a 393 y 1440 px.

## Comprobaciones NO ejecutadas
- Texto ampliado al 200 %, teclado, lector de pantalla (el foco al título se describe, no se implementa en el wireframe).
- Envío real de SMS o WhatsApp; conteo de tramos verificado solo por longitud.

## Desviaciones
- Ninguna.
