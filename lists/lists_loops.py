
places = ['hawai', 'paris', 'bahamas', 'iceland', 'canada']
#loops - executing the code repetitevly
print("Looping through entire list: ")
print(f"I want to visit {places[0]} next summer")

#for var_each_element  in list_name
#    print('lines of the code to repeat')
#    print('this is the code to repeat')

for a in places:
    #comment line

    print(f"I want to visit {a.title()} next summer")
    print(f"How far is  {a.title()}  from Baltimore?")


numbers = [1, 3, 9, 7, 9, 4 ]
for number in numbers:

    num = number + 5
    print(f"numbers is :  {num}")
# Working with list of numbers, range() function
print(range(5))
print(list(range(5)))  #list(range()) gives all list of numbers from 0-5
print("============================")
for num in range(5):
    print(f"Each number in the list is: {num}")
print("======================")

for num in range(2, 6):
    print(f"Each number in the list is: {num}")
print("============================")
for num in range(4, 16, 3):
    print(f"Each number in the list is: {num}")

#Problem solving
print("List all number between 24 and 36 that can be devided by 4")
for num in range(24, 37, 4):
    print(f"Each number in the list is: {num}")


print("List square of number between 25 and 30.")
square_num = []
for num in range(25, 31):
    print(f"num = {num} and square is: {num**2}")
    square_num.append(num**2)
print(square_num)

print("************************************************")
nums = [4, 2, 9, 10]
max(nums)
print(f"Max number is: " , max(nums))
print(f'sum of the nums:  {sum(nums)}')
sum = 0
for num in nums:
    sum = sum + num
print(sum)
print("***************************************************")
nums = [2,9,8,7,4,9,5]
sum = 0
for num in nums:
    sum = sum + num
print(sum)

odds = list(range(1, 21, 2))
print(odds)
print("*********************************")
odds_new = []
odds = list(range(1, 21, 2))
for num in range(1, 21, 2):
    odds_new.append(num)
print(odds_new)
print("******************************************")

cubes_list = []
for num in range(1, 11):
    cubes_list.append((num**3))
print(cubes_list)
#List new, update, add value, delete from list
##Sorting list: list.sort(), list.sort(reverse=True), newList=sorted(list),
# Simple for loop with list, List with range(start, stop, step), scope of the

#Tuples cannot be modified
# Tuples:
animals = ('dog', 'cat', 'horse')
dog_index = animals.index('dog')
sorted_animals = sorted(animals)
print(f"Sorted animals : {sorted_animals}")
for animal in animals[0:2]:
    print(f'each animal : {animal}')









