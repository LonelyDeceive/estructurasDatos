lista = []
c = int(input("Longitud del arreglo> "))
i = 0
while i < c:
    t = int(input("Ingrese numero: "))
    lista.append(t)
    print(lista)
    i=i+1
n = 0
total = 0
def sumaA(c,total,n):
    if n == c:
        print("=",end=" ")  
        return total
    res = lista[n]
    total = total + res
    print(lista[n],end=" ")
    if n+1 < c:
        print("+",end=" ")
    return sumaA(c,total,n+1)
print(sumaA(c,total,n))

