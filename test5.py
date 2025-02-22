num = int(input("Ingrese el numero para la piramide: "))
def piramide(n):
    for i in range(1, n + 1):
        print("".join(str(j) for j in range(1, i + 1)),sep =" ")
piramide(num)
