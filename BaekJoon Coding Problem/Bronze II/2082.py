T=int(input())
for i in range(T):
    N=int(input())
    N2=str(N**2)
    N=str(N)
    if N==N2[-len(N):]:
        print('YES')
    else:
        print('NO')


