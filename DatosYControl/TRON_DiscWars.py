from random import randint
import os
# ---------------------------- TRON: Disc Wars
_StartMessage = "\nTRON: Disc Wars"
print(_StartMessage)

# ---------------------------- Clear terminal
input("\nPress ENTER to start ")
os.system('clear')

# ---------------------------- Life
# Sam Flynn
_SamFlynn_StartLife = 80
_SamFlynn_Life = 80
_SamFlynn_BarLifePercentage = _SamFlynn_Life / _SamFlynn_StartLife
_SamFlynn_BarLife = "Sam Flynn's life [" + (round((_SamFlynn_BarLifePercentage * 10)) * '⣿') + '] ' + str(_SamFlynn_BarLifePercentage * 100) # Life Bar for printing
# Rinzler
_Rinzler_StartLife = 90
_Rinzler_Life = 90
_Rinzler_BarLifePercentage = _Rinzler_Life / _Rinzler_StartLife
_Rinzler_BarLife = "Rinzler's life [" + (round((_Rinzler_BarLifePercentage * 10)) * '⣿') + '] ' + str(_Rinzler_BarLifePercentage * 100) # Life Bar for printing

# ---------------------------- While
while _SamFlynn_Life > 0 and _Rinzler_Life > 0:
    # Combat by turns
    # ---------------------------- Sam Flynn's turn
    print("\n" + "Sam Flynn's turn")
    _SamFlynn_BarLifePercentage = _SamFlynn_Life / _SamFlynn_StartLife
    _SamFlynn_BarLife = "Sam Flynn's life [" + (round((_SamFlynn_BarLifePercentage * 10)) * '⣿') + '] ' + str(_SamFlynn_BarLifePercentage * 100) # Print Life Bar
    print(_SamFlynn_BarLife)
    _SamFlynn_Attack = randint(0, 1)
    if _SamFlynn_Attack == 0:
        # Bouncing
        print("Sam Flynn attacks bouncing")
        _Rinzler_Life -= 10
    else:
        # Floor
        print("Sam Flynn attacks the floor")
        _Rinzler_Life -= 11
    _Rinzler_BarLifePercentage = _Rinzler_Life / _Rinzler_StartLife
    _Rinzler_BarLife = "Rinzler's life [" + (round((_Rinzler_BarLifePercentage * 10)) * '⣿') + '] ' + str(_Rinzler_BarLifePercentage * 100) # Print Life Bar
    print(_Rinzler_BarLife)

    # ---------------------------- Rinzler's turn
    print("\n" + "Rinzler's turn")
    _Rinzler_Attack = None
    while _Rinzler_Attack not in [0, 1, 2, 3]:
        _Rinzler_Attack = int(input("Which attack do you want to perform?\n"
                                "0 - Tackle\n"
                                "1 - Floor\n"
                                "2 - Direct\n"
                                "3 - Nothing\n"
                                "\n"
                                ">> Answer [0/1/2/3]: "))
        os.system('clear')
    if _Rinzler_Attack == 0:
        _SamFlynn_Life -= 10
        print("\n Rinzler attacks with Tackle")
    elif _Rinzler_Attack == 1:
        _SamFlynn_Life -= 11
        print("\nRinzler attacks the Floor")
    elif _Rinzler_Attack == 3:
        print("\nRinzler does Nothing")
    else:
        _SamFlynn_Life -= 12
        print("\n Rinzler attacks Direct")
    _SamFlynn_BarLifePercentage = _SamFlynn_Life / _SamFlynn_StartLife
    if _SamFlynn_BarLifePercentage < 0:
        _SamFlynn_BarLifePercentage = 0
        print("Enters where I want")
    elif _Rinzler_BarLifePercentage < 0:
        _Rinzler_BarLifePercentage = 0
        print("Enters where I want")
    _SamFlynn_BarLife = "Sam Flynn's life [" + (round((_SamFlynn_BarLifePercentage * 10)) * '⣿') + '] ' + str(_SamFlynn_BarLifePercentage * 100) # Print Life Bar
    print(_SamFlynn_BarLife)
    _Rinzler_BarLifePercentage = _Rinzler_Life / _Rinzler_StartLife
    _Rinzler_BarLife = "Rinzler's life [" + (round((_Rinzler_BarLifePercentage * 10)) * '⣿') + '] ' + str(_Rinzler_BarLifePercentage * 100) # Print Life Bar
    print(_Rinzler_BarLife)

if _SamFlynn_Life > _Rinzler_Life:
    print("\nPikachu won")
else:
    print("\nSquirtle won")
