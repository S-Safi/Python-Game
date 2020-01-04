import os

def cls():
    os.system('cls')

class Room:
    def __init__(self, id, text, options):
        self.id = id
        self.text = text
        self.options = options

def printroom(room):
           print("-----------")
           print(room.text)

class Option:
    def __init__(self, text, id):
        self.text = text
        self.id = id

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class GameData:
    def __init__(self, room, health):
        self.room = room
        self.health = health

def decideUponOption(option):
    if option == "dead":
        printInstructions()
    elif option == "won":
        printInstructions()

rooms = {
    "room-1": Room("room-1", "You are in room 1", options = {
        "1": Option("1. Go West", "room-2"),
        "2": Option("2. Go East", "room-3")
    }),
    "room-2": Room("room-2", "You are in room 2", options = {
        "1": Option("1. Go West", "room-4"),
        "2": Option("2. Go East", "room-1")
    }),
    "room-3": Room("room-3", "You are in room 3", options = {
        "1": Option("1. Go West", "room-1"),
        "2": Option("2. Go East", "room-5")
    }),
    "room-4": Room("room-4", "You are in room 4", options = {
        "r": Option("r. you have died, press r to restart", "dead")
    }),
    "room-5": Room("room-5", "You are in room 5", options = {
        "r": Option("r. you win, press r to restart", "won")
    })
}

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

def saveGameData(username, gameData):
    f = open(username + ".txt", "w")
    f.write(gameData.room)
    f.write("\n")
    f.write(str(gameData.health))
    f.write("\n")
    f.close


def loadGameData(username):
    f = open(username + ".txt", "r")
    room = f.readline().rstrip()
    health = int(f.readline().rstrip())
    gameData = GameData(room, health)
    f.close
    return gameData

def initGameData(username):
    if not os.path.exists(username + ".txt"):
        gameData = GameData("room-1", 100)
        saveGameData(username, gameData)
    else:
        gameData = loadGameData(username)
    return gameData

def playGame():
    username = login()
    gameData = initGameData(username)
    printInstructions()
    player = Player(username, gameData.health)
    currentRoomId = gameData.room
    currentRoom = rooms[currentRoomId]
    while True:
        printroom(currentRoom)
        for key in currentRoom.options.values():
            print(key.text)
        print(player.name, "Health: " + str(player.health))
        input1 = input("Input: ")
        if input1 == 'q':
            saveGameData(username, GameData(currentRoom.id, player.health))
            cls()
            break
        if currentRoom.options[input1].id in rooms.keys():
            currentRoom = rooms[currentRoom.options[input1].id]
        else:
            decideUponOption(currentRoom.options[input1].id)
        cls()

playGame()