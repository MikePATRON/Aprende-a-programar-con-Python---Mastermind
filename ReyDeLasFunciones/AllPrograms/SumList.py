# Crea una función que sume una lista de números, no se vale usar la función sum()
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
_NumList = [1, 2, 3, 4, 5]
print("This is the list: {}\n".format(_NumList))
def _SumList():
    _Result = 0
    for _X in _NumList:
        print("This is the operation: {} + {}".format(_Result, _X))
        _Result += _X
    print("\nThis is the final result = {}".format(_Result))
# ---------- Run the program
def _Main():
    _SumList()
if __name__ == "__main__":
    _Main()
