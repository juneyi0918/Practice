class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("Hp {0}, Damage {1}".format(self.hp,self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35) 
wraith1 = Unit("Wraith", 80, 5)
print("Unit name : {0}, Damage : {1}".format(wraith1.name, wraith1.damage))
wraith2 = Unit("Stole Wraith", 80 ,5)
wraith2.cloaking = True       ## you can add .something outside class
if wraith2.cloaking == True:
    print("{0} is now cloaking.".format(wraith2.name))

