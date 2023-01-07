#Chapter 5 EL IF statement
#if expression1:1
#    code to execute when expression in True
#elif expression2:
#    code to execute when expression2 is True
#elif expression3:
#    code to execute when expression3 is True
#elif expression4:
#    code to execute when expression4 is True
#else:
#    code to execute when none of above expressions are True

# input(prompt message) - this asks the user to input and returns a string(always)

# Problem:  older than 25 print don't drink and drive, from 17-25 you can get DL, but  pay more to insurance,
# from  age is less than 0-17 you can not get DL.
print("Awesome programm begins: ")
for i in range(0, 3):
# age = 35
# age = input("Please enter your age: ")
# age = int(age)
    age = int(input("Please enter your age: "))

    if 0 < age < 17:
        print('Sorry, you still young to get DL')
    elif  17 <= age < 25:
        print('From 17-25 you can get DL, but  pay more to insurance')
    elif 25 < age < 100:
        print("If you are older than 25 don't drink and drive")
    else:
        print("Please, enter valid number")

n = int(input("Please enter number : "))
n = 3
if n % 3 == 0:
    print('dividable by 3')
else:
    print('Not dividable by 3')


print('--------------FUZZ-BUZZ---------------------------')
num = int(input("Please enter number : "))
if num % 3 == 0 and num % 5 == 0:
    print("FUZZ-BUZZ")
elif num % 3 == 0:
    print('dividable by 3 "FUZZ"')
elif num % 5 == 0:
    print('Dividable by 5 "BUZZ"')
else:
    print('Not dividable by 3 or 5')

