a = int(input("Numero 1> "))
b = int(input("Numero 2> "))
i = 1
print(a,"(1)")
def sumaMul(a,b,i):
    if i == b:
        return 
    print(a,"+",a*i,"=",end=" ")
    print(a*(i+1),end=" ")
    print("(",i+1,")",sep="")
    return sumaMul(a,b,i+1)
sumaMul(a,b,i)