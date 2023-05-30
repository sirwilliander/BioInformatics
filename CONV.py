f = open("datas/conv.txt")

raw = f.readlines()

list = []


for i in range(len(raw)):
    list.append(raw[i].split())

for i in range(len(list)):
    for j in range(len(list[i])):
        list[i][j]=float(list[i][j])


print(list)

sol=[]

for i in list[0]:
    for j in list[1]:
        sol.append(round(i-j,4))

largestMultiplicity=0
key_=0

myDict={}

print(sol)

for i in sol:
    if i in myDict:
        myDict[i]+=1
    else:
        myDict[i]=1
print(myDict)

for key, val in myDict.items():
    if val>largestMultiplicity:
        largestMultiplicity=val
        key_=key


print(largestMultiplicity)
print(key_)