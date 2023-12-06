# develop a system for the booking of tickets for movie
from threater import Threater
from movie import Movie
from customer import Customer
from booking import Booking

    
# Creating instance of threater class
threater1 = Threater('Shama', 'Mardan', 200)
threater2 = Threater('Gul', 'Takht Bhai', 100)

# creating instances of movie class
movie1 = Movie('Don', '2hr 15min', 300)
movie2 = Movie('Tere Naam', '3hr', 500)

# creating instances of customer class
customer1 = Customer('Khan gul', 'khangul@gmail.com', 'EasyPaisa')
customer2 = Customer('Khan sad', 'khansad123@gmail.com', 'Bank Payment')

while True:
    print('''
                  *** Login ***
          
          ''')
    name = input('Name: ')
    Email = input('Email: ')
    paymethd = input('Payment Method: ')
    
    customer1 = Customer(name, Email, paymethd)
    print('login Successful!')
    break

while True:
    print(f'''
          
        *******_____||\\\///|| Welcome to the Ticket Booking System for Movies ||\\\///||_____********

        Here is the list of movies and threaters:

        1.  {movie1}     ,    {threater1}

        2.  {movie1}     ,    {threater2}

        3.  {movie2}     ,    {threater1}

        4.  {movie2}     ,    {threater2}
        
        5.  Exit

          ''')
    usr = int(input('Enter your choice: '))
    
    if usr == 1: 
        ticket1 = Booking(customer1, movie1, threater1)
        print(ticket1)
    elif usr == 2:
        ticket2 = Booking(customer1, movie1, threater2)
        print(ticket2)
    elif usr == 3:
        ticket3 = Booking(customer1, movie2, threater1)
        print(ticket3)
    elif usr == 4:
        ticket4 = Booking(customer1, movie2, threater2)
        print(ticket4)
    elif usr == 5:
        print('Good bye!')
        break
    else:
        print('Invalid Input!')