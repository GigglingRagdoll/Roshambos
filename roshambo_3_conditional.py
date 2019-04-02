from random import randint

pretty = {
    0 : 'rock',
    1 : 'scissors',
    2 : 'paper'
}
player = int(input('0 for rock\n1 for scissors\n2 for paper\n>>> '))
com = randint(0, 2)

print('You played {}!'.format(pretty[player]))
print('COM played {}!'.format(pretty[com]))

if (player + 1) % 3 == com:
    print('You win!')
elif (com + 1) % 3 == player:
    print('You lose!')
else:
    print('Draw!')