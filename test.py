numeros = list()
numero = int(input("Numero>"))
def agregar (numero:int):

    def menu():
        print("Agregar/1")
        print("Eliminar/2")
        print("Salir/3")

    def add(numero:int)-> None:
        numeros.append(numero)
        print(numeros)

    def delete()-> None:
        numeros.pop()
        print(numeros)

    menu()
    numeros.append(numero)
    c = int(input(">"))
    while c != 3:
        if c == 1:
            numero = int(input("Numero>"))
            add(numero)
            d = input("Continuar?:")
            if d == "y":
                numero = int(input("Numero>"))
                add(numero)
                d = input("Continuar?:")
            if d == "n": 
                print("---------------")
                menu()
                print("---------------")
                c = int(input("Valor>"))
        elif c == 2:
            delete()
            print("---------------")
            menu()
            print("---------------")
            c = int(input("Valor>"))           
    return numeros
print(agregar(numero))