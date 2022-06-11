import random
possible_actions = ["rock", "paper", "scissors"]

print('''\n\n========ROCK - PAPER - SCISSORS GAME========
MOVES : 'R' ==> ROCK  'P' ==> PAPER  'S' ==> SCISSORS
*********************************************
''')

def get_user_selection():
    user_input = input('Enter Your Move: ').lower()
    if user_input == 'r':
        user_input = 'rock'
    elif user_input == 'p':
        user_input = 'paper'
    elif user_input == 's':
        user_input = 'scissors'
    return user_input.lower()

def get_cpu_action():
    computer_action = random.choice(possible_actions)
    return computer_action.lower()


def decide_winner(user_action, cpu_action):
    if user_action == cpu_action:
        print('\n*****<< It is a tie >>*****')
    elif user_action == 'rock':
        if cpu_action == 'scissors':
            print('\n*****<< You Win >>***** \nROCK SMASHES SCISSORS!')
        else:
            print('\n*****<< CPU Wins >>***** \nPAPER COVERS ROCK!')
    elif user_action == 'scissors':
        if cpu_action == 'paper':
            print('\n*****<< You Lose >>***** \nSCISSORS CUTS PAPER!')
        else:
            print('\n*****<< CPU Wins >>***** \nROCK SMASHES SCISSORS!')
    elif user_action == 'paper':
        if cpu_action == 'rock':
            print('\n*****<< You Win >>***** \nPAPER COVERS ROCK!')
        else:
            print('\n*****<< You Lose >>***** \nSCISSORS CUTS PAPER!')

def check_validity():
    if user_action not in possible_actions:
        print('Please choose a valid option!')
        return False
    elif user_action in possible_actions:
        return True

while True:
    user_action = get_user_selection()

    if check_validity() == True:
        
        cpu_action = get_cpu_action()
        #print('\tCPU MOVE: ', cpu_action.lower())
        print(f'User({user_action.capitalize()}) : CPU({cpu_action.capitalize()})')
        decide_winner(user_action, cpu_action)
        break
    else:
        continue
print('''
===============ENF OF THIS ROUND=====================            
            ''')