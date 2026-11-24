# Hacker Script
# ---------- Libraries
import os, sqlite3, re # Import libraries for Python
from time import sleep
from random import randrange
# ---------- Clear Terminal
os.system("clear") # Clear Terminal for Linux
# ---------- Functions
def _DelayAction(): # Function for Waiting time
    _HrsRandom = randrange(1, 4) # Random waiting hrs from 1 to 3
    # sleep(_HrsRandom * 60 * 60) # Wait Random Hrs
    print("\nWait {} seconds".format(_HrsRandom))
    sleep(_HrsRandom) # Action "Wait"
def _GetGoogleChromeHistory(_HistoryPath): # Google Chrome History Function
    try: # Avoid Error when Google Chrome is open
        _ConnectionSQL = sqlite3.connect(_HistoryPath) # Library to work with SQL
        _CursorSQL = _ConnectionSQL.cursor() # Library to work with SQL
        _CursorSQL.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC") # Get the URLS from Google Chrome with SQL
        _urlsSQL_GoogleChomeHistoryList = _CursorSQL.fetchall() # Library to work with SQL
        _ConnectionSQL.close() # Close Google Chrome connection
        print("\nGoogle Chrome is closed, reading file")
        return _urlsSQL_GoogleChomeHistoryList # Result Function
    except: # General Exception
        print("\nGoogle Chrome is open") # Message for the user in Terminal
        return None # Result for Exception
def _CreateHackerFile(_DesktopPath, _urlsSQL_GoogleChomeHistoryList): # Function for Hacker File
    print("\nCreating Hacker File in Desktop")
    with open(_DesktopPath + "Read.txt", "w") as _HackerFile: # Create file in Desktop
        _HackerFile.write("I am a Hacker and I got in your computer\n\nThis is your Google Chrome History:\n\n{}".format(_urlsSQL_GoogleChomeHistoryList)) # Message
        return _HackerFile
def _CheckHistory_ScaryMessages(_HackerFile, _urlsSQL_GoogleChomeHistoryList, _UserName, _DesktopPath):
    print("\nThis are the last 10 urls from the History File\n")
    with open(_DesktopPath + "Read.txt", "w") as _HackerFile: # Create file in Desktop
        for _item in _urlsSQL_GoogleChomeHistoryList[:10]:
            print(_item)
            _HackerFile.write("\nUser [{}] has seen [{}]\n".format(_UserName, _item[0]))
            _HackerFile.write("This is the Web Site Code: [{}]\n".format(_item[1]))
            _HackerFile.write("This is the URL: [{}]\n".format(_item[2]))
    for _item in _urlsSQL_GoogleChomeHistoryList[:10]:
        _Result_FindURL = re.findall("https://mastermind.ac/([A-Za-z0-9]+)", _item[2])
        if _Result_FindURL:
            print("This are the variables I don't know if it exist: {}".format(_Result_FindURL))
            print(_Result_FindURL[0])
# ---------- Main Program
def _Main(): # Create the Main function for the program
    print("\nRunning Hacker program to get Google Chrome History")
    _DelayAction() # Call for Function _DelayAction()
    _UserName = os.getlogin() # Get the username
    print("It got the Username: {}\nFinding path for Google Chrome History file".format(_UserName))
    _DesktopPath = "/home/" + _UserName + "/Desktop/" # Desktop Path
    _HistoryPath = "/home/" + _UserName + "/.config/google-chrome/Default/History" # Path for the History file
    print("This is the path: {}".format(_HistoryPath))
    # ---------- SQL code
    print("Running SQL code to read the file")
    _urlsSQL_GoogleChomeHistoryList = _GetGoogleChromeHistory(_HistoryPath) # Call for Function Google Chrome History
    while _urlsSQL_GoogleChomeHistoryList == None: # Repeat until it gets the History
        print("Repeating action")
        _DelayAction() # Call for Function _DelayAction()
        _urlsSQL_GoogleChomeHistoryList = _GetGoogleChromeHistory(_HistoryPath) # Get the History Path from Function Google Chrome History
    if _urlsSQL_GoogleChomeHistoryList != None: # If it gets the History
        print("Got Google Chrome History")
        _HackerFile = _CreateHackerFile(_DesktopPath, _urlsSQL_GoogleChomeHistoryList) # Variable for the result in Function Hacker File
    # ---------- Writing scary messages in file
    _CheckHistory_ScaryMessages(_HackerFile, _urlsSQL_GoogleChomeHistoryList, _UserName, _DesktopPath)
# ---------- Run the program
if __name__ == "__main__": # Run the program when called
    _Main() # Run the Main Function

# File: ~/.config/google-chrome/Default/History
