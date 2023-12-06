# develop a system for the booking of tickets for movie
from threater import threater1, threater2
from movie import movie1, movie2
from customer import Customer
from booking import Booking


# Loop for log in
def logIn():
    while True:
        print('''
                  *** Login ***
          
          ''')
        name = input('Name: ')
        Email = input('Email: ')
        paymethd = input('Payment Method: ')
    
        print('login Successful!')
        break
    return Customer(name, Email, paymethd)
    

# Main Loop
def main():
    customer1 =logIn()
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
            if remaining_seats < 0 or remaining_seats > threater1.capacity:
                print('Seats Not Available')
            else:
                ticket1 = Booking(customer1, movie1, threater1, no_tickets)
                print(ticket1,'\n','Reamaining Seats: ', remaining_seats)

        elif usr == 2:
            no_tickets = int(input('No of Tickets: '))
            remaining_seats = threater2.seat_update(no_tickets)
            if remaining_seats < 0 or remaining_seats > threater2.capacity:
                print('Seat Not Available!')
            else:
                ticket2 = Booking(customer1, movie1, threater2, no_tickets)
                print(ticket2)
                print('Remaing Seats: ', remaining_seats)
            
        elif usr == 3:
            no_tickets = int(input('No of Tickets: '))
            remaining_seats = threater1.seat_update(no_tickets)
            if remaining_seats < 0 or remaining_seats > threater1.capacity:
                print('Seat Not Available!')
            else:
                ticket3 = Booking(customer1, movie2, threater1, no_tickets)
                print(ticket3)
                print('Remaing Seats: ', remaining_seats)
        elif usr == 4:
            no_tickets = int(input('No of Tickets: '))
            remaining_seats = threater2.seat_update(no_tickets)
            if remaining_seats < 0 or remaining_seats > threater2.capacity:
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

main()
