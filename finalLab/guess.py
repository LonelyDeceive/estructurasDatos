# app.py (Código Python completo)
from fastapi import FastAPI
import os
import random

app = FastAPI(title="GuessGame")

class newNumber:
    def __init__(self):
        self.selNum = random.randint(0,100)
        print(self.selNum) 

guessnum = newNumber()
@app.get("/ins")
def read_root():
    """
    Endpoint de instrucciones
    """
    ins = "Hola, ahora estas en un juego de adivinar un numero entre 0 a 100"
    how = "Entra a /try?number=[numero del 0 al 100] para intentar"
    new = "Entra a /reload para hacer un nuevo juego"
    hint = "Recibiras una pista si tu numero esta 10 unidades mayor o menor al numero por adivinar"
    name = "Jhon Mario Carvajal"
    return {"Instrucciones": ins, "Jugar en": how, "Nuevo juego": new, "Pistas": hint, "Hecho por": name}

@app.get("/try")
def read_root(number: int):
    if number > 100 or number < 0:
        res = "Recuerda el rango de 0 a 100..."
    elif number == guessnum.selNum:
        res = f"Adivinaste el numero! !{guessnum.selNum}!, Entra a /reload para hacer un nuevo juego"
    elif number in range(guessnum.selNum,guessnum.selNum + 10,1):
        res = "Tu numero esta MUY CERCA pero es MAYOR al numero a adivinar"
    elif number in range(guessnum.selNum -10,guessnum.selNum,1):
        res = "Tu numero esta MUY CERCA pero es MENOR al numero a adivinar"        
    elif number > guessnum.selNum:
        res = "Tu numero esta MUY ALTO del numero a adivinar"
    elif number < guessnum.selNum:
        res = "Tu numero esta MUY BAJO del numero a adivinar"

    return {"Tu numero": number, "Intento..": res}

@app.get("/reload")
def read_root():
    guessnum.selNum = random.randint(0,100)
    print(guessnum.selNum)
    return {"Se ha creado un nuevo juego y un nuevo numero , entra a /try?number=[numero del 0 al 100] para intentarlo de nuevo"}