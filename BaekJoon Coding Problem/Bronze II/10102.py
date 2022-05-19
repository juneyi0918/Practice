V=int(input())
vote=list(map(str,input().upper()))
count_a=vote.count('A')
count_b=vote.count('B')

if count_a==count_b:
    print('Tie')
elif count_a>count_b:
    print("A")
else:
    print("B")