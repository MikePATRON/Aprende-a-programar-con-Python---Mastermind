# This is a program to count the caracters in your full name
# ---------- Libraries
import os # Import Terminal Commands
# ---------- Clean Terminal
os.system("clear") # Clear Terminal for Linux
# ---------- Main Code
def _CounterNameCaracters(_UserName, *_UserFullName): # Function with one or more inputs (Optional, not always)
    if _UserFullName: # The program analize if the code has more than one input with Tuples
        _Len = [len(_UserName)] # Creates a list for len caracters in inputs (more than one)
        for _X in _UserFullName: # Bucle for more than one input
            _Len.append(len(_X)) # Adds the result in the list
        return _Len # Returns the list
    return _UserName # If the function doesn't have more than one imput, returns only the single imput
# ---------- Run the program
if __name__ == "__main__": # Runs the main program when Directly
    # ---------- Ask for User's full name
    print(_CounterNameCaracters("Miguel", "Martin", "Diablo")) # Calls the function with more than one input
