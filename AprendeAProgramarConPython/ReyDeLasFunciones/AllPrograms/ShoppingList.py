# Shopping List
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- ---------- Main Code
# ---------- Ask again and Again
def _AskUser():
    return (input("\nWhat product do you want to buy? [Exit/List]\n >> ")).upper()
# ---------- Open and Edit File
def _SaveAndEdittFile(_ShoppingList_User):
    with open("ShoppingList.txt", "w") as _Archive:
        _Archive.write("\n".join(_ShoppingList_User))
    print("\nThis is your final list:")
    for _X in _ShoppingList_User:
        print(" >> {}".format(_X))
 # ---------- Main Function
_ShoppingList_User = []
def _Function():
    _ShoppingList = ["MILK", "EGGS", "BREAD", "CHICKEN", "RISE"]
    _InputUser = _AskUser()
    while _InputUser != "EXIT":
        if _InputUser in _ShoppingList and _InputUser not in _ShoppingList_User:
            _ShoppingList_User.append(_InputUser)
        elif _InputUser == "LIST":
            print("\nThis is what you can buy: {}".format(_ShoppingList))
        _InputUser = _AskUser()
    if _InputUser == "EXIT":
        _SaveAndEdittFile(_ShoppingList_User)
# ---------- Load File
def _LoadFile():
    _ShoppingList_User = []
    if (input("\nDo you want to open your last Shopping List? [Y/N]\n >> ")).upper() == "Y":
        try:
            with open("ShoppingList.txt", "r") as _Archive:
                _ShoppingList_User = _Archive.read().split("\n")
                print("This is your previous file: {}".format(_ShoppingList_User))
        except FileNotFoundError:
            print("\nShopping List file not found")
    return _ShoppingList_User
# ---------- Run the program
def _Main():
    _ShoppingList_User = _LoadFile()
    _Function()
if __name__ == "__main__":
    _Main()
