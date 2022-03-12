# import mainMenu
from validation import inputName, uniqueEmail, passwordCheck, inputPhone



def regiseter():
    user = {}
    print("---------Registeration---------")
    for i in ["firstName", "lastName", "email", "password", "mobilePhone"]:
        word = input(f"please enter your {i}: ")
        if i in ["firstName", "lastName"]:
            user[i] = inputName(word)
        elif i == "email":
            user[i] = uniqueEmail(word)
            print(user[i])
        if i == "password":
            user[i] = passwordCheck(word)
        if i == "mobilePhone":
            user[i] = inputPhone(word)
    else:
        with open("users.txt", 'a') as users:
            l = ":".join(user.values())
            l += '\n'
            users.write(l)
        print("Registered successfully :D ")
    import mainMenu
    mainMenu.menu()
