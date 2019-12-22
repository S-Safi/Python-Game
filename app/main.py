class Room:
    def __init__(self, id, text):
        self.id = id
        self.text = text

def printroom(room):
           print("-----------")
           print(room.text)
           print("")


rooms = {
    "room-1": Room("room-1", "You are in room 1"),
    "room-2": Room("room-2", "You are in room 2"),
    "room-3": Room("room-3", "You are in room 3")
}

playing = True

while playing:
    input1 = input("Input: ")
    if input1 == 'q':
        break
    printroom(rooms[input1])
    

