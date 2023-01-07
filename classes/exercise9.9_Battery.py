from classes.working_with_classes import Car


# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.

class Battery:
    """Add a method to the Battery class called upgrade_battery()."""

    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has", {self.battery_size},  "kWh battery. ")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range}  miles on a full charge. ")

    def upgrade_battery(self):
        if self.battery_size < 85:    # here we are checking battery size
            print("Your battery is less that national standard, you are eligible for free upgrade")
            self.battery_size = 85    # here we are upgrading battery size
            print(f"Battery size upgraded to 85 Kwh")
        else:
            print("Battery size is at the upgraded level.")




class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.make = make # when we did super__init__  we don't need attributes in below line.
        # self.model = model        # we can add attributes related to ElectricCar class below
        # self.year = int(year) # super().__init__() executes the constructor of the parent class
        # self.__mileage = 0
        self.battery = Battery()
       # self.battery_size = 80

    def fill_tank(self):
        """We are overriding the fill_tank() function from parent class Car"""
        print("Sorry, this car doesn't have a tank, please go to charging station.")

    def get_description(self):
        super().get_description()
        print(f"Battery size: {self.battery_size}")


ecar1 = ElectricCar('tesla', 'modelX', '2022')
ecar1.battery.describe_battery()
ecar1.battery.get_range()
ecar1.battery.upgrade_battery()
ecar1.battery.get_range()
#ecar1.fill_tank()
#ecar1.get_description()
# print("---------Check the battery of ecar2 -------")
# ecar2 = ElectricCar('bmw', 'x5', '2022')
# ecar2.battery_size.describe_battery()
# new_battery = 70
# ecar2.battery_size.describe_battery= new_battery
# print("ecar2 battery size is set to 70")
# ecar2.battery_size.describe_battery()
#
# print("*************************ecar3details****************")
# ecar3 = ElectricCar('tesla', 'model Y', 2023)
# ecar3.get_description()






