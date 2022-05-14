## Custom Error
class BigNumberError(Exception):
    def __init__ (self,msg):
        self.msg =msg

    def __str__(self):
        return self.msg     




try:
    print("This is One digit only Calculator")
    num1 =int(input("Type First number: "))
    num2 =int(input("Type Second number: "))
    if num1 >=10 or num2 >=10:
        raise BigNumberError("Typed Input: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))
except BigNumberError as err:
    print("Wrong input. Please use one digit number")
    print(err)
finally:
    print("Thank you for using this calculator")
    