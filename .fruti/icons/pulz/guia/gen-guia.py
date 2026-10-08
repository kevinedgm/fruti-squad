# Genera guia-marca.html desde ../final/svg: los SVG en línea pierden su color fijo para seguir el tema de la página.
import re,base64,os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','final','svg')
def raw(n): return open(os.path.join(D,n+'.svg')).read().strip()
def inline(n,cls='',label=None):
    s=re.sub(r'\sstyle="[^"]*"','',raw(n),count=1)
    s=s.replace('<svg ',f'<svg class="{cls}" ' if cls else '<svg ',1)
    if label is None: s=s.replace('role="img" ','aria-hidden="true" ',1)
    return s
def img(n,w,alt=''): return f'<img src="data:image/svg+xml;base64,{base64.b64encode(raw(n).encode()).decode()}" width="{w}" height="{w}" alt="{alt}">'
def imgw(n,alt): return f'<img src="data:image/svg+xml;base64,{base64.b64encode(raw(n).encode()).decode()}" alt="{alt}" style="width:100%;height:auto;display:block">'
B='<rect x="8" y="9" width="48" height="12" rx="3" fill="currentColor"/><rect x="8" y="43" width="48" height="12" rx="3" fill="currentColor"/>'
A='var(--pulz-color)'
paso1=f'<svg viewBox="0 0 64 64" aria-hidden="true">{B}<rect x="11.5" y="12.5" width="41" height="5" rx="2.5" fill="{A}"/></svg>'
paso2=f'<svg viewBox="0 0 64 64" aria-hidden="true">{B}<rect x="33" y="12.5" width="19.5" height="5" rx="2.5" fill="{A}"/><clipPath id="g2"><polygon points="38,21 56,21 26,43 8,43"/></clipPath><polygon clip-path="url(#g2)" points="38,21 56,21 40,32.7 22,32.7" fill="{A}"/></svg>'
paso3=inline('simbolo')
s16=inline('simbolo-16')
HTML=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'plantilla.html')).read()
for k,v in {'HERO':inline('wordmark-animado','wm',label='PULZ'),'PASO1':paso1,'PASO2':paso2,'PASO3':paso3,
 'FIRMA':inline('firma','firma',label='hecho con PULZ'),'S16':s16,
 'APP':img('app-icon-redondeado',112,'Icono de app de PULZ'),'APPSQ':img('app-icon',112,'Icono para iOS'),'MASK':img('app-icon-maskable',112,'Icono maskable'),
 'FAV16':img('favicon',16,'Favicon a 16 px'),'FAV32':img('favicon',32,'Favicon a 32 px'),'FAV48':img('favicon',48,'Favicon a 48 px'),
 'TARJETA':imgw('tarjeta-redes','Tarjeta para redes: PULZ, Del maguey al granel. Producción de mezcal, trazada.'),
 'WMSTAT':inline('wordmark')}.items(): HTML=HTML.replace('{{'+k+'}}',v)
assert '{{' not in HTML
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'guia-marca.html'),'w').write(HTML)
print(len(HTML))
