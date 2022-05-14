import random
from names import names
from letter_by_letter_print import slow_print

## initial variables
money = 0
inventory=[]
setting=''

# class section
class player:
    
    def __init__ (self, name, age, job, hp, attack):
        self.name= name
        self.age= age
        self.job= job
        self.hp= hp
        self.attack= attack

    def self (name):
        print('my name is ' + name)

class weapon:
    
    def __init__ (self, name, damage, crit):
        self.name= name
        self.damage= damage
        self.crit= crit
    
    
class monster:
    
    def __init__(self, name, hp, damage, crit):
        self.name= name
        self.hp= hp
        self.damage= damage
        self.crit= crit
        slow_print("{0} Monster appeared!".format(self.name))
        

## Basic greeting
slow_print("##################\n")
slow_print("WELCOME to TXT RPG\n")
slow_print("##################\n")

    
##check if setting is correct
while setting !='m' and setting !='r':
    setting = input('We need to set your Name, Age, and Class. \nPlease select game basic setting mode (r for random setting, m for manual setting): ')
    
## Gather Player's basic info

if setting == 'm':
    name = input('Please type your name: ')
    age = input('Okay, Hello '+ name + " what is your age?: ")
    job = input('Lastly, What is your class? (h for hero, v for Villain): ').lower()
    while job!='h' and job!='v':
        job= input("ERROR: please type 'h' or 'v' for class: ")
    
    print ('Your name: ' + name + '\nage: ' + str(age) + ' \nclass: ' +job+ '(Hero)')
       
if setting =='r':
    job_list= ['h', 'v']
    name = random.choice(names)
    age = random.randint(1,101)
    job = random.choice(job_list)

    if job == 'h':
        print ('Your name: ' + name + '\nage: ' + str(age) + ' \nclass: ' +job+ '(Hero)')
    else:
        print ('Your name: ' + name + '\nage: ' + str(age) + ' \nclass: ' +job+ '(Villain)')


# Adventure start





# Monster created
m1 = monster("slime",10,5,0.05)


    
# check class player
# print(user.name)
# print(user.age)
# print(user.job)
