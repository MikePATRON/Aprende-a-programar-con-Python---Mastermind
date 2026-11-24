# Audio
# ---------- Libraries
import pyttsx3, speech_recognition, os, contextlib
# ---------- Functions
def _Engine_Speak(_SayMessage, _SaveFile):
    print("Running Engine Speak")
    _Engine = pyttsx3.init()
    print("\033[1A\033[2K", end="")
    _EngineRate = "rate"
    _EngineRateValue = 120
    print(f"Setting [{_EngineRate}] to [{_EngineRateValue}]")
    _Engine.setProperty(_EngineRate, _EngineRateValue)
    print("\033[1A\033[2K", end="")
    _EngineVoice = "voice"
    _EngineVoiceValue = "gmw/en-us+robotic"
    print(f"Setting [{_EngineVoice}] to [{_EngineVoiceValue}]")
    _Engine.setProperty(_EngineVoice, _EngineVoiceValue)
    print("\033[1A\033[2K", end="")
    print(_SayMessage)
    if _SaveFile == True:
        _Path = os.getcwd()
        with contextlib.redirect_stdout(open(os.devnull, "w")):  # Hide the "Audio saved to" message
            _Engine.save_to_file(_SayMessage, f"{_Path}/speech.wav")  # Save the message to a WAV file
            _Engine.runAndWait()  # Wait for the synthesis to finish
        os.system(f"aplay -q {_Path}/speech.wav")  # Play the WAV
        os.system(f"rm {_Path}/speech.wav")  # Delete the temporary WAV
    else:
        _Engine.say(_SayMessage)
        _Engine.runAndWait()
def _Engine_VoiceRecognizer():
    print("Running Engine Recognizer")
    _Recognizer = speech_recognition.Recognizer()
    _VoiceRecognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as _Source:
        os.system("clear")
        print("Now you can speak... Lintening...")
        _Audio = _Recognizer.listen(_Source)
        try:
            _Recognize = _Recognizer.recognize_google(_Audio)
            print(f"I got this: [{_Recognize}]")
            return _Recognize
        except speech_recognition.UnknownValueError:
            _Engine_Speak("I'm sorry, I didn't understand", True)
            return False
# ---------- Main Program
def _MainProgram():
    os.system("clear")
    _Engine_Speak("This is a test", True)
# ---------- Running the program when it is called internally
if __name__ == "__main__":
    _MainProgram()
print("\nProgram Done")
