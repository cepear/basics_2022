print("Hello world!")
## variable = storage while code runs
a = 45
b =  6.87

print(a)
print(b)

name = ('JOHN DOE')
print(name)

a = 1000

msg = ("Hello, this is my first coding practice.")
print(msg)
print(a, b, name, msg)

a = a + 1
print(a)
## a + = 1 same as a=a+1

a = a - 1
## a - = 1 same as a=a-1

##useful functions
print('name before title' , name)
print('name lower', name.lower())
print('name after title', name.title())
print('using is upper:', name.islower())

## Concatination
print("my message: " + name + ', ' + msg)
print("my message: " + name.title() + ', ' + msg.upper())
print("My message: " + name.title() + ', ' + msg.upper())

print("Special characters : \\t  \\n")
print("My message : \t" + name.title() + '\n' + msg.upper())

a = 45
b =  6.87

print(a)
print(b)

name = ('JOHN DOE')
msg = ("Hello, this is my first coding practice.")
print(msg)
print(a, b, name, msg)

a = a + 1
print(a)
## a + = 1 same as a=a+1

a = a - 1
## a - = 1 same as a=a-1

##useful functions
print('name before title' , name)
print('name lower', name.lower())
print('name after title', name.title())
print('using is upper:', name.islower())

## Concatination
print("my message: " + name + ', ' + msg)
print("my message: " + name.title() + ', ' + msg.upper())
print("My message: " + name.title() + ', ' + msg.upper())

print("Special characters : \\t  \\n")
print("My message : \t" + name.title() + '\n' + msg.upper())
print("Message to everyone: \n\t\t\t" + "please have fun!!".upper())
print("Message to everyone: \n\t\t\t" + "please have fun!!".title())

## \t - tabs, \n - new line

locatn = '  \thawai\n\t'
print(locatn)
print('My wedding venue : ' + locatn.strip().upper()+' islands')
## strip(), rstrp(), lstrip() - removes spaces, whitespaces.

print("#####working with numbers###############")  ### 0.1 floats,
num1 = 3
num2= 8
print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)

print("multiplication: ", num1 * num2)
print("division: ", num1 / num2)
print("floor devision: ", 20 //num1) ### how mahy number 1s in 20, always returns integer
print("modulo: ",20 % num1)  ### what is remainder when you devide 20 to 2
### why we use it:
### find odd numbers from 20 to 50
###if n%2 returns 1 then n is odd number (pseudocode)
###if n%2 returns 0 then n is even number (pseudocode)
print("###str(expression), converts expression to the string")
print("Addition: " + str(num1 + num2)) ## Concatination - merging. Only str can be concatinated to str. If its int, then we should convert it to str.
num3 = '456'# this is a strring data type, becuese covered with single quote
num4 = 45.7566 # float data type.  when converting it gets whole part only.
print(('addition with num3: ', num1+int(num3))) # we need to convert '456' to int.
print('Converted to int: ', int(round(num4)))
### Summary:
# variable = naming, values string, int, float, boolean, double, Primitive data types
# string: concatenate, upper(), title(), Lower(), str(), int(), '\t', 'n'
# numbers: int, float/double, int(), +, -, *, **, //, %

