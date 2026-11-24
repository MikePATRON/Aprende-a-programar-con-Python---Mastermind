# Test while

# Variable without value "None"
_answer = None

# Bucle while
while _answer != 'A' and _answer != 'B' and _answer != 'C':
    _answer = input('Choose an option [A/B/C]: ')
    print("You didn't choose an option")

# Conditional if
if _answer  == 'A':
    print('Great answer')
elif _answer == 'B':
    print('Good answer')
else:
    print('Wrong answer')
