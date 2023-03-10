f = open("./../datas/rosalind_ini5.txt")

raw = f.readlines()

fp = open('output.txt', 'a')



for i in range(len(raw)):
    if i%2 == 1:
        fp.write(raw[i])