N=int(input())
star_minus=0
for i in range(N):
    print(' '*i+'*'*(2*N-1-star_minus))
    star_minus+=2
    