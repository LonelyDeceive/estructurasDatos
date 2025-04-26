import pandas as pd

class Hospital:
    def __init__(self, nombre: str, nit: int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio
    
    def __str__(self):
        return f"Nombre: {self.nombre}, NIT: {self.nit}, Sede: {self.sede}, Municipio: {self.municipio}"

class Nodo:
    def __init__(self, hospital):
        self.hospital = hospital
        self.left = None
        self.right = None
    

hospitales = pd.read_csv('/workspaces/estructurasDatos/excel/hospitales.csv')
hospitales.rename(columns={
    'Razón Social Organización': 'nombre',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'
}, inplace=True)
hospitales['nit'] = hospitales['nit'].str.replace(",","")
hospitales['nit'] = hospitales['nit'].astype(int)
print(hospitales.dtypes)
print(hospitales['nit'])
print(hospitales.columns)

for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    print(hospital)