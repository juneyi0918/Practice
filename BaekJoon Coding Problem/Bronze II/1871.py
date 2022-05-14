N=int(input())
for i in range(N):
    L,D=input().split('-')
    D_value=int(D)
    L_value=0
    for j in range(3):
        L_value+=((ord(L[j])-65)*(26**(2-j)))

    if abs(L_value-D_value)<=100:
        print("nice")
    else:
        print("not nice")
    