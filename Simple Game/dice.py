import random
import time

user_input =''
while user_input != 'q':
    ran = random.randint(1,7)
    print('rolling dice')
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print(ran)
    user_input=input('Do you wan to quit(q)? or roll one more time(enter)?: ')
    
