lista = []
c = int(input("Longitud del arreglo> "))
n = 0  
total = 0  
def sumaA(c,total,n):
    if n == c:
        return " "
    t = int(input("Ingrese numero: "))
    total = total + t
    lista.append(t)
    print(lista)
    return sumaA(c,total,n+1)
print(sumaA(c,total,n))

