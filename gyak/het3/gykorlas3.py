def fibonacci(n):
    a = 0
    b = 1
    for I in range(n):
        a, b = b, a + b
        yield a

if __name__ == '__main__':
    fibo_szamok = fibonacci(10)

    print(fibo_szamok)
    for i in fibo_szamok:
        print(i)