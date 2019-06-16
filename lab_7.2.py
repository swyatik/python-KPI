

class Student(object):
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.number_lab = []
        self.exam_bal = 0
        self.sum_bal = 0
        self.sum_bal_max = ((self.conf['lab_max'] * self.conf['lab_num']) + self.conf['exam_max']) * self.conf['k']

        for i in range(self.conf['lab_num']):
            self.number_lab.append(0)

    def make_lab(self, m, n = None):
        self.m = m
        self.n = n

        if self.n == None:
            for i in range(len(self.number_lab)):
                if self.number_lab[i] == 0:
                    if self.m > self.conf['lab_max']:
                        self.number_lab[i] = self.conf['lab_max']
                    else:
                        self.number_lab[i] = self.m
                    break
        else:
            if self.n < self.conf['lab_num']:
                    if self.m > self.conf['lab_max']:
                        self.number_lab[n] = self.conf['lab_max']
                    else:
                        self.number_lab[n] = self.m

        return self

    def make_exam(self, m):
        self.m = m
        self.exam_bal = 0

        if self.m > self.conf['exam_max']:
            self.exam_bal = self.conf['exam_max']
        else:
            self.exam_bal = self.m

        return self

    def is_certified(self):
        self.sum_bal = 0
        for i in self.number_lab:
            self.sum_bal += i
        self.sum_bal += self.exam_bal

        if self.sum_bal < self.sum_bal_max:
            return (self.sum_bal, False,)
        else:
            return (self.sum_bal, True,)



conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o1 = Student('Oleg', conf1)
print(o1.is_certified())
    # , '(0, False)'
o2 = Student('Oleg', conf1)
o2.make_lab(60).make_lab(35.2)
print(o2.is_certified())
    #, '(75.2, True)'
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print(o3.is_certified())
    #, '(35, False)'
o3.make_lab(20,1).make_lab(20,0)
print(o3.is_certified())
    #, '(55, False)'
o3.make_lab(50,2)
print(o3.is_certified())
    #, '(55, False)'
o3.make_lab(40,1)
print(o3.is_certified())
    #, '(75, True)'
conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print(o4.is_certified())
    #, '(52, True)'
o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1)
print(o5.is_certified())
    #, '(43, False)'
o5.make_lab(7)
print(o5.is_certified())
    #, '(43, False)'
o5.make_exam(7)
conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print(o6.is_certified())
    #, '(51, True)'