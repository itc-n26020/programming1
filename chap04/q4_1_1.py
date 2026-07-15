a = 0
b = 1
b, a = a,b
print(a, b)
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
print(fib(1000))
