import sys

n = int(sys.argv[1])

a_0 = 0
a_1 = 1
fib = 0
if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    for i in range(n - 1):
        fib = a_0 + a_1
        a_0 = a_1
        a_1 = fib
    print(fib)