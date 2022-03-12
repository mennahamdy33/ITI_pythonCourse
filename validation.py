import re
from datetime import datetime
def inputNumber(choice):
    if choice.isdigit():
        return True
    else:
        return False
# ############# user validation ###################
def inputName(name):
    if name.isalpha():
        return name
    else:
        name = input("Please enter a valid name: ")
        return inputName(name)
def uniqueEmail(email):
    with open("users.txt", 'r') as users:
        l = users.readlines()
        for userEmail in l:
            if userEmail.split(":")[2] == email:
                print(userEmail.split(":")[2])
                email = input("This email is used before, please use another one: ")
                return uniqueEmail(email)
        else:
            return inputEmail(email,0)

def inputEmail(email,x=1):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return email
    else:
        email = input("Please enter a valid email: ")
        if x ==0:
            return uniqueEmail(email)
        else:
            return inputEmail(email)


def confirmPassword(pass1):
    pass2 = input("please confirm the password: ")
    if pass1 == pass2:
        return pass1
    else:
        pass1 = input("please renter a password: ")
        return passwordCheck(pass1)
        # return confirmPassword(pass1)

def passwordCheck(password):
    SpecialSym = ['$', '@', '#', '%','_']
    if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char.islower() for char in password)or not any(char in SpecialSym for char in password):
        print('Password should be more than 6 characters and\n'
              ' have at least one uppercase letter,\n'
              'least one numeral,\n'
              'one lowercase letter,\n'
              'one of the symbols $@#_')
        password = input("please renter a password: ")
        return passwordCheck(password)
    return confirmPassword(password)
def inputPhone(phone):
    regex = re.compile(r'^01[\d]{9}$')
    if re.fullmatch(regex, phone):
        return phone
    else:
        phone = input("Please enter a valid phone number: ")
        return inputPhone(phone)
# ################ Project Validation ####################
def inputTitle(title):
    regex = re.compile(r'^[a-zA-Z_][a-zA-Z_0-9\s]{2,50}$')
    if re.fullmatch(regex, title):
        return title
    else:
        title = input("Please enter a valid title, the title should be between 3 to 50 character,\n"
                      "starts with alphabet or under score only\n"
                      "and can contain alphabets, numbers, underscores, and white spaces : ")
        return inputTitle(title)
def inputDetails(details):
    if not details:
        details = input("Details shouldn't be empty: ")
        return inputDetails(details)
    elif ":" in details:
        details = input("Details shouldn't contain ':' symbol : ")
        return inputDetails(details)
    return details
def inputTarget(target):
    regex = re.compile(r'^\d+\.?\d*$')
    if re.fullmatch(regex, target):
        return target
    else:
        target = input("Please enter valid total target in form number(.number)\n"
                       "ex:100 or 10.3, 0.444: ")
        return inputTarget(target)
def inputDate(date,date1="",x=0):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        if x==0:
           return  date
        else:
            return endDateValid(date,date1,x)
    except ValueError:
        date = input("Please enter valid date in form YYYY-MM-DD: ")
        return inputDate(date,date1,x)
def endDateValid(date,date1,x):
    if x==1:
        if date <= date1:
            date = input(f"end date should be after the start date: ")
            return inputDate(date,date1,1)
    elif x==2:
        print("hereeeee")
        if date > date1:
            print("here")
            date = input(f"start date should be before the end date: ")
            return inputDate(date,date1,2)
    return date