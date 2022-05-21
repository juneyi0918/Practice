h,m,s=map(int,input().split(':'))
sh,sm,ss=map(int,input().split(':'))

total_sec=3600*h+60*m+s
total_start_sec=3600*sh+60*sm+ss
diff=total_start_sec-total_sec
if diff>0:
    print('%02d:%02d:%02d'%(diff//3600,diff%3600//60,diff%60))
else:
    diff+=60*60*24
    print('%02d:%02d:%02d'%(diff//3600,diff%3600//60,diff%60))