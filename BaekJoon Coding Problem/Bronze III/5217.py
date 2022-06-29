for _ in range(int(input())):
    n=int(input())
    cnt=1
    print('Pairs for %d:' %n, end=' ')
    
    for i in range((n-1)//2):
        if i!=0:
            print(',', end=' ')
        print(cnt,n-cnt,end='')
        cnt+=1
    print()