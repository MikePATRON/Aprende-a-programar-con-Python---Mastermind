# Crea una función que reciba una lista de strings como entrada y te diga cual es la más larga de todas
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
_StringUser = input("\nWhat String do you want to messure?\n >> ")
_TheLongestString_List = _StringUser.split(" ")
def _TheLongestString():
    _Result = max(_TheLongestString_List, key = len)
    print("\nThis is the list: {}".format(_TheLongestString_List))
    print("This is the longest string: '{}'".format(_Result))
# ---------- Run the program
def _Main():
    _TheLongestString()
if __name__ == "__main__":
    _Main()
