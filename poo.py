class Vehiculo:
    color:str
    marca:str
    modelo:int
    cilindraje:int
    numeroRuedas:int
    combustible:int
    tipo:str

    def __init__(self, marca:str, combustible:int)-> None:
        self.marca = marca
        self.combustible = combustible

    def __str__(self):
        return f"La marca del vehiculo es {self.marca} y combustible es {self.combustible}"
    
    def encender(self):
        pass

    def acelerar(self):
        pass
    
class Moto(Vehiculo):
    def encender(combustible):
        print("El combustible de la Moto =", combustible)
        if combustible < 10:
            print("Combustible bajo, ir a la gasolinera")
    def __init__(self, tipo:str, marca:str, combustible:int)-> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
    def __str__(self):
        return f"La marca de la {self.tipo} es {self.marca} y combustible es {self.combustible}"
    def marcha(combustible):
        dist = 0
        while combustible > 0:
            print("Distancia = ", dist,"m",sep="")
            print("El combustible es ", combustible)
            dist = dist + 5
            combustible = combustible - 5
            if combustible < 10:
                print("BAJO COMBUSTIBLE")
            if combustible == 0:
                print("El combustible es ", combustible)
                print("Sin combustible")
                print("Distancia = ", dist,"m",sep="")
    
class Carro(Vehiculo):
    def __init__(self, tipo:str, marca:str, combustible:int)-> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
    def __str__(self):
        return f"La marca del {self.tipo} es {self.marca} y combustible es {self.combustible}"
    def encender(combustible):
        print("El combustible del Carro =", combustible)
        if combustible < 10:
            print("Combustible bajo, ir a la gasolinera")
    def marcha(combustible):
        dist = 0
        while combustible > 0:
            print("Distancia = ", dist,"m",sep="")
            print("El combustible es ", combustible)
            dist = dist + 5
            combustible = combustible - 5
            if combustible < 10:
                print("BAJO COMBUSTIBLE")
            if combustible == 0:
                print("El combustible es ", combustible)
                print("Sin combustible")
                print("Distancia = ", dist,"m",sep="")
        
res = Vehiculo("Mazda", 80)
print(res)

moto = Moto("Moto","Honda",5)
print(moto)

carro = Carro("Carro","Chevrolet",5)
print(carro)

a = input("Deseas encender los vehiculos? ")
if a == "y":
    Moto.encender(5)
    Carro.encender(5)
    b = input("Poner en marcha la moto? ")
    if b == "y":
        print("Moto")
        Moto.marcha(5)
        e = input("Poner en marcha el carro? ")
        if e == "y":  
            print("Carro")
            Carro.marcha(5) 
    else:
        e = input("Poner en marcha el carro? ")
        if e == "y":  
            print("Carro")
            Carro.marcha(5)


