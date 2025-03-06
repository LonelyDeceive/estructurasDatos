class Empleado:
    nombre:str
    salario:int
    departamento:str

    def work():
        Manager.supwrk()
        print("Equipo de trabajo:")
        z = 1
        for x, y in equipo.items():
            print(z,")","Empleado: ",x," trabajando el lenguaje " ,y,sep="")
            z = z + 1
        Dev.write()

equipo = dict()
class Manager(Empleado):

    def add(key:str, val:str):
        equipo.update({key:val})
        print(equipo)

    def supwrk():
        teamcan = int(input("Ingrese la cantidad de empleados: "))
        for i in range(1,teamcan+1):
            key = input("Ingrese nombre: ")
            val = input("Ingrese lenguaje de programacion: ")
            Manager.add(key,val)


class Dev(Empleado):

    lenguaje:str

    def write():
        for x, y in equipo.items():
            print(x,"esta escribiendo codigo en Github codespace usando",y)

class Shapes:

    def calAr(b,h,l):
        print("Area triangulo = (b * h) / 2")
        print("(",b," * ",h,") ","/ 2",sep="")
        print("(",b*h,") ","/ 2",sep="")
        print("{:.2f}".format((b*h)/2),"uni^2")
        print("Area cuadrado = L * L = L^2")
        print(l,"*",l)
        print(l*l,"uni^2")

class Tri(Shapes):
    b:int
    h:int
    def dataTri(b,h):
        b = int(input("Ingrese la base del rectangulo: "))
        h = int(input("Ingrese la altura del rectangulo: "))
        Squ.dataSqu(b,h)


class Squ(Shapes):
    l:int
    def dataSqu(b,h):
        l = int(input("Ingrese el valor del lado del cuadrado: "))
        Shapes.calAr(b,h,l)

class Electrodomestico:
    marca:str
    modelo:str
    consumo:int
    def encender(m,mo,c,con,mr,mor,conr,fre):
        Lavadora.cicloLavado(m,mo,c,con,mr,mor,conr,fre)
        Refrigerador.regularTemp(mr,mor,conr,fre)

class Lavadora(Electrodomestico):
    c:int

    def datalava(m,mo,c,con):
        m = input("Ingrese la marca de la lavadora: ")
        mo = input("Ingrese el modelo de la lavadora: ")
        con = int(input("Ingrese el consumo (Watts): "))
        c = int(input("Ingrese la capacidad (litros): "))
        Refrigerador.dataRefri(m,mo,c,con)

    def cicloLavado(m,mo,con,c,mr,mor,conr,fre):
        print("Lavadora:",m,"-",mo)
        print("Consumo:",con,"W")
        print("Capacidad:",c)
        print("Ciclo de lavado, tiempo estimado",c*5,"mins")
        print("(1 litro = 5 mins)\n")



class Refrigerador(Electrodomestico):
    fre:bool

    def dataRefri(m,mo,con,c):
        mr = input("Ingrese la marca del refrigerador: ")
        mor = input("Ingrese el modelo del refrigerador: ")
        conr = int(input("Ingrese el consumo (Watts): "))
        fre = input("El refrigerador tiene congelador? (y/n): ")
        if fre == "y":
            fre = True
        else:
            fre = False
        Electrodomestico.encender(m,mo,c,con,mr,mor,conr,fre)
    
    def regularTemp(mr,mor,conr,fre):
        print("Refrigerador: ",mr,"-",mor)
        print("Consumo:",conr,"W")
        print("Regulando temperatura a 19 grados")
        print("Congelador")
        if fre == True:
            print("Regulando temperatura a -3 grados")
        else:
            print("NO SE DETECTA CONGELADOR")

class Usuario:
    nombreUser:str 
    passw:str

    def signin(keyUs,keyPass,genUs,genPass):   
        print("Ingrese sus credenciales")
        checkUS = input("Usuario: ")
        checkPass = input("Contraseña: ")
        if checkUS == keyUs and checkPass == keyPass:
            Admin.manage(keyUs,genUs,genPass)
        elif checkUS == genUs and checkPass == genPass:
            Users.purchases(genUs)
        else:
            print("Credenciales incorrectas")


class Admin(Usuario):
    keyUs:str
    keyPass:str

    def reg(keyUs,keyPass):
        keyUs = input("Ingrese user de admin: ")
        keyPass = input("Ingrese contraseña admin: ")
        Users.regU(keyUs,keyPass,"","")
    def manage(keyUs,genUs,genPass):
        print("Bienvenido Admin", keyUs)
        print("Tienes acceso con los siguientes usuarios: ")
        print("1)",genUs)
        print("Pass:",genPass)




class Users(Usuario):
    genUs:str
    genPass:str

    def regU(keyUs,keyPass,genUs,genPass):
        genUs = input("Ingrese su user de cliente: ")
        genPass = input("Ingrese su contraseña de cliente: ")
        Usuario.signin(keyUs,keyPass,genUs,genPass)

    def purchases(genUs):
        print("Bienvenido Cliente",genUs)
        print("Tienes acceso a realizar compras")

Empleado.work()  

Tri.dataTri("","")

Lavadora.datalava("","","","")

Admin.reg("","")



