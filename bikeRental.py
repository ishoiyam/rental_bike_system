import datetime

class BikeRental:
    def __init__(self, stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock

    def display_stock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print(f"We have currently {self.stock} bikes available to rent.")
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return None

        else:
            now = datetime.datetime.now()
            print(f"You have rented a {n} bike(s) on hourly basis today at {now.hour} hours.")
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")

    def rent_bike_on_daily_basis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {n} bike(s) on daily basis today at {now.hour} hours.")
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rent_bike_on_weekly_basis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bike available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike(s) on weekly basis today at {now.hour} hours.")
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def return_bike(self, request):
        """
        1. Accept a rented Bike from customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += nomOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes

            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            if (3 <= numOfBikes <= 5):
                print("You are eligible for family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print(f"That would be ${bill}")
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def renquest_bike(self):
        """
        Takes a request from the customer for the number of bikes.
        """

        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def return_bike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime , self.rentalBasis, self.bikes
        else:
            return 0, 0, 0
