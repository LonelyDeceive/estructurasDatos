class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeTy:     
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def isEmptyt(self):
        return self.head is None
    addTy = True
    def addNode(self, dato):
        node = Node(dato)

        if self.isEmpty():
            self.head = node
        else:
            actualNode = self.head
            if actualNode.data == node.data:
                    print("Ya has ingresado este dato |",actualNode.data,"| para Nombre")
                    self.addTy = False
                    return None
            while actualNode.next is not None:
                actualNode = actualNode.next
                if actualNode.data == node.data:
                    print("Ya has ingresado este dato |",actualNode.data,"| para Nombre")
                    self.addTy = False
                    return None
            actualNode.next = node

    def addNodet(self, dato):
        nodet = NodeTy(dato)
        if self.isEmptyt():
            self.head = nodet
        else:
            if self.addTy == True:
                actualNode = self.head
                while actualNode.next is not None:
                    actualNode = actualNode.next
                actualNode.next = nodet
        self.addTy = True


    def delete(self, dato):
        actualNode = self.head
        if actualNode.data == dato:
            self.head = actualNode.next
            return
        while actualNode.next is not None:
            if actualNode.next.data == dato:
                actualNode.next = actualNode.next.next
                return
            actualNode = actualNode.next
    
    def print(self):
        actualNode = self.head
        z = 0
        c = 1
        while actualNode is not None:
            if z == 2:
                print("\n")
                z = 0
            else:
                if z == 0:
                    print(c,")","Animal: ",end=" ",sep="")
                elif z == 1:
                    print("Del tipo:",end=" ")
                print(actualNode.data,end=" ")
                actualNode = actualNode.next
                z = z + 1
                c = c + 1
        print("\n")
    n = 0
    def printR(self,actualNode,c,n):
        actualNode = self.head
        if n == c:
            print("")
            return
        if actualNode is not None:
            print(actualNode.data)
        actualNode = actualNode.next
        return ListaEnlazada.printR("",actualNode,c,n)


class Animal:
    nombre:str
    edad:int
    tipo:str
    def menu():
        c = 0
        lista = ListaEnlazada()
        print("Control de animales Zoologico UCC")
        print("1) Agregar animales")
        print("2) Mostrar animales") 
        print("3) Cerrar")
        a = int(input("Seleccione una opcion > "))
        while a != 3:
            if a == 1:
                an = input("Ingrese nombre del animal: ")
                ty = input("Ingrese tipo de animal: ")
                lista.addNode(an)
                lista.addNodet(ty)
                c = c + 2
                a = int(input("Seleccione una opcion > "))
            if a == 2:
                print("(Mostrar lista:)")
                print("1) Metodo iterativo")
                print("2) Metodo Recursivo")
                con = int(input("/"))
                if con == 1: 
                    lista.print()
                    a = int(input("Seleccione una opcion > "))
                if con == 2:
                    lista.printR(actualNode="",c=c,n="")
Animal.menu()

