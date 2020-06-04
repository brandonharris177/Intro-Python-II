class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move_room(self, direction):
        new_room = getattr(self.current_room, f'{direction}_to')
        if not new_room:
            print('\nYou cannot move in that direction!')
        else:
            self.current_room = new_room