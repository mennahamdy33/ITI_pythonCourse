import os
from validation import inputTitle,inputDetails,inputTarget,inputDate
flag = False
projID = 1
def createID():
    global flag
    global projID
    if not flag:
        if os.path.exists('projects.txt'):
            with open("projects.txt") as projs:

                for last_line in projs:
                    projID = int(last_line.split(":")[0]) +1


    else:
        projID+=1


    flag =True
    return projID
def createProject(email):
    project = {}
    project["id"]=str(createID())
    project["userEmail"]= email
    for i in ["title", "details", "totalTarget", "startDate", "endDate"]:
        word= input(f"please enter the {i} of the project: ")

        if i in "title":
            project[i] = inputTitle(word)
        elif i == "details":
            project[i] = inputDetails(word)
        if i == "totalTarget":
            project[i] = inputTarget(word)
        if i == "startDate":
            project[i] = inputDate(word)
            startDate = project[i]
            print(project[i])
        if i == "endDate":
            project[i] = inputDate(word,startDate,1)
            print(project[i])
    else:
        print(project)
        with open("projects.txt", 'a') as projects:
            l = ":".join(project.values())
            l += '\n'
            projects.write(l)



