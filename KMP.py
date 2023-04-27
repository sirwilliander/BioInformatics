f = open("datas/kmp.txt")

raw = f.readlines()

dict={}

#print(raw)


for i in range(len(raw)):
    if(raw[i][0]=='>'):
        dict[raw[i][1:-1]]=''
        j=i+1
        while raw[j][0]!= '>':
            dict[raw[i][1:-1]]=dict[raw[i][1:-1]]+raw[j][0:-1]
            j+=1
            if j==len(raw):
                break

s=dict['Rosalind_3200']
#print(s)

print(s[0:1])



#print(dict)

failArr=[0]*len(s)
#print(failArr)

for i in range(1,len(s)):
    # if i==13:
        # print(s[i], failArr[i-1], s[failArr[i-1]])
    if s[i]==(s[failArr[i-1]]):
        failArr[i] = failArr[i - 1]+1
    else:
        for j in reversed(range(1,failArr[i-1]+1)):
            # if i==13:
                # print(j, s[0:j], s[i-j+1:i+1])
            if s[0:j]==s[i-j+1:i+1]:
                failArr[i]=j
                # print(j, end=" ")
                break
for i in failArr:
    print(i, end=" ")

# print(failArr)