# Snake
# ---------- Libraries
import readchar, os, random
# ---------- Clean terminal
os.system("clear")
# ---------- User Position and Tail
_PositionX = 0
_PositionY = 1
_MyPosition = [1, 1]
_TailLen = 0
_Tail = []
# ---------- Objects
_MapObjects = []
_RandomObjects = 10
# ---------- Create X random objects
_MapWidth = 20
_MapHeight = 15
while len(_MapObjects) < _RandomObjects:
    _RandomObject = [random.randint(0, _MapWidth - 1), random.randint(0, _MapHeight - 1)]
    # ---------- Verify if the object is not in User's position
    if _RandomObject not in _MapObjects and _RandomObject != _MyPosition:
        _MapObjects.append(_RandomObject)
# ---------- Obstacles
_ObstacleDefinition = """\
                        
                        
                      ##  
  ####    #########   ##  
  ####    #########   ##  
  #####                   
  ##     ########   ####  
      #####               
       #         #######  
  #    ######             
  #    #########    ####  
  ##     ######        #  
  ###    #####     #####  
  ####    ######      ##  

                        \
"""
# ---------- Create List for Obstacles map
_ObstacleDefinition = [list(_Row) for _Row in _ObstacleDefinition.split("\n")]
_MapWidth = len(_ObstacleDefinition[0])
# Pad all rows to _MapWidth to handle the escaped-newline last row
for _i in range(len(_ObstacleDefinition)):
    while len(_ObstacleDefinition[_i]) < _MapWidth:
        _ObstacleDefinition[_i].append(" ")
# Crop the obstacle grid — remove empty rows and columns from edges, keep 1 cell padding
_CropMinX = _MapWidth - 1
_CropMaxX = 0
_CropMinY = len(_ObstacleDefinition) - 1
_CropMaxY = 0
for _y in range(len(_ObstacleDefinition)):
    for _x in range(len(_ObstacleDefinition[_y])):
        if _ObstacleDefinition[_y][_x] == "#":
            if _x < _CropMinX: _CropMinX = _x
            if _x > _CropMaxX: _CropMaxX = _x
            if _y < _CropMinY: _CropMinY = _y
            if _y > _CropMaxY: _CropMaxY = _y
_CropMinX = max(0, _CropMinX - 1)
_CropMaxX = min(_MapWidth - 1, _CropMaxX + 1)
_CropMinY = max(0, _CropMinY - 1)
_CropMaxY = min(len(_ObstacleDefinition) - 1, _CropMaxY + 1)
_ObstacleDefinition = [_Row[_CropMinX:_CropMaxX+1] for _Row in _ObstacleDefinition[_CropMinY:_CropMaxY+1]]
# ---------- Map
_MapWidth = len(_ObstacleDefinition[0])
_MapHeight = len(_ObstacleDefinition)
# ---------- Infinite Bucle
while True:
    # ---------- Clean terminal
    os.system("clear")
    # ---------- Map with position
    print("+" + "-" * _MapWidth * 3 + "+")
    for _Coordinate_Y in range(_MapHeight):
        print("|", end = "")
        for _Coordinate_X in range(_MapWidth):
            _CharToDraw = "   "
            _ObjectInCell = None
            for _MapObject in _MapObjects:
                if _MapObject[_PositionX] == _Coordinate_X and _MapObject[_PositionY] == _Coordinate_Y:
                    _CharToDraw = " * "
                    _ObjectInCell = _MapObject
            for _TailPice in _Tail:
                if _TailPice[_PositionX] == _Coordinate_X and _TailPice[_PositionY] == _Coordinate_Y:
                    _CharToDraw = " @ "
            if _MyPosition[_PositionX] == _Coordinate_X and _MyPosition[_PositionY] == _Coordinate_Y:
                _CharToDraw = " @ "
                if _ObjectInCell:
                    _MapObjects.remove(_ObjectInCell)
                    _TailLen += 1
                    # ---------- Create a new random object
                    _RandomObject = [random.randint(0, _MapWidth - 1), random.randint(0, _MapHeight - 1)]
                    # ---------- Verify if the object is not in User's position
                    if _RandomObject not in _MapObjects and _RandomObject != _MyPosition and \
                        _ObstacleDefinition[_NewPosition[_PositionY]][_NewPosition[_PositionX]] != "#":
                        _MapObjects.append(_RandomObject)
            if _ObstacleDefinition[_Coordinate_Y][_Coordinate_X] == "#":
                _CharToDraw = "###"
            print("{}".format(_CharToDraw), end = "")
        print("|")
    print("+" + "-" * _MapWidth * 3 + "+")
    print("If you touch your tail, you die")
    print("This are the Objects: {}".format(_MapObjects))
    print("\nThis is your position: {}".format(_MyPosition))
    # ---------- Ask user where he wants to move
    print("This is the Tail's len: {}".format(_TailLen))
    print("\nYou can move with [WASD]\n >> Press [Q] to end the program")
    _Direction = readchar.readchar()
    _Direction = _Direction.upper()
    _NewPosition = None
    if _Direction == "W":
        _NewPosition = [_MyPosition[_PositionX], (_MyPosition[_PositionY] - 1) % _MapHeight]
    elif _Direction == "S":
        _NewPosition = [_MyPosition[_PositionX], (_MyPosition[_PositionY] + 1) % _MapHeight]
    elif _Direction == "A":
        _NewPosition = [(_MyPosition[_PositionX] - 1) % _MapWidth, _MyPosition[_PositionY]]
    elif _Direction == "D":
        _NewPosition = [(_MyPosition[_PositionX] + 1) % _MapWidth, _MyPosition[_PositionY]]
    elif _Direction == "Q":
        break
    if _MyPosition in _Tail: # If you touch your tail, you die
        print("\nYou have died")
        break
    if _NewPosition:
        if _ObstacleDefinition[_NewPosition[_PositionY]][_NewPosition[_PositionX]] != "#":
            _Tail.insert(0, _MyPosition.copy())
            _Tail = _Tail[0:_TailLen]
            _MyPosition = _NewPosition
