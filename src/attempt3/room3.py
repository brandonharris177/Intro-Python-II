class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return "looking for this, {self.w_to}".format(self=self)