N=int(input())
lst=[]
for i in range (N):
    A,B,C=map(int,input().split())
    if A==B==C:
        total=10000+(A*1000)
    elif A==B or B==C:
        total=1000+(B*100)
    elif A==C:
        total=1000+(A*100)
    else:
        total=max(A,B,C)*100
    lst.append(total)
print(max(lst))


