import itertools

f = open("datas/kmer.txt")

raw = f.readlines()

dict = {}

print(raw)
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

s=dict['Rosalind_7636']

strings= 'ACGT'

list = [''.join(x) for x in (itertools.product(strings, repeat = 4))]
print(list)

dict1={}

for i in list:
    dict1[i]=0

print(dict1)

for i in range(len(s) - 4 + 1):
    dict1[s[i:i+4]] += 1
for i in list:
    print(dict1[i], end=" ")
