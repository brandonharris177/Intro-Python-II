class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item)
    
    def __repr__(self):
        return "{self.name}, {self.description}".format(self=self)