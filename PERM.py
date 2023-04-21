import itertools
import math

num=5
l= list(itertools.permutations(list(range(1,num+1))))
print(l)

print(math.factorial((num)))
for i in l:
    for j in i:
        print(j, end=' ')
    print()