class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None

class Stack:
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)
    
    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp
    
    def pop(self):
        if self.head is None:
            print(": La pila ya esta vacia")
        else:
            temp = self.head.getData()
            self.head = self.head.getNext()
            return temp

    
    def peek(self):
        if self.head is None:
            print("La pila esta vacia")
        else:
            print(self.head.getData())

pila = Stack()
print("1) Push")
print("2) Pop")
print("3) Peek")
print("4) Salir")
a = int(input("> "))
while a != 4:
    if a == 1:
        print("Uso de Push")
        b = input("Ingrese el dato: ")
        pila.push(b)
        a = int(input("> "))
    if a == 2:
        print("Uso de Pop")
        pila.pop()
        a = int(input("> "))
    if a == 3: 
        print("Uso de peek")
        print(":",end=" ")
        pila.peek()
        a = int(input("> "))
