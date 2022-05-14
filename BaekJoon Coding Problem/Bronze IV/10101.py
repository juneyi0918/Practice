A=int(input())
B=int(input())
C=int(input())
sum=A+B+C
if A==B==C==60:
    print('Equilateral')
elif sum==180 and A==B or A==C or B==C:
    print('Isosceles')
elif sum==180 and A!=B!=C:
    print('Scalene')
elif sum!=180:
    print('Error')