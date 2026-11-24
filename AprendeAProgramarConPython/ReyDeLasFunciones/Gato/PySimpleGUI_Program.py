# PySimpleGUI program
# ---------- Libraries
import os
import PySimpleGUI as _PSG
# ---------- Main Program
def _Main_PySimpleGUI():
    # Game Values
    _Player1 = "X"
    _Player2 = "O"
    _CurrentPlayer = _Player1
    _Board = [0, 0, 0,
              0, 0, 0,
              0, 0, 0]
    _WinnerPlays = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]
    _GameOver = False
    # Window config
    _SizeButton = (7, 3)
    # Button lines
    _Layout = [[# First button lines
                _PSG.Button("", size = _SizeButton, key = "-0-"),
                _PSG.Button("", size = _SizeButton, key = "-1-"),
                _PSG.Button("", size = _SizeButton, key = "-2-")
                ],
                [# Second button lines
                _PSG.Button("", size = _SizeButton, key = "-3-"),
                _PSG.Button("", size = _SizeButton, key = "-4-"),
                _PSG.Button("", size = _SizeButton, key = "-5-")
                ],
                [# Third button lines
                _PSG.Button("", size = _SizeButton, key = "-6-"),
                _PSG.Button("", size = _SizeButton, key = "-7-"),
                _PSG.Button("", size = _SizeButton, key = "-8-")
                ],
                [_PSG.Button("I am done", key = "-OK-")]]
    # Title and List with all the values needed for _Window
    _Window = _PSG.Window("GATO", _Layout)
    while True: # To run the program always
        _Event, _Values = _Window.read() # read() returns the event and the values
        if _Event and _Values != None:
            print(_Event, _Values) # show which button was pressed and the Input content
        if _Window.Element(_Event).ButtonText == "":
            _Index = int(_Event.replace("-", ""))
            _Board[_Index] = _CurrentPlayer
            _Window.Element(_Event).Update(text = _CurrentPlayer)
            for _WinnerPlay in _WinnerPlays:
                if _Board[_WinnerPlay[0]] == _Board[_WinnerPlay[1]] == _Board[_WinnerPlay[2]] != 0:
                    print(f"Player {_Board[_WinnerPlay[0]]} won")
                    _GameOver = True
            if 0 not in _Board:
                print("Game done! No Winner")
            if _CurrentPlayer == _Player1:
                _CurrentPlayer = _Player2
            else:
                _CurrentPlayer = _Player1
        if _Event is _PSG.WIN_CLOSED or _Event == "-OK-" or _GameOver == True: # window closed or "I am done" pressed
            break
# Run program
if __name__ == "__main__":
    os.system("clear")
    _Main_PySimpleGUI()
