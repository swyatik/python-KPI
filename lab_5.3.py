import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

def super_fibonacci(n, m):

    list_my = []

    if n <= m:
        return int(1)

    else:
        for i in range(n):
            if i < m:
                list_my.append("1")
            else:
                j = i
                e = 0
                el_i = 0
                while e < m:
                    el_i = el_i + int(list_my[j - 1])
                    j -= 1
                    e += 1
                list_my.append(el_i)

        return list_my[n - 1]


print(super_fibonacci(x, y))


def type_l(b):
    if isinstance(b, str):
        return "s"
    if isinstance(b, float):
        return "f"
    if isinstance(b, int):
        return "i"
    if isinstance(b, list):
        return "l"

print(type_l(super_fibonacci(x, y)))