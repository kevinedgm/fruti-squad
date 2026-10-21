# Datos ficticios de un palenque mediano: 12 lotes en 12 meses. Realistas pero inventados (rendimientos típicos de espadín y tobalá).
import csv,random
random.seed(42)
rows=[]
meses=['2025-10','2025-11','2025-12','2026-01','2026-02','2026-03','2026-04','2026-05','2026-06','2026-07','2026-08','2026-09']
for i,m in enumerate(meses):
    agave='Tobalá' if i in (3,9) else ('Madrecuixe' if i==6 else 'Espadín')
    kg=random.randint(5200,8200) if agave=='Espadín' else random.randint(2400,3600)
    # rendimiento típico: espadín 8–10 kg/L, tobalá 14–18, madrecuixe 12–15
    rend={'Espadín':random.uniform(7.8,10.2),'Tobalá':random.uniform(14,18),'Madrecuixe':random.uniform(12,15)}[agave]
    litros=kg/rend
    # mermas por etapa (% del agave/jugo): horneado (cocción), molienda, fermentación, destilación
    horneado=random.uniform(.04,.09); molienda=random.uniform(.02,.05); ferment=random.uniform(.03,.08); destil=random.uniform(.05,.11)
    if i==4: ferment=.14   # lote con fermentación fallida (lluvia, temperatura)
    if i==8: horneado=.13  # horno mal sellado
    grado=round(random.uniform(45,52),1)
    costo_agave=kg*(random.uniform(9,12) if agave=='Espadín' else random.uniform(28,38))
    costo_lena=random.randint(6000,9500); mano=random.randint(14000,20000); otros=random.randint(3000,5000)
    costo=costo_agave+costo_lena+mano+otros
    dias=random.randint(18,30)
    rows.append(dict(lote=f'L{i+1:02d}',mes=m,agave=agave,kg_agave=kg,litros=round(litros,1),rendimiento_kg_por_l=round(rend,2),grado=grado,
        merma_horneado=round(horneado,3),merma_molienda=round(molienda,3),merma_fermentacion=round(ferment,3),merma_destilacion=round(destil,3),
        costo_total_mxn=round(costo),costo_por_litro_mxn=round(costo/litros,1),dias_proceso=dias,precio_venta_litro_mxn=random.choice([420,450,480]) if agave=='Espadín' else random.choice([900,950,1050])))
with open('lotes.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
# ventas mensuales por canal (litros)
vent=[]
for m in meses:
    for canal,base in (('Nacional',260),('Exportación',140),('Palenque',60)):
        vent.append(dict(mes=m,canal=canal,litros=round(base*random.uniform(.7,1.3)),ingreso_mxn=0))
for v in vent: v['ingreso_mxn']=round(v['litros']*({'Nacional':470,'Exportación':620,'Palenque':380}[v['canal']]))
with open('ventas.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(vent[0])); w.writeheader(); w.writerows(vent)
print(len(rows),len(vent)); import json; print(json.dumps(rows[4],ensure_ascii=False))
