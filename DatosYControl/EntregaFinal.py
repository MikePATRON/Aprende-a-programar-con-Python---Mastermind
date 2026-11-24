# Entrega Pokemon Snake
# ---------- Libraries
import readchar, os, random
# ---------- Clean terminal
os.system("clear")
print("This is a 'TRON Disc War' Game")
# ---------- User Position
_Position_X = 0
_Position_Y = 1
_MyPosition = [1, 1]
# ---------- Map
_ObstacleDefinition = """\
                        
 ##########   ########## 
 #                    ## 
 # ###    #########   ## 
 #####    #########   ## 
 #####                 # 
  ##     ########   #### 
    #  #####             
    #  #         ####### 
 #    ######           # 
 #    #########     #### 
 ##     ######         # 
 ###    #####      ##### 
 ####    ######       ## 
                         \
"""
# ---------- Convert Obstacle string to list of rows
_ObstacleDefinition = [list(_Row) for _Row in _ObstacleDefinition.split("\n")]
# ---------- Pad all rows to the same width
_MapWidth = len(_ObstacleDefinition[0])
for _i in range(len(_ObstacleDefinition)):
    while len(_ObstacleDefinition[_i]) < _MapWidth:
        _ObstacleDefinition[_i].append(" ")
# ---------- Map Dimensions from obstacle grid
_MapWidth = len(_ObstacleDefinition[0])
_MapHeight = len(_ObstacleDefinition)
# ---------- Ensure starting position is not a wall
while _ObstacleDefinition[_MyPosition[_Position_Y]][_MyPosition[_Position_X]] == "#":
    _MyPosition = [random.randint(0, _MapWidth - 1), random.randint(0, _MapHeight - 1)]
# ---------- Masters
_Masters = []
_RandomMasters = 5
# ---------- Create X random Masters
while len(_Masters) < _RandomMasters:
    _RandomMaster = [random.randint(0, _MapWidth - 1), random.randint(0, _MapHeight - 1)]
    # ---------- Verify if the object is not in User's position or inside a wall
    if _RandomMaster not in _Masters and _RandomMaster != _MyPosition and \
        _ObstacleDefinition[_RandomMaster[_Position_Y]][_RandomMaster[_Position_X]] != "#":
        _Masters.append(_RandomMaster)
# ---------- Disc Wars initial HP
_MasterStartHP = 50
_PlayerStartHP = 80
# ---------- Infinite Bucle
while True:
    # ---------- Clean terminal
    os.system("clear")
    # ---------- Map with position
    print("+" + "-" * _MapWidth * 3 + "+") # Map top border
    for _Coordinate_Y in range(_MapHeight):
        print("|", end = "") # Map left border
        for _Coordinate_X in range(_MapWidth):
            _CharToDraw = "   " # Map Spaces
            for _Master in _Masters:
                if _Master[_Position_X] == _Coordinate_X and _Master[_Position_Y] == _Coordinate_Y: # Print Master in Map
                    _CharToDraw = " * "
            if _MyPosition[_Position_X] == _Coordinate_X and _MyPosition[_Position_Y] == _Coordinate_Y: # Print Player
                _CharToDraw = " @ "
            if _ObstacleDefinition[_Coordinate_Y][_Coordinate_X] == "#": # Print Obstacle
                _CharToDraw = "###"
            print("{}".format(_CharToDraw), end = "")
        print("|")
    print("+" + "-" * _MapWidth * 3 + "+") # Map bottom border
    print("Masters: {}  |  Defeated: {}/{}".format(len(_Masters), _RandomMasters - len(_Masters), _RandomMasters))
    print(chr(10) + "This is your position: {}".format(_MyPosition))
    # ---------- Ask user where he wants to move
    print(chr(10) + "You can move with [WASD]" + chr(10) + " >> Press [Q] to end the program")
    _Direction = readchar.readchar()
    _Direction = _Direction.upper()
    _NewPosition = None
    if _Direction == "W":
        _NewPosition = [_MyPosition[_Position_X], (_MyPosition[_Position_Y] - 1) % _MapHeight]
    elif _Direction == "S":
        _NewPosition = [_MyPosition[_Position_X], (_MyPosition[_Position_Y] + 1) % _MapHeight]
    elif _Direction == "A":
        _NewPosition = [(_MyPosition[_Position_X] - 1) % _MapWidth, _MyPosition[_Position_Y]]
    elif _Direction == "D":
        _NewPosition = [(_MyPosition[_Position_X] + 1) % _MapWidth, _MyPosition[_Position_Y]]
    elif _Direction == "Q":
        break
    if _NewPosition:
        if _ObstacleDefinition[_NewPosition[_Position_Y]][_NewPosition[_Position_X]] != "#":
            _MyPosition = _NewPosition
            # ---------- Check if player landed on a Master -> TRON: Disc Wars
            if _MyPosition in _Masters:
                print(chr(10) + "TRON: Disc Wars")
                input("Press ENTER to start the battle ")
                _PlayerHP = _PlayerStartHP
                _MasterHP = _MasterStartHP
                while _PlayerHP > 0 and _MasterHP > 0:
                    os.system("clear")
                    # ---------- Player's turn (Sam Flynn - you)
                    print("Sam Flynn's turn")
                    _PlayerBarPct = _PlayerHP / _PlayerStartHP
                    _PlayerBar = "Sam Flynn's life [" + (round((_PlayerBarPct * 10)) * '⣿') + "] " + str(int(_PlayerBarPct * 100))
                    print(_PlayerBar)
                    _MasterBarPct = _MasterHP / _MasterStartHP
                    if _MasterBarPct < 0:
                        _MasterBarPct = 0
                    _MasterBar = "Master's life [" + (round((_MasterBarPct * 10)) * '⣿') + "] " + str(int(_MasterBarPct * 100))
                    print(_MasterBar)
                    _PlayerAttack = None
                    while _PlayerAttack not in ["0", "1", "2", "3"]:
                        _PlayerAttack = input("\nWhich attack do you want to perform?" + chr(10) +
                                        "0 - Bouncing" + chr(10) +
                                        "1 - Floor" + chr(10) +
                                        "2 - Direct" + chr(10) +
                                        "3 - Nothing" + chr(10) +
                                        chr(10) +
                                        ">> Answer [0/1/2/3]: ")
                    os.system("clear")
                    _PlayerAttack = int(_PlayerAttack)
                    if _PlayerAttack == 0:
                        _MasterHP -= 10
                        print(chr(10) + "Sam Flynn attacks bouncing")
                    elif _PlayerAttack == 1:
                        _MasterHP -= 11
                        print(chr(10) + "Sam Flynn attacks the floor")
                    elif _PlayerAttack == 2:
                        _MasterHP -= 12
                        print(chr(10) + "Sam Flynn attacks Direct")
                    else:
                        print(chr(10) + "Sam Flynn does Nothing")
                    _MasterBarPct = _MasterHP / _MasterStartHP
                    if _MasterBarPct < 0:
                        _MasterBarPct = 0
                    _MasterBar = "Master's life [" + (round((_MasterBarPct * 10)) * '⣿') + "] " + str(int(_MasterBarPct * 100))
                    print(_MasterBar)
                    if _MasterHP <= 0:
                        break
                    # ---------- Master's turn (auto-attack)
                    print(chr(10) + "Master's turn")
                    _MasterAttack = random.randint(0, 2)
                    if _MasterAttack == 0:
                        _PlayerHP -= 10
                        print(chr(10) + "Master attacks with Tackle")
                    elif _MasterAttack == 1:
                        _PlayerHP -= 11
                        print(chr(10) + "Master attacks the Floor")
                    else:
                        _PlayerHP -= 12
                        print(chr(10) + "Master attacks Direct")
                    _PlayerBarPct = _PlayerHP / _PlayerStartHP
                    if _PlayerBarPct < 0:
                        _PlayerBarPct = 0
                    _PlayerBar = "Sam Flynn's life [" + (round((_PlayerBarPct * 10)) * '⣿') + "] " + str(int(_PlayerBarPct * 100))
                    print(_PlayerBar)
                    _MasterBarPct = _MasterHP / _MasterStartHP
                    if _MasterBarPct < 0:
                        _MasterBarPct = 0
                    _MasterBar = "Master's life [" + (round((_MasterBarPct * 10)) * '⣿') + "] " + str(int(_MasterBarPct * 100))
                    print(_MasterBar)
                if _PlayerHP > 0:
                    print(chr(10) + "You defeated the Master!")
                    _Masters.remove([_MyPosition[_Position_X], _MyPosition[_Position_Y]])
                    input("Press ENTER to continue ")
                else:
                    print(chr(10) + "You were defeated...")
                    break
            # ---------- Check if all masters defeated
            if len(_Masters) == 0:
                os.system("clear")
                print("+" + "=" * 30 + "+")
                print("|      YOU BEAT ALL MASTERS!      |")
                print("+" + "=" * 30 + "+")
                break
