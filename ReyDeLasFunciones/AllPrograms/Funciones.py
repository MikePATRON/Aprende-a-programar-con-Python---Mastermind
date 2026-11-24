# Functions
# ---------- Libraries
import os
# ---------- Clear Terminal
os.system("clear")
# ---------- Define Function
def _SectGreeting(_Name):
    print("\nHello '{}'".format(_Name[::-1]))
def _LenName(_LenName):
    _Len = 0
    for _X in _LenName:
        _Len += 1
    return _Len
# ---------- Execute Function
_EnterName = input("What is your name?\n >> ")
_SectGreeting(_EnterName)
_LenNameUser = _LenName(_EnterName)
print(str(_LenNameUser)*3)
