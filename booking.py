# create a Booking class where customer can book for a movie

class Booking:
    def __init__(self, customer, movie , threater):
        self.customer = customer
        self.movie = movie
        self.threater = threater

    def __str__(self):
        return f'You {self.customer} successfully book for {self.movie} in threater {self.threater}'