from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    print("Añadir ticket a la cola")
    name = input("Nombre: ")
    print("dudas, asesor, caja, otros)")
    type = input("Cual servicio necesita?: ")
    if type == "dudas":
        case = "para consultas generales"
    elif type == "asesor":
        case = "para asesorías personalizadas"
    elif type == "caja":
        case = "para operaciones de caja"
    elif type == "otros":
        case = "para cualquier otra gestión"
    identity = input("Ingrese su numero de documento: ")
    age = int(input("Ingrese su edad: "))
    uspriority = input("Necesita atencion prioritaria?: ")
    if uspriority == "si":
        priority = True
        intpriority = 1
    elif uspriority == "no":
        priority = False
        intpriority = 2
    elif uspriority == "" and age > 60:
        priority = True
        intpriority = 1
    else:
        priority = False
        intpriority = 2
    ticket = Ticket(name=name,type=type,identity=identity,case_description=case,age=age,priority_attention=priority,priority=intpriority)
    TicketController.enqueue("",ticket)
    print("Ticket añadido a la cola")