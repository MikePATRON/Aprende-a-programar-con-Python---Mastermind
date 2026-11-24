# This is my general code
# -------------------------------------------------------------------------------- Libraries
import os # Script talk directly to Linux, Windows, or macOS
import pyttsx3 # Text-to-speech (TTS) library: it converts text into spoken audio
import contextlib # Utilities for "with" blocks (automatic setup/cleanup, redirecting print output, ignoring errors)
# -------------------------------------------------------------------------------- Functions
def _ClearTerminal():
    if os.name == "posix": # If system = Linux or Mac
        os.system("clear")
    else: # If system = Windows
        os.system("cls")
def _EngineSpeak(_SayMessage, _Prints = False, _SaveFile = True):
    _Engine = pyttsx3.init()
    _EngineRate = "rate"
    _EngineRateValue = 120
    _Engine.setProperty(_EngineRate, _EngineRateValue)
    if os.name == "posix" and os.uname().sysname == "Linux": # Linux espeak-ng voice
        _EngineVoice = "voice"
        _EngineVoiceValue = "gmw/en-us+robosoft"
        _Engine.setProperty(_EngineVoice, _EngineVoiceValue)
    if _Prints:
        print(_SayMessage)
    if _SaveFile == True:
        _Path = os.getcwd()
        _Path = os.path.join(_Path, "EngineAudioFiles")
        os.makedirs(_Path, exist_ok = True)
        _AudioFile = os.path.join(_Path, "speech.wav") # Build file path for Linux, Windows, or Mac
        with open(os.devnull, "w") as _NullFile: # Open null device ('/dev/null' on Linux/Mac, 'nul' on Windows)
            with contextlib.redirect_stdout(_NullFile): # Hide the "Audio saved to" message
                _Engine.save_to_file(_SayMessage, _AudioFile) # Save the message to a WAV file
                _Engine.runAndWait() # Wait for the synthesis to finish
        if os.name == "nt": # If system = Windows
            os.system(f'powershell -c "(New-Object Media.SoundPlayer \'{_AudioFile}\').PlaySync()"') # Play the WAV on Windows
        elif os.uname().sysname == "Darwin": # If system = Mac
            os.system(f'afplay "{_AudioFile}"') # Play the WAV on Mac
        else: # If system = Linux
            os.system(f'aplay -q "{_AudioFile}"') # Play the WAV on Linux
        os.remove(_AudioFile) # Delete the temporary WAV on Linux, Windows, or Mac
    else:
        _Engine.say(_SayMessage)
        _Engine.runAndWait()
def _ClearTerminal_SavePosition(_Behavior):
    if _Behavior == 0:
        print("\033[s", end="") # Save start position
    elif _Behavior == 1:
        print("\033[u", end="") # Jump back to start
        print("\033[J", end="") # Wipe everything below
# -------------------------------------------------------------------------------- Run Program
if __name__ == "__main__":
    _EngineSpeak()
