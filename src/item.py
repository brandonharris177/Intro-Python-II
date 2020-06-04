class Item:
    def __init__(self, name, description):
        self.name = name 
        self.description = description

    def on_take(self, name):
        print(f"{self.name} you have picked up {self.name}")

    def on_drop(self, name):
        print(f"{self.name}, you have dropped {self.name}")