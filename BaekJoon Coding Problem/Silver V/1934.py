import math 
T=int(input())
lst=[]
for i in range(T):
    A,B=map(int,input().split())
    lcm=math.lcm(A,B)
    lst.append(lcm)
for j in range(T):
    print(lst[j])