# This is Mastermind Final Project for "APRENDE A PROGRAMAR CON PYTHON"
# -------------------------------------------------------------------------------- Libraries
from _General import _ClearTerminal, _EngineSpeak, _ClearTerminal_SavePosition
from playwright.sync_api import sync_playwright # Microsoft's modern browser automation library. It opens a REAL browser, so it can do everything (requests-html)
import pickle
import os
# -------------------------------------------------------------------------------- Values
_PokemonBase = {
    "_Number": None,
    "_Name": None,
    "_CurrentHealth": 100,
    "_BaseHealth": 100,
    "_Level": 1,
    "_Type": None,
    "_Attacks": None,
    "_CurrentExp": 0} # These are the Basic Pokemon Values
_PokeFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_PokeFile.pkl") # Always next to this script, no matter where you run it from
_urlBase = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/buscar" # Main Pokemon Page with all of them
# -------------------------------------------------------------------------------- Functions
# All Pokemons Loads
def _AllPokemonLoads(_CounterPokemons):
    _EngineSpeak("\nGetting Pokemons")
    try:
        with open(_PokeFilePath, "rb") as _PokeFile:
            _AllPokemons = pickle.load(_PokeFile)
            _EngineSpeak("\nProgram already got all Pokemons\n")
    except FileNotFoundError:    
        _AllPokemons = []
        for _Index in range(_CounterPokemons):
            _AllPokemons.append(_PokemonLoad(_Index + 1))
        _EngineSpeak("\nProgram got all Pokemons you asked for\n")
        with open(_PokeFilePath, "wb") as _PokeFile:
            pickle.dump(_AllPokemons, _PokeFile)
    return _AllPokemons
# Pokemon Information Load
def _PokemonLoad(_Index, _RunBackground = True): # Get each Pokemon Values
    #_EngineSpeak(f"\nGetting Pokemon: {_Index}\n") # Message for User
    _url = f"https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk={_Index}" # Single Pokemon page
    with sync_playwright() as p: # start Playwright; it closes itself when done
        _Browser = p.firefox.launch(headless = _RunBackground); print(f"Firefox launched. Running in background = {_RunBackground}") # open Firefox; headless = True = no window
        _Page = _Browser.new_page(); print("New tab oppened") # open a new tab
        _Page.goto(_url); print(f"Navigate to url: {_url}") # navigate to URL
        print(_Page.title()) # print the page title
        _Pokemon = _PokemonBase.copy() # Copy Basic Pokemon Values List
        _Pokemon["_Number"] = _Index # Setting Number Value
        _Pokemon["_Name"] = _Page.locator(".mini").inner_text(); print(f"Name: {_Pokemon["_Name"]}", end = "") # Setting Name Value and print message
        _Pokemon["_Type"] = [img.get_attribute("alt") for img in _Page.locator("td.bordeambos").nth(0).locator('img[src*="3ds/sprites/tipos/"]').all()]; print(f", Type: {_Pokemon["_Type"]}", end = "") # Setting Type value and print message
        _Attacks = []
        _Rows = _Page.locator("table.pkmain").nth(-1).locator("tr.check3.bazul").all()
        for _Row in _Rows:
            _Cells = _Row.locator("td").all()  # List of <td> elements in this row
            _Nv = _Row.locator("th").first.inner_text().strip() # Level is inside <th> (not <td>), and some rows don't have class="verde"
            _Name = _Cells[0].locator("a").nth(1).inner_text() # English name (index 1 of <a> in first <td>)
            _Type = _Cells[1].locator("img").get_attribute("alt") # Image alt text (second <td>)
            try:
                _Power = int(_Cells[3].inner_text().strip()) # Power (fourth <td>, after Category at index 2)
            except ValueError:
                _Power = 0
            _Attacks.append({
                "_Nv": _Nv,
                "_Name": _Name,
                "_Type": _Type,
                "_Power": _Power
            })
        _Pokemon["_Attacks"] = _Attacks; print(", Attacks: Done") # Setting Attacks Values and print message
        #_Browser.close(), print("Browser closed") # close the browser
    return _Pokemon
# -------------------------------------------------------------------------------- Main Function
def _MainFinalProject():
    _ClearTerminal()
    _EngineSpeak("\nRunning")
    _ClearTerminal_SavePosition(0); print(_AllPokemonLoads(151)); _ClearTerminal_SavePosition(1)
# -------------------------------------------------------------------------------- Run Program
if __name__ == "__main__":
    _MainFinalProject()
