# Crea una función que te de True como resultado si el número pasado como argumento es impar
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
def _EvenOrOdd(_NumerEvenOrOdd):
    _Result = _NumerEvenOrOdd % 2
    if _Result == 1:
        print("\nYour number is Odd")
    else:
        print("\nYour number is Even")
# ---------- Run the program
def _Main():
    _NumerUser = int(input("\nWhat number do you want to know?\n >> "))
    _EvenOrOdd(_NumerUser)
if __name__ == "__main__":
    _Main()
