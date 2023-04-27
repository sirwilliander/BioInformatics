f = open("datas/nwck.txt")
raw = f.readlines()

dict = {}

print(raw)

trees = []

twoNodes = []

for i in range(len(raw)):
    if not raw[i] == '\n':
        if (raw[i][0] == '('):
            trees.append(raw[i])
        else:
            twoNodes.append(raw[i])

for i in range(len(twoNodes)):
    twoNodes[i] = twoNodes[i].split()

print(trees[0])
print(twoNodes)

print(trees[2])

# i=2

ind1 = trees[i].find(twoNodes[i][0])
ind2 = trees[i].find(twoNodes[i][1])

s = trees[i][min(ind1, ind2):max(ind1, ind2)]

print(s)

for i in range(len(trees)):

    ind1 = trees[i].find(twoNodes[i][0])
    ind2 = trees[i].find(twoNodes[i][1])

    s = trees[i][min(ind1, ind2):max(ind1, ind2)]
    s1 = ''
    for j in s:
        if j in ['(', ')', ',']:
            s1 += j

    while ',,' in s1:
        s1 = s1.replace(',,', ',')

    while '(,)' in s1:
        s1 = s1.replace('(,)', '')

    # print('\n s1:', s1, s1.count('('), '\n')
    if s1.count('(') == len(s1) or s1.count(')') == len(s1):
        print(len(s1), end=' ')
    else:
        print(s1.count('(') +s1.count(')')+ 2, end=' ')

print(s1)
