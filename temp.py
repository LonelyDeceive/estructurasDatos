temperatura = []
contador = 0
stemperatura = 0
for i in range(0,10):
    t = int(input("Registre temperatura: "))
    temperatura.append(t)
    stemperatura = stemperatura + t
    contador = contador + 1
print(temperatura)
promedio = stemperatura/contador
print(promedio)

