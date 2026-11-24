# Using the new program structure based on the main() function and the final if condition,
# create any type of program you want. Use the debugger to see how the execution thread flows.

# ---------- This is the Program
def main():
    print("Hello world")
# ---------- This is what Nate is asking for

# __name__ is a special variable that Python creates automatically in every file.
# You don't have to declare it — it's always there.
#
# When you run this file directly (python NewFunctions_Main.py):
#     Python sets __name__ = "__main__"
#     → The condition is True → main() runs
#
# When this file is imported from another file (import NewFunctions_Main):
#     Python sets __name__ = "NewFunctions_Main"
#     → The condition is False → main() does NOT run automatically
#
# This lets the same file be both:
#   - A useful script (when run directly)
#   - A reusable module (when imported elsewhere)
if __name__ == "__main__":
    main()
