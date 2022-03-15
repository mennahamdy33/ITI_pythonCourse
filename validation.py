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
        name = input("\033[91mPlease enter a valid name:\033[0m ")
        return inputName(name)
def uniqueEmail(email):
    with open("users.txt", 'r') as users:
        l = users.readlines()
        for userEmail in l:
            if userEmail.split(":")[2] == email:
                print(userEmail.split(":")[2])
                email = input("\033[91mThis email is used before, please use another one:\033[0m ")
                return uniqueEmail(email)
        else:
            return inputEmail(email,0)

def inputEmail(email,x=1):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return email
    else:
        email = input("\033[91mPlease enter a valid email:\033[0m ")
        if x ==0:
            return uniqueEmail(email)
        else:
            return inputEmail(email)


def confirmPassword(pass1):
    pass2 = input("\033[1mplease confirm the password:\033[0m ")
    if pass1 == pass2:
        return pass1
    else:
        pass1 = input("\033[1mplease renter a password:\033[0m ")
        return passwordCheck(pass1)
        # return confirmPassword(pass1)

def passwordCheck(password):
    SpecialSym = ['$', '@', '#', '%','_']
    if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char.islower() for char in password)or not any(char in SpecialSym for char in password):
        print('\033[91mPassword should be more than 6 characters and\n'
              ' have at least one uppercase letter,\n'
              'least one numeral,\n'
              'one lowercase letter,\n'
              'one of the symbols $@#_\033[0m')
        password = input("\033[1mplease renter a password:\033[0m ")
        return passwordCheck(password)
    return confirmPassword(password)
def inputPhone(phone):
    regex = re.compile(r'^01[\d]{9}$')
    if re.fullmatch(regex, phone):
        return phone
    else:
        phone = input("\033[91mPlease enter a valid phone number:\033[0m ")
        return inputPhone(phone)
# ################ Project Validation ####################
def inputTitle(title):
    regex = re.compile(r'^[a-zA-Z_][a-zA-Z_0-9\s]{2,50}$')
    if re.fullmatch(regex, title):
        return title
    else:
        title = input("\033[91mPlease enter a valid title, the title should be between 3 to 50 character,\n"
                      "starts with alphabet or under score only\n"
                      "and can contain alphabets, numbers, underscores, and white spaces :\033[0m ")
        return inputTitle(title)
def inputDetails(details):
    if not details:
        details = input("\033[91mDetails shouldn't be empty:\033[0m ")
        return inputDetails(details)
    elif ":" in details:
        details = input("\033[91mDetails shouldn't contain ':' symbol :\033[0m ")
        return inputDetails(details)
    return details
def inputTarget(target):
    regex = re.compile(r'^\d+\.?\d*$')
    if re.fullmatch(regex, target):
        return target
    else:
        target = input("\033[91mPlease enter valid total target in form number(.number)\n"
                       "ex:100 or 10.3, 0.444:\033[0m ")
        return inputTarget(target)
def inputDate(date,date1="",x=0):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        if x==0:
           return  date
        else:
            return endDateValid(date,date1,x)
    except ValueError:
        date = input("\033[91mPlease enter valid date in form YYYY-MM-DD:\033[0m ")
        return inputDate(date,date1,x)
def endDateValid(date,date1,x):
    if x==1:
        if date <= date1:
            date = input(f"\033[91mend date should be after the start date:\033[0m ")
            return inputDate(date,date1,1)
    elif x==2:

        if date > date1:

            date = input(f"\033[91mstart date should be before the end date:\033[0m ")
            return inputDate(date,date1,2)
    return date