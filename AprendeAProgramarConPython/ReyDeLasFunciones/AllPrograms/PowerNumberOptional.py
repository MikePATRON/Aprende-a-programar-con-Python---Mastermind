# Crea una función para calcular la potencia de un número, la función tendrá un parametro opcional que será la base de la potencia,\
#  si no se especifica ninguna base, la base será 2.
# ---------- Libraries
import os # Import Terminal Commands
# ---------- Clean terminal
os.system("clear") # Clear Terminal for Linux
# ---------- Main Code
def _Potencia(_Numero, _Base = 2):
    return _Numero ** _Base
# ---------- Run the program
def _Main():
    print(_Potencia(4))
    print(_Potencia(4, 5))
if __name__ == "__main__":
    _Main()
