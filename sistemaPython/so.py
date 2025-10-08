from proceso import *

class SistemaOperativo:
    
    def __init__(self):
        self.cola = ColaProcesos()
        self.contadorid = 1

    def addProcess(self, nombre, prioridad):
        proceso = Proceso(self.contadorid, nombre, prioridad)
        self.cola.queue(proceso)
        self.contadorid += 1
        print(f"Proceso '{nombre}' creado y agregado a la cola.")

    def endProcess(self):
        proceso = self.cola.dequeue()
        if proceso:
            proceso.estado = "Terminado"
            print(f"Proceso {proceso.nombre} terminado.")
        else:
            print("No hay procesos en la cola.")

    def tsklist(self):
        if self.cola.empty():
            print("No hay procesos en la cola.")
        else:
            print("\n--- Lista de procesos ---")
            self.cola.listall()
            
    def plan(self):
        if self.cola.empty():
            print("No hay procesos para planificar.")
        else:
            proceso = sorted(self.cola.cola, key=lambda p: p.prioridad, reverse=False)[0]
            print(f"Proceso seleccionado para ejecución: {proceso}")

so = SistemaOperativo()
so.addProcess("Google Chrome", 2)
so.addProcess("Visual Studio Code", 1)
so.addProcess("Microsoft Word", 2)
so.endProcess()
so.tsklist()
so.plan()

