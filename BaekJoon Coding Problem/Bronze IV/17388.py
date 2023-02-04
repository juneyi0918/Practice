s,k,h=map(int,input().split())
total=s+k+h
if total >=100:
    print('OK')
else:
    if s==min(s,k,h):
        print('Soongsil')
    elif k==min(s,k,h):
        