# create a threater class
class Threater:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
    def __str__(self) :
        return f'Threater: {self.name}, Location: {self.location}, Capacity: {self.capacity}'
# method for display movie
    def display(self):
        pass