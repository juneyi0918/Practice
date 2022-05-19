n=int(input())
Q1=Q2=Q3=Q4=AXIS=0
for i in range (n):
    X,Y=map(int,input().split())
    if X==0 or Y==0:
        AXIS+=1
    elif X>0 and Y>0:
        Q1+=1
    elif X<0 and Y>0:
        Q2+=1
    elif X<0 and Y<0:
        Q3+=1
    else:
        Q4+=1
print('Q1:',Q1,'\n''Q2:',Q2,'\n''Q3:',Q3,'\n''Q4:',Q4,'\n''AXIS:',AXIS)