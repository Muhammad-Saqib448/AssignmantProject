# create a threater class
class Threater:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.seats = capacity
    def __str__(self) :
        return f'Threater: {self.name}, Location: {self.location}, Capacity: {self.capacity}'
# method for display movie
    def display(self):
        pass

    def seat_update(self,seat):
        self.seats -= seat
        return self.seats

        
# threater2 = Threater('Gul', 'Takht Bhai', 100)
# print(threater2.seat_update(100))
