import math
T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    ans=math.factorial(b)//(math.factorial(b-a)*math.factorial(a))
    print(ans)