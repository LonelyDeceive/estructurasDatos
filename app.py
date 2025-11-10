# app.py (Código Python completo)
from fastapi import FastAPI
import os

app = FastAPI(title="SimpleHelloAPI")

@app.get("/hello")
def read_root(name: str = "Jhon Mario Carvajal"):
    """
    Endpoint que devuelve un saludo personalizado.
    """
    ambiente = os.getenv("AMBIENTE_DESPLIEGUE", "Local")
    saludo = f"Hola, {name}! Esta es mi API tipo: {ambiente}"
    return {"message": saludo}