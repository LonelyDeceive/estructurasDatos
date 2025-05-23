import node as nd
def menu():
    lista = nd.TaskList()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1) Agregar tarea")
        print("2) Mostrar tareas")
        print("3) Eliminar tarea")
        print("4) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            try:
                prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
                lista.addTask(nombre, prioridad)
            except ValueError:
                print("Por favor, ingrese un número válido para la prioridad.")
        elif opcion == "2":
            lista.mostrarTareas()
        elif opcion == "3":
            nombre = input("Nombre de la tarea a eliminar: ")
            lista.eliminarTarea(nombre)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu() 