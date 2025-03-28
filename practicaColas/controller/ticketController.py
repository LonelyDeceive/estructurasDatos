from model.ticket import Ticket
from model.node import Node

class TicketController:
    def __init__(self) -> None:
        TicketController.head = None
    
    def is_empty(self) -> bool:
        return TicketController.head == None
    
    def enqueue(self, ticket: Ticket) -> None:
        node = Node(ticket, ticket.priority_attention)
        if TicketController.is_empty(self):
            TicketController.head = node
        else:
            current = TicketController.head
            if current.priority < node.priority:
                node.next = current
                TicketController.head = node
            else:
                while current.next != None and current.next.priority > node.priority:
                    current = current.next
                node.next = current.next
                current.next = node

    def dequeue(self) -> Ticket:
        if self.is_empty():
            return None
        else:
            ticket = self.head.data
            self.head = self.head.next
            return ticket
        
    def peek(self, tipo) -> Ticket:
        nextTicket = TicketController.head
        if TicketController.is_empty(self):
            print("No hay mas turnos")
            return "No hay mas turnos"
        else:
            while nextTicket != None:
                if nextTicket.data.type == tipo:
                    print(nextTicket.data)
                    msg = {
                        "Nombre": nextTicket.data.name,
                        "Servicio": nextTicket.data.type,
                        "Prioridad": nextTicket.data.priority
                    }
                    return msg
                nextTicket = nextTicket.next               
            else:
                print("No hay turnos de este tipo", tipo)
                return("No hay mas turnos de tipo", tipo)
    
    def print_queue(self, type) -> Ticket:
        list_queue = []
        current = TicketController.head
        if current == None:
            print("Turnos Vacios")
            return "Turnos Vacios"
        else:
            if type == "todos" or type == " ":
                while current != None:
                    print(f"Turno: {current.data}, Prioridad: {current.priority}")
                    list_queue.append(current.data)
                    current = current.next
                print("Fin de la cola")
                return list_queue               
            elif type != "todos":
                while current != None:
                    if current.data.type == "dudas" and type == "dudas":
                        print(f"Turno: {current.data}, Prioridad: {current.priority}")
                        list_queue.append(current.data)
                    elif current.data.type == "asesor" and type == "asesor":
                        print(f"Turno: {current.data}, Prioridad: {current.priority}")
                        list_queue.append(current.data)
                    elif current.data.type == "caja" and type == "caja":
                        print(f"Turno: {current.data}, Prioridad: {current.priority}")
                        list_queue.append(current.data)
                    elif current.data.type == "otros" and type == "otros":
                        print(f"Turno: {current.data}, Prioridad: {current.priority}")
                        list_queue.append(current.data)
                    else:
                        print("No se encuentran turnos",type)
                        return "No se encuentran turnos"
                    current = current.next
                print("Fin de la cola")
                return list_queue
        