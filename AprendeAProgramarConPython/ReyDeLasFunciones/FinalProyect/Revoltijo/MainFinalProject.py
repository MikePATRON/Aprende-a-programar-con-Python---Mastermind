# ---------- Main
# Instructions
_Instructions = """
For each Pokemon:
 - Name
 - Current Health
 - Base Health
 - Level
 - Current Exp

Write a .txt file with all the pokemons
"""
# ---------- Libraries
from PySide6 import QtWidgets # Qt Python GUI
import sys # Needed for Qt
import os
from EngineAudio import _Engine_Speak
from PokemonLoads import _Main_PokemonLoads
# ---------- Variables
# ---------- Functions
def _ClearTerminal_SavePosition(_Behavior):
    if _Behavior == 0:
        print("\033[s", end="") # Save start position
    elif _Behavior == 1:
        print("\033[u", end="") # jump back to start
        print("\033[J", end="") # wipe everything below
# ---------- Main Function
def _MainFinalProyect():
    _Engine_Speak("Running Main Program", _Prints = True)
    #_ClearTerminal_SavePosition(0), _Main_PokemonLoads(), _ClearTerminal_SavePosition(1)
    _Main_PokemonLoads(False)
    _Engine_Speak("Program done")
# ---------- Run Program
if __name__ == "__main__":
    os.system("clear") # Clear terminal
    print("\033[H\033[2J\033[3J", end = "") # Clear terminal for Kitty
    print("MAIN PROGRAM")
    _MainFinalProyect()
