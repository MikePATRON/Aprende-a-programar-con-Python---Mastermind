# Guess The Best Price - Main Program
# ---------- Libraries
import os
from time import sleep
from PIL import Image
# ---------- Files
from EngineAudio import _Engine_Speak, _Engine_VoiceRecognizer
from EngineWebSite import _Engine_WebSite
# ---------- Variables
_WebSite = "https://www.porsche.com/mexico/"
# ---------- Functions
def _ClearTerminal():
    print("Clear Terminal with Function")
    os.system("clear")
def _Wait(_WaitingTime):
    _Timer = 0
    print(f"Waiting {_WaitingTime} second", end = "")
    if _WaitingTime != 1:
        print("s:", end = " ")
    else:
        print(":", end = " ")
    while _Timer < _WaitingTime:
        _Timer += 0.5
        sleep(0.5)
        if _Timer != _WaitingTime:
            print(_Timer, end = ", ")
        else:
            print(f"{_Timer}. Timer done")
    print("\033[1A\033[2K", end="")
# ---------- Main Program
def _MainProgram(_WebSite):
    print("\nRunning 'Main' Program\n")
    _Wait(1)
    _Engine_Speak("Hello! Welcome to Get The Price program. We are going to guess the price of some cars", True)
    _DictionaryValues = _Engine_WebSite(_WebSite, False)
    _Engine_Speak(f"The dealer is: '{_DictionaryValues.get('_WebSite_Title')}'", True)
    _Engine_Speak("I found this models:", True)
    _Cars = _DictionaryValues.get("_Cars")
    for _Car in _Cars:
        _Engine_Speak(f" > {_Car}", True)
    _SubModel_Index = _DictionaryValues.get('_PickIndex')
    _SubCars = _DictionaryValues.get("_SubCars")
    _Engine_Speak(f"I picked a random model '{_Cars[_SubModel_Index]}'", True)
    _Engine_Speak("These are the submodels", True)
    for _SubCar in _SubCars:
        _Engine_Speak(f" > {_SubCar}", True)
    _SubModel_Picked = _DictionaryValues.get('_PickSubIndex')
    _Engine_Speak(f"I picked a random submodel '{_SubCars[_SubModel_Picked]}'", True)
    _Price = _DictionaryValues.get('_Price')
    if _Price == "not found":
        _Engine_Speak("I could not find a price on this page", True)
    else:
        _Engine_Speak(f"The price is: '{_Price}'", True)
    _ImagePath = _DictionaryValues.get('_ImagePath', "not found") # Get the saved model image path
    if _ImagePath != "not found": # Check the image exists
        _ModelImage = Image.open(_ImagePath) # Open the image with PIL
        _ModelImage.show() # Show it on the screen
# ---------- Running the program when it is called internally
if __name__ == "__main__":
    _ClearTerminal()
    _MainProgram(_WebSite)
print("\nProgram Done")
