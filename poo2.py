class Persona:

    nombre:str
    edad:int
    genero:str

    def __init__(self, nombre):
        self.nombre = nombre

    def resinf(nombre,edad,genero):
        print("\nInfo")
        print("----------")
        print(nombre)
        print(edad)
        print(genero)
        print("----------")
    
    def presentarse():
        print("Esta persona pertenece a la comunidad de la UCC, Ingenieria de Software")

    def inf(nombre:str, edad:int, genero:str):
        print("Su informacion personal")
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")
        genero = input("Ingrese su genero: ")
        Persona.resinf(nombre,edad,genero)
        Persona.presentarse()
    
class CuentaBancaria(Persona):
    saldo:int = 0
    numeroCuenta:int = 9746135802
    print(Persona.nombre)
    
    def cbinf():
        print("Bienvenido al Banco UCC")
        print("¿Que desea hacer?")
        print("1| Depositar")
        print("2| Retirar")
        print("3| Consultar Saldo")

    def cb(titular, saldo, numeroCuenta):
        saldo = CuentaBancaria.saldo
        numeroCuenta = CuentaBancaria.numeroCuenta
        CuentaBancaria.cbinf()
        print("Usuario:")
        print("Numero de cuenta:",numeroCuenta)
        idle = int(input("> "))
        if idle == 1:
            print("Su saldo actual es:$",saldo,sep="")
      

Persona.inf("","","")
CuentaBancaria.cb("","","")