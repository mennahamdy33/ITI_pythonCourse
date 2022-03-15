import os


def showProjects():
    if os.path.exists('projects.txt'):
        print("\033[94m{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}\033[0m".format("Project ID","User Email","Project Title","         Details         ","Total Target" ,"Start Date" ,"End Date"))
        with open("projects.txt") as projs:
            for i in projs:
                line = i.split(":")
                line[-1] = line[-1].strip()
                x1, x2, x3,x4,x5,x6,x7 = line
                print("\033[92m{:<10} {:<20} {:<15} {:<50} {:<15} {:<10} {:<10}\033[0m".format(f"    {x1}    ",x2,x3,x4,x5,x6,x7))
    else:
        print("\033[91mThere is no projects yet.\033[91m")
    input("\033[1mpress enter to continue\033[0m")