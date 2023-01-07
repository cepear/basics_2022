cars = [ 'audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(f'car value was bmw so we are doing upper() : {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() : {car.title()}')
# in Python and - &, or - || (pipe)
for car in cars:
    if car == 'bmw' and 2 == 2:
        print(f'car value was bmw so we are doing upper() : {car.upper()}')
    else:
        print(f'expression returned false so we are doing Title() : {car.title()}')
cars[0] = 'merc'
# and  results of expression: car == bmw and 2 == 2
#true =+ true = true
#true + false = false
#false + true = false
#false + false = false

# or
# true + true = true
#false + true = true
#true + false = true
#false + false = false

#  Expressions always returns True or False
name = 'john'
num = 45.55
is_good = True
friends = []
name.lower() == 'john' #True checking if the value of the name is equal to 'jane'
name.lower() != 'john' #False
name > 'abc'
num == 45 ## False
num < 45 ## False
num <= 45 ##False
num >= 45 #True
num > 45 #True
is_good=True
is_good == False #False
#Multiple conditions:
name = 'john'
name == 'john' and num > 45 # True and True >> True
name == 'john' and num < 45 # True and False >> False

name == 'john' or num > 45 # True and True >> True
name == 'john' or num < 45 # True and False >> True
name == 'jane' or num < 45 # False and False >> False

friends = []
if friends:
    print('friends  is not empty list')
else:
    print('friends expression returned false, this mean it is a empty list')

friends = ['jane']
if friends:
    print('friends  is not empty list')
else:
    print('friends expression returned false, this mean it is a empty list')

#cars = [ 'audi', 'bmw', 'subaru', 'toyota']
print(cars)
if 'tesla' in cars:
    print(f'Cars list include tesla')
else:
    print(f'Tesla is not in cars list ')

#Exercises 5.1
car = 'subaru'
print("Is car == 'subaru'? I preidct True")
print(car == 'subaru')
print("Is car == 'audi'? I predict False")
print(car == 'audi')
print("Is car == 'tesla'? I predict False")
print(car == 'tesla')

names = 'Anna'

if name:
    print('Name list is empty')

else:
    print('Name is ')


