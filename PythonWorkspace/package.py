# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage() 
# trip_to.detail()

from travel import *
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))
print(inspect.getfile(inspect))


