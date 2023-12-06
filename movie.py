# create a movie class

class Movie:
    def __init__(self, movie_name, duration, price):
        self.movie_name = movie_name
        self.duration = duration
        self.price = price
    def __str__(self) :
        return f'Movie: {self.movie_name}, Duration: {self.duration}, for Price: {self.price}'