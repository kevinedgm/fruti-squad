from PIL import ImageDraw
SKIN = (248, 245, 234, 255)
def corrige(im):
    px = im.load()
    for y in range(300, 380):   # arete que se lee como segundo ojo: disco y anillo a piel, sin tocar el pelo
        for x in range(650, 730):
            r, g, b, a = px[x, y]
            if (x - 690) ** 2 + (y - 340) ** 2 <= 34 ** 2 and (x >= 668 or (x >= 652 and y >= 358)) and 0.299 * r + 0.587 * g + 0.114 * b < 235: px[x, y] = SKIN
    d = ImageDraw.Draw(im)   # pico en V de la mandíbula (segunda nariz): se borra y se redibuja suave
    d.polygon([(674, 414), (705, 370), (744, 404), (744, 411)], fill=SKIN)
    d.line([(666, 424), (686, 416), (706, 412), (726, 412), (746, 416)], fill=(15, 15, 15, 255), width=9, joint='curve')
    for p in [(666, 424), (746, 416)]: d.ellipse([p[0] - 4, p[1] - 4, p[0] + 4, p[1] + 4], fill=(15, 15, 15, 255))
    return im
