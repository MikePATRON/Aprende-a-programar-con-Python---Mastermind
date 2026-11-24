# Web Site
# Notes: Obsidian -> 35 — Playwright (CODING/PYTHON/LIBRERIAS PRINCIPALES DE PYTHON/35 — Playwright.md)
# ---------- Libraries
import os, random, requests # os: clear terminal | random: pick a random car | requests: download the model image
from playwright.sync_api import sync_playwright # Importing library 'playwright' (35 — Playwright: Installation)
# ---------- Variables
_WebSite = "https://www.porsche.com/mexico/" # Target web site (Porsche Mexico)
# ---------- Functions
def _GetTitle(_DictionaryValues): # Function: get the web site title and store it in the dictionary
    print("Getting Title variable index")
    _Page = _DictionaryValues.get("_Page") # Read the _Page object stored in the dictionary
    print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it (console progress effect)
    print("Getting Title")
    _WebSite_Title = _Page.title() # page.title() -> the tab title (35 — Playwright: Open a browser and get a page)
    print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
    _DictionaryValues["_WebSite_Title"] = _WebSite_Title # Store the title in the dictionary
    print(f"Returning Title as variable: [{_WebSite_Title}]")
    print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
    return _DictionaryValues # Return the dictionary with the new value
def _ClickPage(_WhereToClick, _DictionaryValues): # Function: click a button by its visible text
    print(f"Clicking {_WhereToClick}")
    _Page = _DictionaryValues.get("_Page") # Read the _Page object from the dictionary
    print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
    _Page.get_by_role("button", name = _WhereToClick, exact = True).click() # Find the button by its accessible name and click it (35 — Playwright: Click by role)
    print("Click done")
    print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
def _Engine_WebSite(_WebSite, _RunBackground): # Function: main engine — opens the browser, navigates, extracts the models
    _DictionaryValues = {} # Dictionary that carries values between functions
    print("Running Engine Web Site")
    with sync_playwright() as p: # Start Playwright; it closes itself when done (35 — Playwright: Open a browser and get a page)
        print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
        print("Launching Web")
        _Browser = p.chromium.launch(headless = _RunBackground) # Launch Web | headless = False (Open Web) or True (Run in background)
        print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
        _DictionaryValues["_Browser"] = _Browser # Store the browser object in the dictionary
        print("Opening a new tab")
        _Page = _Browser.new_page() # Open a new tab (35 — Playwright: Open a browser and get a page)
        print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
        _DictionaryValues["_Page"] = _Page # Store the tab object in the dictionary
        print(f"Entering Web Site: [{_WebSite}]")
        _Page.goto(_WebSite) # Navigate to the URL (35 — Playwright: Open a browser and get a page)
        print("\033[1A\033[2K", end="") # ANSI: move cursor up 1 line and clear it
        _GetTitle(_DictionaryValues) # Call: get and store the page title
        _Page.wait_for_load_state("networkidle") # Wait until the network is quiet (35 — Playwright: Waiting)
        _ClickPage("Menú", _DictionaryValues) # Call: open the burger menu (35 — Playwright: Porsche menu flow)
        _Page.wait_for_load_state("networkidle") # Wait until the menu finishes loading
        _ClickPage("Modelos", _DictionaryValues) # Call: open the models list
        _Page.wait_for_load_state("networkidle") # Wait until the models list finishes loading
        _Cars = _Page.locator("li.models-item .font-weight-600").all_inner_texts() # All car model names -> list (35 — Playwright: Extract values from many elements)
        _DictionaryValues["_Cars"] = _Cars # Store all model names in the dictionary
        _PickIndex = random.randrange(len(_Cars)) # Random position: 0 to last (picks a random car)
        _DictionaryValues["_PickIndex"] = _PickIndex
        _ModelImage = _Page.locator("li.models-item").nth(_PickIndex).locator("img") # The model tile image: its srcset has the model name inside
        _SrcSet = _ModelImage.first.get_attribute("srcset") # Read the srcset attribute (contains the 1x and 2x URLs)
        if _SrcSet: # Guard: the image has a srcset attribute
            _ImageURL = _SrcSet.split(",")[0].strip() # Take the FIRST URL of the srcset (the 1x image)
            _ModelName = _Cars[_PickIndex] # The MODEL name (not the submodel)
            _ImageData = requests.get(_ImageURL).content # Download the image bytes
            _ImagePath = f"{os.getcwd()}/{_ModelName}.webp" # Same path as the audio (current folder) + model name
            _ImageFile = open(_ImagePath, "wb") # Open the file for writing bytes
            _ImageFile.write(_ImageData) # Write the image bytes
            _ImageFile.close() # Close the file
        else: # Fallback: no srcset on the image
            _ImagePath = "not found" # Store the fallback
        _DictionaryValues["_ImagePath"] = _ImagePath # Store the image path in the dictionary
        _Page.locator("li.models-item").nth(_PickIndex).click() # Click THE SAME card: nth(index) -> exact match (35 — Playwright: nth(i) picks one match)
        _Page.wait_for_load_state("networkidle")
        _Page.wait_for_timeout(3000) # Wait for the flyout to render the submodel tiles (networkidle fires too early)
        _SubCars = _Page.locator("span.font-weight-600").all_inner_texts() # Submodel names are spans with that class (dot = class, missing dot = nothing matches)
        _DictionaryValues["_SubCars"] = _SubCars
        _PickSubIndex = random.randrange(len(_SubCars)) # Random position: picks a random submodel
        _DictionaryValues["_PickSubIndex"] = _PickSubIndex
        _Page.locator(".model-area-button").nth(_PickSubIndex).click() # Click THE SAME submodel tile -> goes to its subpage
        _Page.wait_for_load_state("networkidle")
        _Page.wait_for_timeout(3000) # Wait for the subpage to render (networkidle fires too early)
        _DictionaryValues["_SubPageTitle"] = _Page.title() # Store the subpage title
        _DictionaryValues["_SubPageURL"] = _Page.url # Store the subpage URL
        _Page.wait_for_timeout(3000) # Extra wait: the price can load after the page (or never, on variant overview pages)
        _PriceElement = _Page.locator(".ModelPrice__root__8f924.ModelPrice__center__8f924") # The price element (dot + class, both classes on one element)
        if _PriceElement.count() > 0:
            _Price = _PriceElement.evaluate("el => { const c = el.cloneNode(true); c.querySelectorAll('sup').forEach(s => s.remove()); return c.innerText.trim(); }") # Get the price WITHOUT the footnote marker (the <sup> digit)
        else:
            _Price = "not found" # Fallback: variant overview pages have no price element
        _DictionaryValues["_Price"] = _Price # Store the price (or the fallback)
        _Browser.close() # Close web (35 — Playwright: Open a browser and get a page)
        return _DictionaryValues # Return everything collected
# ---------- Main Program
def _MainProgram(_WebSite): # Function: entry point of the program
    os.system("clear") # Clear the terminal screen
    _Engine_WebSite(_WebSite, False) # Run the engine with the window visible (headless = False)
# ---------- Run Program
if __name__ == "__main__": # Only runs when executed directly, not when imported
    _MainProgram(_WebSite) # Call the main program
print("\nProgram Done") # Prints ALWAYS (even on import) because it is outside the if guard
