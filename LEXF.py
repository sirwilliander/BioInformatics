import itertools

f = open("datas/lexf.txt")


raw = f.readlines()

raw[0]=raw[0].split()
print(raw)



n = int(raw[1])
print(n)

result = list(itertools.product(raw[0], repeat = n))

print("\n".join(["".join(x) for x in result]))