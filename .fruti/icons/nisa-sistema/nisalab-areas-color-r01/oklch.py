import math,json
def s2l(c): return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
def l2s(c): return 12.92*c if c<=.0031308 else 1.055*c**(1/2.4)-.055
def hex2rgb(h): h=h.lstrip('#'); return [int(h[i:i+2],16)/255 for i in (0,2,4)]
def rgb2oklab(r,g,b):
    r,g,b=map(s2l,(r,g,b))
    l=.4122214708*r+.5363325363*g+.0514459929*b; m=.2119034982*r+.6806995451*g+.1073969566*b; s=.0883024619*r+.2817188376*g+.6299787005*b
    l,m,s=[x**(1/3) for x in (l,m,s)]
    return .2104542553*l+.7936177850*m-.0040720468*s, 1.9779984951*l-2.4285922050*m+.4505937099*s, .0259040371*l+.7827717662*m-.8086757660*s
def oklab2rgb(L,a,b):
    l=(L+.3963377774*a+.2158037573*b)**3; m=(L-.1055613458*a-.0638541728*b)**3; s=(L-.0894841775*a-1.2914855480*b)**3
    return [4.0767416621*l-3.3077115913*m+.2309699292*s, -1.2684380046*l+2.6097574011*m-.3413193965*s, -.0041960863*l-.7034186147*m+1.7076147010*s]
def lch(h): L,a,b=rgb2oklab(*hex2rgb(h)); return L,math.hypot(a,b),math.degrees(math.atan2(b,a))%360
def tohex(L,C,H):
    a,b=C*math.cos(math.radians(H)),C*math.sin(math.radians(H)); rgb=oklab2rgb(L,a,b)
    if any(x<-1e-4 or x>1+1e-4 for x in rgb): return None
    return '#'+''.join(f'{round(max(0,min(1,l2s(x)))*255):02X}' for x in rgb)
def maxc(L,H):
    c=0
    while tohex(L,c+.002,H): c+=.002
    return c
def lum(h):
    c=[s2l(x) for x in hex2rgb(h)]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+.05)/(lb+.05)
def de(h1,h2):
    a=rgb2oklab(*hex2rgb(h1)); b=rgb2oklab(*hex2rgb(h2)); return 100*math.dist(a,b)
