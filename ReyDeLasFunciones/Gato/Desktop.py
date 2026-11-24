# Gato
_Title = "GATO"
# ---------- Libraries
import pyttsx3, os, contextlib
from PySimpleGUI_Program import _Main_PySimpleGUI
# ---------- Functions
def _DeleteLine(): # My own library to clear terminal
    print("\033[1A\033[2K", end="")
# ---------- Speak
def _Engine_Speak(_SayMessage, _SaveFile):
    print("Running Engine Speak") # Message for terminal
    _Engine = pyttsx3.init()
    _DeleteLine() # My own library to clear terminal
    _EngineRate = "rate"
    _EngineRateValue = 120
    print(f"Setting [{_EngineRate}] to [{_EngineRateValue}]") # Message for terminal
    _Engine.setProperty(_EngineRate, _EngineRateValue)
    _DeleteLine() # My own library to clear terminal
    _EngineVoice = "voice"
    _EngineVoiceValue = "gmw/en-us+robotic"
    print(f"Setting [{_EngineVoice}] to [{_EngineVoiceValue}]") # Message for terminal
    _Engine.setProperty(_EngineVoice, _EngineVoiceValue)
    _DeleteLine() # My own library to clear terminal
    print(_SayMessage)
    if _SaveFile == True:
        _Path = os.getcwd()
        with contextlib.redirect_stdout(open(os.devnull, "w")):  # Hide the "Audio saved to" message
            _Engine.save_to_file(_SayMessage, f"{_Path}/SpeachsFolder/Speech.wav")  # Save the message to a WAV file
            _Engine.runAndWait()  # Wait for the synthesis to finish
        os.system(f"aplay -q {_Path}/SpeachsFolder/Speech.wav")  # Play the WAV
        os.system(f"rm {_Path}/SpeachsFolder/Speech.wav")  # Delete the temporary WAV
    else:
        _Engine.say(_SayMessage)
        _Engine.runAndWait()
# ---------- Main Program
def _MainProgram(_Title):
    os.system("clear")
    print("") # Message for terminal
    _Main_PySimpleGUI()
# ---------- Running the program when it is called internally
if __name__ == "__main__":
    _MainProgram(_Title)
