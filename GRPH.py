f = open("datas/GRPH.txt")

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
k = 3
for key, value in dict.items():
    for key2, value2 in dict.items():
        if key != key2:
           #  print(value2[-3:])
            if value2[0:3] == value[-3:]:
                # print(value, value2)
                print(key, key2)
