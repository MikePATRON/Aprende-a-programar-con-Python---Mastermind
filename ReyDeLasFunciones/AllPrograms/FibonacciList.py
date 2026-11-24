# Experiment with Functions
# ---------- Libraries
import os
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
def _Fibonacci(_NumerFibonacci):
    if _NumerFibonacci <= 1:
        return 1
    return _Fibonacci(_NumerFibonacci - 1) + _Fibonacci(_NumerFibonacci - 2)
# ---------- Run the program
def _Main():
    for _Counter in range(10):
        print(_Fibonacci(_Counter))
if __name__ == "__main__":
    _Main()
