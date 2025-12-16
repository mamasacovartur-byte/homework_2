# # Практическое задание 1
#
# Создайте программу, в которой будет базовый класс Animal
# с приватными атрибутами имени и возраста. Реализуйте для них геттеры и сеттеры.

# Затем создайте два класса-наследника — например,
# Dog и Cat, которые переопределяют метод make_sound() из базового класса,

# чтобы продемонстрировать полиморфизм. В конце создайте объекты этих классов,
# выведите их звуки и измените значения приватных атрибутов через сеттеры.
#
# можно создать и закоммитить новый файл `control_work.py`  запушить на гитхаб и отправить мне ссылку.
# или можно просто прикрепить файл к контрольной
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def make_sound(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError("Имя должно быть от четырёх букв")
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

class Dog(Animal):
    def make_sound(self):
        print("гав гав гав")

dog_one = Dog('Шарик','4')
dog_one.name ='Шарик'
dog_one.age ='4'
dog_one.make_sound()
print(dog_one.name)
print(dog_one.age)

class Cat(Animal):
    def make_sound(self):
        print("мяу мяу мяу")

cat_one = Cat("Муся", 2)
cat_one.name = 'Муся'
cat_one.age = '2'
cat_one.make_sound()
print(cat_one.name)
print(cat_one.age)