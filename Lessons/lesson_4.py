class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Имя должно быть минимум 2 символа")
        self.__name = value


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, value):
        value = int(value)
        if value <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.__age = value

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Мяу-мяу!")



dog_one = Dog("Шарик", 5)
cat_one = Cat("Муся", 3)


dog_one.make_sound()
cat_one.make_sound()


print(dog_one.name, dog_one.age)
print(cat_one.name, cat_one.age)


dog_one.name = "Тузик"
dog_one.age = 7

cat_one.name = "Белка"
cat_one.age = 4


print(dog_one.name, dog_one.age)
print(cat_one.name, cat_one.age)
