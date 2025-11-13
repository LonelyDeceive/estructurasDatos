from proceso import *
from recurso import *
class SistemaOperativo:

    def __init__(self):
        self.cola = ColaProcesos()
        self.recdis = RecursosDisponibles()
        self.contadorid = 1

    def updateRe(self):
        self.ARam = self.recdis.ram
        self.AVRam = self.recdis.vram
        self.ADisco = self.recdis.disco
        self.ACPU = self.recdis.cpu
        print(f"Recursos Disponibles \nRAM: {self.ARam} GB | Disco: {self.ADisco} GB | CPU: {self.ACPU} % | [VRam: {self.AVRam} GB]")
    
    def addProcess(self, nombre, prioridad, ram, disco, cpu):
        if prioridad <= 0 or prioridad > 3: 
            print("La prioridad debe ser entre 1 y 3")
            return None
        proceso = Proceso(self.contadorid, nombre, prioridad)
        recurso = Recurso(self.contadorid, ram, disco, cpu, vram=0)
        if float(self.ARam) - ram <= 0:
            VRPram = self.recdis.usedVRam(ram) 
            usedRam = ram - float(VRPram)
        else:
            usedRam = ram
            VRPram = 0
        if self.recdis.reFree(ram, disco, cpu):
            recurso = Recurso(self.contadorid, usedRam, disco, cpu, VRPram)
            self.cola.queue(proceso, recurso)
            self.contadorid += 1
            print(f"Proceso '{nombre}' creado y agregado a la cola.")

    def endProcess(self, opt):
        if opt == 1:
            proceso = self.cola.dequeue()
            recurso = self.cola.dequeue()
            if proceso:
                proceso.estado = "Terminado"
                print(f"Proceso [{proceso}] encontrado")
                print(f"Recursos [{recurso}] liberados")
                self.recdis.liberar(recurso)
            else:
                print("No hay procesos en la cola.")
        elif opt == 2:
            pid = int(input("Numero PID: "))
            recurso = self.cola.pidDequeue(pid)
            if recurso is not None:
                self.recdis.liberar(recurso)
        else:
            print("Seleccione una opcion valida (1 - 2)")

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
            
    def staMn(self):
        print("Seleccione una opcion \n1: Agregar tareas \n2: Terminar tareas \n3: Listar tareas \n4: Planificar tareas \n5: Salir")
        a = int(input("-> "))
        while a >= 1 or a <= 5:
            if a == 1:
                print("Agregar tareas")
                b = input("Nombre tarea> ")
                c = int(input("Prioridad> "))
                print("Uso de recursos:  ")
                so.updateRe()
                d = float(input("Uso de Ram> "))
                e = float(input("Uso de de Disco> "))
                f = float(input("Uso de CPU> "))
                so.addProcess(b,c,d,e,f)
                a = int(input("-> "))
            elif a == 2:
                print("Terminar tareas")
                print("1/ Terminar primer proceso de cola \n2/ Terminar proceso por PID")
                opt = int(input("->/ "))
                so.endProcess(opt)
                a = int(input("-> "))
            elif a == 3:
                so.updateRe()
                so.tsklist()
                a = int(input("-> "))
            elif a == 4:
                so.plan()
                a = int(input("-> "))
            elif a == 5:
                print("Cerrando Sistema Operativo")
                break
            else:
                print("Seleccione una opcion (1 - 5)")
                a = int(input("-> "))

so = SistemaOperativo()
so.staMn() 
