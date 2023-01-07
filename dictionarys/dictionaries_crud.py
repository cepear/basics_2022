#Chapter 6 Dictionary (key-value pair) CRUD- create, read, update, delete.
print("=======1. Creating the empty dictionary (C)==============")
person1 = {}
person2 = dict()
languages_list = ['eng', 'ru', 'span', 'marsian']

person1 = {'name': 'john doe',
           'age': '25',
           'location': 'ny',
           'cars': ['audi', 'bmw', 'subaru', 'toyota'],      # independent value
           'languages': languages_list}       # two-way reference to the list (connected)
print("======2. Accessing the values (R)")
print(f" getting name of person1: {person1['name']}")
print(f" getting age of person1: {person1['age']}")
print(f" getting location of person1: {person1['location']}")

print("========= 3.adding/updating key value pair to the dictionary =======")
print("person1 before update: ", person1)
person1['phone'] = '443-629-3979'
person1['eyes'] = 'black'
print("person1 after update: ", person1)
# phone does not exist in the
person1['age'] = 30
print("after update age :", person1)
person2 = {'name': 'kim john',
           'age': '37',
           'location': 'ca',
           'cars': ['audi', 'bmw', 'subaru', 'toyota']}
print(f"Before update person2 cars: ", person2)
print(f"Updating list cars with new value")
#cars[0] = 'merc'
person2['cars'][0] = 'merc'
print("Updated cars list in person2: " , person2)
languages_list = ['eng', 'ru', 'span', 'marsian']

print("Updating languages_list (marsian to ger) ...")
languages_list[3] = 'ger'
print('updated list: ', languages_list)
print('dictionary : ', person1)
person1['languages'] [2] = 'french'
person1['languages'] = languages_list
print('updated list: ', languages_list)
print('dictionary : ', person1)
print(f" Person1: ", person1)


print("===========4 . Delete key-value pair from yje list==========")
print("Deleting the location from person1.....")
del person1['location']
print("deleted location from person1: ", person1)
person1['age'] = None
print("deleted age value from person1: ", person1)

fav_nums = {'Nicole': 7, 'Alex': 10, 'Yulia': 5}
print(f"Nicole's favorite number is : {fav_nums['Nicole']}")
print(f"Alex's favorite number is : {fav_nums['Alex']}")
print(f"Yulia's favorite number is : {fav_nums['Yulia']}")







