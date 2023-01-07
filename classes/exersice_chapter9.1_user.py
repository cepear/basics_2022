

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




print("****************AdminUser(User) **************")
class AdminUser(User):
    #privileges = []   # better to put attributes on the top and then all methods will be separated

    def __init__(self, first_name, last_name, resident, profession):
        super().__init__(first_name, last_name, resident, profession)
        self.privileges = []

    def describe_user(self):
        super().describe_user()

    def greet_user(self):
        super().greet_user()
       # print("{self.first_name}  {self.last_name} is our new Administrator")

    def show_privileges(self):
        print(f" She has many privileges, including: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")

print("-------9.8 ---------Privileges Class-----------------")

class Privileges:

    privileges = []

    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print(f" She has many privileges, including: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t{privilege}")
        else:
            print(f"\nNo privileges. ")

user2 = AdminUser('Nana', 'Rubin', 'France', 'Accountant')
user2.describe_user()
user2.greet_user()
user2.privileges = ['can add post', 'can delete post', 'can ban user']
user2.show_privileges()

user3 = AdminUser('Lana', 'Block', 'Italy', 'Broker')
user3.privileges = ['can add post', 'can delete post', 'can ban user']
user3.describe_user()
user3.greet_user()
user3.show_privileges()

# user1 = User('Anna', 'Karenina', 'Vienna', 'singer')
# print(user1.first_name)
# print(user1.last_name)
# user1.describe_user()
# user1.greet_user()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.reset_login_attempts()
# print(f"Your total login attempts set to {user1.login_attempts}")
# user1.increment_login_attempts()
# print(f"Your total login attempts set to {user1.login_attempts}")
# print("----Login to website function--------------")
# user1.reset_login_attempts()
# user1.login_to_website('jo','ans')
# print(f"1. Your total login attempts set to {user1.login_attempts}")
# user1.login_to_website('bob','ans')
# print(f"2. Your total login attempts set to {user1.login_attempts}")
# user1.login_to_website('tom','ytu')
# print(f"3. Your total login attempts set to {user1.login_attempts}")
# user1.login_to_website('jo','ok34')
# print(f"4. Your total login attempts set to {user1.login_attempts}")
# print("---Positive result-------------")
# user1.reset_login_attempts()
# user1.login_to_website('john', '@Today2023')


# Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.















