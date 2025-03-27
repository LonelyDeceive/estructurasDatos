from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    TicketController.print_queue("")
    return {"mensaje": "El siguiente turno es", "datos_turno": tipo}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(type: str):
    return {"mensaje": "Lista de turnos en cola", "datos_turnos": ""}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Bienvenido a la gestion de turnos"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}