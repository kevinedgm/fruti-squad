# Ronda 3: perro genérico con la estética de rabbit/turtle (masa redondeada, patas cortas y anchas, suelo plano).
import perro
C = True
def cuerpo_a(boca):
    nariz, labio, comisura, menton, mandibula = boca
    return [(5.2,11.0),(9.0,10.0),(13.2,9.9),(14.2,7.2),(16.4,4.8),(18.9,4.9),(20.6,6.9),
            (*nariz,C), labio, (*comisura,C), menton, mandibula,(17.4,11.4),(17.1,13.4),(17.1,15.6),
            (17.3,19.0,C),(14.8,19.0,C),(14.8,16.2),(12.0,16.4),(8.6,16.3),(8.3,16.8),(8.4,19.0,C),(5.9,19.0,C),(5.6,16.3),(4.3,14.0)]
CERR = [(21.4,8.4),(20.9,9.4),(20.0,9.7),(20.5,10.0),(18.9,10.9)]
ABIE = [(21.5,8.0),(20.8,9.0),(19.4,9.5),(20.6,11.3),(19.1,11.7)]
colaA = [(5.0,11.2),(3.8,10.4),(3.2,8.8)]
orejaA = [(16.7,5.0),(15.7,6.5),(15.7,8.5),(16.4,9.5)]
# B · sentado compacto (como el conejo): pecho alto, cadera redonda en el suelo
def cuerpo_b(boca):
    nariz, labio, comisura, menton, mandibula = boca
    return [(9.4,10.6),(11.2,8.6),(12.4,6.0),(14.6,4.0),(17.1,4.1),(18.8,6.0),
            (*nariz,C), labio, (*comisura,C), menton, mandibula,(15.6,10.6),(15.4,13.0),(15.5,16.0),
            (15.7,20.4,C),(13.2,20.4,C),(13.0,17.0),(12.0,17.4),(12.2,20.4,C),(6.8,20.4,C),(4.9,18.6),(5.2,15.0),(7.2,12.4)]
CERRb = [(19.6,7.6),(19.1,8.6),(17.9,8.9),(18.6,9.3),(17.1,10.1)]
colaB = [(6.0,19.8),(4.2,20.0),(3.2,18.8)]
orejaB = [(14.2,4.4),(13.1,5.8),(13.0,7.8),(13.8,9.0)]
if __name__ == '__main__':
    open('r3-a.svg','w').write(perro.svg('bruno-a','A · de pie, compacto',cuerpo_a(CERR),colaA,(18.6,7.2),orejaA))
    open('r3-b.svg','w').write(perro.svg('bruno-b','B · sentado, compacto',cuerpo_b(CERRb),colaB,(16.8,6.6),orejaB))
    print('margen A', perro.margen(cuerpo_a(CERR)+colaA), 'B', perro.margen(cuerpo_b(CERRb)+colaB))
