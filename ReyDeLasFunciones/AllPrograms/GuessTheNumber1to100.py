# Experiment with Functions
# ---------- Libraries
import os, random
# ---------- Clean terminal
os.system("clear")
# ---------- Main Code
def _GuessTheNumber1to100():
    _AskUser = int(input("\nGuess the number from 1 to 100\n >> "))
    _RandomNumer = random.randint(1, 10)
    while _AskUser != _RandomNumer:
        if _AskUser == _RandomNumer:
            print("\nYou guessed the number")
            break
        else:
            _AskUser = int(input("\nGuess the number from 1 to 100\n >> "))
# ---------- Run the program
def _Main():
    _GuessTheNumber1to100()
if __name__ == "__main__":
    _Main()
