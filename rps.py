import random

computer_score = 0
human_score = 0
game_over = False
turns = ['rock', 'paper', 'scissors']

while not game_over:
    computer_turn = random.choice(turns)
    human_turn = input('Enter your turn: ')
    if human_turn == 'enough':
        print(computer_score, "vs.", human_score)
        exit()
    if not human_turn in turns:
        exit()

    print(computer_turn, 'vs.', human_turn)
    if computer_turn == human_turn:
        print('Tie')
    elif computer_turn == 'rock' and human_turn == 'paper':
        human_score += 1
        print('Human wins')
    elif computer_turn == 'paper' and human_turn == 'scissors':
        human_score += 1
        print('Human wins')
    elif computer_turn == 'scissors' and human_turn == 'rock':
        human_score += 1
        print('Human wins')
    else:
        computer_score += 1
        print('Computer wins')

    print(computer_score, "vs.", human_score)
    if computer_score == 3:
        print('Machines won the battle!')
        exit()
    if human_score == 3:
        print('You saved Humanity!')
        exit()