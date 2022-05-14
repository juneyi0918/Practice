A,B=map(int,input().split())
area=A*B
if A%2==0 or B%2==0:
    print(0)
else:
    print(min(A,B))
    