# my way
D,H,M = map(int,input().split())

if D<11 or D==11 and H <11 or D==11 and H==11 and M<11:
    print(-1)
else:
    total_min=D*24*60+H*60+M-(11*24*60+60*11+11)
    print(total_min)

# Random smart person's way 
a, b, c = map(int,input().split())
print(max(a * 24 * 60 + b * 60 + c - 11 * 24 * 60 - 11 * 60 - 11, -1))