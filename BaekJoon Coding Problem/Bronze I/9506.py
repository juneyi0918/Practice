while True:
    A=int(input())
    if A==-1:
        break
    else:
        divisor=[]
        divisor_sum=0
        for i in range(1,A):
            if A%i==0:
                divisor.append(str(i))
                divisor_sum+=i
        if divisor_sum==A:
            print(f'{A} = ' + ' + '.join(divisor))
        else:
            print('%i is NOT perfect.' %A)
        
            
         