"""Reemplaza los JSON de informe con KPIs y charts del fenómeno municipal,
no del catálogo. Sobreescribe lo que produce build-data.cjs.
Run: python scripts/build-informes-data.py
"""
import json
from pathlib import Path
from datetime import date

OUT = Path('public/data/informes')
OUT.mkdir(parents=True, exist_ok=True)
TODAY = date.today().isoformat()


def build(slug, title, kpis, charts, rankings=None):
    return {
        'meta': {
            'id': slug,
            'title': title,
            'category': title,
            'source': 'Portal de Datos Abiertos – Luján de Cuyo (datos.lujandecuyo.gob.ar)',
            'date': TODAY,
        },
        'kpis': kpis,
        'charts': charts,
        'rankings': rankings or [],
        'mapData': [],
    }


def kpi(id_, label, value, formatted, unit=None):
    return {'id': id_, 'label': label, 'value': value, 'formatted': formatted, **({'unit': unit} if unit else {})}


def chart(id_, ctype, title, sectionId, data, config=None):
    out = {'id': id_, 'type': ctype, 'title': title, 'sectionId': sectionId, 'data': data}
    if config:
        out['config'] = config
    return out


# 1. GOBIERNO MUNICIPAL
build_data = {}
build_data['gobierto-y-sector-publico'] = build(
    'gobierto-y-sector-publico', 'Gobierno Municipal',
    [
        kpi('presup', 'Presupuesto 2025', 111800000000, '$111,8 mil M'),
        kpi('personal', 'Gasto en personal', 20800000000, '$20,8 mil M', '19% del total'),
        kpi('compras', 'Compras y contrataciones 2024', 5065000000, '$5,1 mil M'),
        kpi('pauta', 'Pauta publicitaria 2024', 296170317, '$296,2 M'),
    ],
    [
        chart('estructura-gasto', 'pie', 'Estructura del gasto 2025', 'el-presupuesto-2025', [
            {'id': 'Erogaciones corrientes', 'label': 'Corrientes', 'value': 71100},
            {'id': 'Erogaciones de capital', 'label': 'Capital', 'value': 38900},
            {'id': 'Otras erogaciones', 'label': 'Otras', 'value': 160},
        ]),
        chart('pauta-evolucion', 'line', 'Pauta publicitaria — evolución 2020-2024 (M $)', 'pauta-publicitaria-el-rubro-de-mayor-crecimiento', [
            {'anio': '2020', 'pauta': 24.5},
            {'anio': '2021', 'pauta': 45.2},
            {'anio': '2022', 'pauta': 92.8},
            {'anio': '2023', 'pauta': 194.8},
            {'anio': '2024', 'pauta': 296.2},
        ], {'xAxis': 'anio'}),
        chart('compras-modalidad', 'bar', 'Compras 2024 por modalidad (M $)', 'compras-y-contrataciones-2024', [
            {'modalidad': 'Licitación pública', 'monto': 4400},
            {'modalidad': 'Compra directa', 'monto': 356},
            {'modalidad': 'Privada', 'monto': 330},
        ], {'xAxis': 'modalidad'}),
    ],
    rankings=[{
        'id': 'top-proveedores',
        'title': 'Top 7 contratos 2024',
        'sectionId': '',
        'order': 'desc',
        'items': [
            {'name': 'Plan Pavimentación 2024 — VIALMANI', 'value': 635000000, 'meta': '$635 M'},
            {'name': 'Servicio de Poda — ECUR S.A.', 'value': 450000000, 'meta': '$450 M'},
            {'name': 'Redes de Agua Potable — CALZETTA S.A.', 'value': 237700000, 'meta': '$237,7 M'},
            {'name': 'Vehículos utilitarios — VALENTINO MOTOS', 'value': 230800000, 'meta': '$230,8 M'},
            {'name': 'Alquiler camiones regadores — ECUR S.A.', 'value': 218600000, 'meta': '$218,6 M'},
            {'name': 'Adquisición hidroelevador — FICAMEN S.A.', 'value': 106500000, 'meta': '$106,5 M'},
            {'name': 'Automóviles — CAPILLITAS S.A.', 'value': 101500000, 'meta': '$101,5 M'},
        ]
    }]
)

# 2. MEDIO AMBIENTE
build_data['medio-ambiente-y-desarrollo-sustentable'] = build(
    'medio-ambiente-y-desarrollo-sustentable', 'Medio Ambiente y Desarrollo Sustentable',
    [
        kpi('residuos', 'Residuos a relleno 2023', 18142, '18.142 ton', 'pico de la serie'),
        kpi('per-capita', 'Per cápita 2023', 105, '105 kg/hab/año'),
        kpi('mediciones-aire', 'Mediciones aire (sensor)', 9632, '9.632'),
        kpi('plantas-agua', 'Plantas potabilizadoras', 2, '2', 'Cipolletti + Santa Elena'),
    ],
    [
        chart('residuos-evolucion', 'bar', 'Residuos dispuestos en El Borbollón (toneladas/año)', 'la-curva-de-los-residuos', [
            {'anio': '2021', 'toneladas': 4485},
            {'anio': '2022', 'toneladas': 10735},
            {'anio': '2023', 'toneladas': 18142},
            {'anio': '2024 *', 'toneladas': 4492},
            {'anio': '2025 *', 'toneladas': 1558},
        ], {'xAxis': 'anio'}),
        chart('aire-medianas', 'bar', 'Calidad del aire — medianas medidas en Parque Cívico', 'calidad-del-aire-lo-que-mide-el-sensor-del-parque-civico', [
            {'parametro': 'Temperatura (°C)', 'valor': 20.6},
            {'parametro': 'Humedad (%)', 'valor': 25.1},
            {'parametro': 'PM 2,5 (µg/m³)', 'valor': 3.0},
            {'parametro': 'PM 10 (µg/m³)', 'valor': 4.0},
            {'parametro': 'NO₂ (µg/m³)', 'valor': 6.1},
        ], {'xAxis': 'parametro', 'layout': 'horizontal'}),
    ],
    rankings=[{
        'id': 'reciclaje',
        'title': 'Centro Verde — material recuperado promedio mensual (kg, ene-may 2025)',
        'sectionId': '',
        'order': 'desc',
        'items': [
            {'name': 'Cartón', 'value': 9000, 'meta': '~9.000 kg/mes'},
            {'name': 'Plástico', 'value': 2500, 'meta': '~2.500 kg/mes'},
            {'name': 'Tetra brik', 'value': 240, 'meta': '~240 kg/mes'},
            {'name': 'Aluminio + Chatarra', 'value': 1800, 'meta': '~1.800 kg/mes'},
        ]
    }]
)

# 3. ECONOMIA
build_data['economia'] = build(
    'economia', 'Economía',
    [
        kpi('presup', 'Presupuesto 2025', 111800000000, '$111,8 mil M'),
        kpi('comercios', 'Comercios registrados', 7245, '7.245', '11.630 registros de rubro'),
        kpi('compras', 'Compras 2024', 5065000000, '$5,1 mil M'),
        kpi('barrios-pop', 'Familias en barrios populares', 2569, '2.569', 'en 47 barrios'),
    ],
    [
        chart('presup-pie', 'pie', 'Estructura del presupuesto 2025 (mil M $)', 'las-finanzas-del-municipio', [
            {'id': 'Corrientes', 'label': 'Corrientes', 'value': 71.1},
            {'id': 'Capital', 'label': 'Capital', 'value': 38.9},
            {'id': 'Otras', 'label': 'Otras', 'value': 0.16},
        ]),
        chart('top-rubros', 'bar', 'Top rubros del padrón comercial 2025', 'el-padron-comercial', [
            {'rubro': 'Almacén', 'comercios': 314},
            {'rubro': 'Productos no clasif.', 'comercios': 181},
            {'rubro': 'Almacenes alimentos', 'comercios': 166},
            {'rubro': 'Servicios empresariales', 'comercios': 115},
            {'rubro': 'Golosinas/Confit.', 'comercios': 109},
            {'rubro': 'Frutas/Verduras', 'comercios': 106},
            {'rubro': 'Tabacos/Cigarrillos', 'comercios': 102},
            {'rubro': 'Prendas/Accesorios', 'comercios': 92},
            {'rubro': 'Servicios inmobiliarios', 'comercios': 91},
        ], {'xAxis': 'rubro', 'layout': 'horizontal'}),
        chart('obras-estado', 'pie', 'Plan de Obras 2025 — estado de avance', 'la-inversion-en-obras', [
            {'id': 'Cumplido', 'label': 'Cumplido', 'value': 67},
            {'id': 'No iniciado', 'label': 'No iniciado', 'value': 40},
            {'id': 'En implementación', 'label': 'En implementación', 'value': 34},
            {'id': 'Atrasado', 'label': 'Atrasado', 'value': 18},
            {'id': 'Cancelado', 'label': 'Cancelado', 'value': 11},
        ]),
    ],
    rankings=[{
        'id': 'barrios-pop-top',
        'title': 'Top 5 barrios populares por familias',
        'sectionId': '',
        'order': 'desc',
        'items': [
            {'name': 'Valle Encantado (Chacras de Coria)', 'value': 290},
            {'name': 'Tierras Vivas (Agrelo)', 'value': 170},
            {'name': 'Patrono Santiago (Ciudad)', 'value': 160},
            {'name': 'Virgen de Lourdes (Perdriel)', 'value': 135},
            {'name': 'Costanera Sur (Ciudad)', 'value': 132},
        ]
    }]
)

# 4. URBANISMO Y TERRITORIO
build_data['urbanismo-y-territorio'] = build(
    'urbanismo-y-territorio', 'Urbanismo y Territorio',
    [
        kpi('hab', 'Habitantes (Censo 2021)', 172109, '172.109'),
        kpi('distritos', 'Distritos', 15, '15'),
        kpi('m2-verde', 'Espacios verdes (m²/hab)', 7.8, '7,8 m²/hab', 'OMS recomienda ≥9'),
        kpi('barrios-pop', 'Barrios populares (RENABAP)', 47, '47', '2.569 familias'),
    ],
    [
        chart('pob-distrito', 'bar', 'Población por distrito', 'la-distribucion-poblacional', [
            {'distrito': 'Ciudad', 'pob': 24594},
            {'distrito': 'Carrodilla', 'pob': 23886},
            {'distrito': 'Perdriel', 'pob': 13687},
            {'distrito': 'Chacras de Coria', 'pob': 12428},
            {'distrito': 'Vistalba', 'pob': 8771},
            {'distrito': 'Mayor Drumond', 'pob': 8223},
            {'distrito': 'Agrelo', 'pob': 7507},
            {'distrito': 'Ugarteche', 'pob': 6603},
            {'distrito': 'El Carrizal', 'pob': 4177},
            {'distrito': 'La Puntilla', 'pob': 2842},
            {'distrito': 'V. Pedemonte', 'pob': 2428},
            {'distrito': 'Potrerillos', 'pob': 2075},
            {'distrito': 'Las Compuertas', 'pob': 1353},
            {'distrito': 'Cacheuta', 'pob': 701},
            {'distrito': 'Industrial', 'pob': 41},
        ], {'xAxis': 'distrito', 'layout': 'horizontal'}),
        chart('m2-hab-distrito', 'bar', 'Espacio verde por habitante (m²/hab) — distritos seleccionados', 'espacios-verdes-una-distribucion-desigual', [
            {'distrito': 'Ciudad', 'm2_hab': 31.5},
            {'distrito': 'Potrerillos', 'm2_hab': 31.4},
            {'distrito': 'La Puntilla', 'm2_hab': 17.4},
            {'distrito': 'V. Pedemonte', 'm2_hab': 10.7},
            {'distrito': 'El Carrizal', 'm2_hab': 9.5},
            {'distrito': 'Carrodilla', 'm2_hab': 9.3},
            {'distrito': 'Mayor Drumond', 'm2_hab': 7.2},
            {'distrito': 'Vistalba', 'm2_hab': 5.3},
            {'distrito': 'Perdriel', 'm2_hab': 1.9},
            {'distrito': 'Chacras de Coria', 'm2_hab': 1.4},
        ], {'xAxis': 'distrito', 'layout': 'horizontal'}),
    ]
)

# 5. DEPORTE / EDU / SALUD
build_data['deporte-educacion-y-salud'] = build(
    'deporte-educacion-y-salud', 'Deporte, Educación y Salud',
    [
        kpi('alumnos', 'Matrícula escolar', 17318, '17.318 alumnos'),
        kpi('escuelas', 'Establecimientos', 112, '112', '76% pública'),
        kpi('centros-salud', 'Centros de salud', 19, '19', 'primer nivel'),
        kpi('farmacias', 'Farmacias', 18, '18'),
    ],
    [
        chart('matricula-nivel', 'pie', 'Matrícula por nivel educativo', 'el-sistema-educativo-17-318-alumnos-en-112-establecimientos', [
            {'id': 'Primaria', 'label': 'Primaria', 'value': 12308},
            {'id': 'Secundaria común', 'label': 'Secundaria común', 'value': 2171},
            {'id': 'Sec. orientada', 'label': 'Sec. orientada', 'value': 1441},
            {'id': 'Sec. técnica', 'label': 'Sec. técnica', 'value': 737},
            {'id': 'CEBJA', 'label': 'CEBJA', 'value': 250},
            {'id': 'Educación superior', 'label': 'Sup./CENS/Especial', 'value': 364},
        ]),
        chart('matricula-distrito', 'bar', 'Matrícula como % de la población local — top distritos', 'el-polo-educativo-mayor-drumond', [
            {'distrito': 'Mayor Drumond', 'porcentaje': 35.4},
            {'distrito': 'Ciudad', 'porcentaje': 22.3},
            {'distrito': 'Ugarteche', 'porcentaje': 20.6},
            {'distrito': 'Perdriel', 'porcentaje': 11.9},
            {'distrito': 'Carrodilla', 'porcentaje': 11.3},
            {'distrito': 'Chacras de Coria', 'porcentaje': 9.5},
            {'distrito': 'Agrelo', 'porcentaje': 8.7},
            {'distrito': 'Vistalba', 'porcentaje': 4.1},
        ], {'xAxis': 'distrito', 'layout': 'horizontal'}),
        chart('hab-centro', 'bar', 'Habitantes por centro de salud (cobertura)', 'la-red-de-salud-cobertura-desigual', [
            {'distrito': 'Ciudad', 'hab_centro': 24594},
            {'distrito': 'Chacras de Coria', 'hab_centro': 12428},
            {'distrito': 'Carrodilla', 'hab_centro': 7962},
            {'distrito': 'Perdriel', 'hab_centro': 6844},
            {'distrito': 'Ugarteche', 'hab_centro': 3302},
            {'distrito': 'Agrelo', 'hab_centro': 2502},
            {'distrito': 'El Carrizal', 'hab_centro': 2088},
            {'distrito': 'Las Compuertas', 'hab_centro': 1353},
            {'distrito': 'Potrerillos', 'hab_centro': 1038},
            {'distrito': 'Cacheuta', 'hab_centro': 350},
        ], {'xAxis': 'distrito', 'layout': 'horizontal'}),
    ]
)

# 6. HCD
build_data['honorable-consejo-deliberante-lujan-de-cuyo'] = build(
    'honorable-consejo-deliberante-lujan-de-cuyo', 'Honorable Concejo Deliberante',
    [
        kpi('concejales', 'Concejales (mandato 2023/2027)', 12, '12'),
        kpi('ddjj', 'Declaraciones juradas publicadas', 13, '13', '12 concejales + 1 secretario'),
        kpi('mesas', 'Mesas escrutadas (Concejal)', 334, '334'),
        kpi('personal', 'Gasto en personal HCD', 1300000000, '$1,3 mil M', '6% del personal total'),
    ],
    [
        chart('concejal-2023-pie', 'pie', 'Concejales 2023 — escrutinio definitivo (votos)', 'la-composicion-del-cuerpo', [
            {'id': 'La Unión Mendocina', 'label': 'La Unión Mendocina', 'value': 32166},
            {'id': 'Cambia Mendoza', 'label': 'Cambia Mendoza', 'value': 22644},
            {'id': 'Elegí Mendoza', 'label': 'Elegí Mendoza', 'value': 6694},
            {'id': 'Partido Verde', 'label': 'Partido Verde', 'value': 5837},
            {'id': 'FIT', 'label': 'FIT', 'value': 2527},
        ]),
        chart('hcd-personal', 'bar', 'Personal HCD por categoría', 'geografia-del-voto', [
            {'categoria': 'Concejal', 'personas': 13},
        ], {'xAxis': 'categoria'}),
    ]
)

# 7. CULTURA Y TURISMO
build_data['cultura-y-turismo'] = build(
    'cultura-y-turismo', 'Turismo y Cultura',
    [
        kpi('gastro', 'Locales gastronómicos', 137, '137'),
        kpi('alojamiento', 'Alojamientos', 73, '73', '73% en Potrerillos'),
        kpi('aventura', 'Prestadores de aventura', 11, '11', 'todos en Potrerillos'),
        kpi('restaurantes', 'Restaurantes', 84, '84', '61% del total gastro'),
    ],
    [
        chart('gastro-tipo', 'pie', 'Locales gastronómicos por tipo', 'los-137-locales-gastronomicos', [
            {'id': 'Restaurante', 'label': 'Restaurante', 'value': 84},
            {'id': 'Cafetería', 'label': 'Cafetería', 'value': 17},
            {'id': 'Heladería', 'label': 'Heladería', 'value': 10},
            {'id': 'Casa de té', 'label': 'Casa de té', 'value': 5},
            {'id': 'Pizzería', 'label': 'Pizzería', 'value': 4},
            {'id': 'Otros', 'label': 'Otros', 'value': 17},
        ]),
        chart('gastro-distrito', 'bar', 'Locales gastronómicos por distrito', 'los-137-locales-gastronomicos', [
            {'distrito': 'Chacras de Coria', 'locales': 43},
            {'distrito': 'Ciudad', 'locales': 28},
            {'distrito': 'Potrerillos', 'locales': 23},
            {'distrito': 'Cacheuta', 'locales': 11},
            {'distrito': 'Las Compuertas', 'locales': 8},
            {'distrito': 'Agrelo', 'locales': 8},
            {'distrito': 'Vistalba', 'locales': 5},
            {'distrito': 'La Puntilla', 'locales': 4},
        ], {'xAxis': 'distrito', 'layout': 'horizontal'}),
        chart('alojamiento-distrito', 'pie', 'Alojamientos por distrito', 'la-oferta-de-pernocte-potrerillos-como-capital', [
            {'id': 'Potrerillos', 'label': 'Potrerillos', 'value': 53},
            {'id': 'Cacheuta', 'label': 'Cacheuta', 'value': 7},
            {'id': 'Las Compuertas', 'label': 'Las Compuertas', 'value': 7},
            {'id': 'Otros', 'label': 'Otros', 'value': 6},
        ]),
    ]
)

# 8. DESARROLLO HUMANO
build_data['desarrollo-humano'] = build(
    'desarrollo-humano', 'Desarrollo Humano',
    [
        kpi('barrios-pop', 'Barrios populares (RENABAP)', 47, '47'),
        kpi('familias', 'Familias en barrios populares', 2569, '2.569'),
        kpi('genero-casos', 'Casos atendidos Género 2022', 480, '480 casos'),
        kpi('barrio-mayor', 'Barrio popular más grande', 290, '290 fam.', 'Valle Encantado, Chacras'),
    ],
    [
        chart('top-barrios', 'bar', 'Top barrios populares por familias residentes', 'la-pobreza-con-direccion-y-nombre', [
            {'barrio': 'Valle Encantado', 'familias': 290},
            {'barrio': 'Tierras Vivas', 'familias': 170},
            {'barrio': 'Patrono Santiago', 'familias': 160},
            {'barrio': 'Virgen de Lourdes', 'familias': 135},
            {'barrio': 'Costanera Sur', 'familias': 132},
            {'barrio': 'Juan XXIII', 'familias': 110},
            {'barrio': 'Villa Costa Canal', 'familias': 102},
            {'barrio': 'Estación Cuadro', 'familias': 100},
        ], {'xAxis': 'barrio', 'layout': 'horizontal'}),
        chart('genero-tipos', 'bar', 'Tipos de violencia reportada (Género 2022, % casos)', 'violencia-de-genero-la-contracara-mas-sensible', [
            {'tipo': 'Psicológica', 'porcentaje': 83},
            {'tipo': 'Física', 'porcentaje': 64},
            {'tipo': 'Económica/Patrimonial', 'porcentaje': 59},
            {'tipo': 'Sexual', 'porcentaje': 22},
        ], {'xAxis': 'tipo'}),
    ]
)

# 9. MOVILIDAD
build_data['movilidad'] = build(
    'movilidad', 'Movilidad',
    [
        kpi('obras', 'Obras del Plan 2025', 42, '42', '174 actividades en total'),
        kpi('cumplido', 'Actividades cumplidas', 67, '39%', 'sobre 174 actividades'),
        kpi('inv-vial', 'Inversión vial 2024 (top 5 contratos)', 1772700000, '$1,77 mil M'),
        kpi('plan-pavi', 'Plan Pavimentación 2024', 635000000, '$635 M', 'VIALMANI'),
    ],
    [
        chart('obras-estado', 'pie', 'Estado del Plan de Obras 2025', 'el-plan-de-obras-2025-174-actividades', [
            {'id': 'Cumplido', 'label': 'Cumplido', 'value': 67},
            {'id': 'No iniciado', 'label': 'No iniciado', 'value': 40},
            {'id': 'En implementación', 'label': 'En implementación', 'value': 34},
            {'id': 'Atrasado', 'label': 'Atrasado', 'value': 18},
            {'id': 'Cancelado', 'label': 'Cancelado', 'value': 11},
        ]),
        chart('obras-eje', 'bar', 'Actividades por eje estratégico', 'el-plan-de-obras-2025-174-actividades', [
            {'eje': 'Transformación espacio público', 'actividades': 165},
            {'eje': 'Luján Sustentable', 'actividades': 9},
        ], {'xAxis': 'eje'}),
        chart('inversion-vial', 'bar', 'Top 5 contratos viales 2024 (M $)', 'las-inversiones-viales-detras-de-las-obras', [
            {'contrato': 'Pavimentación', 'monto': 635},
            {'contrato': 'Poda', 'monto': 450},
            {'contrato': 'Redes Agua', 'monto': 238},
            {'contrato': 'Vehículos util.', 'monto': 231},
            {'contrato': 'Camiones regad.', 'monto': 219},
        ], {'xAxis': 'contrato'}),
    ]
)

# 10. ELECCIONES (Escrutinio Definitivo Concejales 2023 — dataset #59)
build_data['elecciones'] = build(
    'elecciones', 'Elecciones',
    [
        kpi('mesas', 'Mesas escrutadas (Concejal)', 334, '334'),
        kpi('votos-pos', 'Votos positivos (Concejal)', 69868, '69.868'),
        kpi('lu', 'La Unión Mendocina', 32166, '46,0%'),
        kpi('cm', 'Cambia Mendoza', 22644, '32,4%'),
    ],
    [
        chart('concejal-2023-pie', 'pie', 'Concejales 2023 — escrutinio definitivo (votos)', 'el-mapa-politico-paridad-y-dos-polos', [
            {'id': 'La Unión Mendocina', 'label': 'La Unión Mendocina', 'value': 32166},
            {'id': 'Cambia Mendoza', 'label': 'Cambia Mendoza', 'value': 22644},
            {'id': 'Elegí Mendoza', 'label': 'Elegí Mendoza', 'value': 6694},
            {'id': 'Partido Verde', 'label': 'Partido Verde', 'value': 5837},
            {'id': 'FIT', 'label': 'FIT', 'value': 2527},
        ]),
        chart('resumen-votos', 'bar', 'Resumen de votos — Concejales 2023', 'la-geografia-del-voto-dos-lujanes', [
            {'tipo': 'Positivos', 'votos': 69868},
            {'tipo': 'En blanco', 'votos': 9925},
            {'tipo': 'Nulos', 'votos': 2443},
        ], {'xAxis': 'tipo'}),
    ]
)

# 11. GENERO
build_data['genero'] = build(
    'genero', 'Género y Diversidad',
    [
        kpi('casos', 'Casos atendidos en Luján 2022', 480, '480'),
        kpi('pareja-ex', 'Riesgo desde pareja/ex', 90, '90%', 'de los casos'),
        kpi('desocupada', 'Víctimas desocupadas', 38, '38%'),
        kpi('dimensiones', 'Dimensiones por ficha RUC', 87, '87'),
    ],
    [
        chart('vinculo', 'pie', 'Vínculo con el agresor (cat. Concejal 2022)', 'vinculo-con-el-agresor', [
            {'id': 'Ex pareja conviviente', 'label': 'Ex pareja conviv.', 'value': 275},
            {'id': 'Cónyuge', 'label': 'Cónyuge', 'value': 75},
            {'id': 'Ex cónyuge', 'label': 'Ex cónyuge', 'value': 58},
            {'id': 'Ex novio/no conv.', 'label': 'Ex novio/no conv.', 'value': 33},
            {'id': 'Otros', 'label': 'Otros', 'value': 52},
        ]),
        chart('estado-civil', 'bar', 'Estado civil de las víctimas', 'estado-civil', [
            {'estado': 'Soltera', 'casos': 318},
            {'estado': 'Casada', 'casos': 99},
            {'estado': 'Divorciada', 'casos': 41},
            {'estado': 'Separada', 'casos': 14},
        ], {'xAxis': 'estado'}),
        chart('niv-educ', 'bar', 'Nivel educativo de las víctimas', 'nivel-educativo', [
            {'nivel': 'Sec. incompleta', 'casos': 178},
            {'nivel': 'Sec. completa', 'casos': 99},
            {'nivel': 'Terc./Univ. completo', 'casos': 62},
            {'nivel': 'Primaria completa', 'casos': 55},
            {'nivel': 'Primaria incompleta', 'casos': 25},
            {'nivel': 'Sin educación', 'casos': 23},
        ], {'xAxis': 'nivel', 'layout': 'horizontal'}),
        chart('tipo-violencia', 'bar', 'Tipos de violencia reportada (% casos)', 'los-tipos-de-violencia-ejercida', [
            {'tipo': 'Psicológica', 'porcentaje': 83},
            {'tipo': 'Física', 'porcentaje': 64},
            {'tipo': 'Económica/Patrim.', 'porcentaje': 59},
            {'tipo': 'Sexual', 'porcentaje': 22},
        ], {'xAxis': 'tipo'}),
    ]
)

# 12. GESTION DE DATOS
build_data['gestion_de_datos'] = build(
    'gestion_de_datos', 'Gestión de Datos',
    [
        kpi('decreto-ia', 'Decretos sobre IA', 1, 'Dec. 3041'),
        kpi('protocolo', 'Protocolo Ético IA', 1, '1 vigente'),
        kpi('inventario', 'Inventario de Datos', 1, '1 catálogo'),
        kpi('dimensiones', 'Dimensiones gobernanza IA', 3, '3', 'Inst./Regl./Datos pers.'),
    ],
    [
        chart('gobernanza-ia', 'bar', 'Productos del marco de gobernanza IA', 'el-marco-normativo-de-la-ia-municipal', [
            {'producto': 'Decreto 3041', 'value': 1},
            {'producto': 'Estrategia de Datos', 'value': 1},
            {'producto': 'Protocolo Ético IA', 'value': 1},
            {'producto': 'Programas IA', 'value': 1},
            {'producto': 'Innovación y Desarrollo', 'value': 1},
            {'producto': 'Tabla Gobernanza', 'value': 1},
        ], {'xAxis': 'producto', 'layout': 'horizontal'}),
    ]
)

# 13. SEGURIDAD
build_data['seguridad'] = build(
    'seguridad', 'Seguridad',
    [
        kpi('comisarias', 'Comisarías', 6, '6', '+ 1 complejo penitenciario'),
        kpi('bancos', 'Bancos (puntos críticos)', 9, '9 sucursales'),
        kpi('estaciones', 'Estaciones de servicio', 11, '11', 'sobre RN 7 / RP 15 / Acceso Sur'),
        kpi('barrios-pop', 'Barrios populares', 47, '47', '2.569 familias'),
    ],
    [
        chart('infraestructura', 'bar', 'Puntos críticos georreferenciados', 'los-puntos-de-criticidad-economica', [
            {'tipo': 'Escuelas', 'cantidad': 112},
            {'tipo': 'Comercios identif.', 'cantidad': 3501},
            {'tipo': 'Centros de salud', 'cantidad': 19},
            {'tipo': 'Farmacias', 'cantidad': 18},
            {'tipo': 'Estaciones servicio', 'cantidad': 11},
            {'tipo': 'Bancos', 'cantidad': 9},
        ], {'xAxis': 'tipo', 'layout': 'horizontal'}),
    ]
)

# 14. COVID
build_data['covid-19'] = build(
    'covid-19', 'COVID-19',
    [
        kpi('semanas', 'Semanas registradas', 84, '84'),
        kpi('positivos', 'Casos positivos acumulados', 645, '645'),
        kpi('fallecidos', 'Fallecidos', 21, '21'),
        kpi('pico', 'Pico semanal', 128, '128 casos'),
    ],
    [
        chart('curva-resumen', 'bar', 'Resumen pandémico — administración municipal', 'la-curva-pandemica-resumida', [
            {'indicador': 'Positivos acum.', 'valor': 645},
            {'indicador': 'Recuperados', 'valor': 20424},
            {'indicador': 'Fallecidos', 'valor': 21},
            {'indicador': 'Pico semanal', 'valor': 128},
        ], {'xAxis': 'indicador'}),
    ]
)

# Escribir todos
for slug, data in build_data.items():
    fp = OUT / f"{slug}.json"
    fp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"  written: {slug}.json (kpis: {len(data['kpis'])}, charts: {len(data['charts'])}, rankings: {len(data['rankings'])})")

print(f"\nTotal: {len(build_data)} JSONs de informe")
