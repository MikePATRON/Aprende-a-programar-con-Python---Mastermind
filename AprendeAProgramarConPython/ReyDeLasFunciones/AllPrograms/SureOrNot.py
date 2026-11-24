# Crea una función que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False" dependiendo de si el usuario está seguro.
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
def _AreYouSureOrNot(_AswerUser):
    if _AswerUser == "Y":
        _Result = True
    elif _AswerUser == "N":
        _Result = False
    else:
        _Result = "You didn't choose an option"
    print(_Result)
# ---------- Run the program
def _Main():
    _AskUser = input("\nAre you sure or not? [Y/N]\n >> ")
    _AskUser = _AskUser.upper()
    _AreYouSureOrNot(_AskUser)
if __name__ == "__main__":
    _Main()
