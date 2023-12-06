# create a movie class

class Movie:
    def __init__(self, movie_name, duration, price):
        self.movie_name = movie_name
        self.duration = duration
        self.price = price
    def __str__(self) :
        return f'Movie: {self.movie_name}, Duration: {self.duration}, for Price: {self.price}'
    

    
# creating instances of movie class
movie1 = Movie('Don', '2hr 15min', 300)
movie2 = Movie('Tere Naam', '3hr', 500)