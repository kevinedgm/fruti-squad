# Calificación en flores de Laranda: 0–5 lóbulos llenos; el quinto (lóbulo separado) solo en 5 y en accent.
L=[(52.2,49.8),(80.8,44.8),(83.0,72.2),(64.0,86.0),(45.0,72.2)]
TEMAS={'claro':dict(brand='#5B3BB5',accent='#E0611A',surface='#FFFFFF'),'oscuro':dict(brand='#C4B5F0',accent='#F2A074',surface='#1A191D')}
def flor(n,t,css=False):
    b=f'var(--brand, {t["brand"]})' if css else t['brand']; a=f'var(--accent, {t["accent"]})' if css else t['accent']; s=f'var(--surface, {t["surface"]})' if css else t['surface']
    out=''
    for i,(x,y) in enumerate(L):
        lleno=i<n
        if lleno:
            col=a if (n==5 and i==1) else b
            out+=f'<circle cx="{x}" cy="{y}" r="15" fill="{col}"/>'
        else:
            out+=f'<circle cx="{x}" cy="{y}" r="13.5" fill="none" stroke="{b}" stroke-width="3"/>'
    out+=f'<circle cx="64" cy="66" r="7" fill="{s}" stroke="{b}" stroke-width="3"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128" role="img" aria-label="{n} de 5">{out}</svg>'
for tn,t in TEMAS.items():
    for n in range(6):
        open(f'svg/calificacion-{n}-{tn}.svg','w').write(flor(n,t))
# versión con variables CSS (una sola, toma el tema del contexto)
for n in range(6): open(f'svg/calificacion-{n}.svg','w').write(flor(n,TEMAS['claro'],css=True))
print('ok')
