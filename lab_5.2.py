
x = int(123)
y = int(45)

def counter(a, b):

    ax = list(set(list(str(a))))
    ay = list(set(list(str(b))))

    cnt = 0
    for i in range(len(ay)):
        if ay[i] in ax:
            cnt += 1
    return cnt



print(counter(x, y))
print(list(set(list(str(x)))))
print(list(set(list(str(y)))))