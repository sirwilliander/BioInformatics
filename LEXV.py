import itertools

f = open("datas/lexv.txt", "r")

raw = f.readlines()

abc = raw[0].strip().split()
n = int(raw[1])

abc = ["0"] + abc

print(abc)
strings = {}
for i in range(1, n + 1):
    for string in [''.join(j) for j in itertools.product(abc[1:], repeat=i)]:
        strings[string + (n - i) * abc[0]] = string
        print(strings)
print(strings)

index = {}
cnt=1
for i in abc:
    index[i]=cnt
    cnt+=1

print(index)
print(index)
key = lambda x: [index[char] for char in x]
# print(key)
sorted_ = sorted(strings.keys(), key=key)

for string in sorted_:
    print(strings[string])
