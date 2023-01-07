#Chapter 9. Working ith classes and instanses
# OOP concepts -
# Class, Object,
# Encapsulation -hiding from the object and child classes
# Inheritance,
# Polymorphism (overriding)
# Abstractions


class Car:
    # 1st thing think about is which attribute - should I add, which one is required
    # 2nd thing is behaviour - what can I do with this class,  how to CRUD -> set (create, update, delete),
    # get (read) and other
    # attributes - required, optional
    # behaviour - CRUD  -> set (create, update, delete),

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.__mileage = 0    # Encapsulation -hiding from the object, child classes -

    def get_description(self):
        """gets all details of the  car"""
        print(f"Car details: \nManufacturer: {self.make}\nModel: {self.model}\nYear: {self.year}")
        print(f"Current mileage of the car: {self.__mileage}")

    def set_mileage(self, new_mileage):    # here when cars new_mileage is greater then cars current mileage (self.mileage)
        """sets the to not less than current mileage"""  # in this case cars self.mileage will be equal to new_mileage
        if new_mileage > self.__mileage:                    # self.mileage = new_mileage
            print('Setting new value of mileage')         # in any other action we should print some warning message
            self.__mileage = new_mileage
        else:
            print("mileage was less then current mileage, cannot be done ")

    def add_to_mileage(self, miles):   # incrementing mileage
        """ increments the mileage with given miles"""
        if miles > 0:
            self.__mileage = self.__mileage + miles
            #self.__mileage += miles    -  its equivalent to above statement
            print(f"{miles} miles was added to your current miles.")
        else:
            print("You cannot enter negative number to increment mileage.")

    def fill_tank(self):
        print("Filling the tank with gas...")
        print("Done! It is ready to hit the road.")


# make = input('enter the make of the car: ')
# model = input('enter the model of the car: ')
# year = input('enter the year of the car: ')
# car2 = Car(make, model, year )


# All executions are commented out to prevent execution when it's imported to another file
car1 = Car('bmw', 'x5', '2022')
# print(car1.make, car1.year+1)
# print("Getters - here we are getting car description")
# car1.get_description()
# print("Setters - here we are updating (setting) values of attributes")
# car1.model = 'x5 M'
# #car1.__mileage = 50  ## since mileage is hidden from the object, now we cannot update the value
# car1.set_mileage(50)
# car1.get_description()
# car1.set_mileage(10)
# car1.get_description()
# #testing scenarios to test add_to_mileage function: input - 100, -15
# car1.add_to_mileage(100)
# car1.get_description()
# car1.add_to_mileage(-15)
# car1.get_description()
print(car1.fill_tank())


