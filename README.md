# Python-Game
First version

## Phase 1
* Text only
* Rooms
* Choose your own adventure
* end states
* enter q to quit
* Intro screen

## Phase 2
* save current room
* Write and read save file

## Phase 3
* different users

## later points
* inventory
* fights
* text visuals
* listen for events

## planning

Room

* identifier
* text
* options

example:

```
identifier:" room-1"
text: "you are in room 1"
options: [
    { text: "Go west", identifier: "room-2" }, 
    { text: "Go east", identifier: "room-3" } 
]
```

```
identifier:" room-2"
text: "you are in room 2, you won"
options: [
    { text: "Return to start", identifier: "room-2" }, 
]
```

## step 1
* read input, echo
* add end state

## step 2
* create a room class with identifier and text only
* create a room
* write a function printroom
* each time in the loop print the room

## step 3
* create a dictionary with 3 rooms
* in the main loop print room 2

## step 4
* accept the roomid as input
* print that room

