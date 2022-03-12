import os


def showProjects():
    if os.path.exists('projects.txt'):
        print("{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}".format("Project ID","User Email","Project Title","         Details         ","Total Target" ,"Start Date" ,"End Date"))
        with open("projects.txt") as projs:
            for i in projs:
                line = i.split(":")
                line[-1] = line[-1].strip()
                x1, x2, x3,x4,x5,x6,x7 = line
                print("{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}".format(f"    {x1}    ",x2,x3,x4,x5,x6,x7))
    else:
        print("There is no projects yet.")
    input("press enter to continue")