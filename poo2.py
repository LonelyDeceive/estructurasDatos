class Persona:
    nombre: str
    edad: int
    genero: str

    def resinf(nombre, edad, genero):
        print("\nInfo")
        print("----------")
        print(nombre)
        print(edad)
        print(genero)
        print("----------")

    def inf(self):
        print("Su informacion personal")
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        genero = input("Ingrese su genero: ")
        self.nombre = nombre
        Persona.resinf(nombre,edad,genero)

class CuentaBancaria(Persona):

    saldo: int = 0
    numeroCuenta: int = 9746135802

    def __init__(self, nombre):
        self.titular = nombre

    saldo:int = 0
    numeroCuenta:int = 9746135802

    def cbinf():
        print("Bienvenido al Banco UCC")
        print("¿Que desea hacer?")
        print("1| Consultar Saldo")
        print("2| Depositar")
        print("3| Retirar")
        print("4| Continuar...")


    def cb(self,numeroCuenta, saldo):
        saldo = CuentaBancaria.saldo
        numeroCuenta = CuentaBancaria.numeroCuenta
        print("Usuario:", self.titular.nombre)
        print("Numero de cuenta:", numeroCuenta)
        CuentaBancaria.cbinf()
        idle = int(input("> "))
        while idle != 4:        
            if idle == 1:
                print("Su saldo actual es: $", saldo, sep="")
            if idle == 2:
                dep = int(input("Cuanto desea Depositar?> "))
                saldo = saldo + dep
                print("Depositado: $", dep, sep="")
            if idle == 3:
                ret = int(input("Cuanto desea Retirar?> "))
                if ret > saldo:
                    print("FONDOS INSUFICIENTES")
                    print("Su saldo actual es: $", saldo, sep="")
                else:
                    print("----------------------")
                    print("Usted retiro: $", ret, sep="")
                    print("De su Saldo de: $",saldo,sep="")
                    saldo = saldo - ret
                    print("Su saldo actual es: $", saldo, sep="")
                    print("----------------------")
            print("Selecciona otra opcion")
            idle = int(input("> "))    
            
class Rectangulo():

    b:int
    h:int

    def basHi(b:int, h:int):
        b = int(input("Ingrese la base del rectangulo: "))
        h = int(input("Ingrese la altura del rectangulo: "))
        Rectangulo.calAr(b,h)
        print("-----------")
        Rectangulo.calPer(b,h)
    def calAr(b:int, h:int):
        res = b*h
        print("Calculo de area")
        print("Area rectangulo = bh")
        print("Area =",b,"*",h)
        print("Area =",res,"cm²")

    def calPer(b:int, h:int):
        res1 = 2*b
        res2 = 2*h
        rest = res1+res2
        print("Calculo de perimetro")
        print("Perimetro = b + b + h + h = 2b + 2h")
        print("Perimetro =",b,"+",b,"+",h,"+",h,"=",res1,"+",res2)
        print("Perimetro =",rest,"cm")

class Circulo():

    r:int
    
    def pirad(r:int):
        r = int(input("Ingrese el radio del circulo: "))
        Circulo.calArC(r)
        print("-----------")
        Circulo.calPerC(r)

    def calArC(r:int):
        res = 3.14*(r*r)
        pre = r*r
        print("Calculo de area")
        print("Area Circulo = πr²")
        print("π ≈ 3.14")
        print("Area =",3.14,"*",r,"²")
        print("Area =",3.14,"*",pre)        
        print("Area =",res,"cm²")

    def calPerC(r:int):
        rest = 2*3.14*r
        print("Calculo de la circunferencia")
        print("Circunferencia = 2πr")
        print("π ≈ 3.14")
        print("Circunferencia =","2","*","π","*",r)
        print("Circunferencia =",end=" ")
        print("{0:.2f}".format(rest),"cm")

class Libro:

    titulo:str
    autor:str
    genero:str
    año:int

    def resinfl(titulo, autor, genero, año):
        print("\nDetalles")
        print("-----------------")
        print("Titulo:",titulo)
        print("Autor(a):",autor)
        print("Genero:",genero)
        print("Año de publicacion:",año)
        print("-----------------")

    def infl():
        print("Su informacion libro")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor o autora: ")
        genero = input("Ingrese el genero: ")
        año = int(input("Ingrese el año de publicacion: "))
        Libro.resinfl(titulo,autor,genero,año)

class Cancion:
    titulo:str
    artista:str
    album:str
    duracion:int

    def resinfC(titulo, artista, album, duracion):
        duracion = float(duracion/60)
        duracion2 = int(duracion)
        re = duracion - duracion2
        res = 60*re
        print("\nReproduciendo ahora")
        print("-----------------")
        print(titulo)
        print(artista,"-",album)
        print("0:00"," ------------ ",duracion2,":","{:02.0f}".format(res),sep="")
        print("-----------------")

    def inflC():
        print("Su informacion cancion")
        titulo = input("Ingrese el titulo de la cancion: ")
        artista = input("Ingrese el artista: ")
        album = input("Ingrese el album de la cancion: ")
        duracion = int(input("Ingrese la duracion (segundos): "))
        Cancion.resinfC(titulo,artista,album,duracion)

class Producto:
    nombre:str
    precio:int
    cantidad:int
    def calCan(nombre,precio,cantidad):
        buycan = int(input("Cuantos de este producto desea comprar?: "))
        prican = buycan * precio
        exc = cantidad - buycan
        print("\nSu recibo")
        print("-----------------")
        print("Nombre del producto:",nombre)
        print("Precio: $",precio,sep="")
        print("Cantidad en Inventario:", cantidad)
        print("Cantidad ingresada:", buycan,end=" ")
        print("Exceso:", exc)
        print("Precio total: $", prican,sep="")
        print("-----------------")
    
    def resinfl(nombre,precio,cantidad):
        print("\nInventario")
        print("-----------------")
        print("Nombre del producto:",nombre)
        print("Precio: $",precio,sep="")
        print("Cantidad:",cantidad)
        print("-----------------")
        Producto.calCan(nombre,precio,cantidad)

    def infl():
        print("Su informacion Inventario")
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        Producto.resinfl(nombre,precio,cantidad)

class Estudiante:

    nombre:str
    edad:int
    curso:str

    def average(grades,gradescan):
        total = 0
        for i in range(0,gradescan+1):
            t = grades[i]
            total = total + t
        print(total)
        
    def addgrades():
        grades = []
        gradescan = int(input("Ingrese la cantidad de calificaciones: "))
        for i in range(1,gradescan+1):
            t = int(input("Ingrese calificacion: "))
            grades.append(t)
            print(grades)
        Estudiante.average(grades,gradescan)

    def inflE():
        print("Su informacion Estudiante")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad "))
        curso = input("Ingrese el curso ")
        Estudiante.addgrades()



#persona = Persona()
#persona.inf()
#cuenta = CuentaBancaria(persona)
#cuenta.cb("","")

#Rectangulo.basHi("","")
#Circulo.pirad("")

#Libro.infl()

#Cancion.inflC()

#Producto.infl()

#Estudiante.inflE()

