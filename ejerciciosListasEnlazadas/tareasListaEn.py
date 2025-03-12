class NodeTa:     
    def __init__(self, data):
        self.data = data
        self.next = None


class Task:   

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def taskManager():
        print("Bienvenido al gestor de tareas")
        print("1) Agregar Tareas")
        print("2) Eliminar Tareas") 
        print("3) Mostrar Tareas")
        print("4) Buscar Tarea")
        print("5) Completar Tareas")
        print("6) Cerrar")
        a = int(input("Seleccione una opcion> "))
        while a != 6:
            if a == 1:
                print("Agregar Tareas")
                des = input("Ingrese la descripcion de la tarea: ")
                pri = int(input("Ingrese la prioridad (1: Alta, 2: Media, 3: Baja): "))
                dat = int(input("Ingrese fecha de vencimiento (horas): "))
                Task.addtask("",des,pri,dat)

    def addtask(self, dato,dato2,dato3):
        node = NodeTa(dato)
        node2 = NodeTa(dato2)
        node3 = NodeTa(dato3)
        if self.isEmpty():
            self.head = node
        else:
            actualNode = self.head
            while actualNode.next is not None:
                actualNode = actualNode.next
            actualNode.next = node
            actualNode.next = node2
            actualNode.next = node3

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

Task.taskManager()