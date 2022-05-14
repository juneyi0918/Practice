# Quiz) You are a taxi driver, you have 50 chances to match with customer. 
# Make program how many customer you can match.

# Rule 1: Customer use taxi for 5~50 mins ( randomly generated )
# Rule 2: you only can match with 5~15 mins 

# Printed Example 
# [0] #1 customer (use time: 15 mins)
# [ ] #2 customer (use time: 50 mins)
# [0] #3 customer (use time: 5 mins)
# ...
# [ ] #50 customer (use time: 16 mins)

# Total customer : 2 person

from random import *

customer = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5<=time<=15:
        print("[O] #{0} customer (use time: {1} mins)".format(i,time))
        customer += 1
    else:
        print("[ ] #{0} customer (use time: {1} mins)".format(i,time))
        
print ("\nTotal customer : {0} person".format(customer))