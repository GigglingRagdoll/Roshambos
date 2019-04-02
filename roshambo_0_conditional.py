from random import randint

pretty = {
    0 : 'rock',
    1 : 'scissors',
    2 : 'paper'
}
outcomes = ['You win!','Draw!','You lose!']

player = int(input('0 for rock\n1 for scissors\n2 for paper\n>>> '))
com = randint(0, 2)

print('You played {}!'.format(pretty[player]))
print('COM played {}!'.format(pretty[com]))
# equation gives 0 when you win, 1 when you draw, and -1 when you lose
print(outcomes[((player + 1) % 3) - com])
