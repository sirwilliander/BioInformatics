def lcsq(a, b):
    m = len(a)
    n = len(b)
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if a[i - 1] == b[j - 1]:
            lcs_algo[index - 1] = a[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("".join(lcs_algo))


f = open("datas/lcsq.txt")

raw = f.readlines()

print(raw)

dict = {}

length = 0

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

a = dict['Rosalind_7308']
b = dict['Rosalind_6700']
lcsq(a, b)
