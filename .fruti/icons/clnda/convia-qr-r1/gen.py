# Convia · identidad de los QR de mesa (r1). Pedido del usuario (2026-10-31): tarjetas para que el comensal escanee (cámara o NFC) y vea el menú
# en Convia; el establecimiento es el protagonista y Convia aparece discreto (estrella + «Menú en Convia» en pequeño).
# r1.2 (usuario): estrella más grande, QR encajado al centro sin recuadro visible, difuminado de color intenso a blanco hacia el QR.
# El QR se genera en el navegador con qrcode-generator 1.4.4 (Kazuhiko Arase, MIT) desde cdnjs; corrección de errores M, zona de silencio de 4 módulos.
# En la demo el QR abre el menú publicado en modo mesa (#qr). Uso: python3 gen.py <carpeta de salida>.
import os, re, json, sys
D = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(D, '..', 'convia-final')
STAR = re.search(r'd="([^"]+)"', open(os.path.join(F, 'svg/simbolo.svg')).read()).group(1)
SIL = re.search(r'd="([^"]+)"', open(os.path.join(F, 'svg/simbolo-silueta.svg')).read()).group(1)  # silueta sólida (convia-final/silueta.cjs)
A1 = 'https://claude.ai/artifact/'
NEG = {
 'fuegos': dict(n='Cocina Siete Fuegos', ini='SF', sub='Cocina de temporada · Xochimilco', que='Menú', what='Menu', slug='siete-fuegos',
                url=A1 + 'MMk5Ck3qhFLxzx1dYcc2HF#qr', colores=['#7a2e1f', '#1f3b33', '#b8862f']),
 'tostadora': dict(n='Tostadora Norte', ini='TN', sub='Café de especialidad · Reforma', que='Carta', what='Menu', slug='tostadora-norte',
                   url=A1 + '7HoET7Tj5544sRNVzESfdh#qr', colores=['#1b1d1a', '#8a5a1c', '#e6c36a']),
}
html = open(os.path.join(D, 'plantilla.html')).read().replace('/*DATA*/', 'const NEG=' + json.dumps(NEG, ensure_ascii=False) + ';const STAR=' + json.dumps(STAR) + ';const SIL=' + json.dumps(SIL) + ';')
OUT = sys.argv[1] if len(sys.argv) > 1 else D
open(os.path.join(OUT, 'index.html'), 'w').write(html); print('ok', len(html))
