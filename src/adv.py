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

username = input("Welcome Hero please input your name: ")

player = Player(username, room['outside'], [])

def look_around():
    print(f"You find yourself in the {player.current_room.name} {player.current_room.description}")
    if len(player.current_room.items):
        print("looking around you you see:")
        for item in range(len(player.current_room.items)):
            print(f"a {player.current_room.items[item]}")

look_around()

user = input("\n Options are: \n\n [n] - travel North \n [s] - travel South \n [e] - travel East \n [w] - travel West \n [q] - quit \n [get/take (item)] - pick up item \n [drop (item)] \n [i] - list current inventory \n [l] - look around \n\n What would you like to do: " )

while not user == "q":

    if user in ["n", "s", "e", "w"]:
        player.move(user)
        look_around()
    elif user == "i":
        print(player.inventory)
    elif user == "l":
        look_around()
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
                print(f"{user_split[1]} is not in your inventory")
        else:
            print("Invalid input")
    else:
        print("Invalid input")


    user = input("\n Options are: \n\n [n] - travel North \n [s] - travel South \n [e] - travel East \n [w] - travel West \n [q] - quit \n [get/take (item)] - pick up item \n [drop (item)] \n [i] - list current inventory \n [l] - look around \n\n What would you like to do: " )

print("Game Ended thank you for playing")