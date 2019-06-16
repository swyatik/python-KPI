
def find_fraction(summ):
    numerator = 0
    if summ < 3:
        return False
    else:
        if summ % 2 == 0:
            numerator = summ / 2 - 1
        else:
            numerator = summ // 2
    denominator = summ - numerator
    if numerator % 2 == 0 and denominator % 2 == 0:
        numerator -= 1
        denominator += 1
    return (int(numerator), int(denominator),)


print(find_fraction(2))
# False
print(find_fraction(3))
# (1, 2)
print(find_fraction(10))
# (3, 7)
print(find_fraction(62))
# (29, 33)
print(find_fraction(150000001))
# (75000000, 75000001)