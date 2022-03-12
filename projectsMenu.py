
from validation import inputNumber
import createProject
from showProjects import showProjects
from editProject import editProject
from deleteProject import deleteProject
def projectMenu(email):
        choice = input("Please enter number of your choice: \n1. Create new project\n2. Show all projects\n3. Edit project\n4. Delete project\n5. log out\n6. Exit\n  ")

        if inputNumber(choice):
            if choice in "123456":
                if choice == "1":
                    createProject.createProject(email)
                elif choice == "2":
                    showProjects()
                elif choice == "3":
                    editProject(email)
                elif choice == "4":
                    deleteProject(email)
                elif choice == "5":
                    import mainMenu
                    mainMenu.menu()
                elif choice == "6":
                    exit()
                else:
                    print("please enter a valid choice")
        projectMenu(email)