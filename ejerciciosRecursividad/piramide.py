num = int(input("Ingrese el numero para la piramide> "))
def piramide(n: int):
    if n == 1:
        print("1")
    else:
        piramide(n - 1)
        print(" ".join(str(j) for j in range(1, n + 1)))
piramide(num)