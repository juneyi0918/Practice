T=int(input())
for i in range(T):
    yonsei=[]
    korea=[]
    for j in range(9):
        a,b=map(int,input().split())
        yonsei.append(a)
        korea.append(b)
    if sum(yonsei)>sum(korea):
        print('Yonsei')
    elif sum(yonsei)<sum(korea):
        print('Korea')
    else:
        print('Draw')
        
##NOTE: NO NEED TO MAKE YONSEI AND KOREA AS LIST.. CAN JUST DO Y_score, K_score as variable and adds score in 2nd for loop ##