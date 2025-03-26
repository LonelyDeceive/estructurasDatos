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
    typee = input("Cual servicio necesita?: ")
    identity = input("Ingrese su numero de documento: ")
    case = "Prueba"
    age = int(input("Ingrese su edad: "))
    priority = True
    ticket = Ticket(name=name,type=typee,identity=identity,case_description=case,age=age,priority_attention=priority)
    TicketController.enqueue(ticket,ticket)
    TicketController.print_queue("")
    print("Ticket añadido a la cola")