from Employee import Employee

Samy = Employee("Samy", "fiat 128", "samy@gmail.com", 100)
print("Samy's car: ",Samy.car)

print("Before changing the salary: ",Samy.salary)
Samy.salary = -100
print("After changing the salary: ",Samy.salary)

print("samy's ID: ",Samy.id)

print("Before changing the distanceToWork: ",Samy.distanceToWork)
Samy.distanceToWork = -100
print("After changing the distanceToWork: ",Samy.distanceToWork)

Samy.work(10)
print("samy if he worked 10 hours, his mood: ",Samy.mood)

Samy.sleep(13)
print("samy if he slept 13 hours, his mood: ",Samy.mood)

Samy.money = 10000
print("samy's money: ",Samy.money)
Samy.buy(3)
print("samy's money after buing 3 items: ",Samy.money)
Samy.eat(3)
print("if samy eats 3 meals,his heath rate:",Samy.healthRate,"%")
Samy.eat(0)

Samy.send_mail("ahmed@gmail.com", "alert", "There is an important meeting today after noon\nPlease attend. ", "Ahmed Mohamed")
