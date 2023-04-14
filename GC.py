def countGcContent(s):
    cnt=0
    for i in range(len(s)):
        if(s[i]=='G' or s[i]=='C'):
            cnt+=1
    return cnt


f = open("datas/gc.txt")

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

cntDict={}

for key in dict:
    cntDict[key]=countGcContent(dict[key])

for key in dict:
    cntDict[key]=float(cntDict[key]/(len(dict[key])))

print((cntDict))
key=max(cntDict, key=lambda x:cntDict[x])
print(key)
print(round(cntDict[key]*100,6))