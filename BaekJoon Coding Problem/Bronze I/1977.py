i=1
perfect=[]
ans=[]
for _ in range(100):
    p=i*i
    perfect.append(p)
    i+=1
M=int(input())
N=int(input())
for j in perfect:
    if j>=M and j<=N:
        ans.append(j)
if len(ans)>=1:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)