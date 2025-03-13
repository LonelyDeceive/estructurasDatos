class NodeTa:     
    def __init__(self, data):
        self.data = data
        self.next = None


class Task:   
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def addtask(self, dato,dato2,dato3):
        node = NodeTa(dato)
        node2 = NodeTa(dato2)
        node3 = NodeTa(dato3)
        if self.isEmpty():
            self.head = node2
            actualNode = self.head
            actualNode.next = node
            actualNode.next.next = node3
        else:
            actualNode = self.head
            while actualNode.next is not None:
                actualNode = actualNode.next
            actualNode.next = node2
            actualNode.next.next = node
            actualNode.next.next.next = node3

    newdato = ""
    pridata = ""
    def delete(self, dato):
        actualNode = self.head
        if actualNode.data == dato:
            self.head = actualNode.next
            return
        while actualNode.next is not None:
            if actualNode.next.data == dato:
                self.pridata = actualNode.data
                actualNode.next = actualNode.next.next
                self.newdato = actualNode.next.data
                return
            actualNode = actualNode.next

    def delete2(self, dato2):
        dato2 = self.newdato
        actualNode = self.head
        if actualNode.data == dato2:
            self.head = actualNode.next
            return
        while actualNode.next is not None:
            if actualNode.next.data == dato2:
                actualNode.next = actualNode.next.next
                return
            actualNode = actualNode.next

    def delete3(self, dato3):
        dato3 = self.pridata
        actualNode = self.head
        if actualNode.data == dato3:
            self.head = actualNode.next
            return
        while actualNode.next is not None:
            if actualNode.next.data == dato3:
                actualNode.next = actualNode.next.next
                return
            actualNode = actualNode.next

    def print(self):
        z = 0
        actualNode = self.head
        print("Prioridad 1")
        if actualNode == None:
            print("No hay tareas prioridad 1\n")
        else:
            while actualNode is not None:
                if actualNode == None:
                    print("No hay tareas prioridad 1\n")
                else:
                    if actualNode.data == 1:
                        print("Tarea:",actualNode.next.data)
                        print("Tiempo:",actualNode.next.next.data)
                        z = z + 1
                actualNode = actualNode.next
            if z == 0:
                print("No hay tareas prioridad 1\n")
            else:
                print("")

    def print2(self):
        z = 0
        actualNode = self.head
        print("Prioridad 2")
        if actualNode == None:
            print("No hay tareas prioridad 2\n")
        else:
            while actualNode is not None:
                if actualNode == None:
                    print("No hay tareas prioridad 2\n")
                else:
                    if actualNode.data == 2:
                        print("Tarea:",actualNode.next.data)
                        print("Tiempo:",actualNode.next.next.data)
                        z = z + 1
                actualNode = actualNode.next
            if z == 0:
                print("No hay tareas prioridad 2\n")
            else:
                print("")

    def print3(self):
        z = 0
        actualNode = self.head
        print("Prioridad 3")
        if actualNode == None:
            print("No hay tareas prioridad 3\n")
        else:
            while actualNode is not None:
                if actualNode == None:
                    print("No hay tareas prioridad 3\n")
                else:
                    if actualNode.data == 3:
                        print("Tarea:",actualNode.next.data)
                        print("Tiempo:",actualNode.next.next.data)
                        z = z + 1
                actualNode = actualNode.next
            if z == 0:
                print("No hay tareas prioridad 3\n")
            else:
                print("")
            
class Menu:

    def taskManager():
        tarea = Task()
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
                tarea.addtask(des,pri,dat)
                a = int(input("Seleccione una opcion> "))
            if a == 2:
                print("Eliminar una tarea")
                b = input("Especifique descripcion: ")
                tarea.delete(b)
                tarea.delete2("")
                tarea.delete3("")
                a = int(input("Seleccione una opcion> "))
            if a == 3:
                tarea.print()
                tarea.print2()
                tarea.print3()
                a = int(input("Seleccione una opcion> "))
                

Menu.taskManager()