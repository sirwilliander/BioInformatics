f = open("datas/splc.txt")

raw = f.readlines()

dict={}

print(raw)


for i in range(len(raw)):
    if(raw[i][0]=='>'):
        dict[raw[i][1:-1]]=''
        j=i+1
        while raw[j][0]!= '>':
            dict[raw[i][1:-1]]=dict[raw[i][1:-1]]+raw[j][0:-1]
            j+=1
            if j==len(raw):
                break

print(dict)

s=dict[next(iter(dict))]

del dict[next(iter(dict))]


# s=dict[next(iter(dict))]


for val in dict.values():
    print(val)
    s = s.replace(val, '')

print(s)


f = open("codonRNA")

raw = f.readlines()

list = []
codonTable = {}

for i in range(len(raw)):
    list.append(raw[i].split())

for i in range(len(list)):
    for j in range(len(list[i])):
        if j%2==0:
            codonTable[list[i][j]] = list[i][j + 1]
print(codonTable)


output=''
for i in range(len(s)):
    if i%3==0:
        temp = s[i] +s[i + 1] + s[i + 2]
        output = output + codonTable[temp]


print(output)
