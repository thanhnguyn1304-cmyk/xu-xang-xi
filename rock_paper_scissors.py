import random

options = ('rock', 'paper', 'scissors')

def player_choice():
    a = input("Choose rock, paper, scissors : ")
    return a
def computer_choice():
    return random.choice(options)

def decidewinner(player,computer):
    if player not in options:
        return 'Invalid choice'
    print('Player chose : ' + player )
    print('PC chose : ' + computer)
    if player not in options:
        return 'Invalid choice'
    elif player == computer :
        return "It's a draw"
    elif player == 'rock' and computer== 'scissors':
        return 'You have Won'
    elif player == 'scissors' and computer == 'paper':
        return 'You have Won'
    elif player == 'paper' and computer == 'rock':
        return 'You have Won'
    else:
        return 'You have Lost'

def play_game():
    result = ''
    round = 1
    round_win = 0
    
    while True:
        print(f'Round number {round}, History of your wins: {round_win}')
        result = decidewinner(player_choice(),computer_choice())

        print(result)
        round+=1
        round_win += 1 if result == 'You have Won' else 0
        #if result == 'You have Won':
            ##break

play_game()
