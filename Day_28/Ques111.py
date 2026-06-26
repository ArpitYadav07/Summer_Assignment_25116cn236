# Ticket Booking System
tickets = 50

book = int(input("How many tickets: "))

if book <= tickets:
    tickets -= book
    print("Booked Successfully")
else:
    print("Not Available")