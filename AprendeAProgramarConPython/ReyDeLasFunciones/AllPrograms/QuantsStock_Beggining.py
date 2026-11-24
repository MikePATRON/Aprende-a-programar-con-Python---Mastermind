# Sniper Bot
# ---------- Libraries
import os # Import libraries for Python
from requests_html import HTML # Class to search elements in the HTML
from curl_cffi import requests # Fake Chrome fingerprint so Amazon serves the real page
from time import sleep
# ---------- Ask User Sock
#_StockURL = input("What Stock do you want to buy?\n >> ")
# ---------- Main Program
def _MainProgram(_URL): # Function that receives the URL
    _WaitingTime = 30 # 30 seconds
    #sleep(1 * _WaitingTime)
    # ---------- JARVIS help START
    _Response = requests.get(_URL, impersonate = "chrome") # Get the page pretending to be Chrome
    _Document = HTML(html=_Response.text) # Convert HTML text into a searchable document
    # ---------- JARVIS help END
    _PriceStock_YahooFinance = _Document.find('[data-testid="qsp-price"]') # Search the stock price by data-testid
    print("\nThis is the price for: {}".format(_PriceStock_YahooFinance)) # Show the result
# ---------- Run Program
if __name__ == "__main__": # Run the program when called
    os.system("clear") # Clear Terminal for Linux
    _MainProgram("https://finance.yahoo.com/quote/SPCX/") # Call the Main Function with the URL
