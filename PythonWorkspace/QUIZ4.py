from random import *


comment = range(1,21) # generate 1~20
comment =list(comment)
print(comment)
shuffle(comment)
print(comment)

winners = sample(comment,4)

print(" -- Winner Announcement -- " )
print(" Chicken winner is : {0}".format(winners[0]))
print(" Coffee winner is : {0}".format(winners[1:]))
print(" -- Congratulations! --")


