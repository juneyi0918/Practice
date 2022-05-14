
try:
    print("This is Division Calculator")
    nums=[]
    nums.append(int(input("Please enter first number : ")))
    nums.append(int(input("Please enter second number : ")))
    nums.append(int(nums[0]/ nums[1]))
    print("{0} divide by {1} is {2}".format(nums[0], nums[1], float(nums[2]) ))
except ValueError:
    print("There is Error [Wrong input]")
except ZeroDivisionError as err:
    print(err)
except:
    print("Unkown Error!")
    

