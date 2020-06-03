from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Rick Sanchz", "outside")
# print(player1.name, player1.room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(room["outside"])

user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )

while not user == "q":
    if player1.room == "outside":
        if user == "n":
           player1.room = "foyer"
           user = ""
        if user == "s":
            print("nothing ventured nothing gained")
        if user == "e":
            print("Almost...kind of I mean its 1 in 4")
        if user == "w":
            print("stop stalling")
    
    if player1.room == "foyer":
        if user == "n":
           player1.room = "overlook"
           user = ""
        if user == "s":
           player1.room = "outside"
           user == ""
        if user == "e":
           player1.room = "narrow"
           user == ""
        if user == "w":
            print("to the west ye behold an yonder wall")

    if player1.room == "overlook":
        if user == "n":
           print("You step off the edge and tumble to your death")
        if user == "s":
           player1.room = "foyer"
           user == ""
        if user == "e":
           print("You step confidently into the abyss")
        if user == "w":
           print("sharp rocks line the ocean under your decent but wait!! a single patch of water between the murderous spikes, you try to turn your aim towards it even as you hurl to the earth")

    if player1.room == "narrow":
        if user == "n":
           player1.room = "treasure"
           user == ""
        if user == "s":
           print("you bang your head on the wall")
        if user == "e":
           print("thou knockest thine noggin")
        if user == "w":
           player1.room = "foyer"
           user == ""

    if player1.room == "treasure":
        if user == "n":
           print("wall")
        if user == "s":
           player1.room = "narrow"
           user == ""
        if user == "e":
           print("another wall")
        if user == "w":
           print("still a wall")

    print(f"You find yourself in the {room[player1.room]}")

    user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )
    
print("Game Ended thank you for playing")
