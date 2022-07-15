A3=int(input())
A2=int(input())
A1=int(input())
B3=int(input())
B2=int(input())
B1=int(input())
A_total=3*A3+2*A2+A1
B_total=3*B3+2*B2+B1
if A_total>B_total:
    print('A')
elif B_total>A_total:
    print('B')
else:
    print('T')