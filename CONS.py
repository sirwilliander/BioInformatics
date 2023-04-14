f = open("datas/cons.txt")

raw = f.readlines()

print(raw)

dict={}

length=0


for i in range(len(raw)):
    if(raw[i][0]=='>'):
        dict[raw[i][1:-1]]=''
        j=i+1
        while raw[j][0]!= '>':
            dict[raw[i][1:-1]]=dict[raw[i][1:-1]]+raw[j][0:-1]
            j+=1
            if j==len(raw):
                break

for key in dict.keys():
    length=len(dict[key])
    break



print(dict)

list = [0] *length

matrix={}

matrix['A']=list.copy()
matrix['C']=list.copy()
matrix['G']=list.copy()

matrix['T']=list.copy()

for value in dict.values():
    for i in range(len(value)):
        matrix[value[i]][i]+=1


s=''
for i in range(length):
    maxKey='A'
    for key in matrix:
        if matrix[key][i]>matrix[maxKey][i]:
            maxKey=key
    # print(maxKey)
    s=s+maxKey

print(s)
result={}
for key in matrix:
    result[key] = ' '.join(str(item) for item in matrix[key])

for i in result:
    print(f'{i}:', result[i])

