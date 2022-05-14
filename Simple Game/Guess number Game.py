import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    user_guess = 0 
    while guess!= random_number:
        user_guess += 1
        guess = int(input(f"Guess number between 1 and {x}:    "))
        print(guess)
        
        if guess < random_number:
            print("your guess is smaller than answer")

        elif guess > random_number:
            print("your guess is higher than answer")

    print("you got it right! you guessed right in {0} times".format(user_guess))
    return user_guess

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    computer_guess_number = 0

    while feedback != 'c':
        computer_guess_number += 1
        if low != high:
            guess =random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?? '.lower())

        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
     
    
    print (f'Computer guessed your number correctly in {computer_guess_number} times which is {guess}')
    return computer_guess_number


x = int(input("put max number you want to set: "))

user_score = guess (x)
computer_score = computer_guess(x)

if user_score < computer_score:
    print("user tried  = {0}   VS  computer tried = {1} \nYAY! I won computer!!!!".format(user_score,computer_score))
elif user_score == computer_score:
    print("user tried  = {0}   VS  computer tried = {1} \nUser & computer tied".format(user_score,computer_score))
else:
    print("user tried  = {0}   VS  computer tried = {1} \nUser lost...".format(user_score,computer_score))


