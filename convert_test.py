
def convert_n_to_m(str_int, n, m):

    letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def leter_digit(a, b):
        ax = 0
        if isinstance(a, str) or isinstance(a, int) or isinstance(a, long):
            if isinstance(a, int) or isinstance(a, long):
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

    if (isinstance(str_int, int) or isinstance(str_int, long)) and str_int == 0:
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
    if isinstance(str_int, long):
        xl = str(str_int)
        if xl[len(xl) - 1] == 'L':
            x = xl[:len(xl - 1)]
        else:
            x = xl
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


#print(convert_n_to_m([1], 2, 2), '-result: False')
#print(convert_n_to_m(True, 1, 2), '-result: False')
#print(convert_n_to_m({1: 0}, 2, 2), '-result: False')
#print(convert_n_to_m(-777, 10, 2), '-result: False')
#print(convert_n_to_m(123123123123123123123.0, 11, 16), '-result: False')
#print(convert_n_to_m(100, 2, 1), '-result: 0000')
#print(convert_n_to_m(0, 10, 2), '-result: 0')
#print(convert_n_to_m(000, 10, 2), '-result: 0')
#print(convert_n_to_m(777, 10, 2), '-result: 1100001001')
print(convert_n_to_m('777L', 10, 2), '-error 777L, 10, 2', '-result: 1100001001') # 777L SyntaxError: invalid syntax
#print(convert_n_to_m('000', 10, 2), '-result: 0')
#print(convert_n_to_m('ZZZZ', 36, 13), '-result: 46A672')
#print(convert_n_to_m('000ZZZZ', 36, 13), '-result: 46A672')
#print(convert_n_to_m('ZZZZ', 35, 13), '-result: False')
#print(convert_n_to_m('qweasd', 33, 36), '-result: HGPEYJ')
print(convert_n_to_m('123123123123123123123', 11, 16), '-result: 2C09BC518E8048D23A')
print(convert_n_to_m(123123123123123123123, 11, 16), '-error 123123123123123123123, 11, 16', '-result: 2C09BC518E8048D23A')
print(convert_n_to_m(123123123123123123123, 10, 10), '-error 123123123123123123123, 10, 10', '-result: 123123123123123123123')
#print(convert_n_to_m('bnh34521', 31, 14), '-result: 119337DC2BC')
#print(convert_n_to_m('bnh34521', 11, 14), '-result: False')