T=int(input())
lst=list(map(int,input().strip().split()))
cnt=0
for i in lst:
    if i == T:
        cnt+=1
print(cnt)