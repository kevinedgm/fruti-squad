import numpy as np, potrace
from PIL import Image
from scipy import ndimage as nd
A=np.array(Image.open('pz1.png').convert('L').crop((0,0,2272,2296)))<128
B=np.array(Image.open('pz2.png').convert('L').crop((0,0,2272,2296)))<128
s=8; CX,CY,R=265.97,226.1,136.1
yy,xx=np.mgrid[0:2296,0:2272]; X=127+(xx+.5)/s; Y=87+(yy+.5)/s
C=(X-CX)**2+(Y-CY)**2<=(R-0.3)**2
dA=nd.distance_transform_edt(~A); dB=nd.distance_transform_edt(~B)
G=C&~A&~B&(dA<45*s)&(dB<45*s)
lab,n=nd.label(G); sz=nd.sum(G,lab,range(1,n+1)); G=lab==(1+np.argmax(sz)); print('comps',n,sorted(sz)[-3:])
for xc in (132,140,170,365,380,395):
  col=G[:,int((xc-127)*s)]; ys=np.nonzero(col)[0]; print(xc,'gap y %.2f..%.2f'%(87+ys.min()/s,87+(ys.max()+1)/s))
Image.fromarray((G*255).astype(np.uint8)).resize((284,287)).save('gap.png')
np.save('G.npy',G)
bm=potrace.Bitmap(~G)
pl=bm.trace(turdsize=10,alphamax=1.0,opticurve=True,opttolerance=0.2)
def f(p): return '%.2f,%.2f'%(127+p.x/s,87+p.y/s)
d=[]
for c in pl:
  d.append('M'+f(c.start_point))
  for seg in c.segments:
    if seg.is_corner: d.append('L'+f(seg.c)+' '+f(seg.end_point))
    else: d.append('C'+f(seg.c1)+' '+f(seg.c2)+' '+f(seg.end_point))
  d.append('Z')
D=''.join(d); open('gap.d','w').write(D); print(len(pl),len(D))
