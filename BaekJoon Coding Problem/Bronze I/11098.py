n=int(input())
for _ in range(n):
    p=int(input())
    max_price=0
    max_player=''
    for _ in range(p):
        price,player=input().split()
        price=int(price)
        if price>max_price:
            max_price=price
            max_player=player
    print(max_player)