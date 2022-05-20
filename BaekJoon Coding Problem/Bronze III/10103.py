n=int(input())
C=100
S=100
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        S-=a
    elif a<b:
        C-=b
print(C,S,sep='\n')