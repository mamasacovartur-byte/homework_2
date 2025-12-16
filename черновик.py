# class Book:
#     def __init__(self, title, author, year, pages):
#         self.title = title #название
#         self.author = author #автор
#         self.year = year #год
#         self.pages = pages #страница
#
#     def info(self):
#         print(f'название книги {self.title},',f'афтор книги {self.author},', f'создано в {self.year},', f'страница {self.pages}')
#
# book_one = Book('война и мир','Л.Т','1978','189')
# book_two = Book('крвсное яблоко','Ч.А','1997','120')
# book_free = Book('девять объезян','М.Р','1980','489')
# book_for = Book('белый пороход','Ч.А','1906','236')
#
# print(book_one.title , book_one.author , book_one.year , book_one.pages)
# print(book_two.title , book_two.author , book_two.year , book_two.pages)
# print(book_free.title , book_free.author , book_free.year , book_free.pages)
# print(book_for.title , book_for.author , book_for.year , book_for.pages)
#
# book_one.info()
# book_two.info()
# book_free.info()
# book_for.info()
# 3. Класс Student
#
# Создать файл students.py.
#
# Создать класс Student
#
# Атрибуты: name, age, course, grades (список оценок)
#
# Метод average_grade() возвращает средний балл
#
# Метод introduce() рассказывает о студенте
#
# Создать пару студентов и вывести их средние оценки.
#
# 4. Класс Animal
#
# Создать файл animals.py.
#
# Создать класс Animal
#
# Атрибуты: species, name, age
#
# Метод speak() выводит звук:
# Например: "Кот Барсик говорит: мяу!"
#
# Создать объекты разных животных.
#
# 5. Класс Movie
#
# Создать файл movies.py.
#
# Создать класс Movie
#
# Атрибуты: title, director, year, genre
#
# Метод describe() выводит описание фильма
#
# Создать 3 фильма и вывести их атрибуты.
#
# 6. Класс Employee
#
# Создать файл employee.py.
#
# Создать класс Employee
#
# Атрибуты: name, position, salary
#
# Метод info() выводит:
# "Имя: Анна, должность: менеджер, зарплата: 70000"
#
# Метод increase_salary(percent) увеличивает зарплату на заданный процент
#
# Создать несколько сотрудников и поднять одному зарплату.
#
# 7. Класс Country
#
# Создать файл countries.py.
#
# Создать класс Country
#
# Атрибуты: name, population, continent, capital
#
# Метод describe() выводит сводную информацию
#
# Создать 2–3 страны.#
# 3. Класс Student
#from pydoc import describe


#Создать файл students.py.

#  Создать класс Student
#
# Атрибуты: name, age, course, grades (список оценок)
#
# Метод average_grade() возвращает средний балл
#
# Метод introduce() рассказывает о студенте
# #
# Создать пару студентов и вывести их средние оценки.#
# class Student:
#     def __init__(self, name, age, course, grades):
#         self.name = name  # имя студента
#         self.age = age  # возраст
#         self.course = course  # курс обучения
#         self.grades = grades  # список оценок
#
#     def average_grade(self):
#         """Возвращает средний балл студента"""
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#     def introduce(self):
#         """Выводит информацию о студенте"""
#         print(f"Меня зовут {self.name}, мне {self.age} лет, "
#               f"я учусь на {self.course} курсе. "
#               f"Мой средний балл: {self.average_grade():.2f}")
#
#
# # Создание объектов студентов
# student_one = Student("Алибек", 18, 1, [5, 4, 5, 3, 4])
# student_two = Student("Айдана", 20, 2, [4, 4, 5, 5, 5])
#
# # Вывод средних оценок
# print("Средний балл студента 1:", student_one.average_grade())
# print("Средний балл студента 2:", student_two.average_grade())
#
# # Представление студентов
# student_one.introduce()

# student_two.introduce()
###Создайте несколько разных объектов (Classmate, Friend, Person).
# Поместите их все в один список. Затем напишите цикл, который проходит
# по этому списку и для каждого объекта вызывает метод introduce().№№
# class Person:
#     def __init__(self, name, birth_date, occupation, higher_education):
#         self.name = name
#         self.birth_date = birth_date
#         self.occupation = occupation
#         self.higher_education = higher_education
#
#     def introduce(self):
#         introduce = ("по професия я "
#                      if self.higher_education
#                      else "нет професии")
#         print(f"Меня зовут {self.name},", f"я родился {self.birth_date}", f"по профессии {self.occupation}",
#               f"{introduce}.")
#
#
# class Classmate(Person):
#     def __init__(self, name, birth_date, occupation, higher_education, group_name):
#         super().__init__(name, birth_date, occupation, higher_education)
#         self.group_name = group_name
#
#     def introduce(self):
#         """Дополнительная информация"""
#         print(f"Меня зовут {self.name}", f"я родился {self.birth_date}",
#               f"по профессии {self.occupation} , имею {self.higher_education},мой одногрупник  {self.group_name}")
#
#
# classmate_one = Classmate("Artur", "16.01.2008", "прошраммист", "среднее образование", "Алмаз")
# classmate_two = Classmate("Arslan", "23.04.2005", "врач", "высшее оброзование", "Алмаз")
# classmate_one.introduce()
# classmate_two.introduce()
#
#
# class Friend(Person):
#     def __init__(self, name, birth_date, occupation, higher_education, hobby, friend):
#         super().__init__(name, birth_date, occupation, higher_education)
#         self.hobby = hobby
#         self.friend = friend
#
#     def introduce(self):
#         """Дополнительная информация"""
#         print(f"Меня зовут {self.name},", f"я родился {self.birth_date}", f',я друг {self.friend}',
#               f"по профессии {self.occupation} , имею {self.higher_education},моё хобби {self.hobby}")
#
#
# friend_one = Friend("Бексултан", "27.09.2000", "хирург", "высшее образование", "бокс", "Алмаза")
# friend_two = Friend("Арген", "15.03.2007", "машинист", "среднее образование", "бег", "Алмаза")
# friend_one.introduce()
# friend_two.introduce()
#
# people = [classmate_one,classmate_two,friend_one,friend_two]
#
# for v in people:
#     v.introduce()
# 🔹 Задача 1. Животные и их особенности
#
# Создай класс Animal с атрибутами: name, age.
#
# Добавь метод describe(), который выводит информацию о животном.
#
# Создай два класса-наследника:
#
# Dog — добавь атрибут breed
#
# Cat — добавь атрибут color
#
# Переопредели метод describe() так, чтобы он выводил дополнительные данные.
#
# Создай по два объекта каждого класса и вызови метод describe().

class Water:
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability,):
        self.name = name
        self.surname = surname
        self.light = light
        self.liter = liter
        self.design = design
        self.height = height
        self.taste = taste
        self.strength = strength
        self.recyclability = recyclability

    def tool(self):
        if self.strength:
            print(f'Прочность бутылки:{self.strength} прошол')
        else:
            print(f'Прочность бутылки:{self.strength} не прошол ')
            print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}')

water_one =  Water('Артур','Мамасаков','белый','1л','черного цвета ','50см','','','')
water_two =  Water('Антон','Павлович','черный','0.5л','белого цвета','25см','','','')
water_free =  Water('Мирослав','Василевич','крсный','1.5л','ярко синего света','50см','','','')
water_for =  Water('Темирлан','Токтрбеков','синий','2л','красного цекта','50см','','','')
water_five =  Water('Бексултан','Турабалдиев','розовый','5л','красного цвета','53см','','','')
water_sics =  Water('Нурдин','Калыков','','зеленый','3л','синего цвета','50см','','')

water_one.tool()
water_two.tool()
water_free.tool()
water_for.tool()
water_five.tool()
water_sics.tool()
class Kola(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability, temperature):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.temperature = temperature

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'температура сока {self.temperature}')

kola_one = Kola('','','','','','','','','','')
kola_one.tool()

class Fanta(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability,gas):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.gas = gas

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'газированная {self.gas}')

fanta_one = Fanta('Бека','Кылдыбеков','черный','10','красный','56','сладкий','100','100','нет')
fanta_one.tool()
class Sprit(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability, hot):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.hot = hot

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'горячий сок {self.hot}')

sprit_one = Sprit('Акмат','Бегалы','green','1.0','чёрный','23','слаткий','100','100','да')
sprit_one.tool()

class Pepsi(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability, color):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.color = color

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'свет сока {self.color}')

pepsi_one = Pepsi('Фатих','Малиев','чёрный','1','красный','53','горький','100','100','blec')
pepsi_one.tool()

class Ava(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability, hot):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.hot = hot

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'горячий сок {self.hot}')

ava_one = Ava('Фатих','Малиев','чёрный','1','красный','53','горький','100','100','да')
ava_one.tool()

class Peko(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability,hot):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.hot = hot

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'горячий сок {self.hot}')

peko_one = Peko('Фатих','Малиев','чёрный','1','красный','53','горький','100','100','да')
peko_one.tool()

class Pekoblek(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability,hot):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.hot = hot

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'горячий сок {self.hot}')

pekoblek_one = Pekoblek('Фатих','Малиев','чёрный','1','красный','53','горький','100','100','да')
pekoblek_one.tool()

class JalalAbad(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability,hot):
        super().__init__(name, surname,light, liter, design, height, taste, strength, recyclability)
        self.hot = hot

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'горячий сок {self.hot}')

jalalAbad_one = JalalAbad('Фатих','Малиев','чёрный','1','красный','53','горький','100','100','да')
jalalAbad_one.tool()

class Niktare(Water):
    def __init__(self,name,surname, light, liter, design, height, taste, strength, recyclability, hot):
        super().__init__(name,surname,light, liter, design, height, taste, strength, recyclability)
        self.hot = hot

    def tool(self):
        print(f'Данные о воде::',f'Имя тестировщика:{self.name}',f'Фамилия тестировщика:{self.surname}',
                  f'Свет воды:{self.light}',f'Объём воды:{self.liter}',f'Дизайин бутлки:{self.design}',
                  f'Высота бутылки:{self.height}',f'Вкус напитка:{self.taste}',f'Прочность бутылки:{self.strength}',
                  f'Переробатываемость:{self.recyclability}',f'{self.strength}' f'горячий сок {self.hot}')

niktare_one = Niktare('Фатих','Малиев','чёрный','1','красный','53','горький','100','100','да')
niktare_one.tool()