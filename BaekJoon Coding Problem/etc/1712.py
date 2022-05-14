# When A is Fixed cost, B is Variable cost, C is Price of unit.
# Find Break Even Point.


A,B,C=map(int,input().split())
if C-B<=0: 
    print("-1")
else:
    print(int(A/(C-B)+1))