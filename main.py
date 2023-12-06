# develop a system for the booking of tickets for movie
from threater import Threater
from movie import Movie
from customer import Customer
from booking import Booking

list_threaters = []
# Creating instance of threater class
threater1 = Threater('Shama', 'Mardan', 200)
threater2 = Threater('Gul', 'Takht Bhai', 100)
list_threaters.append(threater1)
list_threaters.append(threater2)


# creating instances of movie class
movie1 = Movie('Don', '2hr 15min', 300)
movie2 = Movie('Tere Naam', '3hr', 500)

# creating instances of customer class
customer1 = Customer('Khan gul', 'khangul@gmail.com', 'EasyPaisa')
customer2 = Customer('Khan sad', 'khansad123@gmail.com', 'Bank Payment')


# Loop for log in
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


# Main Loop
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
    
    # Taking Input From User
    usr = int(input('Enter your choice: '))

    # Response to the User Input
    if usr == 1: 
        no_tickets = int(input('No of Tickets: '))
        remaining_seats = threater1.seat_update(no_tickets)
        if remaining_seats < 0:
            print('Seats Not Available')
        else:
            ticket1 = Booking(customer1, movie1, threater1, no_tickets)
            print(ticket1,'\n','Reamaining Seats: ', remaining_seats)

    elif usr == 2:
        no_tickets = int(input('No of Tickets: '))
        remaining_seats = threater2.seat_update(no_tickets)
        if remaining_seats < 0:
            print('Seat Not Available!')
        else:
            ticket2 = Booking(customer1, movie1, threater2, no_tickets)
            print(ticket2)
            print('Remaing Seats: ', remaining_seats)
            
    elif usr == 3:
        no_tickets = int(input('No of Tickets: '))
        remaining_seats = threater1.seat_update(no_tickets)
        if remaining_seats < 0:
            print('Seat Not Available!')
        else:
            ticket3 = Booking(customer1, movie2, threater1, no_tickets)
            print(ticket3)
            print('Remaing Seats: ', remaining_seats)
    elif usr == 4:
        no_tickets = int(input('No of Tickets: '))
        remaining_seats = threater2.seat_update(no_tickets)
        if remaining_seats < 0:
            print('Seat Not Available!')
        else:
            ticket4 = Booking(customer1, movie2, threater2, no_tickets)
            print(ticket4)
            print('Remaing Seats: ', remaining_seats)
    elif usr == 5:
        print('Good bye!')
        break

    
    else:
        print('Invalid Input!')

