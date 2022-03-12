from validation import inputEmail
from projectsMenu import projectMenu
def login():
    print("---------Login---------")
    email = input("please enter your email: ")
    email =inputEmail(email)
    password = input("please enter your password: ")
    with open("users.txt", 'r') as users:
        l = users.readlines()
        for userEmail in l:
            if userEmail.split(":")[2] ==email and userEmail.split(":")[3] ==password :
                return projectMenu(email)
        else:
            print(userEmail.split(":")[2], userEmail.split(":")[3])
            print("This email or the password is wrong,please try again")
            return login()
