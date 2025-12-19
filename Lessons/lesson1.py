class Car:

    def __init__(self,color,made,name):
        self.color = color
        self.made = made
        self.name = name

    def intrudus (self):
        intrudus= ("имею высшее образование"
        if self.name
        else "высшего образования нет")


car_honda = Car(color='blue',made='china')
car_subaru = Car(color='red',made='KG')

print(car_subaru.color)
print(car_honda.color)
car_subaru.year = 2008
print(car_subaru.year)


class Truck(Car):
    pass

truck_one = Truck('red','bmw')

class Bus(Car):
    def __init__(self,color,model,number):
bus_one = Bus('blue','mersedes')
bus_one.intrudus()