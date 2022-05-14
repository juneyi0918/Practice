import math

L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

if A/C>=B/D:
    print(int(L-math.ceil(A/C)))
else:
    print(int(L-math.ceil(B/D)))
