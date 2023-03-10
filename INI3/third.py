f = open("./../datas/rosalind_ini3.txt")

raw = f.readlines()

list=[int(number) for number in raw[1].split(" ")]
print(list[1])


print(raw[0][list[0]:int(list[1])+1], raw[0][list[2]:int(list[3])+1])