from typing import Optional

class Node:
    def __init__(self, numero:int):
        self.dato = numero
        self.next: Optional["Node"] = None

class Lista:
    def __init__(self) -> None:
        self.cabeza = Optional["Node"] = None
    
    def add(self, numero:int) -> None:
        node: Node = Node(numero)
        if self.cabeza is None:
            self.cabeza = node
        else:
            while self.cabeza.next is not None:
                self.cabeza = self.cabeza.next