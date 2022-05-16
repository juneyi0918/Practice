T=int(input())
A=0  #300sec
B=0  #60sec
C=0  #10sec
if T >=300:
    A=T//300
    T=T%300
if T>=60:
    B=T//60
    T=T%60
if T>=10:
    C=T//10
    T=T%10
if T==0:
    print(A,B,C,sep=(" "))
else:
    print(-1)