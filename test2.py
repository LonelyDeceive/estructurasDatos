words = dict()
key = input("Clave: ")
val = input("Valor: ")
def agregar (key:str,val:str):
    
    def menu():
        print("Agregar/1")
        print("Eliminar/2")
        print("Salir/3")

    def add(key:str,val:str)-> None:
        words.update({key:val})
        print(words)

    def delete()-> None:
        words.popitem()
        print(words)

    words.update({key:val})
    print(words)
    menu()
    c = int(input(">"))
    while c != 3:
        if c == 1:
            key = input("Clave: ")
            val = input("Valor: ")
            add(key,val)
            d = input("Continuar?:")
            if d == "y":
                key = input("Clave: ")
                val = input("Valor: ")
                add(key,val)
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
    return words
print(agregar(key,val))