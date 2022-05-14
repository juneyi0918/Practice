import math
L=int(input())
print(math.ceil(L/5))

# or

Ans=L//5
if L%5==0:
    print(Ans)
else:
    print(int(Ans+1))