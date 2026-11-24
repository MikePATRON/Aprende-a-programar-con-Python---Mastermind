# Cheese test

welcome_text = 'Welcome to the cheese test\n'
print('\n' + welcome_text + '-' * len(welcome_text) + '\n')

result = 0

# Question 1
option1 = input('\n'
                'Question 1: What do you do when you see a cheese board?\n'
                'A - I run away\n'
                'B - I eat at least one\n'
                'C - I can not stop eating them\n'
                '\n'
                'Answer (A/B/C): ')

if option1 == 'A':
    result += 0
elif option1 == 'B':
    result += 5
elif option1 == 'C':
    result += 10
else:
    print("You didn't chose an option (A/B/C)")

# Question 2
option2 = input('\n'
                'Question 2: How do you like Hamburguer?\n'
                'A - Without cheese\n'
                'B - With cheese\n'
                'C - Only breath and cheese\n'
                '\n'
                'Answer (A/B/C): ')

if option2 == 'A':
    result += 0
elif option2 == 'B':
    result += 5
elif option2 == 'C':
    result += 10
else:
    print("You didn't chose an option (A/B/C)")

# Question 3
option3 = input('\n'
                'Question 3: Are you lactose intolerant?\n'
                'A - Yes\n'
                'B - Some times\n'
                'C - No\n'
                '\n'
                'Answer (A/B/C): ')

if option3 == 'A':
    result += 0
elif option3 == 'B':
    result += 5
elif option3 == 'C':
    result += 10
else:
    print("You didn't chose an option (A/B/C)")

# Final Result
print('')
if result >= 25:
    print('Result: Congratulations! you are a cheese fan')
elif result >= 15:
    print('Result: You are a normal person')
else:
    print('Result: You do not like cheese')
