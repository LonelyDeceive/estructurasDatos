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
        
    def peek(self) -> Ticket:
        if TicketController.is_empty(self):
            return None
        else:
            return TicketController.head.data
    
    def print_queue(self) -> None:
        current = TicketController.head
        while current != None:
            print(f"Turno: {current.data}, Prioridad: {current.priority}")
            current = current.next
        print("Fin de la cola")