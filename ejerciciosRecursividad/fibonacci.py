a = int(input("Numero para Fibonacci> "))
def fibonacci_secuencia(n: int) -> None:
    if n == 1:
        print(0)
    else:
        print(0, 1, end=" ")
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a = b
            b = c
fibonacci_secuencia(a)
 