from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    print("Añadir ticket a la cola")
    name = input("Nombre: ")
    print("(dudas, asesor, caja, otros)")
    type = input("Cual servicio necesita?: ")
    identity = input("Ingrese su numero de documento: ")
    case = "Prueba"
    age = int(input("Ingrese su edad: "))
    uspriority = input("Necesita atencion prioritaria?: ")
    if uspriority == "si":
        priority = True
    elif uspriority == "no":
        priority = False
    elif uspriority == "" and age > 60:
        priority = True
    else:
        priority = False
    if priority == True:
        intpriority = 1
    else:
        intpriority = 2
    ticket = Ticket(name=name,type=type,identity=identity,case_description=case,age=age,priority_attention=priority,priority=intpriority)
    TicketController.enqueue("",ticket)
    TicketController.print_queue("")
    print("Ticket añadido a la cola")