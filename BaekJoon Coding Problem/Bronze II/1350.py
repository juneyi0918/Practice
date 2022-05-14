N=int(input())
F=list(map(int,input().strip().split()))
C=int(input())
cluster=0
for i in F:
    if i % C ==0:
        cluster+=i//C
    else:
        cluster+=i//C+1
print(cluster*C)
     
     