import random

def play():
    user = input("What is your choice??\n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f"computer choice was {computer}")
    while user == 'r' or 'p' or 's':

        if user == computer:
            return 'It\'s a tie'
        
        if is_win(user,computer):
            return 'You won!'

        if is_lost(user,computer):
            return 'you lost :('   
    else:
        print("Please put right input..")
        



def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True

def is_lost(player,opponent):
    if (player == 's' and opponent == 'r') or (player =='p' and opponent == 's') or (player == 'r' and opponent =='p'):
        return True

print(play())