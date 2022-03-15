# import mainMenu
from validation import inputName, uniqueEmail, passwordCheck, inputPhone



def regiseter():
    user = {}
    print("\033[1m---------Registeration---------\033[0m")
    for i in ["firstName", "lastName", "email", "password", "mobilePhone"]:
        word = input(f"\033[1mplease enter your {i}:\033[0m ")
        if i in ["firstName", "lastName"]:
            user[i] = inputName(word)
        elif i == "email":
            user[i] = uniqueEmail(word)
        if i == "password":
            user[i] = passwordCheck(word)
        if i == "mobilePhone":
            user[i] = inputPhone(word)
    else:
        with open("users.txt", 'a') as users:
            l = ":".join(user.values())
            l += '\n'
            users.write(l)
        print("\033[94mRegistered successfully :D\033[0m ")
    import mainMenu
    mainMenu.menu()
