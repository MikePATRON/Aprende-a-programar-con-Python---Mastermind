# Code to Audio
# ---------- Libraries
import pyttsx3, os, re
from time import sleep
import speech_recognition as _SR
# ---------- Help Functions
def _ClearTerminal():
    os.system("clear")
def _WaitingTimer(_WaitingTime):
    print(f"Waiting [{_WaitingTime}] seconds")
    _Counter = 0
    while _Counter < _WaitingTime:
        sleep(0.5)
        _Counter += 0.5
        print(f" >> {_Counter}")
def _EngineSpeak(_Message):
    print("Starting Audio Motor")
    _Engine = pyttsx3.init()
    _VoiceRate = "rate"
    _VoiceRateValue = 120
    print(f"Setting [{_VoiceRate}] to [{_VoiceRateValue}]")
    _Engine.setProperty(_VoiceRate, _VoiceRateValue)
    _Engine.setProperty("voice", "gmw/en-us+robotic")
    print(f"Message: [{_Message}]")
    _Engine.say(_Message)
    _Engine.runAndWait()
# ---------- Main Code
def _MainFunction():
    _EngineSpeak("Hello User! What is your name?")
    _WaitingTimer(3)
    print("Setting 'Recognizer' to listen audio and try to understand it")
    _Recognizer = _SR.Recognizer()
    print("'Recognizer' done")
    with _SR.Microphone() as source:
        _ClearTerminal()
        print("Opening microphone source")
        print("Now 'user' can respond")
        _Audio = _Recognizer.listen(source)
        print("Calling function to recognize audio with Google")        
        try:
            _Text = _Recognizer.recognize_google(_Audio)
            _ClearTerminal()
        except:
            _ClearTerminal()
            print("It couldn't hear anything. Starting with TEST ANSWER")
            _Text = "Miguel"
        print(f"This is the result\n >> User: '{_Text}'")
        print("Setting the answer to UPPER CASE")
        _Text = _Text.upper()
        print(f"This is the final result: '{_Text}'")
        _Patterns = ["MY NAME IS ([A-Za-z]+)", "I AM ([A-Za-z]+)", "^([A-Za-z]+)$"]
        _UserName_NotFound = True
        for _Pattern in _Patterns:
            _UserName = re.findall(_Pattern, _Text)
            print(f" >> Trying with pattern [{_Pattern}], result: [{_UserName}]")
            if _UserName:
                print(f"Found User Name")
                _Message = f"Nice to meet you {_UserName}"
                _EngineSpeak(_Message)
                _UserName_NotFound = False
                break
            else:
                print("It couldn't find the User Name")
        if _UserName_NotFound == True:
            _EngineSpeak("I couldn't hear your name")
# ---------- Run Program
if __name__ == "__main__":
    _ClearTerminal()
    print("\nRunning Program\n")
    _MainFunction()
print("\nProgram Ended")
