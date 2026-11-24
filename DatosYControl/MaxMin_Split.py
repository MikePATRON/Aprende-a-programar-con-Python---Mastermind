# (Split) and (List Comprehension)

# ---------- Libraries
import os

# ---------- Clear terminal
os.system("clear")

# ---------- Program
print("\nThis is a program to analyze the MAX and MIN in your numbers")
_UserNumbers = input("\nIntroduce your numbers separeted by (, )\n >> ")
_List_UserNumbers_MaxMin = [float(_x) for _x in _UserNumbers.split(", ")] # List Comprehension
_MaxValue = max(_List_UserNumbers_MaxMin)
_MinValue = min(_List_UserNumbers_MaxMin)
print("\nThis are your MAX and MIN numbers:\n >> Max = {}\n >> Min = {}".format(_MaxValue, _MinValue))
