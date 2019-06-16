number = ['1', '2', '5', '1', '1.2', '-123', '2', '-123', '5']
letter = ['qwe', 'reg', 'qwe', 'REG']
l1 = []
m = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
k = [0, 'q', 'qq', 'qqq', 'qqq', 'qqq', 'qqqq', 0, 'qqq']
o = ['asd', 'dsa', 1, '1', 1.0]


def clean_list(a):
    list_in = a

    if not list_in:
        return a
    spisok = []

    def type_l(b):
        if isinstance(b, str):
            return "s"
        if isinstance(b, float):
            return "f"
        if isinstance(b, int):
            return "i"
        if isinstance(b, list):
            return "l"


    for i in range(len(list_in)):
        x = 0
        for j in range(len(spisok)):
            if type_l(list_in[i]) == type_l(spisok[j]):
                if list_in[i] == spisok[j]:
                    x += 1
        if x == 0:
            spisok.append(list_in[i])

    return spisok

print(clean_list(number))
print(clean_list(letter))
print(clean_list(l1))
print(clean_list(m))
print(clean_list(n))
print(clean_list(k))
print(clean_list(o))