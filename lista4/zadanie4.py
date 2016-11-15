
def fib(arg1):
    b = 0
    c = 1
    if arg1 == 0 or arg1 == 1:
        print(arg1)
    else:
        for i in range(0, arg1):
            b = b+c
            c, b = b, c
        print(b)



a = int(input())
fib(a)
