# Audio
# Instructions
_Instructions = """
This is a Python code to make the machine speak when giving a text
"""
# ---------- Libraries
import pyttsx3, os, contextlib
# ---------- Functions
def _Engine_Speak(_SayMessage, _Prints = False, _SaveFile = True): # Add the True or False to print the Config, but giving only one value at the beggining
    if _Prints:
        print("\nRunning Engine Speak: pyttsx3")
    _Engine = pyttsx3.init()
    _EngineRate = "rate"
    _EngineRateValue = 120
    if _Prints:
        print(f"[{_EngineRate}] = [{_EngineRateValue}]")
    _Engine.setProperty(_EngineRate, _EngineRateValue)
    _EngineVoice = "voice"
    _EngineVoiceValue = "gmw/en-us+robosoft"
    if _Prints:
        print(f"[{_EngineVoice}] = [{_EngineVoiceValue}]\n")
    _Engine.setProperty(_EngineVoice, _EngineVoiceValue)
    print(_SayMessage)
    if _SaveFile == True:
        _Path = os.getcwd()
        _Path = os.path.join(_Path, "EngineAudioFiles")
        os.makedirs(_Path, exist_ok = True)
        with contextlib.redirect_stdout(open(os.devnull, "w")):  # Hide the "Audio saved to" message
            _Engine.save_to_file(_SayMessage, f"{_Path}/speech.wav")  # Save the message to a WAV file
            _Engine.runAndWait()  # Wait for the synthesis to finish
        os.system(f"aplay -q {_Path}/speech.wav")  # Play the WAV
        os.system(f"rm {_Path}/speech.wav")  # Delete the temporary WAV
    else:
        _Engine.say(_SayMessage)
        _Engine.runAndWait()
# ---------- Main Program
def _MainProgram():
    _Engine_Speak("This is a test with a darker voice")
# ---------- Running the program when it is called internally
if __name__ == "__main__":
    os.system("clear")
    print(_Instructions)
    _MainProgram()
