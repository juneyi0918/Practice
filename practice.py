##### HOW TO REVERSE STR [::-1] #####
txt = "Hello World"[::-1]

print(txt)
#####################################


#####  ONE LINE IF & ELSE in PRINT #####
variable=0
condition=1
print ('something' if variable == condition else "some other thing")
##### #####################################                 


#### Different ways to print ####
a=1
b=2
c=3
print('%02d:%02d:%02d'%(a,b,c))
print('{0}:{1}:{2}'.format(a,b,c))
print(a,b,c,sep=':')

######################################################

### round ###

a=1.23
b=1.234
c=1.2346
print(round(a,1)) # decimal 1th
print(round(b,2)) # decimal 2nd
print(round(c,3)) # decimal 3rd


## How to get LIST with Int  as input ##

lst=list(map(int,input().strip().split()))

##############################################

## Make code Faster with Bigger Num ##

import sys
a= int(sys.stdin.readline())

#################################################