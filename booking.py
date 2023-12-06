# create a Booking class where customer can book for a movie
from threater import Threater
class Booking:
    def __init__(self, customer, movie , threater, seats = 1):
        self.customer = customer
        self.movie = movie
        self.threater = threater
        self.seats = seats

    def __str__(self):
        return f'You {self.customer} successfully book for {self.movie} in threater {self.threater}'
    
    