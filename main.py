class User:
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.all_users = []
        self.f_name = first_name
        self.l_name = last_name
        self.email = email
        self.password = password
        self.status = status


    def display_users(self):
        print(f"First Name= {self.f_name}")
        print(f"Last Name= {self.l_name}")
        print(f"email= {self.email}")
        print(f"User Status= {self.status}")
        print("_" * 20)

    def show_all_users(self):
        if self.all_users:
            for user in self.all_users:
                user.display_users()

        else:
            print("Sorry there is to user to display")


    def new_user(self):
        pass
    @staticmethod
    def main_list():
        print("Welcome to user Management System")
        print("Choose number for list below:")
        print("1- Add new user")
        print("2- Display all users")
        print("3- Exit")



    def add_user(self):
        pass




