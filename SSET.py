n=814

sum_=1
for i in range(n):
    sum_=(sum_*2%1000000)

print(sum_)