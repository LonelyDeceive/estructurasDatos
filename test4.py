a = int(input("Numero 1> "))
b = int(input("Numero 2> "))
def restaDiv():
    print(a, "(1)")
    res = a
    for i in range(1, (a // b) + 1):
        res -= b
        print(res, "(", i + 1, ")", sep="")
        if res == 0:
            print("(El resultado es aprox: ",i,")")
    return res
restaDiv()
