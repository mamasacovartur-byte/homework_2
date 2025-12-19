class Moto:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False
        self.__max_speed =120

    def drive_to(self, destination):
        print(f"Moto {self.model} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Car {self.model} changed to {self.color}")

    def get_max_speed(self):
        return self.__max_speed

    def set_maz_speed(self,value):
        if value<=0:
            raise ValueError('максимальная скорость больше позитивной')
        self.__max_speed = value

car_honda = Moto(color = "red", model = "Honda")
car_subaru = Moto(color = "blue", model = "Subaru" )
car_subaru.drive_to("Karakol")
car_honda.drive_to('bishkek')
car_honda.set_maz_speed(1)