# wrong code "too big"
# T=int(input())
# lst=[]
# for i in range(T):
#     a,b=map(int,input().split())
#     num=a**b
#     num=str(num)[-1]
#     lst.append(num)

# print(*lst, sep="\n")

T=int(input())
lst=[]
for i in range(T):
    a,b=map(int,input().split())
    a= a %10
    
    if a==0:
        lst.append(10)
    elif a==1 or a==5 or a==6:
        lst.append(a)
    elif a==4 or a==9:
        b=b%2
        if b==1:
            lst.append(a)
        else:
            lst.append(a**2%10)
    else:
        b=b%4
        if b==0:
            lst.append(a**4%10)
        else:
            lst.append(a**b%10)
print(*lst, sep="\n")