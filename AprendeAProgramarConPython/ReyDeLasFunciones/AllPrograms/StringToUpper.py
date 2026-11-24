# Crea una función que convierta toda una string en mayúsculas, no vale usar el método upper()
# Experiment with Functions
# ---------- Libraries
import os, string
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
# ---------- List for Upper and Lower
_LowerCase = (string.ascii_lowercase)
_LowerCaseList = []
for _X in _LowerCase:
    _LowerCaseList.append(_X)
_UpperCase = string.ascii_uppercase
_UpperCaseList = []
for _X in _UpperCase:
    _UpperCaseList.append(_X)
# ---------- Function
def _StringToUpper(_StringUser):
    _UserText = ""
    for _X in _StringUser:
        if _X in _UpperCaseList:
            _UserText += str(_X)
        elif _X in _LowerCaseList:
            _Position = _LowerCaseList.index(_X)
            _GetUpper = _UpperCaseList[_Position]
            _UserText += str(_GetUpper)
        else:
            _UserText += str(_X)
    print("\nThis is the final result without .upper(): \n >> {}".format(_UserText))
# ---------- Run the program
def _Main():
    _StringUser = input("\nWhat string do you want to conver to Upper?\n >> ")
    _StringToUpper(_StringUser)
if __name__ == "__main__":
    _Main()
