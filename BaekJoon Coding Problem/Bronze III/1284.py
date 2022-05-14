while True:
    N=input()
    if N=='0':
        break
    ans =len(N)+1

    for n in N:
        if n=='0':
            ans+=4
        elif n=='1':
            ans+=2
        else:
            ans+=3
    print(ans)