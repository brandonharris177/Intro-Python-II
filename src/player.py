# Add capability to add Items to the player's inventory. The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.

class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move(self, direction):
        if hasattr(self.current_room, f"{direction}_to"):
            new_room = getattr(self.current_room, f"{direction}_to")
            self.current_room = new_room
        else:
            print("Cannot go that direction")

    def take_item(self, item):
        self.inventory.append(item)
        print(f"You have picked up {item}")

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"You have dropped {item}")