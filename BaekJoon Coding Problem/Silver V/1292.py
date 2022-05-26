lst=[]
for i in range(1,1001):
    for j in range(i):
        lst.append(i)
sum=0
A,B=map(int,input().split())
for k in range(A-1,B):
    sum+=lst[k]
print(sum)
