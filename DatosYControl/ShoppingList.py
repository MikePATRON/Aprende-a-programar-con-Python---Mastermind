# Shopping List

# ---------- Import libraries
import os

# ---------- Clear Terminal
os.system("clear")

# ---------- Start message
print("\nThis is a Shopping List Program")

# ---------- List
_ShoppingList = []

# ---------- Bucle to add and check the List
while True:
    _QuestionMessage = input("\nWhat do you want to buy? ([Q] to exit)\n >> ")
    if _QuestionMessage not in _ShoppingList and _QuestionMessage != "Q":
        if input("\nAre you sure you want to buy {}? [Y/N]\n >> ".format(_QuestionMessage)) == "Y":
            _ShoppingList.append(_QuestionMessage)
    elif _QuestionMessage == "Q":
        break
    else:
        print("You already have [{}]".format(_QuestionMessage))

# ---------- End program
os.system("clear")
print("\nThis is your Shopping List: {}".format(_ShoppingList))
