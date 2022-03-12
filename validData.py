import re
def validation(key,string):
    if(key=="name"):
        if string.isalpha():
            return True
    if(key=="email"):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, string):
            return True


def enterData():
    global user
    for i in ["name","email"]:
        while True:
            string = input(f"please enter your {i}: ")
            if validation(i,string):
                user[i]=string
                break

user={}
enterData()
print(user)