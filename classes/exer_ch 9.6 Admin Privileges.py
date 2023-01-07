

print("----------class User()--------------")


class User:

    username = 'john'
    password = '@Today2023'

    def __init__(self, first_name, last_name, resident, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.resident = resident
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        print(f"Guest of the honor is  {self.first_name}  {self.last_name} and she is from {self.resident}. "
              f"She is a {self.profession}.")

    def greet_user(self):
        print(f'Welcome to our party {self.first_name} {self.last_name}.')

    def increment_login_attempts(self):
        """method called increment_
# login_attempts() that increments the value of login_attempts by 1"""
    #  self.login_attempts=self.login_attempts = 1 it is same as line below
        self.login_attempts += 1
        print(f"User had {self.login_attempts} login attempts during day.")

    def reset_login_attempts(self):
        """reset_login_attempts() to 0 """
        self.login_attempts = 0
        print("Your login attempt is set to 0 ")

    def login_to_website(self, username:str, password: str):
        if username.lower() == self.username and password == self.password:
            self.reset_login_attempts()
            print("you have logged in successfully")
        else:
            if self.login_attempts > 3:
                print("Your account is blocked. Please, try in 15 min")
            else:
                self.increment_login_attempts()
                print("Your username or password is incorrect. Try again")


print("-------9.8 ---------Privileges Class-----------------")

class Privileges:

    list_of_privileges = []

    def __init__(self):
        self.list_of_privileges = []

    def show_privileges(self):
        if self.list_of_privileges:
            for privilege in self.list_of_privileges:
                print(f"\t{privilege}")
        else:
            print(f"\nNo privileges. ")

print("****************Admin(User) **************")
class Admin(User):
    #privileges = Privileges()  # better to put attributes on the top and then all methods will be separated

    def __init__(self, first_name, last_name, resident, profession):
        """here we make a Privileges instance as an attribute in the Admin class.
        And Creating a new instance of Admin and using this method to show its privileges."""
        super().__init__(first_name, last_name, resident, profession)
        self.admin_privileges = Privileges()   #Privileges instance as an attribute in the Admin class.

    def test(self):
        print('Privileges: ')
        print(self.admin_privileges)

    # def describe_user(self):
    #     super().describe_user()
    #
    # def greet_user(self):
    #     super().greet_user()
       # print("{self.first_name}  {self.last_name} is our new Administrator")
admin1 = Admin('Jackie', 'Jonas', 'Rome', 'baker')
admin1.describe_user()
admin1.admin_privileges.show_privileges()
print("\nNew addition ->")
admin1_new_privileges = [
    'can override error',
    'can reset account',
    'can moderate comments'
]
# admin1 is the object of Admin class
# admin_privileges is the object inside the Admin class
# list_of_privileges is the attribute inside Privileges class
admin1.admin_privileges.list_of_privileges = admin1_new_privileges

# show_privileges is the method (behaviour) inside Privileges class.
admin1.admin_privileges.show_privileges()
