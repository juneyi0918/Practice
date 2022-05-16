N,M,K=map(int,input().split())
group=0
while N>=2 and M>=1 and N+M>=K+3:
    N-=2
    M-=1
    group+=1
print(group)