class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        if hasattr(self.current_room, f"{direction}_to"):
            new_room = getattr(self.current_room, f"{direction}_to")
            self.current_room = new_room
        else:
            print("cannot go that direction")