from validation import inputNumber
from login import login
import regiseter

def menu():

    choice = input("Please enter number of your choice: \n1. Login\n2. Regiseter\n3. Exit\n  ")

    if inputNumber(choice):
        if choice in "123":
            if choice == "1":
                login()
            elif choice == "2":
                regiseter.regiseter()
            elif choice=="3":
                exit()
            else:
                print("please enter a valid choice")
    menu()





menu()