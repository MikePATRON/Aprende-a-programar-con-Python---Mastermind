# Exercise For

# ---------- Libraries
import os

# ----------Clear terminal
os.system("clear")

# ---------- Program
print("\nThis program creates a Multiplication Table")
_NumberUser = int(input("What number do you want to use for your Multiplication Table?\n>> "))
print("")
_ListValues = []
for _x in range(1, 11):
    if ((_NumberUser * _x) % 2) == 0:
        _ListValues.append(_NumberUser * _x)
    print("{}*{} = {}".format(_NumberUser, _x, _NumberUser * _x))
print("\nThese are the multiples of 2: {}".format(_ListValues))
