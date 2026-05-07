"""Verifica los conteos de cada KPI cruzando con los archivos crudos.
Run: python scripts/verificar-kpis.py
"""
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

print("="*70)
print("  HCD — Concejales vs DDJJ vs Funcionarios HCD")
print("="*70)
fp = find(60) / 'Declaraciones juradas_ HCD_2025.xlsx'
df = pd.read_excel(fp)
print(f"  DDJJ HCD: {len(df)} filas")
print(f"  Cargos: {df['Cargo'].value_counts().to_dict()}")
# Concejales puros (excluyendo Secretario)
concejales = df[df['Cargo'].astype(str).str.upper().str.contains('CONCEJAL', na=False)]
print(f"  Filas con cargo CONCEJAL: {len(concejales)}")
secretarios = df[df['Cargo'].astype(str).str.upper().str.contains('SECRETARIO', na=False)]
print(f"  Filas con cargo SECRETARIO: {len(secretarios)}")

print("\n  Nómina HCD 2025:")
fp_nom = find(55) / 'Nómina HCD_2025.xlsx'
df_nom = pd.read_excel(fp_nom)
print(f"    Total filas: {len(df_nom)}")
print(f"    Cols: {list(df_nom.columns)}")
if 'CategoriaDescripcion' in df_nom.columns:
    print(f"    Por cargo:\n{df_nom['CategoriaDescripcion'].value_counts()}")

print("\n" + "="*70)
print("  FUNCIONARIOS EJECUTIVO (#55)")
print("="*70)
fp = find(55) / 'Nómina Funcionarios Ejecutivo_2025.xlsx'
df = pd.read_excel(fp)
print(f"  Filas: {len(df)}")
# Verificar duplicados por legajo
if 'Legajo' in df.columns:
    print(f"  Legajos únicos: {df['Legajo'].nunique()}")
    dups = df[df['Legajo'].duplicated(keep=False)]
    print(f"  Filas con legajo duplicado: {len(dups)}")
print(f"  Por categoría:\n{df['CategoriaDescripcion'].value_counts()}")

print("\n" + "="*70)
print("  COMERCIOS — total vs activos vs facturan")
print("="*70)
fp = find(87) / 'Comercios por Rubro 2025.xlsx'
df = pd.read_excel(fp)
df['ValorPesos'] = pd.to_numeric(df['ValorPesos'], errors='coerce').fillna(0)
df['UnidadesTributarias'] = pd.to_numeric(df['UnidadesTributarias'], errors='coerce').fillna(0)
print(f"  Total filas: {len(df):,}")
print(f"  Padrones únicos: {df['Padron_Comercio'].nunique():,}")
dup = df[df['Padron_Comercio'].duplicated(keep=False)]
print(f"  Filas con padrón duplicado: {len(dup)}")
print(f"  Con UnidadesTributarias > 0: {(df['UnidadesTributarias']>0).sum():,}")
print(f"  Con ValorPesos > 0: {(df['ValorPesos']>0).sum():,}")
print(f"  Factura == 'Si': {(df['Factura']=='Si').sum():,}")
print(f"  Factura == 'No': {(df['Factura']=='No').sum():,}")
# Padrones únicos que facturan
unicos_factura = df[df['Factura']=='Si']['Padron_Comercio'].nunique()
print(f"  Padrones únicos que facturan: {unicos_factura:,}")
unicos_ut0 = df[df['UnidadesTributarias']==0]['Padron_Comercio'].nunique()
print(f"  Padrones únicos con UT==0 (¿bajas?): {unicos_ut0:,}")

print("\n" + "="*70)
print("  ESCUELAS — total vs duplicados")
print("="*70)
fp = find(6) / 'escuelas.csv'
df = pd.read_csv(fp, encoding='latin-1')
print(f"  Filas: {len(df)}")
print(f"  IDs únicos: {df['id'].nunique()}")
print(f"  Numero (CUE) únicos: {df['numero'].nunique()}")
dups = df[df['numero'].duplicated(keep=False)].sort_values('numero')
if len(dups) > 0:
    print(f"  Duplicados por CUE:")
    print(dups[['id','nombre','numero','distrito','nivel']].to_string())
df['matricula'] = pd.to_numeric(df['matricula'], errors='coerce')
print(f"  Matrícula total (todas las filas): {df['matricula'].sum():,.0f}")
# Matrícula sin duplicados
unique_df = df.drop_duplicates(subset='numero', keep='first')
print(f"  Filas únicas por CUE: {len(unique_df)}")
print(f"  Matrícula total (sin duplicados CUE): {unique_df['matricula'].sum():,.0f}")

print("\n" + "="*70)
print("  CENTROS DE SALUD")
print("="*70)
fp = find(75) / 'centros-de-salud_2025.xlsx'
df = pd.read_excel(fp)
print(f"  Filas: {len(df)}")
print(f"  Cols: {list(df.columns)}")
if 'id_centro_' in df.columns:
    print(f"  IDs centro únicos: {df['id_centro_'].nunique()}")

print("\n" + "="*70)
print("  FARMACIAS")
print("="*70)
fp = find(27) / 'farmacias.csv'
df = pd.read_csv(fp, encoding='latin-1')
print(f"  Filas: {len(df)}")
print(f"  Por nombre único: {df['NombreFant'].nunique()}")

print("\n" + "="*70)
print("  COMISARIAS (#24)")
print("="*70)
fp = find(24)
if fp:
    for f in fp.iterdir():
        if f.suffix.lower() == '.xlsx':
            df = pd.read_excel(f)
            print(f"  Archivo: {f.name}")
            print(f"  Filas: {len(df)}")
            print(f"  Cols: {list(df.columns)}")
            print(df.head(20).to_string(max_colwidth=30))

print("\n" + "="*70)
print("  OBRAS 2025 — actividades vs proyectos únicos")
print("="*70)
fp = find(74) / 'Obras Publicas_2025.xlsx'
df = pd.read_excel(fp)
print(f"  Filas (actividades): {len(df)}")
if 'ID Proyecto' in df.columns:
    print(f"  Proyectos únicos: {df['ID Proyecto'].nunique()}")
    print(f"  Actividades por proyecto (top 10):")
    print(df['ID Proyecto'].value_counts().head(10).to_string())

print("\n" + "="*70)
print("  GASTRONOMIA (#20) — duplicados")
print("="*70)
fp = find(20) / 'gastronomia.csv'
df = pd.read_csv(fp, encoding='latin-1')
print(f"  Filas: {len(df)}")
print(f"  Nombres únicos: {df['nombre'].nunique()}")
dup = df[df['nombre'].duplicated(keep=False)]
if len(dup) > 0:
    print(f"  Duplicados ({len(dup)} filas):")
    print(dup.sort_values('nombre')[['nombre','distrito','TIPO']].head(10).to_string())

print("\n" + "="*70)
print("  ALOJAMIENTOS — duplicados")
print("="*70)
fp = find(12) / 'alojamiento.csv'
df = pd.read_csv(fp, encoding='latin-1')
print(f"  Filas: {len(df)}")
print(f"  Nombres únicos: {df['nombre'].nunique()}")
dup = df[df['nombre'].duplicated(keep=False)]
if len(dup) > 0:
    print(f"  Duplicados ({len(dup)} filas):")
    print(dup.sort_values('nombre')[['nombre','distrito']].head(10).to_string())

print("\n" + "="*70)
print("  ESPACIOS VERDES — total vs únicos")
print("="*70)
fp = find(9) / 'espacios_verdes.csv'
df = pd.read_csv(fp, encoding='latin-1')
print(f"  Filas: {len(df)}")
print(f"  GIDs únicos: {df['gid'].nunique()}")
df['sup_m2'] = pd.to_numeric(df['sup_m2'], errors='coerce')
print(f"  Suma m2 (con NA): {df['sup_m2'].sum():,.0f}")
print(f"  Filas con NA en sup_m2: {df['sup_m2'].isna().sum()}")

print("\n" + "="*70)
print("  BARRIOS POPULARES — total vs únicos")
print("="*70)
fp = find(5) / 'barrios_populares_1.csv'
df = pd.read_csv(fp, encoding='latin-1')
print(f"  Filas: {len(df)}")
print(f"  IDs RENABAP únicos: {df['id_renabap'].nunique()}")

print("\n" + "="*70)
print("  DECLARACIONES JURADAS EJECUTIVO (#60)")
print("="*70)
fp = find(60) / 'DDJJ 2025.xlsx'
df = pd.read_excel(fp)
print(f"  Filas: {len(df)}")
print(f"  Por cargo (top): {df['Cargo'].value_counts().head(10).to_dict()}")
