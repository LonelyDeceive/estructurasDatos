from recurso import Recurso

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

    def queue(self, proceso):
        self.cola.append(proceso)

    def dequeue(self):
        if not self.empty():
            return self.cola.pop(0)
        return None

    def empty(self):
        return len(self.cola) == 0

    def listall(self):
        for proceso in self.cola:
            print(proceso)



