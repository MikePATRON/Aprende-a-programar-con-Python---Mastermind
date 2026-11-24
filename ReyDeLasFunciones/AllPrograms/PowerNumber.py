# Crea un programa que contenga una función que calcule la potencia de un numero introducido como argumento
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
def _Main(_Number):
    _Result_Numer = _Number ** 2
    return _Result_Numer
# ---------- Run the program
if __name__ == "__main__":
    print(_Main(float(input("\nInsert a number\n >> "))))
