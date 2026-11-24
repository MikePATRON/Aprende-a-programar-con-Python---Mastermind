# This is Mastermind Final Project for "APRENDE A PROGRAMAR CON PYTHON"
# -------------------------------------------------------------------------------- Libraries
from _General import _ClearTerminal, _EngineSpeak
from _PokemonLoad import _AllPokemonLoads
import random
import copy
# -------------------------------------------------------------------------------- Values
# Attack type: types that receive double damage
_SuperEffective = {
    "fuego": ["planta", "hielo", "bicho", "acero"],
    "agua": ["fuego", "tierra", "roca"],
    "planta": ["agua", "tierra", "roca"],
    "electrico": ["agua", "volador"],
    "hielo": ["planta", "tierra", "volador", "dragon"],
    "lucha": ["normal", "hielo", "roca"],
    "veneno": ["planta", "hada"],
    "tierra": ["fuego", "electrico", "veneno", "roca"],
    "volador": ["planta", "lucha", "bicho"],
    "psiquico": ["lucha", "veneno"],
    "bicho": ["planta", "psiquico"],
    "roca": ["fuego", "hielo", "volador", "bicho"],
    "fantasma": ["psiquico", "fantasma"],
    "dragon": ["dragon"]}
# Pokemon number: number it evolves into (it evolves at level 10 and 20)
_Evolutions = {1: 2, 2: 3, 4: 5, 5: 6, 7: 8, 8: 9, 10: 11, 11: 12, 13: 14, 14: 15, 16: 17, 17: 18,
               19: 20, 21: 22, 23: 24, 25: 26, 27: 28, 29: 30, 30: 31, 32: 33, 33: 34, 35: 36,
               37: 38, 39: 40, 41: 42, 43: 44, 44: 45, 46: 47, 48: 49, 50: 51, 52: 53, 54: 55,
               56: 57, 58: 59, 60: 61, 61: 62, 63: 64, 64: 65, 66: 67, 67: 68, 69: 70, 70: 71,
               72: 73, 74: 75, 75: 76, 77: 78, 79: 80, 81: 82, 84: 85, 86: 87, 88: 89, 90: 91,
               92: 93, 93: 94, 96: 97, 98: 99, 100: 101, 102: 103, 104: 105, 109: 110, 111: 112,
               116: 117, 118: 119, 120: 121, 129: 130, 133: 134, 138: 139, 140: 141, 147: 148, 148: 149}
_Struggle = {"_Nv": "1", "_Name": "Struggle", "_Type": "normal", "_Power": 35} # If a Pokemon has no attacks
# -------------------------------------------------------------------------------- Functions
def _NewPokemon(_PokemonData, _Level = 1):
    _Pokemon = copy.deepcopy(_PokemonData) # Copy, so two equal Pokemons don't share the same health
    _Pokemon["_Level"] = _Level
    _Pokemon["_CurrentExp"] = 0
    _Pokemon["_BaseHealth"] = 100 + (_Level - 1) * 10
    _Pokemon["_CurrentHealth"] = _Pokemon["_BaseHealth"]
    return _Pokemon
def _GetPlayerProfile(_PokemonList):
    return {
        "_PlayerName": input("What is your name? "),
        "_PokemonInventory": [_NewPokemon(random.choice(_PokemonList)) for i in range(3)],
        "_Combats": 0,
        "_Pokeballs": 3,
        "_HealthPotion": 3,
        "_History": []
    }
def _AnyPlayerPokemonLives(_PlayerProfile):
    return sum([_Pokemon["_CurrentHealth"] for _Pokemon in _PlayerProfile["_PokemonInventory"]]) > 0
def _GetPokemonInfo(_Pokemon):
    return f"{_Pokemon["_Name"]} | Lvl {_Pokemon["_Level"]} | {"/".join(_Pokemon["_Type"])} | Hp {_Pokemon["_CurrentHealth"]}/{_Pokemon["_BaseHealth"]} | Exp {_Pokemon["_CurrentExp"]}/{_Pokemon["_Level"] * 10}"
def _ShowInventory(_PlayerProfile):
    print("\n--- Inventory ---")
    for _Pokemon in _PlayerProfile["_PokemonInventory"]:
        print(_GetPokemonInfo(_Pokemon))
    print(f"Poke Balls: {_PlayerProfile["_Pokeballs"]} | Health Potions: {_PlayerProfile["_HealthPotion"]}")
def _ShowHistory(_PlayerProfile):
    print("\n--- Combat History ---")
    for _Combat in _PlayerProfile["_History"]:
        print(_Combat)
def _ChoosePokemon(_PlayerProfile):
    print("Choose your Pokemon")
    for _Index in range(len(_PlayerProfile["_PokemonInventory"])):
        print(f"{_Index} {_GetPokemonInfo(_PlayerProfile["_PokemonInventory"][_Index])}")
    while True:
        try:
            _Chosen = _PlayerProfile["_PokemonInventory"][int(input("Which one do you choose? "))]
            if _Chosen["_CurrentHealth"] > 0:
                return _Chosen
            print("That Pokemon has no health")
        except (ValueError, IndexError):
            print("Wrong answer")
def _GetAttacks(_Pokemon):
    # Only the attacks available at its level, and only the last 4
    _Attacks = [_Attack for _Attack in _Pokemon["_Attacks"] if _Attack["_Power"] > 0 and int(_Attack["_Nv"] or 1) <= _Pokemon["_Level"]]
    return _Attacks[-4:] or [_Struggle]
def _Attack(_Attacker, _Defender, _Attack):
    _Damage = _Attack["_Power"] / 3 + _Attacker["_Level"] * 2
    if _Attack["_Type"] in _Attacker["_Type"]: # Same type as the Pokemon: attack x1.5
        _Damage *= 1.5
    if any(_Type in _SuperEffective.get(_Attack["_Type"], []) for _Type in _Defender["_Type"]):
        _Damage *= 2
        print("It's super effective!")
    _Damage = int(_Damage * random.uniform(0.8, 1.2))
    _Defender["_CurrentHealth"] = max(0, _Defender["_CurrentHealth"] - _Damage) # Health never goes below 0
    print(f"{_Attacker["_Name"]} uses {_Attack["_Name"]}: {_Defender["_Name"]} loses {_Damage} Hp")
def _PlayerAttack(_PlayerPokemon, _EnemyPokemon):
    _Attacks = _GetAttacks(_PlayerPokemon)
    for _Index in range(len(_Attacks)):
        print(f"{_Index} {_Attacks[_Index]["_Name"]} | {_Attacks[_Index]["_Type"]} | Power {_Attacks[_Index]["_Power"]}")
    while True:
        try:
            _Attack(_PlayerPokemon, _EnemyPokemon, _Attacks[int(input("Which attack? "))])
            return
        except (ValueError, IndexError):
            print("Wrong answer")
def _EnemyAttack(_EnemyPokemon, _PlayerPokemon):
    _Attack(_EnemyPokemon, _PlayerPokemon, random.choice(_GetAttacks(_EnemyPokemon)))
def _CurePokemon(_PlayerProfile, _PlayerPokemon):
    if _PlayerProfile["_HealthPotion"] == 0:
        print("You don't have Health Potions")
        return
    _PlayerProfile["_HealthPotion"] -= 1
    _PlayerPokemon["_CurrentHealth"] = min(_PlayerPokemon["_BaseHealth"], _PlayerPokemon["_CurrentHealth"] + 50)
    print(f"{_PlayerPokemon["_Name"]} has been cured: {_PlayerPokemon["_CurrentHealth"]}/{_PlayerPokemon["_BaseHealth"]}")
def _CapturePokemonWithPokeBall(_PlayerProfile, _EnemyPokemon):
    if _PlayerProfile["_Pokeballs"] == 0:
        print("You don't have Poke Balls")
        return False
    _PlayerProfile["_Pokeballs"] -= 1
    # Less health = more probability to capture it
    if random.random() > _EnemyPokemon["_CurrentHealth"] / _EnemyPokemon["_BaseHealth"]:
        _PlayerProfile["_PokemonInventory"].append(_EnemyPokemon)
        print(f"You captured {_EnemyPokemon["_Name"]}!")
        return True
    print(f"{_EnemyPokemon["_Name"]} escaped from the Poke Ball")
    return False
def _Evolve(_Pokemon, _PokemonList):
    _OldName = _Pokemon["_Name"]
    _NewData = _PokemonList[_Evolutions[_Pokemon["_Number"]] - 1]
    _Pokemon["_Number"] = _NewData["_Number"]
    _Pokemon["_Name"] = _NewData["_Name"]
    _Pokemon["_Type"] = _NewData["_Type"]
    _Pokemon["_Attacks"] = _NewData["_Attacks"]
    print(f"{_OldName} evolved into {_Pokemon["_Name"]}!")
def _AssignExperience(_AttackHistory, _EnemyPokemon, _PokemonList):
    for _Pokemon in _AttackHistory:
        _Points = _EnemyPokemon["_Level"] * random.randint(5, 10) # Stronger enemies give more experience
        _Pokemon["_CurrentExp"] += _Points
        print(f"{_Pokemon["_Name"]} gets {_Points} Exp")
        while _Pokemon["_CurrentExp"] >= _Pokemon["_Level"] * 10:
            _Pokemon["_CurrentExp"] -= _Pokemon["_Level"] * 10
            _Pokemon["_Level"] += 1
            _Pokemon["_BaseHealth"] += 10
            _Pokemon["_CurrentHealth"] = _Pokemon["_BaseHealth"]
            print(f"Your Pokemon has upgraded {_GetPokemonInfo(_Pokemon)}")
            if _Pokemon["_Level"] in [10, 20] and _Pokemon["_Number"] in _Evolutions:
                _Evolve(_Pokemon, _PokemonList)
def _Fight(_PlayerProfile, _EnemyPokemon, _PokemonList):
    print("\n--- New Combat ---")
    _AttackHistory = []
    _Result = "Lost"
    _PlayerPokemon = _ChoosePokemon(_PlayerProfile)
    while _AnyPlayerPokemonLives(_PlayerProfile) and _EnemyPokemon["_CurrentHealth"] > 0:
        print(f"\nYou: {_GetPokemonInfo(_PlayerPokemon)}\nEnemy: {_GetPokemonInfo(_EnemyPokemon)}")
        _Action = None
        while _Action not in ["A", "P", "L", "C", "I", "H"]:
            _Action = input("What do you want to do?\n - (A) Attack\n - (P) Poke Ball\n - (L) Life Potion\n - (C) Change Pokemon\n - (I) Inventory\n - (H) History\n").upper()
        if _Action == "A":
            _PlayerAttack(_PlayerPokemon, _EnemyPokemon)
            if _PlayerPokemon not in _AttackHistory:
                _AttackHistory.append(_PlayerPokemon)
        elif _Action == "L":
            _CurePokemon(_PlayerProfile, _PlayerPokemon)
        elif _Action == "P":
            if _CapturePokemonWithPokeBall(_PlayerProfile, _EnemyPokemon):
                _Result = "Captured"
                break
        elif _Action == "C":
            _PlayerPokemon = _ChoosePokemon(_PlayerProfile)
        elif _Action == "I":
            _ShowInventory(_PlayerProfile)
            continue # Looking doesn't use your turn
        elif _Action == "H":
            _ShowHistory(_PlayerProfile)
            continue
        if _EnemyPokemon["_CurrentHealth"] > 0:
            _EnemyAttack(_EnemyPokemon, _PlayerPokemon)
        if _PlayerPokemon["_CurrentHealth"] == 0 and _AnyPlayerPokemonLives(_PlayerProfile):
            print(f"{_PlayerPokemon["_Name"]} can't fight anymore")
            _PlayerPokemon = _ChoosePokemon(_PlayerProfile)
    if _EnemyPokemon["_CurrentHealth"] == 0:
        _Result = "Won"
    if _Result in ["Won", "Captured"]:
        _AssignExperience(_AttackHistory, _EnemyPokemon, _PokemonList)
        _Prize = random.choice(["_Pokeballs", "_HealthPotion", None]) # Prize draw at the end of the combat
        if _Prize:
            _PlayerProfile[_Prize] += 1
            print(f"You won one more {_Prize[1:]}!")
    _PlayerProfile["_History"].append(f"Combat {_PlayerProfile["_Combats"]}: {_Result} vs {_EnemyPokemon["_Name"]} Lvl {_EnemyPokemon["_Level"]}")
    input("Press ENTER to continue")
    print("--- Combat Done ---")
# -------------------------------------------------------------------------------- Main Function
def _MainFinalProject():
    _ClearTerminal()
    _EngineSpeak("\nRunning")
    _PokemonList = _AllPokemonLoads(151)
    _PlayerProfile = _GetPlayerProfile(_PokemonList)
    while _AnyPlayerPokemonLives(_PlayerProfile):
        _PlayerProfile["_Combats"] += 1
        _MaxLevel = max([_Pokemon["_Level"] for _Pokemon in _PlayerProfile["_PokemonInventory"]])
        _EnemyPokemon = _NewPokemon(random.choice(_PokemonList), random.randint(1, _MaxLevel)) # Enemy grows with you
        _Fight(_PlayerProfile, _EnemyPokemon, _PokemonList)
    print(f"You have lost on combat {_PlayerProfile["_Combats"]}")
    _ShowHistory(_PlayerProfile)
# -------------------------------------------------------------------------------- Run Program
if __name__ == "__main__":
    _MainFinalProject()
