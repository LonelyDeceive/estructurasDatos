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
            print("La pila ya esta vacia")
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
pila.peek()
pila.push("1ro") 
pila.peek()
pila.push("2do")
pila.peek()
pila.push("3ro")
pila.peek()
pila.push("4to")
pila.peek()
pila.pop()
pila.peek()
pila.pop()
pila.peek()
pila.pop()
pila.peek()
pila.pop()
pila.peek()
pila.pop()
pila.push("5to")
pila.peek()