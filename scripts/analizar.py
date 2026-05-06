"""Análisis profundo de los datasets clave para los informes ejecutivos."""
import pandas as pd
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

DS = Path('data/datasets')
def find(ds_id):
    for d in DS.iterdir():
        if d.name.startswith(f"{ds_id}-"):
            return d/'archivos'
    return None
def fmt_M(n):
    if pd.isna(n) or n == 0: return '-'
    n = float(n)
    if abs(n) >= 1e9: return f"${n/1e9:,.1f} mil M"
    if abs(n) >= 1e6: return f"${n/1e6:,.1f} M"
    if abs(n) >= 1e3: return f"${n/1e3:,.0f} mil"
    return f"${n:,.0f}"

print("="*70)
print("  PAUTA PUBLICITARIA evolucion 2020-2024 (#42)")
print("="*70)
fp = find(42) / 'pauta_publicitaria-2020-2021-2022 - 2023 - 2024.xlsx'
df = pd.read_excel(fp, sheet_name='Pauta Contratada')
total_row = df[df.iloc[:,0].astype(str).str.upper().str.contains('TOTAL', na=False)].iloc[0]
years = ['2020','2021','2022','2023','2024']
totales = []
for col in df.columns[1:6]:
    val = pd.to_numeric(total_row[col], errors='coerce')
    totales.append(val)
print("Anio | Pauta total       | Variacion nominal interanual")
prev = None
for y, t in zip(years, totales):
    var = f"+{(t/prev-1)*100:.0f}%" if prev else "-"
    print(f"  {y} | {fmt_M(t):>16} | {var}")
    prev = t
print(f"Crecimiento total 2020->2024 nominal: x{totales[-1]/totales[0]:.1f}")

print("\n" + "="*70)
print("  RESIDUOS - Disposicion final El Borbollon (#88)")
print("="*70)
fp = find(88) / 'Cantidad_2021-2022-2023-2024-2025.xlsx'
xl = pd.ExcelFile(fp)
totales_anuales = {}
for sh in ['2021','2022','2023','2024','2025']:
    if sh not in xl.sheet_names: continue
    df = pd.read_excel(fp, sheet_name=sh, skiprows=6, usecols=[0,1])
    df.columns = ['MES', 'TON']
    df['TON'] = pd.to_numeric(df['TON'], errors='coerce')
    df = df[df['TON'].notna() & (df['TON']>0)]
    totales_anuales[sh] = df['TON'].sum()
    print(f"  {sh}: {df['TON'].sum():>9,.0f} ton ({len(df)} meses con dato | promedio mensual: {df['TON'].mean():.0f} ton)")
hab = 172109
for y in ['2022','2023']:
    if y in totales_anuales:
        print(f"  Per capita {y} (n={hab} hab): {totales_anuales[y]/hab*1000:.1f} kg/hab/anio = {totales_anuales[y]/hab/365:.2f} kg/hab/dia")

print("\n" + "="*70)
print("  CALIDAD DEL AIRE - Sensor Parque Civico (#44)")
print("="*70)
fp = find(44) / 'metricas-snsores-ambientals.xlsx'
df = pd.read_excel(fp, sheet_name='Histórico')
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
print(f"  Mediciones totales: {len(df):,} | periodo {df['Fecha'].min().date()} -> {df['Fecha'].max().date()} | dias con datos: {df['Fecha'].dt.date.nunique()}")
for param in df['Parámetro'].unique():
    sub = df[df['Parámetro']==param]['Valor'].dropna()
    print(f"  {param}: n={len(sub):,} | min {sub.min():.1f} | max {sub.max():.1f} | mean {sub.mean():.1f} | mediana {sub.median():.1f}")

print("\n" + "="*70)
print("  ESPACIOS VERDES - densidad por distrito (#9)")
print("="*70)
fp = find(9) / 'espacios_verdes.csv'
df = pd.read_csv(fp, encoding='latin-1')
df['sup_m2'] = pd.to_numeric(df['sup_m2'], errors='coerce')
pop = pd.read_csv(find(8)/'distritos.csv', encoding='latin-1')[['distrito','poblacion']]
pop['distrito'] = pop['distrito'].str.strip().str.upper()
df['distrito_n'] = (df['distrito'].astype(str).str.strip().str.upper()
                    .str.replace('CHACRAS DE CORIS','CHACRAS DE CORIA')
                    .str.replace('CARRODILLA{','CARRODILLA')
                    .str.replace('MAYOR DRUMMOND','MAYOR DRUMOND'))
ev_dist = df.groupby('distrito_n').agg(espacios=('gid','count'), m2=('sup_m2','sum')).reset_index()
m = ev_dist.merge(pop, left_on='distrito_n', right_on='distrito', how='left')
m['m2_per_cap'] = m['m2'] / m['poblacion'].replace(0, pd.NA)
print("  Distrito        | Pob.   | Espacios | m2 total   | m2/hab")
for _, r in m.sort_values('m2', ascending=False).head(10).iterrows():
    pop_v = r['poblacion'] if pd.notna(r['poblacion']) else 0
    pc = r['m2_per_cap'] if pd.notna(r['m2_per_cap']) else 0
    print(f"  {str(r['distrito_n'])[:15]:<15} | {pop_v:>6.0f} | {r['espacios']:>4.0f}     | {r['m2']:>10,.0f} | {pc:>6.1f}")
print(f"\n  Total municipal: {df.shape[0]} espacios | {df['sup_m2'].sum():,.0f} m2 | {df['sup_m2'].sum()/172109:.1f} m2/hab")

print("\n" + "="*70)
print("  ESCUELAS - distribucion y matricula (#6)")
print("="*70)
fp = find(6) / 'escuelas.csv'
df = pd.read_csv(fp, encoding='latin-1')
df['matricula'] = pd.to_numeric(df['matricula'], errors='coerce')
print(f"  Establecimientos: {len(df)} | matricula total: {df['matricula'].sum():,.0f}")
gestion = df['gestion'].value_counts()
print(f"  Por gestion: {gestion.to_dict()}")
ambito = df['ambito'].value_counts()
print(f"  Por ambito: {ambito.to_dict()}")
nivel_top = df.groupby('nivel')['matricula'].agg(['count','sum']).sort_values('sum', ascending=False).head(8)
print("  Por nivel (con matricula):")
for niv, r in nivel_top.iterrows():
    print(f"    {str(niv)[:35]:<35} | {r['count']:>3.0f} estab | {r['sum']:>6,.0f} alumnos")
df['distrito_n'] = df['distrito'].astype(str).str.strip().str.upper().str.replace('MAYOR DRUMMOND','MAYOR DRUMOND')
mat_dist = df.groupby('distrito_n').agg(esc=('id','count'), mat=('matricula','sum')).reset_index()
m = mat_dist.merge(pop, left_on='distrito_n', right_on='distrito', how='left')
m['mat_per_pob'] = m['mat'] / m['poblacion'].replace(0, pd.NA) * 100
print("  Por distrito - % de la poblacion local matriculada en escuelas locales:")
for _, r in m.sort_values('mat', ascending=False).head(10).iterrows():
    pop_v = r['poblacion'] if pd.notna(r['poblacion']) else 0
    pc = r['mat_per_pob'] if pd.notna(r['mat_per_pob']) else 0
    print(f"    {str(r['distrito_n'])[:18]:<18} | pob {pop_v:>6.0f} | esc {r['esc']:>3.0f} | mat {r['mat']:>6,.0f} | {pc:>5.1f}%")

print("\n" + "="*70)
print("  ELECCIONES PASO 2023 - agrupaciones por distrito (#32)")
print("="*70)
fp = find(32) / 'resultados_pasos_2023.xlsx'
df = pd.read_excel(fp)
df['cantidad_por_mesa'] = pd.to_numeric(df['cantidad_por_mesa'], errors='coerce').fillna(0)
print(f"  Mesas relevadas: {df['mesa'].nunique()}")
print(f"  Total votos: {df['cantidad_por_mesa'].sum():,.0f}")
top = df.groupby('nombre_agrupacion')['cantidad_por_mesa'].sum().sort_values(ascending=False)
total = top.sum()
print("  Top agrupaciones (cat. Concejal):")
for ag, v in top.head(8).items():
    print(f"    {str(ag)[:50]:<50} | {v:>5,.0f} ({v/total*100:.1f}%)")
print("  Por distrito:")
for d, sub in df.groupby('distrito'):
    tot_d = sub['cantidad_por_mesa'].sum()
    top1 = sub.groupby('nombre_agrupacion')['cantidad_por_mesa'].sum().sort_values(ascending=False).head(2)
    items = list(top1.items())
    if len(items) >= 2:
        primero, segundo = items[0], items[1]
        print(f"    {d:<18} | total {tot_d:>5,.0f} | 1deg {primero[0][:25]}: {primero[1]:.0f} ({primero[1]/tot_d*100:.0f}%) | 2deg {segundo[0][:25]}: {segundo[1]:.0f} ({segundo[1]/tot_d*100:.0f}%)")

print("\n" + "="*70)
print("  COVID 2022 (#67)")
print("="*70)
fp = find(67) / 'informe-covid-2022.xlsx'
df = pd.read_excel(fp, header=None)
df.columns = list(df.iloc[0])
df = df.iloc[1:]
for c in ['Positivos','Recuperados','Fallecidos','En tratamiento','Total']:
    df[c] = pd.to_numeric(df[c], errors='coerce')
print(f"  Semanas registradas: {df['Positivos'].notna().sum()}")
print(f"  Total positivos:    {df['Positivos'].sum():.0f}")
print(f"  Total recuperados:  {df['Recuperados'].sum():.0f}")
print(f"  Total fallecidos:   {df['Fallecidos'].sum():.0f}")
print(f"  Pico semanal positivos: {df['Positivos'].max():.0f}")
print(f"  Promedio semanal positivos: {df['Positivos'].mean():.1f}")
print(f"  Total acumulado al cierre: {df['Total'].max():.0f}")

print("\n" + "="*70)
print("  COMERCIOS POR RUBRO 2025 (#87)")
print("="*70)
fp = find(87) / 'Comercios por Rubro 2025.xlsx'
df = pd.read_excel(fp)
df['ValorPesos'] = pd.to_numeric(df['ValorPesos'], errors='coerce').fillna(0)
df['UnidadesTributarias'] = pd.to_numeric(df['UnidadesTributarias'], errors='coerce').fillna(0)
print(f"  Comercios: {len(df):,} | UT total: {df['UnidadesTributarias'].sum():,.0f}")
print(f"  Valor pesos total: {fmt_M(df['ValorPesos'].sum())} | facturan: {(df['Factura']=='Si').sum():,} ({(df['Factura']=='Si').mean()*100:.0f}%)")
non_gen = df[df['Descripción'].fillna('').str.upper().ne('GENERICO')].copy()
print(f"  Comercios con rubro identificado (no GENERICO): {len(non_gen):,}")
top_rub = non_gen.groupby('Descripción').size().sort_values(ascending=False).head(10)
print("  Top rubros identificados:")
for r, c in top_rub.items():
    print(f"    {str(r)[:55]:<55} | {c}")

print("\n" + "="*70)
print("  OBRAS PUBLICAS 2025 (#74)")
print("="*70)
fp = find(74) / 'Obras Publicas_2025.xlsx'
df = pd.read_excel(fp)
print(f"  Actividades: {len(df)}")
print(f"  Por estado:\n{df['Estado Actividad'].value_counts()}")
print(f"  Por eje:\n{df['Eje'].value_counts()}")
if 'Programa' in df.columns:
    print(f"  Top programas:\n{df['Programa'].value_counts().head(8)}")
if 'Secretaria' in df.columns:
    print(f"  Por secretaria:\n{df['Secretaria'].value_counts().head(8)}")

print("\n" + "="*70)
print("  GASTRONOMIA y ALOJAMIENTO (#20, #12) - oferta turistica")
print("="*70)
gas = pd.read_csv(find(20)/'gastronomia.csv', encoding='latin-1')
alo = pd.read_csv(find(12)/'alojamiento.csv', encoding='latin-1')
print(f"  Gastronomia: {len(gas)} locales | tipos: {gas['TIPO'].value_counts().head(5).to_dict()}")
print(f"  Alojamiento: {len(alo)} | concentracion en Potrerillos: {(alo['distrito'].str.upper()=='POTRERILLOS').sum()}/{len(alo)}")

print("\n" + "="*70)
print("  CENTROS DE SALUD por DISTRITO vs poblacion (#75)")
print("="*70)
fp = find(75) / 'centros-de-salud_2025.xlsx'
df = pd.read_excel(fp)
df['distrito_n'] = df['distrito'].astype(str).str.strip().str.upper()
cs = df.groupby('distrito_n').size().reset_index(name='centros')
m = cs.merge(pop, left_on='distrito_n', right_on='distrito', how='left')
m['hab_por_centro'] = m['poblacion'] / m['centros']
print("  Distrito        | Pob.   | Centros | Hab/Centro")
for _, r in m.sort_values('hab_por_centro', ascending=True).iterrows():
    pop_v = r['poblacion'] if pd.notna(r['poblacion']) else 0
    hpc = r['hab_por_centro'] if pd.notna(r['hab_por_centro']) else 0
    print(f"  {str(r['distrito_n'])[:15]:<15} | {pop_v:>6.0f} | {r['centros']:>4.0f}    | {hpc:>8,.0f}")

print("\n" + "="*70)
print("  GENERO - cortes 2022 (#72)")
print("="*70)
fp = find(72) / 'estadisticas2022-copia.xlsx'
xl = pd.ExcelFile(fp)
def read_sh(sh, fp=fp):
    df = pd.read_excel(fp, sheet_name=sh, header=None)
    df = df.iloc[3:]
    out = []
    for _, r in df.iterrows():
        l = r.iloc[0]
        v = r.iloc[1]
        if pd.notna(l) and pd.notna(v) and isinstance(v, (int, float)):
            out.append((str(l).strip(), int(v)))
    return out

for sh in ['niv_educ','depto_victima','tipo_lugar','est_civ_v','vinculo','tiene_disc','75_fisica','75_piscol','75_econ_patr','75_sexual','82_viol_ant','64_cond_act','78_cons_alc','94_penal']:
    try:
        rows = read_sh(sh)
        if rows:
            total = sum(v for _,v in rows)
            print(f"  {sh} (total: {total}):")
            for l,v in sorted(rows, key=lambda x: -x[1])[:5]:
                print(f"    {l[:40]:<40}: {v} ({v/total*100:.0f}%)")
    except Exception as e:
        print(f"  {sh}: error {e}")
