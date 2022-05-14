N = int(input())
layer=1
cnt=1
while N > layer:
    layer=layer+6*cnt
    cnt+=1
print(cnt)

