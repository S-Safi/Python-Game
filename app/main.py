import os
saveDirectory = "saves"
roomDirectory = "rooms"

def getSaveFilePath(username):
    return saveDirectory + '/' + username + ".txt"

def getRoomFilePath(roomName):
    return roomDirectory + '/' + roomName + ".txt"

def cls():
    os.system('cls')

class Room:
    def __init__(self, id, text, options, visited):
        self.id = id
        self.text = text
        self.options = options
        self.visited = visited

class Option:
    def __init__(self, text, id):
        self.text = text
        self.id = id

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class RoomData:
    def __init__(self, id, visited):
        self.id = id
        self.visited = visited

class GameData:
    def __init__(self, room, health, rooms):
        self.room = room
        self.health = health
        self.rooms = rooms

def readRoom(roomName):
    f = open(getRoomFilePath(roomName), "r")
    line = f.readline().rstrip()
    fullText = ''
    while line != "---":
        fullText = fullText + line
        line = f.readline().rstrip()
    options = {}
    i = 1
    line = f.readline().rstrip()
    while line != "|-|":
        Id = f.readline().rstrip()
        options[str(i)] = Option(line, Id)
        line = f.readline().rstrip()
        i += 1
    room = Room(roomName, fullText, options, False)
    return room

def readRooms():
    rooms = {}
    for file in os.listdir("rooms"):
        roomName = file.strip(".txt")
        rooms[roomName] = readRoom(roomName)
    return rooms

def printroom(room):
    print("-----------")
    print(room.text)
    for key in room.options.values():
        print(key.text)
    if room.visited == True:
        print("You have visited this room before") 

def printPlayer(player):
    print(player.name, "Health: " + str(player.health))

def printInstructions():
    cls()
    print("welcome to game test")
    introput = input("Press enter to continue: ")
    while introput != '':
        introput = input()
    cls()

def login():
    cls()
    return input('enter username: ')

def createDir():
    os.mkdir(saveDirectory)

def createRoomData(rooms):
    roomDataArray = []
    for id in rooms.keys():
        temp = RoomData(id, rooms[id].visited)
        roomDataArray.append(temp)
    return roomDataArray

def createGameData(currentRoom, player, rooms):
    roomData = createRoomData(rooms)
    gameData = GameData(currentRoom.id, player.health, roomData)
    return gameData

def saveGameData(username, gameData):
    f = open(getSaveFilePath(username), "w")
    f.write(gameData.room)
    f.write("\n")
    f.write(str(gameData.health))
    f.write("\n")
    for i in gameData.rooms:
        f.write("---\n")
        f.write(i.id)
        f.write("\n")
        f.write("visited: " + str(i.visited))
        f.write("\n")
    f.close()

def loadGameData(username):
    f = open(getSaveFilePath(username), "r")
    room = f.readline().rstrip()
    health = int(f.readline().rstrip())
    gameData = GameData(room, health, [])
    f.close()
    return gameData

def initGameData(username):
    if not os.path.exists(saveDirectory):
        createDir()
    if not os.path.exists(getSaveFilePath(username)):
        gameData = GameData("room-1", 100,[])
        saveGameData(username, gameData)
    else:
        gameData = loadGameData(username)
    return gameData

def playGame():
    username = login()
    gameData = initGameData(username)
    rooms = readRooms()
    printInstructions()
    player = Player(username, gameData.health)
    currentRoomId = gameData.room
    currentRoom = rooms[currentRoomId]
    while True:
        printroom(currentRoom)
        printPlayer(player)
        input1 = input("Input: ")
        if input1 == 'q':
            gameData = createGameData(currentRoom, player, rooms)
            saveGameData(username, gameData)
            cls()
            break
        currentRoom.visited = True
        currentRoom = rooms[currentRoom.options[input1].id]
        cls()
playGame()