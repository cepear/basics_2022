#Chapter 7  FUNCTIONS


#built-in finctions - print(arg1, arg2), input(), append(), sorted().
#user defined functions -
def greet_user():
    print("hello class!")
    print("Wonderful sunny day today!")

# here we defining function, declaring function name.
def greet_user():
    print("hello class!")
    print("Wonderful sunny day today!")
# Calling function:

greet_user()
greet_user()
greet_user()
greet_user()

#overriding the function:
def greet_user():
    print("hello class!")
    print("Wonderful sunny day today!")


def greet_user():
    print("hello class!")
    print("Enjoy your day!")
# Calling function:

greet_user()
greet_user()


#function with argument: positional argument, required
def greet_user_by_name(name):
    print(f"hello,  {name.upper()}!")
    print("Enjoy your day!")
# Calling function:

greet_user()
greet_user_by_name("jane")


def greet_user_by_name(name, day_of_the_week):
    print(f"hello,  {name.upper()}!")
    print(f"Enjoy your {day_of_the_week} today!")
# Calling function:

greet_user()
greet_user_by_name("jane", 'Saturday')
greet_user_by_name("mike", 'Sunday')
greet_user_by_name(day_of_the_week='Monday', name='mike')


def greet_user_by_name_with_def(name, day_of_the_week='Monday'):
    """function with default value: name is required, day_of_the_week is not required"""
    print(f"hello,  {name.upper()}!")
    print(f"Enjoy your {day_of_the_week} today!")
print("=========Default values==================")
greet_user_by_name_with_def('kamran', 'Sunday')
greet_user_by_name_with_def('Alla')
greet_user_by_name_with_def(day_of_the_week='Wednesday', name = 'Alla')


print('===========exercise 8.3 ======')

def make_shirt(size, text_to_print):
    """ Prints message and size of the shirt
    :return:"""
    print(f"The size of your shirt is : {size}")
    print(f"The message to be printed on your shirt is : \n\t\t{text_to_print}")

make_shirt('M', 'Awesome')
make_shirt(text_to_print='Cool shirt', size='L')


def make_shirt(text_to_print, size='XXL'):
    """ Prints message and size of the shirt
    :return:"""
    print(f"The size of your shirt is : {size}")
    print(f"The message to be printed on your shirt is : \n\t\t{text_to_print}")

make_shirt('Level Up Consalting', '')

# Login page.py:
#
# 1. Elements on the page (variables)
# -username = ''
# -password = ''
# -Cancel = ''
# error_message = ''
#
# 2. Actions can be done on the page (functions)
#
# def enter_username(username):
#   """enters username in the username field"""
#     pass
#
# def clear_username():
#    """Clears field from inputs"""
#     pass
#
# def enter_password():
#     """enters password in the password field"""
#     pss
#
# def click_login():
#   """clicks login Button"""
#   pass
#
# def click_cancel():
#   """clicks Cancel button"""
#   pass
#
# def get_error_message():
#   """Returns the text of the error message"""
#   msg = ''  #code to get the text from the webpage for this element
#   return msg
#
#
# login-scenarios.py:
#
# positive test  : valid username and  password
# open browser
# go to website
# go to login page
# enter username(......)
# enter password(......)
# click_login()
# verify it opens welcome page.
#
# negative test : invalid username
# open browser
# go to website
# go to login page
# enter username(invalid)
# enter password(......)
# click_login()
# assert 'Invalid email address' == get.error_msg()
#
# negative test : invalid  password
# open browser
# go to website
# go to login page
# enter username(.......)
# enter password(invalid)
# click_login()
# assert 'Invalid email address' == get.error_msg()

