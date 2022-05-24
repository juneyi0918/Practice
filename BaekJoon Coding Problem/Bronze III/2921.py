N=int(input())
summ=0
for i in range(N+1):
    for j in range(i,N+1):
        summ+=i+j
print(summ)