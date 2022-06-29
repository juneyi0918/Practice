A,B=map(int,input().split())
num1 = min(A,B)
num2 = max(A,B)
if num1==num2:
    print(0)
else:
    print(num2-num1-1)
for i in range(num1+1,num2):
    print(i,end=' ')
