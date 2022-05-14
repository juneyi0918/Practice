# solution 1
Ash,Asm,Ass,Aeh,Aem,Aes=map(int,input().split())
Bsh,Bsm,Bss,Beh,Bem,Bes=map(int,input().split())
Csh,Csm,Css,Ceh,Cem,Ces=map(int,input().split())

A_work=(Aeh*3600+Aem*60+Aes)-(Ash*3600+Asm*60+Ass)
B_work=(Beh*3600+Bem*60+Bes)-(Bsh*3600+Bsm*60+Bss)
C_work=(Ceh*3600+Cem*60+Ces)-(Csh*3600+Csm*60+Css)

print(A_work//3600,A_work%3600//60,A_work%60)
print(B_work//3600,B_work%3600//60,B_work%60)
print(C_work//3600,C_work%3600//60,C_work%60)

# solution 2
for i in range(3):
    sh,sm,ss,eh,em,es=map(int,input().split())
    work=(eh*3600+em*60+es)-(sh*3600+sm*60+ss)
    print(work//3600,work%3600//60,work%60)
