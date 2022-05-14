# empty space leave it as empty, right side, 10 space total
print("{0: >10}".format(500))

# Positive number as + , Negatieve number as -
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# Left side, empty space as _
print("{0:_<+10}".format(500))

# Adding , for every 3rd number
print("{0:,}".format(123456789))
print("{0:+,}".format(123456789))
print("{0:+,}".format(-123456789))
print("{0:^<+30,}".format(10000000000))

#Print Float 
print("{0:f}".format(5/3))
#Print Float with rounding
print("{0:.2f}".format(5/3))

