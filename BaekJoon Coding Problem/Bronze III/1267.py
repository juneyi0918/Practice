N=int(input())
a=list(map(int,input().split()))
Y=0
M=0

for i in range(N):
    if a[i]<30:
        Y+=10
        M+=15
    elif 30<=a[i]<60:
        Y+= (a[i]//30+1)*10
        M+=15
    elif a[i]>=60:
        Y+= (a[i]//30+1)*10
        M+= (a[i]//60+1)*15
        

if Y==M:
    print("Y","M",Y)
elif Y>M:
    print("M",M)
else:
    print("Y",Y)
   
   
