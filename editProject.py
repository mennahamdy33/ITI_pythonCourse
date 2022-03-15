import os
from  validation import inputNumber,inputTitle,inputDetails,inputDate,inputTarget

def rightID(id,lines):
    if inputNumber(id):
        for i in lines:
            print(i[0])

            if id == i[0]:
                return i

    id = input("\033[91mplease enter a valid id of the project to edit:\033[0m")
    return rightID(id,lines)

def editProject(email):
    if os.path.exists('projects.txt'):
        print("\033[94m{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}\033[0m".format("Project ID","User Email","Project Title","         Details         ","Total Target" ,"Start Date" ,"End Date"))
        with open("projects.txt") as projs:
            lines=[]
            for i in projs:
                l = i.split(":")
                if l[1] ==email:
                    lines.append(l)
                    l[-1] = l[-1].strip()
                    x1, x2, x3, x4, x5, x6, x7 = l
                    print("\033[92m{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}\033[0m".format(f"    {x1}    ", x2,
                                                                                                   x3, x4, x5, x6, x7))

        ID = input("\033[1mplease enter the id of the project to edit:\033[0m")
        newline= rightID(ID,lines)
        oldLine = newline.copy()
        choice = input("\033[1mPlease enter number of your choice to edit: \n1. title\n2. details\n3. total target\n4. start date\n5. end date\n6. back to menu\n \033[0m ")
        if inputNumber(choice):
            if choice in "123456":
                editValue = input("\033[1mplease enter the new value:\033[0m ")
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
                print("\033[94mproject is updated.\033[0m")

            else:
                    print("\033[91mplease enter a valid choice\033[0m")
        else:
                print("\033[91mplease enter a valid choice\033[0m")

    else:
        print("\033[91mThere is no projects yet.\033[0m")