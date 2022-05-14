import math
D,H,W=map(int,input().split())
x_2= D**2/(H**2 + W**2)
x=math.sqrt(x_2)
print(int(x*H), int(x*W))


