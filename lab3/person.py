class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name):
        self.name = name
        self.__money = 0
        self.mood = None
        self.__healthRate = 0

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, val):
        if isinstance(val, int):
            if self.__healthRate in range(0, 100):
                self.__healthRate = val
            else:
                print("healthRate must be between 0 and 100")
        else:
            print("healthRate must be integer")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, val):
        if isinstance(val, int):
            if self.__money >= 0:
                self.__money = val
            else:
                print("money must be greater than 0")
        else:
            print("money must be integer")

    def sleep(self, hours):
        if isinstance(hours, int):
            if hours == 7:
                self.mood = Person.moods[0]
            elif hours < 7:
                self.mood = Person.moods[1]
            else:
                self.mood = Person.moods[2]
        else:
            print("hours of sleep must be integer")

    def eat(self, meals):
        if isinstance(meals, int):
            if meals in range(1, 4):
                if meals == 3:
                    self.__healthRate = 100
                elif meals == 2:
                    self.__healthRate = 75
                elif meals == 1:
                    self.__healthRate = 50
            else:
                print("meals should be between 1 to 3 meals")
        else:
            print("number of meals must be integer")

    def buy(self, items):
        if isinstance(items, int):
            if items > 0:
                self.__money -= 10 * items
            else:
                print("number of items must be greater than 0")
        else:
            print("number of meals must be integer")

