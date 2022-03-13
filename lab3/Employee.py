import person
import re

Emailregex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class Employee(person.Person):
    id = 0

    def __init__(self, name: str, car: str, email: str, distanceToWork: int):
        super(Employee, self).__init__(name)
        Employee.id += 1
        self.car = car
        self.email = email
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, val):
        if isinstance(val, int):
            self.__salary = 1000
            if val > 1000:
                self.__salary = val
        else:
            self.__salary = 0

    @property
    def distanceToWork(self):
        return self.__distanceToWork

    @distanceToWork.setter
    def distanceToWork(self, val):
        self.__distanceToWork = 0
        if isinstance(val, int):
            if val > 0:
                self.__distanceToWork = val

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, val):
        if isinstance(val, str):
            if re.fullmatch(Emailregex, val):
                self.__email = val
            else:
                raise Exception("email is not valid")
        else:
            raise Exception("email must be string")

    def work(self, hours):
        if isinstance(hours, int):
            if hours == 8:
                self.mood = person.Person.moods[0]
            elif hours > 8:
                self.mood = person.Person.moods[1]
            else:
                self.mood = person.Person.moods[2]

    def drive(self):
        pass

    def refuel(self):
        pass

    def send_mail(self, to, subject, msg, receiver_name):

        if isinstance(to, str) and isinstance(subject, str) and isinstance(msg, str) and isinstance(receiver_name, str):
            if not re.fullmatch(Emailregex, to):
                raise Exception("email is not valid")
            with open(f"{subject}to{to}.txt", 'w') as email:
                message = f"From: {self.email}\n" \
                          f"To: {to}\n" \
                          f"Subject: {subject}\n" \
                          f"" \
                          f"Hi,{receiver_name}\n" \
                          f"{msg}\n" \
                          f"Thanks"
                email.write(message)


Samy = Employee("Samy", "fiat 128", "samy@gmail.com", 100)
print(Samy.car)
Samy.salary = -100
print(Samy.salary)
print(Samy.id)
Samy.distanceToWork = -100
print(Samy.distanceToWork)
print(Employee.id)
Samy.work(10)
print(Samy.mood)
Samy.send_mail("to@g.com", "subject2", "msfsdfsfs\nrsfsfsfsefsef ffe", "receiver_name")
