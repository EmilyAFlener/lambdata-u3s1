# This is an file for OOP examples for U3S1M2 assignments.
# I'll attempt to automate an Aloha Valet Services quote intake and generation.

class EventBooking:
    #Basic information for any Aloha event proposal.
    def __init__(self, attendants, cars, guests, parking_avail, account_type):
        self.attendants = attendants
        self.cars = cars
        self.guests = guests
        self.parking_avail = False
        self.account_type = account_type

    #Calculating attendant needs based on car quantity.
    def attendant_needs(self):
        if cars > 40:
            attendants = 2
        elif cars > 60:
            attendants = 3
    
    #Determining level of effort for the event. This could factor into rate.
    def effort_level(self):
        if self.cars < 40:
            easy
        elif self.cars <= 39 & >= 71:
            average
        else self.cars > 70:
            difficult
        
    def rate_type(self)
        if account_type = company:
            rate *  2
        elif account_type = private_event:
            rate * 1.5
        else:
            print('We will be in touch to complete your quote.')

class Venues(EventBooking):
    #Account specific needs for event venue contracts.
    #Should just adjust rates for venue specific contracts?