def corrige(im):
    px = im.load()
    for y in range(364, 452):   # segunda oreja en el lado de la cara: fuera todo lo que queda a la izquierda de la mejilla
        xc = 906 + (y - 380) * 0.633
        for x in range(868, 952):
            if x < xc - (3 if y < 386 else 7): px[x, y] = (255, 255, 255, 0)
    return im
