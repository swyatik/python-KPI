import sys

a1 = sys.argv[1]
a2 = sys.argv[2]
x = a1
y = a2
count_ticket = 0

def compare(a):
    if len(a) < 6:
        a = "0" * (6 - len(a)) + a
    s1 = int(a[0]) + int(a[1]) + int(a[2])
    s2 = int(a[3]) + int(a[4]) + int(a[5])
    if s1 == s2:
        return True
    else:
        return False

if int(x) <= int(y) and int(x):

    while int(x) < int(y) + 1:
        if compare(x):
            count_ticket += 1
        x = str(int(x) + 1)
    print(count_ticket)

else:
    if compare(x) or int(x) == 0:
        count_ticket += 1
        print(count_ticket)
    else:
        print("0")
