N=int(input())
star=1
star_minus=2
for i in range(1,N+1):
    print(' '*(N-i)+'*'*star)
    star+=2
for j in range(1,N+1):
    print(' '*j+'*'*(2*N-1-star_minus))
    star_minus+=2