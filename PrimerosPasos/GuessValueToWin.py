# The user needs to guess the number

# Import library 'random'
import random
variable = random.randint(1, 10)

ask_user = int(input('Guess the number from 1 to 10: '))
if ask_user == variable:
    print('Congratulations! you have won')
if ask_user != variable:
    print('You are a loser. The correct number was {}'.format(variable))
print('End')
