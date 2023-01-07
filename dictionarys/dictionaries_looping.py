#Looping through dictionary: keys, values, key-value pairs

person1 = {'name': 'john doe', 'age': '25', 'location': 'ny'}
# default is looping through keys only:
for key in person1:
    print(key)
print("------------Default case, looping through keys only: ------------------------- " )
for key in person1.keys():
    print(key)

print("------------Default case, looping through keys only: ------------------------- " )
for key in person1:
    print('key in this iteration is : ', key)
    print('value in this iteration is : ', person1[key])

print("-------------looping through keys only: --------------------------------" )
for key in person1.keys():  # it is optional
    print('key in this iteration is : ', key)
    print('value in this iteration is : ', person1[key])

print("-------------looping through values only: --------------------------------" )
for value in person1.values():  # it is optional
    print('value in this iteration is : ', value)

print("-------------looping through keys and values  (mostly used one) items()--------------------------------" )
for key, value in person1.items():
    print('key in this iteration is : ', key)
    print('value in this iteration is : ', value)

rivers_countries = {'nile': 'egypt', 'amazon': 'brasil', 'volga': 'russia', 'missisippi': 'usa', 'thames': 'uk'}
print("Exercise 5.6 from book==========================")
for river, country in rivers_countries.items():
    print(f"The {river.title()} runs through the {country.title()}.")

print("2. User loop to print the name of each river in the dictionary==========================")
for river in rivers_countries.keys():
    print(f"The {river.title()} is in the dictionary")

print("2. User loop to print the name of each country in the dictionary==========================")
for country in rivers_countries.values():
    print(f"The {country.title()} is in the dictionary")

