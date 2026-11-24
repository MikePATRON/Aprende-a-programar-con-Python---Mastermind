age = int(input('How old are you? '))
card_type = input('What special card do you have? (S - Student / P - Pensioner / B - Big family / N - None): ')

if (25 <= age <= 35 and card_type == 'S') \
        or (age <= 10) \
        or (age >= 65 and card_type == 'P') \
        or (card_type == 'B'):
    print('You have discount')
else:
    print("You don't have discount")
