# Currency converter

# Welcome message print
_welcome_message = '\nWelcome to the Euro currency converter\n'
print(_welcome_message + '-' * len(_welcome_message))

# Currencies
_dolar_euro = 0.91
_pound_euro = 1.18

# User choose an option
_option = input('\n'
               'Choose a currency:\n'
               'A - Convert Dolar to Euro\n'
               'B - Convert Pound to Euro\n'
               'C - Convert Euro to Dolar\n'
               'D - Convert Euro to Pound\n'
               '\n'
               'Answer (A/B/C/D): ')
print('')

# Money User
_money = 0
_text_user = "How many {} do you have?\n>> "
# Options
if _option == 'A':
    _user_dolar = float(input(_text_user.format('Dolars')))
    _money = _dolar_euro * _user_dolar
    _currency = 'Euros'
elif _option == 'B':
    _user_pound = float(input(_text_user.format('Pounds')))
    _money = _pound_euro * _user_pound
    _currency = 'Euros'
elif _option == 'C':
    _user_euro = float(input(_text_user.format('Euros')))
    _money = _user_euro / _dolar_euro
    _currency = 'Dolars'
elif _option == 'D':
    _user_euro = float(input(_text_user.format('Euros')))
    _money = _user_euro / _pound_euro
    _currency = 'Pounds'
else:
    print("You didn't choose an option")

# Result
_money = round(_money, 2)
print('\nYou can have {} {}'.format(_money, _currency))