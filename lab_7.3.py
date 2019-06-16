
class SuperStr(str):

    def __init__(self, string):
        self.string = string
        self.string_list = []
        self.string_list_revers = []

        if isinstance(self.string, str) and len(self.string) > 1:

            self.string_list = list(self.string)

            for i in range(len(self.string_list)):
                if self.string_list[i].isalpha():
                    self.string_list[i] = self.string_list[i].lower()

            self.string_list_revers = self.string_list[::-1]

    def is_repeatance(self, s):
        self.s = s
        if isinstance(self.string, str) and isinstance(self.s, str) and self.string != '' and self.s != '':
            if len(self.string) % len(self.s) == 0:
                n = 0
                for i in range(len(self.string)):
                    if n == len(self.s):
                        n = 0
                    if self.s[n].isalpha() and self.string[i].isalpha():
                        if self.s[n].lower() == self.string[i].lower():
                            n += 1
                        else:
                            return False
                    else:
                        if self.s[n] == self.string[i]:
                            n += 1
                        else:
                            return False
                return True
            else:
                return False
        else:
            return False

    def is_palindrom(self):

        if isinstance(self.string, str):
            if self.string == '' or len(self.string) == 1:
                return True

            for i in range(len(self.string_list)):
                if self.string_list[i] != self.string_list_revers[i]:
                    return False

            return True

        else:
            return False


# рішення від викладача

class SuperStr(str):
    def is_repeatance(self, substring):
        # спробуємо перевернути рядок
        try:
            if len(substring) == 0 or len(self) == 0:
                return False
            multiplier = len(self) / len(substring)
            return self == substring * multiplier
        # якщо помилка - тип аргументу не підходить
        except TypeError:
            return False

    def is_palindrom(self):
        try:
            return self.lower() == self[::-1].lower()
        except TypeError:
            return False

s = SuperStr('123123123123')
print(s.is_repeatance('123'))
# True
print(s.is_repeatance('123123'))
# True
print(s.is_repeatance('123123123123'))
# True
print(s.is_repeatance('12312'))
# False
print(s.is_repeatance(123))
# False
print(s.is_palindrom())
# False
print(s)
# 123123123123 (рядок)
print(int(s))
# 123123123123 (ціле число)
print(s + 'qwe')
# 123123123123qwe
p = SuperStr('123_321')
print(p.is_palindrom())
# True


print('------------------------------------')
print('------------------------------------')

s1 = SuperStr('678678678678')
print(s1.is_repeatance('6786'))
    #,  '=', 'False'
print(s1.is_repeatance('678'))
    #, '=', 'True'
print(s1.is_repeatance('678678'))
    #,  '=', 'True'
print(s1.is_repeatance('678678678'))
    #,  '=', 'False'
print(s1.is_repeatance('q'))
    #,  '=', 'False'
print(s1.is_repeatance(''))
    #,  '=', 'False'
print(s1.is_repeatance(678))
    #,  '=', 'False'
print(s1.is_repeatance([]))
    #,  '=', 'False'
print(s1.is_repeatance([678]))
    #,  '=', 'False'
print(s1.is_palindrom())
    #,  '=', 'False'
print(s1.isdigit())
    #,  '=', 'True'
print(int(s1))
    #,  '=', '678678678678'
print('("' + s1 + '")',  '=', '("678678678678")')
s2 = SuperStr('')
print(s2.is_repeatance(''))
    #,  '=', 'False'
print(s2.is_repeatance('a'))
    #,  '=', 'False'
print(s2.is_palindrom())
    #,  '=', 'True'
print(bool(s2))
    #,  '=', 'False'
s3 = SuperStr('mystring1Gnirtsym')
print(s3.is_repeatance('my'))
    #,  '=', 'False'
print(s3.is_repeatance('q,.%;#'))
    #,  '=', 'False'
print(s3.is_palindrom())
    #,  '=', 'True'
print(s3.lower())
    #,  '=', 'mystring1gnirtsym'
print(s3, '=', 'mystring1Gnirtsym')
s4 = SuperStr('q')
print(s4.is_repeatance(''))
    #,  '=', 'False'
print(s4.is_repeatance('q'))
    #,  '=', 'True'
print(s4.is_palindrom())
    #,  '=', 'True'
print(s4.upper(),  '=', 'Q')