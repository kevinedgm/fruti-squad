# Uva E3 · arma banco.html por icono: variantes + confusiones reales de Lucide a trazo 2
import glob,subprocess,os,sys
U='/home/user/fruti-squad/agentes/uva'
CONF={'agave':['sprout','tree-palm','flame','crown'],'earth-oven':['ice-cream-cone','martini','flame','cooking-pot'],
 'masonry-oven':['house','tent','warehouse','brick-wall-fire'],'stone-mill':['cog','ferris-wheel','disc','tractor'],
 'fermenting':['barrel','database','trash','cylinder']}
T=open(f'{U}/assets/banco-prueba.html').read()
for id,cs in CONF.items():
    v=''.join(open(f).read().replace('<svg ',f'<svg data-nombre="{f.split("-")[-1][:-4].upper()} · {os.path.basename(f)[:-4]}" ',1) for f in sorted(glob.glob(f'{id}/variantes/*.svg')))
    c=''
    for n in cs:
        r=subprocess.run(['node',f'{U}/scripts/buscar-lucide.mjs','--svg',n,'--stroke','2'],capture_output=True,text=True).stdout
        if '<svg' not in r: print('falta',n,file=sys.stderr); continue
        c+=r[r.index('<svg'):].replace('<svg ',f'<svg data-nombre="Lucide · {n}" ',1)
    open(f'{id}/banco.html','w').write(T.replace('<!-- UVA:ICONOS -->',v).replace('<!-- UVA:CONFUSIONES -->',c))
print('ok')
