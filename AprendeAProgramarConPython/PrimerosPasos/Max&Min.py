# I ask the user to enter the values, but I change them to int() so that I can analyze them
num_1 = int(input('Enter the value 1: '))
num_2 = int(input('Enter the value 2: '))
num_3 = int(input('Enter the value 3: '))

# Message for the user
print('''
      This is my process''')
# I analyze each value to find max() and min()
max_value = max(num_1, num_2, num_3)
min_value = min(num_1, num_2, num_3)

# I print the values by changing them to str() so that I can print them with text
print('This is your max value: ' + str(max_value))
print('This is your min value: ' + str(min_value))

# Message for the user
print('''
      This is Nate's process''')

# Print everything with one line
print('El número más grande entre {}, {} y {} es: {}, y el más pequeño es: {}'.format(num_1, num_2, num_3,
max(num_1, num_2, num_3),
min(num_1, num_2, num_3)))