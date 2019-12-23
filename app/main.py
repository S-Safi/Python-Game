import os
import os.path
from os import path


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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

def decideUponOption(option):
    if option == "dead":
        start()
    elif option == "won":
        start()

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

playing = True

def start():
    cls()
    print("welcome to game test")
    introput = input("Press enter to continue: ")
    while introput != '':
        introput = input()
    cls()

username = input('enter username: ')
if path.exists(username + ".txt"):
    f = open(username + ".txt", "r")
    currentRoom = rooms[f.readline().rstrip()]
    player = Player(username, f.readline().rstrip())
else:
    currentRoom = rooms["room-1"]
    f = open(username + ".txt", "w")
    f.write(currentRoom.id)
    f.write("\n")
    f.write("100")
    f.close
    player = Player(username, "100")

start()
while playing:
    printroom(currentRoom)
    for key in currentRoom.options.values():
        print(key.text)
    print(player.name, "Health: " + player.health)
    input1 = input("Input: ")
    if input1 == 'q':
        f = open(username + ".txt", "w")
        f.write(currentRoom.id)
        f.write("\n")
        f.write(player.health)
        f.close
        break
    if currentRoom.options[input1].id in rooms.keys():
        currentRoom = rooms[currentRoom.options[input1].id]
    else:
        decideUponOption(currentRoom.options[input1].id)
        currentRoom = rooms["room-1"]
    cls()