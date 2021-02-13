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
            print(f"You have rented {n} bike(s) on hourly basis today at {now.hour} hours.")
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rent_bike_on_daily_basis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike(s) on daily basis today at {now.hour) hours.")
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
            print(f"Sorry! We have currenly {self.stock} bikes available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented {n} bike(s) on weekly basis today at {now.hour} hours.")
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def return_bike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """

        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
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

    def request_bike(self):
        """

        """

