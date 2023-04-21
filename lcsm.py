f = open("datas/lcsm.txt")

raw = f.readlines()

dict = {}

# print(raw)

for i in range(len(raw)):
    if (raw[i][0] == '>'):
        dict[raw[i][1:-1]] = ''
        j = i + 1
        while raw[j][0] != '>':
            dict[raw[i][1:-1]] = dict[raw[i][1:-1]] + raw[j][0:-1]
            j += 1
            if j == len(raw):
                break

print(dict)

zeroKey='Rosalind_1852'

maxNum=0
maxSubString=''



for i in range(len(dict[zeroKey])):
    for j in reversed(range(len(dict[zeroKey]))):
        cnt = 0
        for val in dict.values():
            if(cnt==0):
                cnt+=1
            else:
                if(dict[zeroKey][i:j+1] in val):
                    cnt+=1
        # print(i, j, cnt, len(dict), maxNum)
        if(cnt== len(dict)):

            if(maxNum<j-i+1):
                print(i, j, cnt, len(dict), maxNum)
                maxNum=j-i+1
                print(maxNum, 'maxnum')
                maxSubString= dict[zeroKey][i:j+1]
                print(maxSubString)


print(maxSubString)