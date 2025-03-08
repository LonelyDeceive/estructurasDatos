class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def addNode(self, dato):
        node = Node(dato)
        if self.isEmpty():
            self.head = node
        else:
            actualNode = self.head
            #if actualNode.data == node.data:
                    #print("Same")
                    #return None
            while actualNode.next is not None:
                actualNode = actualNode.next
                if actualNode.data == node.data:
                    print("Same")
                    return None
                actualNode.next = node


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
        while actualNode is not None:
            print(actualNode.data,end=" ")
            actualNode = actualNode.next

lista = ListaEnlazada()
lista.addNode(5)
lista.addNode(10)
lista.addNode(15)
lista.addNode(5)
lista.print()

