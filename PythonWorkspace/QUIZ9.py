class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[Chicken Left:{0}] ".format(chicken))
        order = int(input("How many chickens would you like to order? :"))
        if order > chicken:
            print("Not enough chicken")
        elif order<=0:
            raise ValueError
        else:
            print("[Waiting number {0}] {1} chickens order is completed".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError


    except ValueError:
        print("Wrong input typed")

    except SoldOutError:
        print("Soldout, No more order can be accepted")
        break