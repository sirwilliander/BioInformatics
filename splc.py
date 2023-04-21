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

output=''
for key in dict:
    cnt=len(dict[key])%3
    for j in range(len(dict[key])-cnt):
        if j % 3 == 0:
            temp=dict[key][j]+dict[key][j+1]+dict[key][j+2]
            output=output+codonTable[temp]
print(output)
