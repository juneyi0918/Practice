gun = 10

# def checkpoint(soldiers):
#     global gun # Global let use Global variable instead of local
#     gun = gun -soldiers
#     print("[In the function] left over gun: {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[In the function] left over gun: {0}".format(gun))
    return gun

print("Total gun: {0}".format(gun))
gun=checkpoint_ret(gun,2)
print("Left  gun: {0}".format(gun))

