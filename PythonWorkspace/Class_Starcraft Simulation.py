from random import*

# Normal Unit
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed 
        print("{0} Unit is created.".format(self.name))

    def move(self, location):
        print("{0} : Move to {1} direction. [Speed: {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} damage taken.".format(self.name, damage))
        self.hp -= damage
        print("{0} : Current health is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : Destroyed.".format(self.name))

      

# Attacking Unit 
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self,location):
        print("{0} : Attack enemy on {1} direction [Damage: {2}]".format(self.name, location, self.damage))

# Marine

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)
    
    # stimpack effect : speed and attack_speed up, decrease health by 10
    def stimpack(self):
        if self.hp > 10:
            self.hp -=10
            print("{0}: Stimpack used. [HP decreased by 10]".format(self.name))
        else: 
            print("{0}: Not enough HP. [Stimpack CAN'T be used]".format(self.name))


# Tank

class Tank(AttackUnit):

    seize_developed = False # seize mode is not devloped initally 

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0}: Transform to seize mode.".format(self.name))
            self.damage *= 2
            self.seize_mode = True

        else: 
            print("{0}: Transform to tank mode.".format(self.name))
            self.damage /= 2
            self.seize_mode = False



            
# Flyunit 
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : Fly over {1} direction. [Speed: {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)



# Wraith

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.cloacked = False
    
    def cloacking(self):
        if self.cloacked == False:
            print("{0} : Cloaking is activated.".format(self.name))
            self.cloacked = True
        else :
            print("{0} : Cloaking is deactivated.".format(self.name))
            self.cloacked = False


def game_start():
    print("Game Start!")


def game_end():
    print("Player : gg")
    print("[Player] left game.")




### Game Simulation Start ###

game_start()

# create 3 marine
m1 = Marine()
m2 = Marine()
m3 = Marine()

# create 2 tank
t1 = Tank()
t2 = Tank()

# create 1 wraith
w1 = Wraith()

# Unit control
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# move All unit
for unit in attack_units:
    unit.move("North")

# upgrade seize mode
Tank.seize_developed = True
print("Tank Seize Mode is Upgraded")


# prepare Attack (marine-> stimpack, tank->seize mode, wraith ->cloaking)

for unit in attack_units: 
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloacking()

# Attack All

for unit in attack_units:
    unit.attack("North")

# All Damaged

for unit in attack_units:
    unit.damaged(randint(50,500))  # get some random damage 5~20

# Game is Done 

game_end()





# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

