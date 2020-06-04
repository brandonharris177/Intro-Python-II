from player import Player
from room import Room

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(room['outside'])

print(f"You find yourself in the {player.current_room.name} {player.current_room.description} ")

user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )

while not user == "q":

    if user in ["n", "s", "e", "w"]:
        player.move(user)
    else:
        print("invalid input")
    
    print(f"You find yourself in the {player.current_room.name} {player.current_room.description} ")

    user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )

print("Game Ended thank you for playing")