# scenarios

#from while_loop import fuzz_buzz as fb  -imports only one function, we can use alies name when we import.
from while_loop import *  #imports all functions from module
from  functions.functions_return import*


print("executions from while_loop.py")
#fuzz_buzz()
while_loop_increment()
while_loop_decrement()


print("executions from functions_return.py")
print('Result of the function : ', build_full_name('john', 'doe'))
person2 = build_full_name('John', 'Doe')
print('Person2: ', person2)

print('-----------------------imported from functions_return---------------------')
print(city_country('paris', 'france'))
print(city_country('london', 'uk'))
print(city_country('new york', 'united states'))

# HW 8-4, 8-5, 8-7, 8-8, 8-15