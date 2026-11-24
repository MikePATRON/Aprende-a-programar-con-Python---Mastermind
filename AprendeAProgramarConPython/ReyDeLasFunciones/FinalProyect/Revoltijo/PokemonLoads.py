# Program to load all Pokemons
_Instructions = """
This is the Final Project Program from MASTERMIND to get all the Pokemons with their behavior
The web site is [https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/buscar]
"""
# ---------- Libraries
from playwright.sync_api import sync_playwright # import Playwright's sync API
from EngineAudio import _Engine_Speak
from time import sleep
import os, re, glob, random # os: paths + system calls | re: regex | glob: Playwright's lock files | random: pick one Pokemon at random
# ---------- Functions

# ------------------------------------------------------------------------------------------------------------------------------------------------------ This is not mine
def _CleanPlaywrightDebris():
    _Patterns = [ # Every lock file Playwright's Firefox can leave behind inside its own folder
        "~/.cache/ms-playwright/firefox*/firefox/lock*",  # lock, lock.stal (the crash of Sep 8)
        "~/.cache/ms-playwright/firefox*/firefox/*.lock", # parent.lock
        "~/.cache/ms-playwright/firefox*/firefox/.*lock"  # .parentlock (hidden)
        ]
    _Locks = [] # Full paths of the stale locks found
    for _Pattern in _Patterns: # Check each pattern
        _Locks += glob.glob(os.path.expanduser(_Pattern)) # Add every match found
    _Locks = sorted(set(_Locks)) # Remove duplicates (the patterns can overlap)
    for _Lock in _Locks: # Walk the stale locks
        try:
            os.remove(_Lock) # Delete the stale lock
        except OSError:
            pass # Ignore it if it vanished or cannot be deleted
    _Mine = {str(os.getpid()), str(os.getppid())} # Never kill this program, nor the shell that launched it
    _Orphans = os.popen('pgrep -f "playwright_firefoxdev_profile"').read().split() # PIDs of the Firefox an interrupted run left behind
    _Orphans = [_Pid for _Pid in _Orphans if _Pid not in _Mine] # Drop our own PID if it ever matched
    for _Pid in _Orphans: # Walk the leftover processes
        os.system(f"kill {_Pid} 2>/dev/null") # Kill only Playwright's own Firefox, never the system Firefox
    if _Locks or _Orphans: # Report only when something was really cleaned
        print(f"Cleanup: removed {len(_Locks)} stale lock(s), killed {len(_Orphans)} leftover Firefox process(es)")
# ------------------------------------------------------------------------------------------------------------------------------------------------------ This was not mine

def _GetPokemonValues(_PkNumber, _Page, _PokemonBase): # Continue getting the information for each one here
    _Page.goto("https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk=" + _PkNumber)
    _Page.wait_for_selector('td.bordeambos img[src*="sprites/tipos/"]', timeout = 60000)
    _DatosBasicos = _Page.locator("td.bordeambos").nth(0) # Only the first "Datos básicos" box
    _ImgsTipo = _DatosBasicos.locator('img[src*="sprites/tipos/"]') # Type images inside that box (1 or 2)
    _Tipos = []
    for _Index in range(_ImgsTipo.count()):
        _Tipos.append(_ImgsTipo.nth(_Index).get_attribute("alt"))
    print(f"|Type:{_Tipos}", end = "")
    _Page.goto("https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_pokemon&pk=" + _PkNumber)
    _Page.wait_for_selector('a[href*="movedex/pokemon"]', timeout = 60000) # wait until the pokemon moves really exist, instead of waiting for the whole network to go quiet
    _Attack = _Page.locator('a[href*="movedex/pokemon"]').all_inner_texts()[1::2] # Get all inner texts for all moves. Start at index 1, step by 2 to get the "English Moves"
    print(_Attack)
    _AttackBase = {
        "_Name":"",
        "_AttackType":"",
        "_AttackMainLevel":"",
        "_AttackDamage":"",
    }
    with open("Pokemons.txt", "r", encoding = "utf-8") as _Document:
        _Lines = [_Line.strip() for _Line in _Document]
        _LineIndex = int(_PkNumber) - 1
        _TypeStr = ",".join(_Tipos)
        _AttackStr = ",".join(_Attack)
        _Lines[_LineIndex] = f"{_Lines[_LineIndex]}|Type:[{_TypeStr}|Attack:[{_AttackStr}]]"
    with open("Pokemons.txt", "w", encoding = "utf-8") as _Document:
        _Document.write("\n".join(_Lines))
def _GetPokemonByIndex(_Index, _Links, _PokemonBase):
    _Href = _Links.nth(_Index).get_attribute("href") # Link of pokemon _Index. Give me the Pokemon at position (_Index)
    _Name = _Links.nth(_Index).inner_text() # Name of pokemon
    if len(_Name) > 1:
        _PkNumber = re.search(r'=(\d+)', _Href).group(1) # Get the real number of the Pokemon
        _NewPokemon = _PokemonBase.copy() # Copy main dictionary
        _NewPokemon["_Name"] = _Name
        _NewPokemon["_Number"] = _PkNumber
        with open("Pokemons.txt", "a", encoding = "utf-8") as _Document:
            if _NewPokemon["_Number"] != "1":
                _Document.write(f"\n{_PkNumber}:{_Name}") # I can't write a Dictionary, it has to be a str
            else:
                _Document.write(f"{_PkNumber}:{_Name}") # I can't write a Dictionary, it has to be a str
# ---------- Main Function
def _Main_PokemonLoads(_RunBackground = True, _Speak = True):
    # ---------- Variables
    _Url = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/buscar"
    _PokemonBase = {
            "_Number":"",
            "_Name":"",
            "_CurrentHealth":100,
            "_BaseHealth":100,
            "_Level":1,
            "_Type":None,
            "_CurrentExp":0
            }
    # ---------- Cleanup
    _CleanPlaywrightDebris() # Remove what a previous crash left behind, so Firefox always starts clean
    # ---------- playwright
    with sync_playwright() as p:
        if _Speak:
            _Engine_Speak("Running Playwright")
            _Engine_Speak("Opening Firefox")
        _Browser = p.firefox.launch(headless = _RunBackground) # open Firefox; headless = True = no window
        if _Speak:
            _Engine_Speak("Opening new page")
        _Page = _Browser.new_page()
        if _Speak:
            _Engine_Speak("Going to url")
            print(f" > {_Url}")
        _Page.goto(_Url)
        _Page.wait_for_selector('a[href*="nationaldex/pkmn"]', timeout = 60000) # wait until the pokemon links really exist, instead of waiting for the whole network to go quiet
        _Title = _Page.title()
        if _Speak:
            _Engine_Speak(f"Got the title: [{_Title}]")
        _Links = _Page.locator('a[href*="nationaldex/pkmn"]') # All pokemon links. Finds the general href
        _Count = _Links.count() # How many pokemon links found
        if _Speak:
            _Engine_Speak(f"Found {_Count} possible pokemons in the list")
            _Engine_Speak("Getting Pokemons")
        with open("Pokemons.txt", "w", encoding = "utf-8") as _Document:
            _Document.write("")
        for _Index in range(_Count):
            _GetPokemonByIndex(_Index, _Links, _PokemonBase)
        _Page.wait_for_selector('a[href*="nationaldex/pkmn"]', timeout = 60000)
        if _Speak:
            _Engine_Speak("All Pokemons saved")
            _Engine_Speak("Choosing a random Pokemon")
        with open("Pokemons.txt", "r", encoding = "utf-8") as archivo: # Read back the file we just wrote
            _Pokemons = [linea.strip() for linea in archivo] # One clean "number:name" string per Pokemon, newline removed
        _RandomPokemon = random.choice(_Pokemons) # Pick one element at random out of all of them
        _PkNumber, _PkName = _RandomPokemon.split(":") # Cut the picked line at the colon: number and name apart
        print(f"Random Pokemon: {_PkNumber} = {_PkName}") # Show the one that came out
        if _Speak:
            _Engine_Speak(f"Going to {_PkName} page")
            print(f" > https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk={_PkNumber}")
            _Engine_Speak(f"Getting {_PkName} values")
        print(f"{_PkNumber}:{_PkName}", end = "")
        _GetPokemonValues(_PkNumber, _Page, _PokemonBase)
        if _Speak:
            _Engine_Speak("Closing browser")
        _Browser.close()
# ---------- Run Program
if __name__ == "__main__":
    os.system("clear")
    print(_Instructions)
    _Main_PokemonLoads(_Speak = False)
