class Student:
    def __init__(self,name):
        self.name = name


movies = ["matrix","john wyck"]

class Garage:
    def __init__(self):
        self.cars=[]
    
    def get_cars(self):
        return self.cars

    def show_list(self):
        car = self.cars
        return f'{"-".join(car)}'


ford = Garage()
ford.cars.append("Rx4")
ford.cars.append("fiesta Nano")

##########

from datetime import date

class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)


###########

class Toys:
    def __init__(self, toy:str) -> None:
        self.toy = toy

    @property
    def name(self):
        return self.toy

    @name.setter
    def set_toy(self,value):
        self.toy = value.lower().strip()

    

cowboy = Toys("Buzz Light Year")
print(cowboy.name)
cowboy.set_toy("Danny")
print(cowboy.name)