from sys import stdin
A=int(stdin.readline())
symbol=str(input())
B=int(stdin.readline())

if symbol=='+':
    print(A+B)
elif symbol=='*':
    print(A*B)