import os
from  validation import inputNumber,inputTitle,inputDetails,inputDate,inputTarget

def rightID(id,lines):
    if inputNumber(id):
        for i in lines:
            print(i[0])

            if id == i[0]:
                return i

    id = input("please enter a valid id of the project to edit:")
    return rightID(id,lines)

def editProject(email):
    if os.path.exists('projects.txt'):
        print("{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}".format("Project ID", "User Email", "Project Title","         Details         ", "Total Target","Start Date", "End Date"))
        with open("projects.txt") as projs:
            lines=[]
            for i in projs:
                l = i.split(":")
                if l[1] ==email:
                    lines.append(l)
                    l[-1] = l[-1].strip()
                    x1, x2, x3, x4, x5, x6, x7 = l
                    print(
                        "{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}".format(f"    {x1}    ", x2, x3, x4, x5, x6, x7))

        ID = input("please enter the id of the project to edit:")
        newline= rightID(ID,lines)
        print(newline)
        oldLine = newline.copy()
        choice = input("Please enter number of your choice to edit: \n1. title\n2. details\n3. total target\n4. start date\n5. end date\n6. back to menu\n  ")
        if inputNumber(choice):
            if choice in "123456":
                editValue = input("please enter the new value: ")
                if choice == "1":
                    newline[2]=inputTitle(editValue)
                elif choice == "2":
                    newline[3]=inputDetails(editValue)
                elif choice == "3":
                    newline[4]=inputTarget(editValue)
                elif choice == "4":
                    newline[5]=inputDate(editValue,l[6],2)
                elif choice == "5":
                    newline[6]=inputDate(editValue,l[5],1)
                elif choice == "6":
                    return
                else:
                    print("please enter a valid choice")

            reading_file = open("projects.txt", "r")
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_i = stripped_line.replace(f"{':'.join(oldLine)}", f"{':'.join(newline)}")
                new_file_content += new_i + "\n"
            reading_file.close()

            writing_file = open("projects.txt", "w")
            writing_file.write(new_file_content)
            writing_file.close()


    else:
        print("There is no projects yet.")