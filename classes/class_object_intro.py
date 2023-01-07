# Chapter 9. CLASSES and OBJECTS
#PEP8 guidelines:
# use combination of lowercase letters and underscores for - packages, folder, file,
# variable(objects of classes), function names.
#use combination of title case for classes.
# self keyword -shows that functions or variables belongs to the current class.
# 'this' is used in JAVA instead of self


msg = 'wouf  wouf'
breed = 'General '
class Dog():
    """ Model of dogs, template for dogs"""
    #attribute,(description)

    name = 'A'
    # breed = 'no breed' no use because of def __init__(self, name, breed, color,
    # size = 'medium' no use because of def __init__(self, name, breed, color, size = 'medium'):
    # color = '' no use because of def __init__(self, name, breed, color,
    age = '2'

    #  def __init__(self) - CONSTRUCTOR of the class when you instantiate
    # default functions to make required arguments
    # executed automatically everytime when you create an object (instance)
    def __init__(self, name, breed, color, size='medium'):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size



    # behaviour (action)
    def eat(self):
        print(f'{self.name} is eating ....')
        print(f'{self.name} wants more....')
        print(f'{self.name} done eating!')
        print(f"{self.breed}  is  {msg}") # msg is coming from outside the class
        print(f"{self.breed}  is   {breed}") # breed is coming from outside the class

    def run(self):
        print(f'{self.name} is running')

    def get_description(self):
        # #run()  #comes outside of the class
        # self.run()   #within the class
        print(f"Name of dog: {self.name}")
        print(f"Breed of dog: {self.breed}")
        print(f"Color  of dog: {self.color}")
        print(f"Size  of dog: {self.size}")
        print(f"Age  of dog: {self.age}")



# instantiation - creating of the instance of the class - creating object.
# dog1 and dog2 are objects
#dog1 = Dog() #copying everything from the model to a new object
print("---------------dog1-------------------")
dog1 = Dog('chubby', 'chow chow', 'brown') #copying everything from the model to a new object
print('name of the dog before assigning new name: ', dog1.name)
dog1.name = 'trex'# assigning the value to the attributes
print('name of the dog: ', dog1.name)
dog1.eat()

dog1.run()

dog1.get_description()
# dog1.breed = 'Colly'
#print(f"The breed of our dog is : ", dog1.breed)

print("---------------dog2--------------")
dog2 = Dog('Reks', 'colly', 'black', 'large')
print(f" Description of the dog2 is : ", dog2.name, dog2.breed, dog2.color)
print(dog2.name, dog2.breed)
dog2.get_description()






