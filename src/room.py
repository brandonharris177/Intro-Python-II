# Add the ability to add items to rooms.
# The Room class should be extended with a list that holds the Items that are currently in that room.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    
    def __repr__(self):
        return "{self.name}, {self.description}".format(self=self)