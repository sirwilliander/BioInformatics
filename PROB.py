import math

f = open("datas/prob.txt")

raw = f.readlines()

s = raw[0]

list_ = raw[1].split()

print(list_)

for i in list_:
    temp = 0
    prod = 1
    p = float(i) / 2
    q = (1 - float(i)) / 2
    for j in s:
        if j == 'G' or j == 'C':
            temp = temp + math.log10(p)
            prod = prod * p
        elif j == 'A' or j == 'T':
            temp = temp + math.log10(q)
            prod = prod * q
    print(round(temp,3))
