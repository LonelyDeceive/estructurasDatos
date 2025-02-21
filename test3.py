a = int(input("Numero 1> "))
b = int(input("Numero 2> "))
def sumaMul():
    print(a,"(1)")
    for i in range (1,b):
        print(a,"+",a*i,"=",end=" ")
        print(a*(i+1),end=" ")
        print("(",i+1,")",sep="")
    return a
sumaMul()