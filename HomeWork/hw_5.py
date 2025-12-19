# # Homework 5
#
# Все сделать в отдельной ветке `hw5` и потом сделать слияние этой ветки с `main`
#
# Есть классы:
#
# - `Vehicle` (общий транспорт, имеет метод `start()`),
# - `Car` ,
# - `ElectricCar`
# - `Tesla` (наследуется от `ElectricCar` и `Car`).
#
# Требуется так реализовать `start()`, чтобы вызов `Tesla().start()` проходил по цепочке MRO и выводил( `print`), следующее:
class Vehicle:
    def start(self):
        print('Vehicle starting')


class Car(Vehicle):
    def start(self):
        super().start()
        print('Car starting')

    pass


class ElectricCar(Vehicle):
    def __str__(self):
        super().__str__()
        print('ElectricCar starting')

    pass


class Tesla(Car, ElectricCar):
    def start(self):
        super().start()
        print('Tesla redy')

    pass


print(Tesla.mro())
car_one = Tesla()
car_one.start()
#ctrl+ alt +l = правильно выстовляет