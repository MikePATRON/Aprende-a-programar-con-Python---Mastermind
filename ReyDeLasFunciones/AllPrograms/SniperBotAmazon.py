# Sniper Bot
# ---------- Libraries
import os
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By # Locators: By.ID, By.CSS_SELECTOR, By.XPATH
from time import sleep
# ---------- Main Code
_URL_Coolmod_Available = "https://www.coolmod.com/asus-rog-astral-geforce-rtx-5080-oc-gaming-16gb-gddr7/" # Link with Stock
_URL_Coolmod_NoStock = "https://www.coolmod.com/asus-rog-astral-geforce-rtx-5090-oc-gaming-32gb-gddr7/" # Link with No Stock
def _MainCode(_URL_Coolmod): # Function MAIN CODE
    print("\nMain Function\n >> URL: [{}]".format(_URL_Coolmod))
    _Session = HTMLSession()
    _Product_Page = _Session.get(_URL_Coolmod)
    _Found = _Product_Page.html.find("#product-extra-component") # Write the div id = #...
    if len(_Found) > 0:
        print("\nStarting Firefox")
        _Driver = webdriver.Firefox()
        _Driver.get(_URL_Coolmod)
        print("\nCockies click")
        _Driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click() # Allow Cockies click
        # AI help start
        print("\nWaiting for pop up")
        for _X in range(20): # Check up to 20 times (max 20 seconds)
            print(" >> Attempt: {}".format(_X))
            _CloseSubscription = _Driver.find_elements(By.CSS_SELECTOR, "a[href*='cn_close_content']") # Search for the X link: href CONTAINS cn_close_content
            if _CloseSubscription: # If the link exists, the popup is showing
                print(" >> Pop up TRUE. Click")
                _Driver.execute_script("arguments[0].click();", _CloseSubscription[0]) # JS click: works even if covered by an overlay
                print(" >> Done")
                break # Popup closed: stop the loop NOW
            sleep(1) # Not found yet: wait 1 second, then check again
            # AI help end
        input("\nENTER to finish process: ")
# ---------- Run Program
if __name__ == "__main__": # Check if running
    os.system("clear") # Clear Linux terminal
    print("\nRunning Program\n >> Calling Main Function")
    _MainCode(_URL_Coolmod_Available) # Call main function
