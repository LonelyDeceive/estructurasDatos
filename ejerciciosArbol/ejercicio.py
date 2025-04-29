import pandas as pd

class Hospital:
    def __init__(self, nombre: str, nit: int, sede: str, municipio: str):
        self.nombre = nombre
        self.nit = nit
        self.sede = sede
        self.municipio = municipio
    
    def __str__(self):
        return f"NIT: {self.nit}, Nombre: {self.nombre}, Sede: {self.sede}, Municipio: {self.municipio}"
    
    def found(self):
        return f" Hospital: {self.nombre}\n Sede: {self.sede}\n Municipio: {self.municipio}"

class Nodo:
    def __init__(self, hospital):
        self.hospital = hospital
        self.valor = hospital
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor, nodo):
        if valor.nit < nodo.valor.nit:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(valor, nodo.der)

    def buscar(self, valor):
        if self.raiz is None:
            return "Hospital no encontrado"
        else:
            return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        if valor == nodo.valor.nit:
            return Hospital.found(nodo.valor)
        elif valor < nodo.valor.nit and nodo.izq is not None:
            return self._buscar(valor, nodo.izq)
        elif valor > nodo.valor.nit and nodo.der is not None:
            return self._buscar(valor, nodo.der)
        return "Hospital no encontrado"
    
    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo.izq is not None:
            self._inorden(nodo.izq)
        print(nodo.valor)
        if nodo.der is not None:
            self._inorden(nodo.der)

hospitales = pd.read_csv('/workspaces/estructurasDatos/excel/hospitales.csv')
hospitales.rename(columns={
    'Razón Social Organización': 'nombre',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'
}, inplace=True)
hospitales['nit'] = hospitales['nit'].str.replace(",","")
hospitales['nit'] = hospitales['nit'].astype(int)
print(hospitales['nit'])
arbol = ArbolBinario()
for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    arbol.insertar(hospital)
arbol.inorden()
print(arbol.buscar(891982128))