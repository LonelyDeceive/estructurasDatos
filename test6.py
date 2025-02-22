numero = 5
def factorial(n:int)->int:
    if n == 1:
        print(n)
        return n
    print(n,"x",end=" ")
    return factorial(n-1)*n
print(factorial(numero))