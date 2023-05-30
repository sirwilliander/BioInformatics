f = open("datas/sseq.txt")

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

print(dict)

list=[]

for i in dict.values():
    list.append(i)

print(list)

counter=0

solution=[]

for i in range(len(list[0])):
    if list[0][i]==list[1][counter]:
        solution.append(i)
        counter+=1
    if counter==len(list[1]):
        break



for i in solution:
    print(i+1, end=" ")