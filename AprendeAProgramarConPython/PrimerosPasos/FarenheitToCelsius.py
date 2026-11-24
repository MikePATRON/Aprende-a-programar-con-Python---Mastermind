# Corriendo tu primer programa

# We create a program to convert Farenheit to Celsius
print('Welcome to this unit converter program')
# Formula1: (1° * 9/5) + 32
celsius = float(input('Give me the temperature in Celsius: '))
formula1_temperature = (celsius * 9/5) + 32
print('This is your temperature in Farenheit: {}'.format(formula1_temperature))

# Formula2: (1°F − 32) × 5/9
farenheit = float(input('Give me the temperature in Farenheit: '))
formula2_temperature = (farenheit - 32) * 5/9
print('This is your temperature in Celsius: {}'.format(formula2_temperature))
