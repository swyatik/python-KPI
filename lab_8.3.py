
def bouquets(narcissus_price, tulip_price, rose_price, summ):
    if narcissus_price > summ and tulip_price > summ and rose_price > summ:
        return 0
    amount = 0
    bouquet = [0, 0, 0]
    len_range = int(summ / min([narcissus_price, tulip_price, rose_price])) + 1
    for narcissus in range(len_range):
        for tulip in range(len_range):
            for rose in range(len_range):
                bouquet[0] = rose
                bouquet[1] = tulip
                bouquet[2] = narcissus
                if (bouquet[0] + bouquet[1] + bouquet[2]) % 2 != 0:
                    if (bouquet[0] * narcissus_price) + (bouquet[1] * tulip_price) + (bouquet[2] * rose_price) <= summ:
                        amount += 1
                    else:
                        break
    return amount

print(bouquets(1,1,1,5))
# 34
print(bouquets(2,3,4,10))
# 12
print(bouquets(2,3,4,100))
# 4019
print(bouquets(200,300,400,10000))
# 4019
print(bouquets(200,300,400,100000))
# 3524556
print(bouquets(22,44,150,20000))
#, 4666877)
