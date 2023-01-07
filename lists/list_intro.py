# Chapter 3: Data structure - storage to hold multiple values, manage (create, add,, update, remove).
# 1. Lists 2. Dictionary (Set, Tuple)
# [4, 5, 6]; ['john', 'mark', 'jane']- list
# ctrl + alt + l - autoformat the file
# List and Dictionaty is mutable object - we can make a change in the list
#tuple - immutable , cannot add or remove values after defining
friends = []  # empty list
players = list()  # empty list
nums = [6, 9, 25]
names = ['john', 'marka', 'jane', 'ted' , 'larry']
bool_values = [True, False, True]
print(nums)
print(names)
#add elements, remove, update, read through values(access each value)
print(nums[1])
print(nums[0])
print(nums[2])
print(nums[-1])
print(nums[-2])
print(nums[-3])
print('Hi, ', names[1].title())
print('Hi, ', names[-1].title())
print('Hi, ', names[2].title())
print('Hi, ', names[-2].upper())
#listname.append(newvalue) 
names.append('anna')
print(names)
# listname.insert(index, 'value') puts value to specific place
names.insert(0, 'araz')
print(names)
names.insert(2, 'maya')
print(names)
#updating elements in list listname [index] = 'value'
names [-1] = 'lara'
print(names)
names [1] = 'lana'
print(names)
names[3] = 'bot'

#remove values from list by index   del listname[index]

del names[3]
print(names)
deleted_name = names.pop(3)
print("we deleted following name: \t\t ".strip(), deleted_name)
# remove elements by index  listname.pop(), if no index mentioned by default it will remove last element from list
names.pop()
print(names)
names.pop(2)
print(names)
#removing element by value: listname.remove(value)
names.remove('ted')
print(names)

# 10/16/2022
guests = ['akmal', 'said', 'lenur','anna', 'lana', 'vera']
print(guests[0], 'I am inviting you to the party')
print(f'Hello + {guests[0].title()}, I am inviting you to the party')
print(f'Hello + {guests[1].title()}, I am inviting you to the party')
print(guests[2].title(),  'I am inviting you to the party.')
removed_guest = guests.pop(1)
print(f"{removed_guest}, can't make it ot the party")
guests.append('Alla')
guests.insert(0, 'Tima')
print(guests)

#





