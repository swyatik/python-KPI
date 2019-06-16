import sys

x = sys.argv[1]



def count_holes(n):

    a = str(n)

    if a[0] == '-' and a[1:].isdigit() or a.isdigit():
        if a[0] == '-':
            y = str(abs(int(a)))
        else:
            y = str(int(a))

        number = 0

        for i in y:
            if int(i) == 8:
                number += 2
            elif int(i) == 0 or int(i) == 4 or int(i) == 6 or int(i) == 9:
                number += 1

        return number

    else:
        return 'ERROR'

print(count_holes(x))
