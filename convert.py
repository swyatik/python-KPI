
def convert_n_to_m(str_int, n, m):

    letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def leter_digit(a, b):
        ax = 0
        if isinstance(a, str) or isinstance(a, int):
            if isinstance(a, int):
                ax = str(a)
            else:
                ax = a
            for i in ax:
                el = 0
                if i.isalpha():
                    el = i.upper()
                else:
                    el = i
                if el not in b:
                    return False
            return True
        else:
            return False

    if leter_digit(str_int, letter) == False:
        return False

    if isinstance(str_int, int) and str_int == 0:
        return '0'

    if isinstance(str_int, str):
        d = 0
        for i in str_int:
            if i.isdigit():
                d += 1
        if d == len(str_int) and int(str_int) == 0:
            return '0'

    x = 0
    result = ''

    if isinstance(str_int, str):
        x = str_int
    else:
        x = str(str_int)

    for item in x:
        if letter.index(item.upper()) >= n:
            return False

    string_in = str(x[::-1])
    decimal = 0

    if n == 1:
        decimal = len(x)
    else:
        for i in range(len(string_in)):
            if string_in[i].isdigit():
                decimal += int(string_in[i]) * (n ** i)
            else:
                decimal += letter.index(string_in[i].upper()) * (n ** i)
    if m > 1:
        el = -1
        temp = decimal
        while temp > 0:
            if temp % m < 10:
                el = temp % m
            else:
                el = letter[temp % m]
            result += str(el)
            if (temp - (temp % m)) == 1:
                temp = 1
            else:
                temp = (temp // m)
        result = str(result[::-1])
    else:
        for i in range(decimal):
            result += "0"

    return result