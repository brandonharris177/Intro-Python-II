from room1 import Room
from player1 import Player

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance",
    "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
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



player = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )

while not user == "q":
    if user in ["n", "s", "e", "w"]:
	    player.move_room(user)

    user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )
    
print("Game Ended thank you for playing")



	
	






# from player1 import Player

# class Room:
#     def __init__(self, name, description, n_to = False,  s_to = False,  e_to = False,  w_to = False):
#         self.name = name
#         self.description = description
#         self.n_to = n_to
#         self.s_to = s_to
#         self.e_to = e_to
#         self.w_to = w_to

    
#     def __repr__(self):
#         return "{self.name}, {self.description}".format(self=self)

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# player = Player(room['outside'])

# user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )


# print(f"you find yourself in the {player.current_room.name} {player.current_room.description} ")

# while not user == "q":
#     print(f"you find yourself in the {player.current_room.name} {player.current_room.description} ")

#     if user in ["n", "s", "e", "w"]:
#         direction = user
#         player.move(direction)
#     else:
#         print("incorrect input")
    
#     user = input("\n Options for travel are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n\n In what direction would you like to travel: " )

# print("Game Ended thank you for playing")