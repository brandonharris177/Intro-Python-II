from player import Player
from room import Room
from item import Item

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["rock", "stick"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["candle", "clock"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["telescope", "flag"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["quill", "club"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["chocolate_coins", "foam_sword"]),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.

# Add a new type of sentence the parser can understand: two words.
# Until now, the parser could just understand one sentence form:
# verb
# such as "n" or "q".
# But now we want to add the form:
# verb object
# such as "take coins" or "drop sword".
# Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.

player = Player("Rick Sanchz", room['outside'], [])

print(f"You find yourself in the {player.current_room.name} {player.current_room.description} looking around you see:")
for item in range(len(player.current_room.items)):
    print(f"a {player.current_room.items[item]}")

user = input("\n Options are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n [get/take (item)] - pick up item \n [drop (item)] \n [i] - list current inventory \n [l] - look around \n\n What would you like to do: " )

while not user == "q":

    if user in ["n", "s", "e", "w"]:
        player.move(user)
    elif user == "i":
        print(player.inventory)
    elif user == "l":
        print(f"You look around and see")
    elif len(user) > 2:
        user_split = user.split(" ")
        if user_split[0] == "get" or user_split[0] == "take":
            if user_split[1] in player.current_room.items: 
                player.current_room.remove_item(user_split[1])
                player.take_item(user_split[1])
            else:
                print(f"{user_split[1]} is not in this room")
        elif user_split[0] == "drop":
            if user_split[1] in player.inventory: 
                player.current_room.add_item(user_split[1])
                player.drop_item(user_split[1])
        else:
            print("Invalid input")
    else:
        print("Invalid input")
    
    print(f"You find yourself in the {player.current_room.name} {player.current_room.description}")
    if len(player.current_room.items):
        print("looking around you you see:")
        for item in range(len(player.current_room.items)):
            print(f"a {player.current_room.items[item]}")


    user = input("\n Options are: \n\n [n] - north \n [s] - south \n [e] - east \n [w] - west \n [q] - quit \n [get/take (item)] - pick up item \n [drop (item)] \n [i] - list current inventory \n [l] - look around \n\n What would you like to do: " )

print("Game Ended thank you for playing")