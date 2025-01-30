class User:
    def __init__(self, first_name="", last_name="", email="", password="", status="inactive"):
        self.all_users = []
        self.f_name = first_name
        self.l_name = last_name
        self.email = email
        self.password = password
        self.status = status

    @staticmethod
    def main_list():
        print("\nWelcome to user Management System")
        print("Choose number for list below:")
        print("1- Add new user")
        print("2- Display all users")
        print("3- Exit")

    def display_users(self):
        print("-" * 20)
        print(f"First Name= {self.f_name}")
        print(f"Last Name= {self.l_name}")
        print(f"email= {self.email}")
        print(f"User Status= {self.status}")
        print("-" * 20)

    def show_all_users(self):
        if self.all_users:
            for member in self.all_users:
                member.display_users()
        else:
            print("Sorry there is to user to display")
            print("-" * 50)

    def add_user(self):

        first_name = input("Enter you first name: ")
        last_name = input("Enter you last name: ")
        email = input("Enter your email: ")
        password = input("Enter you a password: ")

        new_user = User(first_name, last_name, email, password)
        self.all_users.append(new_user)

user = User()
system_on = True
while system_on:
    User.main_list()

    user_entry= input("Enter your choice: ")
    if user_entry == "1":
        user.add_user()
        print("-" * 27)
        print("User was added Successfully")
        print("-" * 27)

    elif user_entry == "2":
        user.show_all_users()

    elif user_entry == "3":
        print("Exiting...")
        break
    else:
        print("Invalid input, Try again")
        pprint("_" * 50)

