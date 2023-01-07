
class Restaurant():
    def __init__(self, restaurant_name, cusine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = number_served


    def describe_restaurant(self):

        print(f"We went to {self.restaurant_name} and eat {self.cusine_type} food")


    def open_restaurant(self):

        print(f"Welcome everyone! '{self.restaurant_name}' are Open now! ")


    def set_number_served(self, new_num_served):
        """ Add a method called set_number_served() that lets you set the number that have been served"""
        self.number_served = new_num_served
       # print(f"{self.restaurant_name} served {self.number_served} customers yesterday")

    def increment_number_served(self, num_served):
        if num_served > 0:
        #self.number_served = self.number_served + num_served   - same as 1 line lower
            self.number_served += num_served
            print(f"You did good job today!")
        else:
            print("How it is possible? ")

class IceCreamStand(Restaurant):

    #flavors = []

    def __init__(self, restaurant_name, cusine_type= 'italian', number_served=0):
        super().__init__(restaurant_name, cusine_type, number_served=0)
        # self.restaurant_name = restaurant_name
        # self.cusine_type = cusine_type
        # self.number_served = number_served
        self.flavors = []

    def all_flavors(self):
        print(f"{self.restaurant_name} has many flavors of ice cream, including: ")
        if self.flavors:
            for flavor in self.flavors:
                print(f'\t{flavor}')
        else:
            print('\nNo such flavor!')





rest4 = IceCreamStand('Rome', 'greek')
rest4.describe_restaurant()
rest4.flavors = ['vanilla', 'chocolate', 'strawberry', 'pistachio','mint']
rest4.all_flavors()

rest5 = IceCreamStand("Rita's", 'american')
rest5.describe_restaurant()
rest5.flavors = ['chocolate', 'raspberry', 'lime']
rest5.all_flavors()

# restaurant1 = Restaurant('Oasis', 'uzbek cusine')
# # prints the two attributes individually
# print(restaurant1.restaurant_name)
# print(restaurant1.cusine_type)
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()
# #Print the number of customers restaurant served
# print(f"1. Number of customers {restaurant1.restaurant_name} served: {restaurant1.number_served}")
# # And change this value and print it again
# restaurant1.number_served = 55
# print(f"2. Number of customers {restaurant1.restaurant_name} served: {restaurant1.number_served}")
# restaurant1.set_number_served(20)
# print(f"3. Number of customers {restaurant1.restaurant_name} served: {restaurant1.number_served}")
# restaurant1.increment_number_served(3)
# print(f"4. Number of customers {restaurant1.restaurant_name} served: {restaurant1.number_served}")
# print(restaurant1.increment_number_served(-15))
# # and then call both methods
#
# print("-----------restaurant2------------")
# restaurant2 = Restaurant('Edo mae', 'japaneese')
# print(restaurant2.restaurant_name)
# print(restaurant2.cusine_type)
# restaurant2.describe_restaurant()
# restaurant2.open_restaurant()
# print("------------restaurant3 ---------------")
# restaurant3 = Restaurant('Bone fish', 'american cuisine')
# print(restaurant3.restaurant_name)
# print(restaurant3.cusine_type)
# restaurant3.describe_restaurant()
# restaurant3.open_restaurant()