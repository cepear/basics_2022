
car= 'subaru'
#expression ? code_if_true; code_if_false
print("is car=='subaru'? i predict true.")
print(car=='subaru')

car= 'bmw'
print("is car=='subaru'? i predict false.")
print(car=='subaru')
print(45==233)
if 45==45:
    print("True statement")

allien_colors = ['green', 'yellow', 'red']

for color in allien_colors:
    if color=='green':
        print("You just earned 5 points")
    else:
        print("You just earned 10 points")

for color in allien_colors:
    if color=='green':
        print(f"You just earned 5 points, {color} allien.")
    elif color=='yellow':
        print(f"You just earned 10 points, {color} allien.")
    else:
        print(f"You just earned 15 points, {color} allien")

#for i in range(0,5):

#    age = int(input("Please enter age: "))

#    if age<2:
#        print('You are a baby')
#    elif 2 <= age < 4:
#        print("You are a toddler")
#    elif  4<=age<13:
#        print("You ar a kid")
#    elif 13<= age <20:
#        print('You are a teenager')
#    elif 20 <= age < 65:
#        print("You are an adult")
#    else:
#        print('You are an elder')

for i in range(0, 3):
    user_names = ['Admin', 'Anna', 'Inna', 'Lana']

#    name = str(input("Please enter your name:"))

    for name in user_names:
        if name == 'Admin':
            print(f"Hello {name}, you are so special for us!!!!")
        else:
            print(f"Hello {name}, welcome to the club!")


#How to find out if list is empty or not?
member_names1 = []
if not member_names1:
    print("list is empty, we need to add members.")
    for member in member_names1:
        member = str(member)
        if member.lower() == 'admin':
            print(f"Hello {member}. You are so special guest!")
        elif member != 'admin':
            print(f"Hello {member}, welcome.")



member_names2 = ['Admin', 'John', 23, '']
for member in member_names2:
    member=str(member)
    if member.lower() == 'admin':
        print(f"Hello {member}. You are so special guest!")
    elif member != 'admin':
        print(f"Hello {member}, welcome.")
    else:
        print("list is empty, we need to add members.")

