# Chapter 4. Slicing is iterating through part of the list

pizzas = ['chicken', 'cheese', 'pepperoni', 'capriciosa', 'funghi', 'sicilian']
for pizza in pizzas[0:3]:  # starts from 0 and ands before 3.
    print(f"We have {pizza} pizza today")

pizzas = ['chicken', 'cheese', 'pepperoni', 'capriciosa', 'funghi', 'sicilian']
for pizza in pizzas[3:-1]:  # from 3rd index to until last index. Last index not included. [3:] last index included
    print(f"We have {pizza} pizza today")

pizzas = ['chicken', 'cheese', 'pepperoni', 'capriciosa', 'funghi', 'sicilian']
for pizza in pizzas[:]:  # prints whole list
    print(f"We have {pizza} pizza today")

pizzas = ['chicken', 'cheese', 'pepperoni', 'capriciosa', 'funghi', 'sicilian']
for pizza in pizzas[:3]:  # prints from beginning to the 3rd index
    print(f"We have {pizza} pizza today")
print("___________________________________________ copy the list")
new_pizzas = pizzas # creates the new reference list to the same list
copy_pizzas = pizzas[:] # creates the totally independent list (copy_pizzas)
print(f"Lists before updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}")
pizzas.append('cheese steak')
new_pizzas.append('mushroom')
copy_pizzas.append('veggie')
copy_pizzas.append('grandma')
print(f"Lists after updating \n{pizzas}\n{new_pizzas}\n{copy_pizzas}")