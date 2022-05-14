# There is a game where three dice with eyes 1 to 6 are rolled and the prize money is awarded according to the following rules.

# If there are 3 identical eyes, you will receive a prize of 10,000 won + (same eye) x 1,000 won.
# If there are only two identical eyes, you will receive a prize of 1,000 won + (same eye) x 100 won.
# If all eyes are different, (the largest one among them) will receive a prize of 100 won.
# For example, if 3 eyes 3, 3, and 6 are given, the prize money is calculated as 1,000+3×100, giving you 1,300 won. Also, if 3 eyes are given as 2, 2, and 2, it is calculated as 10,000+2×1,000 and you get 12,000 won. If 3 eyes are given as 6, 2, and 5, the largest value among them is 6, so it is calculated as 6×100 and you will receive 600 won as a prize.

# Write a program that calculates the prize money when three dice are rolled.

a,b,c=map(int,input().split())

if a==b==c:
    R=10000+1000*a
    print(R)
elif a==b:
    R=1000+a*100
    print(R)
elif b==c:
    R=1000+b*100
    print(R)
elif a==c:
    R=1000+a*100
    print(R)
else:
    R=max(a,b,c)*100
    print(R)
    