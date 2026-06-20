class Car:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    
    def pr_brand(self):
        return self.brand

    def describe(self):
        return f"{self.brand} может разогнаться до {self.max_speed} км/ч."
    

Opel = Car("Opel", "7")
Reno = Car("Reno", "27")

print(Opel.pr_brand())
print(Reno.pr_brand())

print(Opel.describe())
print(Reno.describe())
class Team:
    def __init__(self, name):
        self.name = name
        self.drivers = []
    
    def add_driver(self, driver_name):
        self.drivers.append(driver_name)
        
    def driver_list(self):
        list=""
        for driver in self.drivers:
            list+=driver+" "
        print(list)
        
s=Team("sa")
s.add_driver("re")
s.add_driver("ry")

x = s.driver_list
x()
