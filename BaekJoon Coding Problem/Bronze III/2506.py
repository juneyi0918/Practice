N=int(input())
score=0
count=0
lst=list(map(int,input().split()))

for i in range(N):
    if lst[i]==1:
        count+=1
        score+=count
    else:
        count=0
    
print(score)