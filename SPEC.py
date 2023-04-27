f = open("massTable.txt")

raw = f.readlines()

list = []


for i in range(len(raw)):
    list.append(raw[i].split())

dict={}

for i in range(len(raw)):
    dict[list[i][0]]=list[i][1]

print(dict)
print(list)

g = open("datas/spec.txt")

raw = g.readlines()
for i in range(len(raw)):
    raw[i]=float(raw[i])

solution=''
for i in range(len(raw)-1):
    diff=raw[i+1]-raw[i]
    print(diff)
    for key, val in dict.items():
        if round(float(val),4)== round(diff,4):
            solution+=key
            break



print(raw)
print(solution)

