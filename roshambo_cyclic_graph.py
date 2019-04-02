from random import choice

cycle = {
    'rock' : 'scissors',
    'scissors' : 'paper',
    'paper' : 'rock'
}
player = input('Roshambo!\n(rock/scissors/paper) >>> ')
com = choice(list(cycle.keys())) # or .values() works the same

print('You played {}'.format(player))
print('COM played {}'.format(com))

if cycle[player] == com:
    print('You win!')
elif cycle[com] == player:
    print('You lose!')
else:
    print('Draw!')