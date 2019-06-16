
class CombStr(object):
    def __init__(self, string):
        self.string = string
        self.amount = 0

    def count_substrings(self, length):
        self.length = length
        self.sab = []
        if self.string == '' or self.length == 0 or len(self.string) < self.length:
            return 0
        elif len(self.string) == self.length:
            return 1
        else:
            self.amount = 0
            for i in range(len(self.string) - self.length + 1):
                self.sab.append(self.string[i:i + self.length])

            self.sab = set(self.sab)
            for i in self.sab:
                if len(i) == self.length:
                    self.amount += 1
            return self.amount



s1  = CombStr('')
print(s1.count_substrings(0))
#, 0
print(s1.count_substrings(1))
#, 0
s2  = CombStr('?')
print(s2.count_substrings(0))
#, 0
print(s2.count_substrings(1))
#, 1
print(s2.count_substrings(2))
#, 0
s3  = CombStr('qweqweqwe')
print(s3.count_substrings(1))
#, 3
print(s3.count_substrings(2))
#, 3
print(s3.count_substrings(3))
#, 3
print(s3.count_substrings(4))
#, 3
print(s3.count_substrings(9))
#, 1
print(s3.count_substrings(10))
#, 0
s4  = CombStr('29389efj s9fbsyaedg dBD QYDUEHWFUHB&*#(@)(#!')
print(s4.count_substrings(1))
#, 30
print(s4.count_substrings(2))
#, 43
print(s4.count_substrings(5))
#, 40
print(s4.count_substrings(15))
#, 30
s5  = CombStr("A taste of honey. Tasting much sweeter than wine. I dream of your first kiss. And then I feel upon my lips again. A taste of honey. Tasting much sweeter than wine. I will return, yes I will return. I'll come back for the honey and you. Yours was the kiss that awoke my heart. There lingers still, though we're far apart. That taste of honey. Tasting much sweeter than wine. Oh I will return, yes I will return. I'll come back (He'll come back). for the honey (For the honey). and you")
print(s5.count_substrings(1))
#, 34
print(s5.count_substrings(7))
#, 311
print(s5.count_substrings(14))
#, 355
print(s5.count_substrings(21))
#, 372
print(s5.count_substrings(45))
#, 420