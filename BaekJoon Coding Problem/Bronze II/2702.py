from math import gcd

T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    print(a*b//gcd(a,b),gcd(a,b))
    
