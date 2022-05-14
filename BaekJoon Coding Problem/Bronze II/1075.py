N=input()
F=int(input())
n=int(N[:-2]+'00')
while True:
    if n%F==0:
        break
    n+=1
print(str(n)[-2:])
