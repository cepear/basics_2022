# Classes - INHERITANCE
# class A is a parent of class B
# class B (child) has access to everything that class A has.

from classes.working_with_classes import Car


class A:
    name = "i am from class A"

    def greet(self):
        print('Hello!')


class B:
    age = 25

    def get_age(self):
        print(f"My age is : {self.age}")


# this is possible if A and B is independent.
class C(A, B):
    pass


# object of class B has access to attributes and methods of class A and B
# item1 = B()   #when class B inherits class A
item1 = C()  # when class C inherits class A and B
print(item1.name)
print(item1.age)
item1.greet()
item1.get_age()

# parent class does not have access to child class attr and methods
item2 = A()
print(item2.name)
item2.greet()

print("************** Implementing concept of inheritance***********")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.make = make # when we did super__init__  we don't need attributes in below line.
        # self.model = model        # we can add attributes related to ElectricCar class below
        # self.year = int(year) # super().__init__() executes the constructor of the parent class
        # self.__mileage = 0
        self.battery_size = 80

    def fill_tank(self):
        """We are overriding the fill_tank() function from parent class Car"""
        print("Sorry, this car doesn't have a tank, please go to charging station.")

    def get_description(self):
        super().get_description()
        print(f"Battery size: {self.battery_size}")


ecar1 = ElectricCar('tesla', 'modelX', '2022')
ecar1.get_description()
ecar1.fill_tank()
ecar1.get_description()
print("---------Same function from parent class------")
car1 = Car('bmw', 'x5', '2022')
car1.fill_tank()
car1.get_description()
car1.make = 'toyota'
car1.get_description()

print("*************************ecar2 details****************")
ecar2 = ElectricCar('tesla', 'model Y', 2023)
ecar2.get_description()

# HW- 9.1-9.4 Practice Classes;   9.6 - 9.9 Practice inheritance
