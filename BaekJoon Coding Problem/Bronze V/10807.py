N=int(input())
lst=list(map(int,input().strip().split()))
v=int(input())
cnt=0
for i in lst:
    if i == v:
        cnt+=1
print(cnt)