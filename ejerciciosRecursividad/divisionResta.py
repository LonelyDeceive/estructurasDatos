a = int(input("Numero 1> "))
b = int(input("Numero 2> "))
print(a, "(1)", sep="")
def restaDiv(a, b, i=1):
    if a == 0:
        print("(El resultado es aprox: ", i - 1, ")", sep="")
        return 0
    elif a - b < 0:
        a == 0
        print("(El resultado es aprox: ", (i)-(((a-b)/b)*-1), ")", sep="")
        return 0
    else:
        print(a - b, "(", i + 1, ")", sep="")
        return restaDiv(a - b, b, i + 1) 
restaDiv(a, b)
 