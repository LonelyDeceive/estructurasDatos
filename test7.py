a = int(input("Numero para Fibonacci> "))
# 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13
def fibonacci(a:int)->int:
    b = 0
    if b == a:
        return a
    print(b)
    return fibonacci(b+1)
print(fibonacci(a))