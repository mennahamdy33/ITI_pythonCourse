from validation import inputEmail
from projectsMenu import projectMenu
def login():
    print("\033[1m---------Login---------\033[0m")
    email = input("\033[1mplease enter your email:\033[0m ")
    email =inputEmail(email)
    password = input("\033[1mplease enter your password:\033[0m ")
    with open("users.txt", 'r') as users:
        l = users.readlines()
        for userEmail in l:
            if userEmail.split(":")[2] ==email and userEmail.split(":")[3] ==password :
                return projectMenu(email)
        else:
            print(userEmail.split(":")[2], userEmail.split(":")[3])
            print("\033[91mThis email or the password is wrong,please try again\033[0m")
            return login()
