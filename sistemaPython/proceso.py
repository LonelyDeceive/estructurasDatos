class Proceso:
    def __init__(self, id_proceso, nombre, prioridad, estado="Listo"):
        self.id = id_proceso
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = estado
        
    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Prioridad: {self.prioridad} | Estado: {self.estado}"

class ColaProcesos:
    def __init__(self):
        self.cola = []

    def queue(self, proceso, recurso):
        self.cola.append(proceso)
        self.cola.append(recurso)

    def dequeue(self):
        if not self.empty():
            return self.cola.pop(0)
        return None

    def empty(self):
        return len(self.cola) == 0

    def listall(self):
        for proceso in self.cola:
            print(proceso)
    
    def pidDequeue(self, pid):
        z = 0
        for proceso in self.cola:
            if proceso.id == pid:
                proceso.estado = "Terminado"
                print(f"Se ha encontrado el proceso {proceso}")
                self.cola.pop(z)
                recurso = self.cola.pop(z)
                print(f"Se han encontrado los recursos {recurso}")
                return recurso
            z += 1
        else:
            print("No se ha encontrado la tarea")
            return None
