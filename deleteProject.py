import os
from  validation import inputNumber

def rightID(id,lines):
    if inputNumber(id):
        for i in lines:
            print(i[0])

            if id == i[0]:
                return i

    id = input("please enter a valid id of the project to edit:")
    return rightID(id,lines)

def deleteProject(email):
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

        ID = input("please enter the id of the project to delete:")
        deleteLine= rightID(ID,lines)
        print(deleteLine)
        a_file = open("projects.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        new_file = open("projects.txt", "w")
        for line in lines:
            if line.strip("\n") != f"{':'.join(deleteLine)}":
                new_file.write(line)

        new_file.close()


    else:
        print("There is no projects yet.")