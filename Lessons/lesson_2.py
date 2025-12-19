# родительский класс, суперкласс
class Moto:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

    def drive_to(self, destination):
        print(f"Moto {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")


# дочерний класс, подкласс
class Bmw(Moto):
    pass


class Kavasaki(Moto):
    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Truck {self.model} driving to {destination}")

    def test(self):
        print(f"Truck test: {self.model}")



car_honda = Moto(color = "red", model = "Honda")
car_subaru = Moto(color = "blue", model = "Subaru")
car_subaru.drive_to("Karakol")
truck_1 = Kavasaki("red", "Mercedes")
truck_1.drive_to("Bishkek")
print("Truck 1:", truck_1.color, truck_1.model)
truck_1.test()