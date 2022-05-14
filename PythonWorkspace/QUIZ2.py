
# You recnetly make coding study group.
# There are 4 studies in a month which is 3 online study and 1 offline 
# Make program that generate offline date meeting rules below

#Rule 1: Date should be generated random
#Rule 2: Use least available month date which is 28
#Rule 3: Every month 1~3 date can't be study day because of preparing study
# Example print statement "Offline study date is selected as  x date"


from random import *

random_date1 = randint(4,28)
random_date2 = randint(4,28)
random_date3 = randint(4,28)

print("Offline study date is selected as day " + str(random_date1))

