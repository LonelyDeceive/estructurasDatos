import numpy as np
import ML
class TaskNode:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None
        self.model = ML.entrenar_modelo()

    def isEmpty(self):
        return self.head is None

    def addTask(self, nombre, prioridad):
        if prioridad not in [1, 2, 3]:
            print("Prioridad inválida. Use 1 (alta), 2 (media), o 3 (baja).")
            return

        actual = self.head
        while actual:
            if actual.nombre == nombre:
                print(f"La tarea '{nombre}' ya está en la lista.")
                return
            actual = actual.next

        nueva_tarea = TaskNode(nombre, prioridad)

        if self.head is None or self.head.prioridad > prioridad:
            nueva_tarea.next = self.head
            self.head = nueva_tarea
        else:
            actual = self.head
            while actual.next and actual.next.prioridad <= prioridad:
                actual = actual.next
            nueva_tarea.next = actual.next
            actual.next = nueva_tarea

    def mostrarTareas(self):
        if self.isEmpty():
            print("La lista de tareas está vacía.")
            return
        actual = self.head
        print("\nLista de Tareas:")
        while actual:
            print(f"- {actual.nombre} (Prioridad {actual.prioridad})")
            actual = actual.next

        self.recomendarTarea()

    def eliminarTarea(self, nombre):
        actual = self.head
        anterior = None
        while actual:
            if actual.nombre == nombre:
                if anterior:
                    anterior.next = actual.next
                else:
                    self.head = actual.next
                print(f"Tarea '{nombre}' eliminada.")
                return
            anterior = actual
            actual = actual.next
        print(f"Tarea '{nombre}' no encontrada.")

    def recomendarTarea(self):
        if self.isEmpty():
            print("No hay tareas para recomendar.")
            return

        prioridades = {1: 0, 2: 0, 3: 0}
        actual = self.head
        while actual:
            prioridades[actual.prioridad] += 1
            actual = actual.next

        entrada = np.array([[prioridades[1], prioridades[2], prioridades[3]]])
        recomendada = self.model.predict(entrada)[0]
        nombres_prioridad = {1: "Alta", 2: "Media", 3: "Baja"}
        print(f"\n[ML] Recomendación: Considera hacer una tarea de prioridad {nombres_prioridad[recomendada]} (Prioridad {recomendada}).")
