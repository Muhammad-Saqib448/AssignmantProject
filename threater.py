# create a threater class
from movie import movie1, movie2
list_threaters = []

class Threater:
    def __init__(self, name, location, capacity, *args):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.move = args
        self.seats = capacity
    def __str__(self) :
        return f'Threater: {self.name}, Location: {self.location}, Capacity: {self.capacity}'
# method for display movie
    def display(self):
        pass

    def seat_update(self,seat):
        if seat < self.seats:
            self.seats -= seat
            return self.seats
        else:
            return seat


# Creating instance of threater class
threater1 = Threater('Shama', 'Mardan', 200, movie1, movie2)
threater2 = Threater('Gul', 'Takht Bhai', 100, movie1)
list_threaters.append(threater1)
list_threaters.append(threater2)

print("Welcome to the Threater ticket Booking system.\n\nHere is a list of Threaters:")
for i in list_threaters:
    print(i)
