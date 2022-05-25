i=1
while True:
    n=int(input())
    if n==0:
        break
    else:
        n1=3*n
        if n1%2==0:
            n2=n1//2
        else:
            n2=(n1+1)//2
        n3=3*n2
        n4=int(n3//9)
        print(f'{i}. odd {n4}'if n1%2!=0 else f'{i}. even {n4}')
        i+=1