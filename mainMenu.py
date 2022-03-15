from validation import inputNumber
from login import login
import regiseter

def menu():

    choice = input("\033[1mPlease enter number of your choice: \n1. Login\n2. Regiseter\n3. Exit\n \033[0m ")

    if inputNumber(choice):
        if choice in "123":
            if choice == "1":
                login()
            elif choice == "2":
                regiseter.regiseter()
            else:
                exit()
        else:
            print("\033[91mplease enter a valid choice\033[0m")
    else:
        print("\033[91mplease enter a valid choice\033[0m")
    menu()





menu()