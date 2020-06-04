class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move(self, direction):
        print(getattr(self.current_room, f"w_to"))
        if getattr(self.current_room, f"{direction}_to") != "False":
            new_room = getattr(self.current_room, f"{direction}_to")
            if new_room:
                self.current_room = new_room
            else:
                print("cannot go this direction")
        else:
            print("cannot go that direction")